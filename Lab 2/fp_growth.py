import csv
from collections import defaultdict, namedtuple
from optparse import OptionParser

from fp_growth.fp_node import FPNode
from fp_growth.fp_tree import FPTree


def conditional_tree_from_paths(paths, minimum_support):
    """Builds a conditional FP-tree from the given prefix paths."""
    tree = FPTree()
    condition_item = None
    items = set()

    for path in paths:
        if condition_item is None:
            condition_item = path[-1].item

        point = tree.root
        for node in path:
            next_point = point.search(node.item)
            if not next_point:
                items.add(node.item)
                count = node.count if node.item == condition_item else 0
                next_point = FPNode(tree, node.item, count)
                point.add(next_point)
                tree._update_route(next_point)
            point = next_point

    assert condition_item is not None

    for path in tree.prefix_paths(condition_item):
        count = path[-1].count
        for node in reversed(path[:-1]):
            node._count += count

    for item in items:
        support = sum(n.count for n in tree.nodes(item))
        if support < minimum_support:
            # Doesn't make the cut anymore
            for node in tree.nodes(item):
                if node.parent is not None:
                    node.parent.remove(node)

    for node in tree.nodes(condition_item):
        if node.parent is not None:
            node.parent.remove(node)

    return tree

def find_frequent_itemsets(transactions, minimum_support, include_support=False):
    '''FINDS FREQUENT ITEMSETS IN THE GIVEN TRANSACTIONS'''
    items = defaultdict(lambda:0)
    processed_transactions = []

    for transaction in transactions:
        transaction = transaction[0].split()
        processed = []
        for item in transaction:
            items[item] += 1
            processed.append(item)
        processed_transactions.append(processed)
  
    items = dict((item, support) for item, support in items.items()
                  if support >= minimum_support)

    def clean_transaction(transaction):
        '''STRIPS TRANSACTIONS OF INFREQUENT ITEMS AND SURVIVING ITEMS ARE SORTED IN DECREASING ORDER OF FREQUENCY'''
        transaction = list(filter(lambda v: v in items, transaction))
        transaction.sort(key=lambda v: items[v], reverse=True)
        return transaction

    master = FPTree()
    for transaction in map(clean_transaction, processed_transactions):
        master.add(transaction) 
    # master.inspect()

    def find_with_suffix(tree, suffix):
        for item, nodes in tree.items():
            support = sum(n.count for n in nodes)
            if support >= minimum_support and item not in suffix:
                found_set = [item] + suffix
                yield (found_set, support) if include_support else found_set

                '''Build a conditional tree and recursively search for frequent itemsets within it.'''
                cond_tree = conditional_tree_from_paths(tree.prefix_paths(item),
                    minimum_support)
                for found_suffix in find_with_suffix(cond_tree, found_set):
                    yield found_suffix

    '''Search for frequent itemsets, and yield the results we find.'''
    for itemset in find_with_suffix(master, []):
        yield itemset

def main():
    '''MAIN METHOD'''
    p = OptionParser(usage='%prog data_file')
    p.add_option('-s', '--minimum-support', dest='minsup', type='int',
        help='Minimum itemset support (default: 2)')
    p.set_defaults(minsup=2)

    options, args = p.parse_args()
    if len(args) < 1:
        p.error('must provide the path to a CSV file to read')

    filename = open(args[0])
    try:
        for itemset, support in find_frequent_itemsets(csv.reader(filename), options.minsup, True):
            print('{' + ', '.join(itemset) + '} ' + str(support))
    finally:
        filename.close()

if __name__ == '__main__':
    main()
