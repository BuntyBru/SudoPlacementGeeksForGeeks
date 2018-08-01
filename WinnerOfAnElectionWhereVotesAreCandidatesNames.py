class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None]*self.size
		self.data = [None]*self.size

	def put(self, key, data):
		hashValue = self.hashfunction(key,len(self.slots))

		if self.slots[hashValue] == None:
			self.slots[hashValue] = key
			self.data[hashValue] = data
		else:
			if self.slots[hashValue] == key:
				self.data[hashValue] = self.data[hashValue]+data #Replacement of the data if the same key is called in again
			else:
				nextHashvalue = self.rehash(hashValue,len(self.slots))
				while self.slots[nextHashvalue] != None and self.slots[nextHashvalue] != key:
					nextHashvalue = self.rehash(nextHashvalue,len(self.slots))
				if self.slots[nextHashvalue] == None:
					self.slots[hashValue] =key
					self.data[hashValue] =data
				else:
					self.data[hashValue]=self.data[hashValue]+data #Replacement of data if the same kind of key is entered again
	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))
		data = None
		found = False
		position = startslot
		stop = False
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data=self.data[position]
			else:
				position = self.rehash(position,len(self.slots))
				if position == startslot:
					stop=True
		return data

	def hashfunction(self,key,size):
		return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size
	
	def __setitem__(self,key,data):
		self.put(key,data)

	def __getitem__(self,key):
		return self.get(key)

H = HashTable()
#H[54]="cat"
#H[26]="dog"
#H[93]="lion"
#H[17]="tiger"
#H[77]="bird"
#H[31]="cow"
#H[44]="goat"
#H[55]="pig"
#H[44]="goat"
#H[20]="chicken"		
arr=["john","johnny","jackie","johnny","john","jackie","jamie","jamie","john","johnny","jamie","johnny","john"]
ans = set(arr)
ans = list(ans)
print(ans)
for i in range(len(arr)):
	if arr[i] in ans:
		p = ans.index(arr[i])
		H[p] =1
		print(p)

for i in range(len(H.data)):
	if H.data[i] == None:
		H.data[i] = 0
print(H.data)
answer = max(H.data)
answer2=[]
for i in range(len(H.data)):
	if H.data[i] == answer:
		answer2.append(ans[H.slots[i]])
answer2.sort()
print(answer2[0], answer)


