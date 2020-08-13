Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> int
<class 'int'>
>>> a
10
>>> 10 == int
False
>>> type(a) == int
True
>>> int(False)
0
>>> int(True)
1
>>> 'aaa'**10
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'aaa'**10
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> a
10
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> if type(a) == int:
	print("labi")

	
labi
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=10
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> a=10
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a=5.5
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> 
>>> 
>>> 
>>> a = 10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
labi
>>> a = 5.5
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
arī labi
>>> a = "dfhlsrklkwr"
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
else:
	print("slikti")

	
slikti
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi")
else:
	print("slikti")

	
slikti
>>> a = 10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi")
else:
	print("slikti")

	
labi
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tekstu neviens nekad neredzēs")
else:
	print("slikti")

	
labi
>>> a = 10
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
	print("arī labi")
elif type(a) == int:
	print("ir jau labi - bet šo tekstu neviens nekad neredzēs")
else:
	print("slikti")

	
labi
>>> print("aaa bbbb ccc")
aaa bbbb ccc
>>> print("aaa\n bbbb\n ccc")
aaa
 bbbb
 ccc
>>> print("aaa\t bbbb\n ccc")
aaa	 bbbb
 ccc
>>> print("aaa\t bbbb\v ccc\nddd")
aaa	 bbbb ccc
ddd
>>> 
