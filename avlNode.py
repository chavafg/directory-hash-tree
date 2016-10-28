from item import DirectoryItem


class avlnode(object):

    def __init__(self, key, DirectoryItem):
        self.left = None
        self.right = None
        self.key = key
        self.DirectoryItem = DirectoryItem

    def __str__(self):
        return str(self.DirectoryItem)

    def __repr__(self):
        # return str( str(self.key) + ' - ' + str(self.DirectoryItem))
        return str(self.key)
