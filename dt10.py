class A:
    def dictionary(self):
	seq = ('Name' , 'Age' , 'Location')
	dict1 = dict.fromkeys(seq ,10)
	print(dict1)
obj = A()
obj.dictionary()
