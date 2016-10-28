from avlTree import avltree
from item import DirectoryItem
from avlNode import avlnode


class HashTable(object):

    def hash_function(self, x): return x % 10

    # def insert(self, table, key, value):
    #   index = self.hash_function(key)
    #  table[index] = value

    def insert_in_avl_tree(self, table, key, record):
        print 'Inserting ' + str(key)
        index = self.hash_function(key)
        hashTree = avltree()
        if isinstance(table[index], avltree):
            table[index].insert(key, record)
        else:
            table[index] = hashTree
            hashTree.insert(key, record)

    def search(self, table, key):
        print 'Searching ' + str(key)
        index = self.hash_function(key)
        result = table[index]
        item = result.search(key)
        return item

    def delete(self, table, key):
        print 'Deleting ' + str(key)
        index = self.hash_function(key)
        result = table[index]
        if isinstance(result, avltree):
            result.delete(key)
            print 'Key ' + str(key) + ' was deleted successfully'
            return 0
        else:
            print 'Key ' + str(key) + ' cannot be deleted as it is not stored'
            return 1

    def modify_record(self, table, key, record):
        print 'Modifying ' + str(key)
        rc = self.delete(table, key)
        if rc == 0:
            self.insert_in_avl_tree(table, key, record)
        else:
            print 'Key ' + str(key) + ' cannot be modified as it is not stored'
