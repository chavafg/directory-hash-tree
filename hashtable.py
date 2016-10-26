from avlTree import avltree 
from item import DirectoryItem
from avlNode import avlnode 

class Hastable(object):
	hastable = [0] * 10
	result=''
    
	def hash_function(self, x): return x % 10 

	def insert(self,table,key,value):
            index = self.hash_function(key) 
	    table[index] = value

        def insertInAVLtree(self,table,key,record):
            index = self.hash_function(key) 
            hashTree = avltree()
            table[index] = hashTree
            hashTree.insert(key, record)
	
	def search(self,table,key):
            index = self.hash_function(key)
            result = table[index]
            item = result.search(key)
	    return item

        def delete(self,table,key):
            index = self.hash_function(key)
            result = table[index]
            result.delete(key)
