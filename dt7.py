class A:
    def dictionary(self):
	d = {"Employee":{"Name":["Logesh","Krishna"] , "Age":[22,23] ,"Address":"Chennai"}}
	print((d['Employee']['Name'][0]),(d['Employee']['Age'][0]))
	print((d['Employee']['Name'][1]),(d['Employee']['Age'][1]))
obj = A()
obj.dictionary() 
