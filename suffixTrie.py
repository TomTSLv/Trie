class suffixTrie:

    class Node:
        def __init__(self,label):
            self._label=label
            self._branches={}

    def __init__(self,string='$'):
        self._root=self.Node(None)
        self._root._branches['$']=self.Node('$')

    def insert(self, string):
        string+='$'
        cursor=self._root
        for i in range(len(string)):
            cursor._branches[string[i]]=self.Node(string[i:])
            cursor = cursor._branches[string[i]]
        for i in range(1,len(string)):
            cursor=self._root
            j=i
            flag = False
            while j<len(string) and not flag:
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
                        middleCursor=middle
                        for n in range(1,k-j):
                            middleCursor._branches[substring[n]]=self.Node(substring[n:k-j])
                            middleCursor=middleCursor._branches[substring[n]]
                        l=j
                        cursor1=cursor
                        while cursor1._label!=substring[k-j-1:]:
                            cursor1=cursor1._branches[string[l]]
                            l+=1
                        middleCursor._branches=cursor1._branches
                        newCursor=middleCursor
                        for n in range(k,len(string)):
                            newCursor._branches[string[n]]=self.Node(string[n:])
                            newCursor=newCursor._branches[string[n]]
                        cursor._branches[string[j]]=middle
                        flag = True
                else:
                    while j<len(string):
                        cursor._branches[string[j]]=self.Node(string[j:])
                        cursor = cursor._branches[string[j]]
                        j+=1
                    flag = True

