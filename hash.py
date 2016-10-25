class Hastable(self):
	hastable = [0] * 10
	result=''
	def hash_function(x): return x % 10 

	def insert(table,key,value):
		table[hash_function(key)] = value
	
	def search(table,key):
		result = table[hash_function(key)]
		return result

insert(hastable,41,'apple')
insert(hastable,93,'banana')
print(search(hastable,41))
print (hastable)
