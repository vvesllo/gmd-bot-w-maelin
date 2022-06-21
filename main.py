import gmdapi

ng = gmdapi.NewGrounds()
a = ng.get(1)
for i in a:
	print(i, ":", a[i])