from collections import namedtuple
from fp_growth.fp_node import FPNode

class FPTree(object):
    '''FP TREE STRUCTURE'''
    Route = namedtuple('Route', 'head tail')

    def __init__(self):
        self._root = FPNode(self, None, None)
        self._routes = {}

    @property
    def root(self):
        '''RETURNS ROOT OF THE FP TREE'''
        return self._root

    def add(self, transaction):
        '''ADDS A TRANSACTION TO THE TREE'''
        point = self._root
        for item in transaction:
            next_point = point.search(item)
            if next_point:
                next_point.increment()
            else:
                next_point = FPNode(self, item)
                point.add(next_point)
                self._update_route(next_point)
            point = next_point

    def _update_route(self, point):
        '''ADD THE NODE POINT TO THE ROUTE THROUGH ALL NODES FOR ITS ITEM'''
        assert self is point.tree

        try:
            route = self._routes[point.item]
            route[1].neighbour = point
            self._routes[point.item] = self.Route(route[0], point)
        except KeyError:
            self._routes[point.item] = self.Route(point, point)

    def items(self):
        '''GENERATE 2-TUPLES FOR EACH ITEM OF THE FORM (ITEM, GENERATOR)'''
        for item in self._routes:
            yield(item, self.nodes(item))

    def nodes(self, item):
        '''GENERATES THE SEQUENCE OF NODES THAT CONTAIN THE GIVEN ITEM'''
        try:
            node = self._routes[item][0]
        except KeyError:
            return
        while node:
            yield node
            node = node.neighbour

    def prefix_paths(self, item):
        '''GENERATES PREFIX PATHS ENDING WITH CURRENT ITEM'''

        def collect_path(node):
            path = []
            while node and not node.root:
                path.append(node)
                node = node.parent
            path.reverse()
            return path

        return (collect_path(node) for node in self.nodes(item))

    def inspect(self):
        print('\nTREE:')
        self.root.inspect(1)
        print('\nROUTES:')
        for item, nodes in self.items():
            print('%r' % item)
            for node in nodes:
                print('%r' % node)

    def _removed(self, node_to_remove):
        '''PERFORMS CLEANUP DURING REMOVAL OF A NODE'''
        head, tail = self._routes[node_to_remove.item]
        if node_to_remove is head:
            if node_to_remove is tail or not node_to_remove.neighbour:
                # It was the sole node.
                del self._routes[node_to_remove.item]
            else:
                self._routes[node_to_remove.item] = self.Route(node_to_remove.neighbour, tail)
        else:
            for node in self.nodes(node_to_remove.item):
                if node.neighbour is node_to_remove:
                    node.neighbour = node_to_remove.neighbour # skip over
                    if node_to_remove is tail:
                        self._routes[node_to_remove.item] = self.Route(head, node)
                    break
