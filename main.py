from avlNode import avlnode
from item import DirectoryItem
from hashtable import Hastable
from avlTree import avltree

record = DirectoryItem('TestUser1', 'Test1', 'address', 99901, 99991)
record2 = DirectoryItem('TestUser2', 'Test2', 'otraaddress', 99902, 8882)
record3 = DirectoryItem('TestUser3', 'Test3', 'otraaddress', 99903, 8883)
record4 = DirectoryItem('TestUser4', 'Test4', 'otraaddress', 99904, 8884)
record5 = DirectoryItem('TestUser5', 'Test5', 'otraaddress', 99905, 8885)
record6 = DirectoryItem('TestUser6', 'Test6', 'otraaddress', 99906, 8886)

tree = avltree()
hashTable = Hastable()
table = [0] * 10

# hashTable.insert(table,41,record)
hashTable.insertInAVLtree(table, 41, record)
hashTable.insertInAVLtree(table, 52, record2)
hashTable.insertInAVLtree(table, 53, record3)
hashTable.insertInAVLtree(table, 49, record4)
hashTable.insertInAVLtree(table, 81, record5)
hashTable.insertInAVLtree(table, 11, record5)
hashTable.insertInAVLtree(table, 31, record5)
hashTable.insertInAVLtree(table, 51, record5)
hashTable.insertInAVLtree(table, 111, record5)
hashTable.insertInAVLtree(table, 201, record5)
hashTable.insertInAVLtree(table, 91, record2)
hashTable.insertInAVLtree(table, 23, record6)
# print hashTable.search(table,201)

for item in table:
    if isinstance(item, avltree):
        print item.inorder_traverse()
    else:
        print item

# print table
hashTable.delete(table, 49)
hashTable.delete(table, 52)
hashTable.delete(table, 201)
hashTable.search(table, 201)
hashTable.search(table, 31)
# print table

for item in table:
    if isinstance(item, avltree):
        print item.inorder_traverse()
    else:
        print item
