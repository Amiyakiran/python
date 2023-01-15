a = input("enter the first number")
b = input("enter the second number")
txt = "The larger number is {}"
if  a>b:
	print(txt.format(a))
else:
	print(txt.format(b))