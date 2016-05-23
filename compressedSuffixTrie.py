class compressedSuffixTrie:
    class Node:
		def __init__(self,label):
			self._label=label
			self._branches={}

	def __init__(self,string='$'):
		self._root=self.Node(None)
		self._root._branches['$']=self.Node('$')

	def insert(self,string):
		string+='$'
		self._root._branches[string[0]]=self.Node(string)
		for i in range(1,len(string)):
			cursor=self._root
			j=i
			flag=False
			while j<len(string):
				if string[j] in cursor._branches:
					node=cursor._branches[string[j]]
					substring=node._label
					k=j+1
					while k-j<len(substring) and string[k]==substring[k-j]:
						k+=1
					if k-j==len(substring):
						cursor=node
						j=k
					else:
						exist,new=substring[k-j],string[k]
						middle=self.Node(substring[:k-j])
						middle._branches[new]=self.Node(string[k:])
						middle._branches[exist]=node
						node._label=substring[k-j:]
						cursor._branches[string[j]]=middle
						flag=True
				else:
					cursor._branches[string[j]]=self.Node(string[j:])
					flag=True