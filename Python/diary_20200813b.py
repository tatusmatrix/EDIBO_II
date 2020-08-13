Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> fruit[0]+fruit[3]
'ba'
>>> fruit[1]+fruit[3]+fruit[5]
'aaa'
>>> N = len(fruit)
>>> N
6
>>> fruit[N-1]
'a'
>>> numbers = []
>>> len(numbers)
0
>>> numbers.append(1)
>>> len(numbers)
1
>>> NUMBERS
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    NUMBERS
NameError: name 'NUMBERS' is not defined
>>> numbers
[1]
>>> numbers.append(55)
>>> len(numbers)
2
>>> numbers
[1, 55]
>>> vaardi = ['a','ab', 'abc']
>>> vaardi
['a', 'ab', 'abc']
>>> vaardu_garumi = []
>>> vaardu_garumi.append(len(vaardi[0]))
>>> vaardu_garumi.append(len(vaardi[1]))
>>> vaardu_garumi.append(len(vaardi[2]))
>>> vaardu_garumi
[1, 2, 3]
>>> typpe(vaardi)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    typpe(vaardi)
NameError: name 'typpe' is not defined
>>> typpe(vaardi)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    typpe(vaardi)
NameError: name 'typpe' is not defined
>>> type(vaardi)
<class 'list'>
>>> type(vaardu_garumi)
<class 'list'>
>>> vaardi = (['a','ab', 'abc'])
>>> type(vaardi)
<class 'list'>
>>> vaardi = ['a','ab', 'abc', 10]
>>> vaardi
['a', 'ab', 'abc', 10]
>>> fruit
'banana'
>>> len(fruit)
6
>>> fruit[0]
'b'
>>> fruit[1]
'a'
>>> fruit[2]
'n'
>>> fruit[3]
'a'
>>> fruit[4]
'n'
>>> fruit[5]
'a'
>>> N = len(fruit)
>>> N
6
>>> fruit[N]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    fruit[N]
IndexError: string index out of range
>>> fruit[N-1]
'a'
>>> N
6
>>> fruit[ len(fruit) - 1 ]
'a'
>>> fruit = 'abcdef'
>>> fruit
'abcdef'
>>> len(fruit)
6
>>> fruit[ len(fruit) - 1 ]
'f'
>>> len(fruit)
6
>>> 
