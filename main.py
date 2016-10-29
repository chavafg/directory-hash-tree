from avlNode import avlnode
from item import DirectoryItem
from hashTable import HashTable
from avlTree import avltree

record1 = DirectoryItem('TestUser1', 'LastNameTest1', 'street1', 33990001, 338700081)
record2 = DirectoryItem('TestUser2', 'LastNameTest2', 'street2', 33990002, 338700082)
record3 = DirectoryItem('TestUser3', 'LastNameTest3', 'street3', 33990003, 338700083)
record4 = DirectoryItem('TestUser4', 'LastNameTest4', 'street4', 33990004, 338700084)
record5 = DirectoryItem('TestUser5', 'LastNameTest5', 'street5', 33990005, 338700085)
record6 = DirectoryItem('TestUser6', 'LastNameTest6', 'street6', 33990006, 338700086)
record7 = DirectoryItem('TestUser7', 'LastNameTest7', 'street7', 33990006, 338700086)
record8 = DirectoryItem('TestUser8', 'LastNameTest8', 'street8', 33990006, 338700086)
record9 = DirectoryItem('TestUser9', 'LastNameTest9', 'street9', 33990006, 338700086)
record10 = DirectoryItem('TestUser10', 'LastNameTest10', 'street10', 33990006, 338700086)
record11 = DirectoryItem('TestUser11', 'LastNameTest11', 'street11', 33990006, 338700086)
record12 = DirectoryItem('TestUser12', 'LastNameTest12', 'street12', 33990006, 338700086)
record13 = DirectoryItem('TestUser13', 'LastNameTest13', 'street13', 33990006, 338700086)
record14 = DirectoryItem('TestUser14', 'LastNameTest14', 'street14', 33990006, 338700086)
record15 = DirectoryItem('TestUser15', 'LastNameTest15', 'street15', 33990006, 338700086)
record16 = DirectoryItem('TestUser16', 'LastNameTest16', 'street16', 33990006, 338700086)
record17 = DirectoryItem('TestUser17', 'LastNameTest17', 'street17', 33990006, 338700086)
record18 = DirectoryItem('TestUser18', 'LastNameTest18', 'street18', 33990006, 338700086)
record19 = DirectoryItem('TestUser19', 'LastNameTest19', 'street19', 33990006, 338700086)

tree = avltree()
hashTable = HashTable()
table = [0] * 10

hashTable.insert_in_avl_tree(table, 41, record1)
hashTable.insert_in_avl_tree(table, 52, record2)
hashTable.insert_in_avl_tree(table, 53, record3)
hashTable.insert_in_avl_tree(table, 49, record4)
hashTable.insert_in_avl_tree(table, 81, record5)
hashTable.insert_in_avl_tree(table, 11, record6)
hashTable.insert_in_avl_tree(table, 31, record7)
hashTable.insert_in_avl_tree(table, 51, record8)
hashTable.insert_in_avl_tree(table, 111, record9)
hashTable.insert_in_avl_tree(table, 201, record10)
hashTable.insert_in_avl_tree(table, 91, record11)
hashTable.insert_in_avl_tree(table, 23, record12)
hashTable.insert_in_avl_tree(table, 3, record13)
hashTable.insert_in_avl_tree(table, 65, record14)
hashTable.insert_in_avl_tree(table, 45, record15)
hashTable.insert_in_avl_tree(table, 505, record16)
hashTable.insert_in_avl_tree(table, 90, record17)
hashTable.insert_in_avl_tree(table, 9, record18)
hashTable.insert_in_avl_tree(table, 76, record19)

print '---------------'
for item in table:
    print '-----'
    if isinstance(item, avltree):
        print item.inorder_traverse()
    else:
        print item
print '---------------'

hashTable.delete(table, 49)
print '***'
hashTable.delete(table, 52)
print '***'
hashTable.delete(table, 201)
print '***'
record99 = DirectoryItem('TestUser99', 'LastNameTest99', 'street', 33990009, 338700089)
print '***'
hashTable.modify_record(table, 505, record99)
print '***'
hashTable.search(table, 201)
print '***'
hashTable.search(table, 31)

print '---------------'
for item in table:
    print '-----'
    if isinstance(item, avltree):
        print item.inorder_traverse()
    else:
        print item
print '---------------'
