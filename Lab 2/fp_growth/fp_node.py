class FPNode(object):
    '''A NODE IN AN FP TREE'''

    def __init__(self, tree, item, count=1):
        self._tree = tree
        self._item = item
        self._count = count
        self._parent = None
        self._children = {}
        self._neighbour = None

    def __repr__(self):
        if self.root:
            return '<%s (root)>' % type(self).__name__
        return '<%s %r (%r)>' % (type(self).__name__, self.item, self.count)


    def add(self, child):
        '''ADDS GIVEN NODE AS A CHILD OF THE CURRENT NODE'''
        if not isinstance(child, FPNode):
            raise TypeError("ERROR: CHILD TO BE ADDED MUST BE FPNode")
        
        if not child.item in self._children:
            self._children[child.item] = child
            child.parent = self

    def search(self, item):
        '''CHECKS IF CURRENT NODE HAS A CHILD NODE FOR THE GIVEN ITEM'''
        try:
            return self._children[item]
        except KeyError:
            return None

    def remove(self, child):
        '''REMOVES CHILD NODE FROM CHILDREN OF CURRENT NODE'''
        try:
            if self._children[child.item] is child:
                del self._children[child.item]
                child.parent = None
                self._tree._removed(child)
                for sub_child in child.children:
                    try:
                        self._children[sub_child.item]._count += sub_child.count
                        sub_child.parent = None
                    except KeyError:
                        self.add(sub_child)
                child._children = {}
            else:
                raise ValueError('ERROR: CHILD TO BE REMOVED IS NOT THE CHILD OF THIS NODE')
        except:
            raise ValueError('ERROR: CHILD TO BE REMOVED IS NOT THE CHILD OF THIS NODE')

    def __contains__(self, item):
        return item in self._children

    @property
    def tree(self):
        '''RETURNS THE TREE TO WHICH CURRENT NODE BELONGS'''
        return self._tree

    @property
    def item(self):
        '''RETURNS ITEM CONTAINED IN CURRENT NODE'''
        return self._item

    @property
    def count(self):
        '''RETURNS THE COUNT OF CURRENT NODE\'S ITEM'''
        return self._count

    def increment(self):
        '''INCREMENTS THE COUNT OF CURRENT NODE\'S ITEM'''
        if self._count is None:
            raise ValueError('ERROR: ROOT NODE HAS NO COUNT')
        self._count += 1

    @property
    def root(self):
        '''CHECKS IF CURRENT NODE IS ROOT OF THE FP TREE'''
        return self._item is None and self._count is None

    @property
    def leaf(self):
        '''CHECKS IF CURRENT NODE IS NODE OF THE FP TREE'''
        return len(self._children) == 0

    def parent():
        def fget(self):
            return self._parent
        def fset(self, value):
            if value is not None and not isinstance(value, FPNode):
                raise TypeError('ERROR: A NODE MUST HAVE AN FP NODE AS A PARENT')
            if value and value.tree is not self.tree:
                raise ValueError('ERROR: NODE OF ONE TREE CANNOT HAVE PARENT FROM ANOTHER TREE')
            self._parent = value
        return locals()
    parent = property(**parent())

    def neighbour():
        def fget(self):
            return self._neighbour
        def fset(self, value):
            if value is not None and not isinstance(value, FPNode):
                raise TypeError('ERROR: A NODE MUST HAVE AN FP NODE AS A NEIGHBOUR')
            if value and value.tree is not self.tree:
                raise ValueError('ERROR: NODE OF ONE TREE CANNOT HAVE NEIGHBOUR FROM ANOTHER TREE')
            self._neighbour = value
        return locals()
    neighbour = property(**neighbour())
                
    @property
    def children(self):
        '''RETURNS CHILDREN OF CURRENT NODE'''
        return tuple(self._children.values())

    def inspect(self, depth=0):
        print('   ' * depth + repr(self))
        for child in self.children:
            child.inspect(depth + 1)
