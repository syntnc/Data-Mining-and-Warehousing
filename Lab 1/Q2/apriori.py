import argparse
from itertools import chain, combinations

class Rule(object):
    '''ASSOCIATION RULES'''
    def __init__(self, A, B, support, confidence, time):
        self.A = A
        self.B = B
        self.support = support
        self.confidence = confidence
        self.time = time

    def __repr__(self):
        return '%s ==> %-6s\t%.3f\t\t%.3f' % (' '.join(sorted(list(self.A))),
                                        ' '.join(sorted(list(self.B))),
                                        self.confidence,
                                        self.support)

class Apriori(object):
    '''APRIORI'''
    def __init__(self, data, min_support, min_confidence):
        self.data = data
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.itemset, self.transaction_list = self.get_itemset_from_data()
        self.frequent_itemset = self.get_frequent_itemset()

    @staticmethod
    def join_set(itemset, k):
        '''JOINS TWO ITEMSETS TO GET A k LENGTH UNION'''
        return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == k])

    @staticmethod
    def get_combined_subsets(itemset):
        '''COMBINES ITEMSETS'''
        return chain(*[combinations(itemset, index + 1) for index, item in enumerate(itemset)])

    def get_itemset_from_data(self):
        '''EXTRACTS ITEMSET FROM DATABASE'''
        itemset = set()
        transaction_list = list()
        for row in self.data:
            transaction_list.append(frozenset(row))
            for item in row:
                if item:
                    itemset.add(frozenset([item]))
        return itemset, transaction_list

    def get_support_list(self):
        '''GENERATES SUPPORT LIST HIGHER THAN MINIMUM SUPPORT THRESHOLD'''
        unpruned_list = [(item, float(sum(1 for row in self.transaction_list if item.issubset(row)))/len(self.transaction_list))
                         for item in self.itemset]
        return dict([(item, support) for item, support in unpruned_list if support >= self.min_support])

    def get_frequent_itemset(self):
        '''GENERATES FREQUENT ITEMSETS'''
        frequent_itemset = dict()
        k = 1
        while True:
            if k > 1:
                self.itemset = self.join_set(next_itemset, k)
            next_itemset = self.get_support_list()
            if not next_itemset:
                break
            frequent_itemset.update(next_itemset)
            k += 1
        return frequent_itemset

    def run(self):
        '''RUNS APRIORI ALGORITHM'''
        rules, time = list(), 0
        for item, support in self.frequent_itemset.items():
            if len(item) > 1:
                for A in self.get_combined_subsets(item):
                    B = item.difference(A)
                    if B:
                        A = frozenset(A)
                        AB = A | B
                        confidence = float(self.frequent_itemset[AB]) / self.frequent_itemset[A]
                        if confidence >= self.min_confidence:
                            rules.append(Rule(A, B, support=self.frequent_itemset[AB], confidence=confidence, time=time))
                            time += 1
        return rules, self.frequent_itemset

def parse_arguments():
    '''PARSES COMMAND LINE ARGUMENTS'''
    argparser = argparse.ArgumentParser(description='Apriori Algorithm.')
    argparser.add_argument(
        '-s', '--min_support',
        dest='min_support',
        help='minimum support',
        default=0.6,
        type=float
    )
    argparser.add_argument(
        '-c', '--min_confidence',
        dest='min_confidence',
        help='minimum confidence',
        default=0.8,
        type=float
    )
    argparser.add_argument(
        dest='filename',
        help='filename containing transactions',
        default='transactions.txt',
    )
    return argparser.parse_args()

def data_from_txt(filename):
    '''EXTRACTS DATABASE FROM .txt FILE'''
    file = open(filename, 'r')
    for line in file:
        if line[:3] == 'TID':
            continue
        row = line.strip().split(',')
        row[0] = row[0][8:]
        yield row

def print_frequent_itemsets(itemset):
    '''PRINTS FREQUENT ITEMSETS'''
    print('========================')
    print('Itemset\t\tSupport')
    print('========================')
    for item in itemset.keys():
        print('%s\t\t%.3f' % (' '.join(sorted(list(item))), itemset[item]))

def print_association_rules(rules):
    '''PRINTS ASSOCIATION RULES'''
    print('========================================')
    print('    Rule\tConfidence\tSupport')
    print('========================================')
    rules.sort(key=lambda x: (len(x.A) + len(x.B), x.confidence, x.support, -x.time), reverse=True)
    for rule in rules:
        print(rule)

def main():
    '''MAIN METHOD'''
    arguments = parse_arguments()
    data = data_from_txt(arguments.filename)
    rules, itemset = Apriori(data, arguments.min_support, arguments.min_confidence).run()
    #print_association_rules(rules)
    print_frequent_itemsets(itemset)

if __name__ == '__main__':
    main()
