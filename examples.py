Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
=============================== RESTART: Shell ===============================
>>> data = [100, 200, 300, 400]
>>> first, _, _, last = data
>>> print(first)
100
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(arr - 1):
		for j in range(0, arr - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

				
>>> arr = [23, 1, -9, -1, 0, 2, 8]
>>> bubbleSort(arr)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    bubbleSort(arr)
  File "<pyshell#9>", line 2, in bubbleSort
    for i in range(arr - 1):
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(0, arr - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

				
>>> arr = [2, 1, 0, 3, -2, -4, -8]
>>> bubbleSort(arr)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bubbleSort(arr)
  File "<pyshell#13>", line 3, in bubbleSort
    for j in range(0, arr - i - 1):
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(0, len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

				
>>> arr = [2, 1, -1, 9, 0, -4, 4]
>>> bubbleSort(arr)
>>> print(arr)
[-4, -1, 0, 1, 2, 4, 9]
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(0, len(arr) - i - 1):
		print("*")
		
SyntaxError: expected an indented block
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(0, len(arr) - i - 1):
	print("*")
	
SyntaxError: expected an indented block
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		for j in range(0, len(arr) - i - 1):print("*")

		
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		print(i)

		
>>> bubbleSort([1, 2,9, 4])
0
1
2
>>> bubbleSort([1, 2,9])
0
1
>>> 
=============================== RESTART: Shell ===============================
>>> def bubbleSort(arr):
	for i in range(len(arr) - 1):
		print(i)

		
>>> bubbleSort([0, 2, 1, 9])
0
1
2
>>> bubbleSort([2, 1, 9])
0
1
>>> 
=============================== RESTART: Shell ===============================
>>> def maxNums([3, 2, 0, -1]):
	
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def maxNums([]):
	
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def maxNums(nums):
	for i in range(len(nums) - 1):
		for j in range(0, len(nums) - i - 1):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]
	return nums[-1]

>>> maxNums([2, 0, 4, -1])
4
>>> maxNums([2, 0, 4, -1, 3, 9])
9
>>> 
=============================== RESTART: Shell ===============================
>>> def max_of_two(x, y):
	if x > y:
		return x

	
>>> def max_of_three(x, y, z):
	return max_of_two(, max_of_two(y, z))
SyntaxError: invalid syntax
>>> def max_of_three(x, y, z):
	return max_of_two( max_of_two(y, z))

>>> print(max_of_three(3, 0, 1))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(max_of_three(3, 0, 1))
  File "<pyshell#56>", line 2, in max_of_three
    return max_of_two( max_of_two(y, z))
TypeError: max_of_two() missing 1 required positional argument: 'y'
>>> 
=============================== RESTART: Shell ===============================
>>> def max_two(x, y):
	if x > y:
		return x
	return y

>>> def max_three(x, y, z):
	return max_two(x, max_two(y, z))

>>> print(max_tree(2, 9, -1))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(max_tree(2, 9, -1))
NameError: name 'max_tree' is not defined
>>> print(max_three(2, 9, -1))
9
>>> 
=============================== RESTART: Shell ===============================
>>> def max_Nums(arr):
	for i in range(len(arr) - 1):
		for j in range(0, len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	return arr[-1]

>>> max_Nums([-2, 4, -1, 2, 8, 9, 23])
23
>>> 
