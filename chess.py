Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n = "246.2458"
>>> print(float(n))
246.2458
>>> print(int(float(n)))
246
>>> for i in range(1, 10):
	print("*", end='')
	print("\n")

	
*

*

*

*

*

*

*

*

*

>>> for i in range(1, 10):
	print("*", end='')
print("\n")
SyntaxError: invalid syntax
>>> for i in range(1, 10):
	print("*", end='')
    print("\n")
    
SyntaxError: unindent does not match any outer indentation level
>>> for i in range(1, 10):
	print("*", end='')

	
*********
>>> 
=============================== RESTART: Shell ===============================
>>> def terminal_size():
	import fcntl, termios, struct
	th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
	return tw, th

>>> print('Number of columns and rows : ', terminal_size())
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('Number of columns and rows : ', terminal_size())
  File "<pyshell#15>", line 2, in terminal_size
    import fcntl, termios, struct
ModuleNotFoundError: No module named 'fcntl'
>>> 
=============================== RESTART: Shell ===============================
>>> from random import randint
>>> number = random.randint(20, 47)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    number = random.randint(20, 47)
NameError: name 'random' is not defined
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table(n, s):
	n = int(input("enter number : Э))
		      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table(n, s):
	for i in range(n == 8 and s == 8):
		t = int(input("enter number : Э))
			      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table(n, s):
	for i in range(n == 8 and s == 8):
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : Э))
			      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table(n, s):
	for i in range(n == 8 and s == 8):
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> def chess_table():
	for i in range(n == 8 and s == 8):
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> chess_table()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    chess_table()
  File "<pyshell#47>", line 2, in chess_table
    for i in range(n == 8 and s == 8):
UnboundLocalError: local variable 'n' referenced before assignment
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	for i in range(8):
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 5
enter numb string : 2
no
enter number : 3
enter string numb : 2
enter number : 2
enter numb string : 3
yes
enter number : 12
enter string numb : 13
enter number : 1
enter numb string : 2
no
enter number : 4
enter string numb : 8
enter number : 5
enter numb string : 7
yes
enter number : 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			print("wrong number enter one more time", input(t))
		p = int(input("enter string numb : "))
		if p > 8:
			print("wrong number enter one more time")
		n = int(input("enter number : "))
		if n > 8:
			print("wrong number enter one more time")
		s = int(input("enter numb string : "))
		if s > 8:
			print("wrong number enter one more time")
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> chess_table()
enter number : 9
9
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    chess_table()
  File "<pyshell#53>", line 4, in chess_table
    print("wrong number enter one more time", input(t))
  File "C:\idlex-1.18\idlexlib\idlefork\idlelib\PyShell.py", line 1386, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			print("wrong number enter one more time")
			t = int(input(""))
		else:
			continue
		p = int(input("enter string numb : "))
		if p > 8:
			print("wrong number enter one more time")
		n = int(input("enter number : "))
		if n > 8:
			print("wrong number enter one more time")
		s = int(input("enter numb string : "))
		if s > 8:
			print("wrong number enter one more time")
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")
			
SyntaxError: 'continue' not properly in loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			print("wrong number enter one more time")
			t = int(input(""))
		continue
		p = int(input("enter string numb : "))
		if p > 8:
			print("wrong number enter one more time")
		n = int(input("enter number : "))
		if n > 8:
			print("wrong number enter one more time")
		s = int(input("enter numb string : "))
		if s > 8:
			print("wrong number enter one more time")
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")
			
SyntaxError: 'continue' not properly in loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			print("wrong number enter one more time")
			t = int(input(""))
		else:
			break
		p = int(input("enter string numb : "))
		if p > 8:
			print("wrong number enter one more time")
		n = int(input("enter number : "))
		if n > 8:
			print("wrong number enter one more time")
		s = int(input("enter numb string : "))
		if s > 8:
			print("wrong number enter one more time")
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")
			
SyntaxError: 'break' outside loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	for i in range(8):
		t = int(input("enter number : "))
	for i in range(8):
		p = int(input("enter string numb : "))
	for i in range(8):
		n = int(input("enter number : "))
	for i in range(8):
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> chess_table()
enter number : 9
enter number : 3
enter number : 44
enter number : 
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    chess_table()
  File "<pyshell#59>", line 3, in chess_table
    t = int(input("enter number : "))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t <= 8:
			break
		else:
			print("enter one more : ")
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")
			
SyntaxError: 'break' outside loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		else:
			print("no")

			
>>> chess_table()
enter number : 3
enter string numb : 1
enter number : 1
enter numb string : 7
no
>>> chess_table()
enter number : 5
enter string numb : 6
enter number : 6
enter numb string : 6
no
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 7
enter numb string : 8
no
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 2
enter numb string : 3
yes
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 2
enter numb string : 1
yes
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 2
enter numb string : 2
yes
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 3
enter numb string : 1
no
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 3
enter numb string : 3
yes
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 4
enter numb string : 1
yes
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 4
enter numb string : 2
no
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 4
enter numb string : 3
yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:
			print("no")

			
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 3
enter numb string : 1
eys
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 4
enter numb string : 2
eys
>>> chess_table()
enter number : 3
enter string numb : 2
enter number : 8
enter numb string : 4
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			break
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:
			print("no")
			
SyntaxError: 'break' outside loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
		continue
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:
			print("no")
			
SyntaxError: expected an indented block
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			continue
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:
			print("no")
			
SyntaxError: 'continue' not properly in loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:
			break
		else:
			continue
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:print("no")
		
SyntaxError: 'break' outside loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number : "))
		if t > 8:break
		else:
			continue
		p = int(input("enter string numb : "))
		n = int(input("enter number : "))
		s = int(input("enter numb string : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("yes")
		elif t == n or p == s:
			print("eys")
		else:print("no")
		
SyntaxError: 'break' outside loop
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : Э))
			      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break

		
>>> chess_table()
enter number column : 9
enter number column : 4
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else:
			break
		n = int(input("enter number column2 : Э))
			      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else:
			break
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else:
			break
		s = int(input("enter number row2 : Э))
			      
SyntaxError: EOL while scanning string literal
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else:
			break
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else:
			break
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else:
			break
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		elif t == n or p == s:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 3
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		p = int(input("enter number row : "))
		if p > 8:
			continue
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		elif t == n or p == s:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 4
enter number row : 9
enter number column : 
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    chess_table()
  File "<pyshell#124>", line 3, in chess_table
    t = int(input("enter number column : "))
  File "C:\idlex-1.18\idlexlib\idlefork\idlelib\PyShell.py", line 1386, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
Yes
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
enter number column : 2
enter number row : 2
enter number column2 : 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else:
			break
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		elif t == n or p == s:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 9
enter number column : 4
enter number row : 9
enter number row : 3
enter number column2 : 2
enter number row2 : 3
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else:
			break
	if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
	elif t == n or p == s:
			print("Yes")
	else:
			print("No")

			
>>> chess_table()
enter number column : 9
enter number column : 9
enter number column : 10
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 2
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 3
Yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else:
			break
	if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
	elif t == n and p == s:
			print("Yes")
	else:
			print("No")

			
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 3
Yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else:
			break
	if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
	else:
			print("No")

			
>>> chess_table()
enter number column : 
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    chess_table()
  File "<pyshell#140>", line 3, in chess_table
    t = int(input("enter number column : "))
ValueError: invalid literal for int() with base 10: ''
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 3
Yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number column : "))
		p = int(input("enter number row : "))
		n = int(input("enter number column2 : "))
		s = int(input("enter number row2 : "))
	if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
	else:
			print("No")
			
SyntaxError: unindent does not match any outer indentation level
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number column : "))
		p = int(input("enter number row : "))
		n = int(input("enter number column2 : "))
		s = int(input("enter number row2 : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 2
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 8
No
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
		t = int(input("enter number column : "))
		p = int(input("enter number row : "))
		n = int(input("enter number column2 : "))
		s = int(input("enter number row2 : "))
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		elif t == n and p == s:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 1
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 2
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 4
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
		if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
			print("Yes")
		elif t == n and p == s:
			print("Yes")
		else:
			print("No")

			
>>> chess_table()
enter number column : 9
enter number column : 12
enter number column : 2
enter number row : 3
enter number column2 : 8
enter number row2 : 3
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 or t == n - 1 and p == s + 1 or p == s - 1:
		print("Yes")
	elif t == n and p == s:
		print("Yes")
	else:
		print("No")

		
>>> chess_table()
enter number column : 9
enter number column : 12
enter number column : 8
enter number row : 2
enter number column2 : 1
enter number row2 : 2
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
>>> chess_table()
enter number column : 3
enter number row : 1
enter number column2 : 8
enter number row2 : 1
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 2
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 4
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 35
enter number column2 : 3
enter number row2 : 5
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 4
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
No
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n and p == s:
		print("Yes")
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	else:
		print("No")

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 8
enter number row2 : 3
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
No
>>> 
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 5
enter number row2 : 2
No
>>> chess_table()
enter number column : 7
enter number row : 1
enter number column2 : 2
enter number row2 : 1
No
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n and p == s:
		print("Yes")
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	elif print("no")
	
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n and p == s:
		print("Yes")
	else: print("no")
	if t == n + 1 and p == s + 1:
		print("Yes")
	else: print("no")
	if t == n - 1 and p == s -1:
		print("Yes")
	else: print("no")
	if t == n - 1 and p == s + 1:
		print("Yes")
	else: print("no")
	if t == n + 1 and p == s - 1:
		print("Yes")
	else: print("no")

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
no
no
no
Yes
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n and p == s:
		print("Yes")
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	else: print("no")

	
>>> chess_table()
enter number column : 9
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else:
			break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n and p == s:
		print("Yes")
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	else: print("no")

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 4
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s:
	else: print("no")
	
SyntaxError: expected an indented block
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s:	else: print("no")
	
SyntaxError: invalid syntax
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s:
		print("Yes")
		else:
			
SyntaxError: invalid syntax
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s:
		print("Yes")
	else:
		print("No")

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
No
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
No
>>> 
=============================== RESTART: Shell ===============================
>>> while True:
	t = int(input("enter number column : " ))
	if t > 8:
		continue
	else: break
while True:
	
SyntaxError: invalid syntax
>>> while True:
	t = int(input("enter number column : " ))
	if t > 8:
		continue
	else: break

	
enter number column : 9
enter number column : 8
>>> while True:
	p = int(input("enter number row : " ))
	if t > 8:
		continue
	else: break

	
enter number row : 3
>>> while True:
	n = int(input("enter number column : " ))
	if t > 8:
		continue
	else: break

	
enter number column : 4
>>> while True:
	s = int(input("enter number row : " ))
	if t > 8:
		continue
	else: break

	
enter number row : 4
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if t == n + 1 and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s -1:
		print("Yes")
	if t == n - 1 and p == s + 1:
		print("Yes")
	if t == n + 1 and p == s - 1:
		print("Yes")
	if t == n and p == s + 1:
		print("Yes")
	if t == n - 1 and p == s:
		print("Yes")
	else:
		return "no"

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 3
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 7
enter number row2 : 5
'no'
>>> chess_table()
enter number column : 8
enter number row : 1
enter number column2 : 7
enter number row2 : 1
'no'
>>> chess_table()
enter number column : 8
enter number row : 1
enter number column2 : 8
enter number row2 : 2
'no'
>>> chess_table()
enter number column : 8
enter number row : 1
enter number column2 : 7
enter number row2 : 2
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
'no'
>>> chess_table()
enter number column : 8
enter number row : 1
enter number column2 : 7
enter number row2 : 1
'no'
>>> chess_table()
enter number column : 8
enter number row : 1
enter number column2 : 7
enter number row2 : 2
Yes
'no'
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	else:
		return "no"

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
Yes
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 3
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
'no'
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if t == n and s == p + 1:
		print("Yes")
	if n == t - 1 and p == s:
		print("Yes")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
no
>>> chess_table()
enter number column : 9
enter number column : 90
enter number column : 2
enter number row : 3
enter number column2 : 2
enter number row2 : 2
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 6
enter number row2 : 8
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if t - n == 0 and s == p + 1:
		print("Yes")
	if n == t - 1 and p - s == 0:
		print("Yes")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	if n == t + 1 and s == p:
		print("Es")
	if n == t and s == p - 1:
		print("eys")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
eys
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
Es
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 1
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 3
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 3
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
Yes
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
Es
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
eys
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	if n == t + 1 and s == p:
		print("Es")
	if n == t and s == p - 1:
		print("eys")
	else:
		print('no')

		
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 5
enter number row2 : 6
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 1
enter number row2 : 6
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 6
enter number row2 : 1
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 9
enter number column2 : 6
enter number row2 : 4
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	if n == t + 1 and s == p:
		print("Es")
	if n == t and s == p - 1:
		print("eys")
	else:
		print('no')
	return 0

>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
eys
0
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	if n == t + 1 and s == p:
		print("Es")
	if n == t and s == p - 1:
		print("eys")
	else:
		print('no')
	return

>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
eys
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
Yes
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p -1:
		print("Yes")
	if n == t - 1 and s == p + 1:
		print("Yes")
	if n == t + 1 and s == p - 1:
		print("Yes")
	if n == t and s == p + 1:
		print("Yes")
	if n == t - 1 and s == p:
		print("Yes")
	if n == t + 1 and s == p:
		print("Es")
	if n == t and s == p - 1:
		print("eys")
	else:
		return print("no")

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
eys
>>> chess_table()
enter number column : 2
enter number row : 2
enter number column2 : 2
enter number row2 : 7
no
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
Yes
no
>>> 
=============================== RESTART: Shell ===============================
>>> def chess_table():
	while True:
		t = int(input("enter number column : "))
		if t > 8:
			continue
		else: break
	while True:
		p = int(input("enter number row : "))
		if p > 8:
			continue
		else: break
	while True:
		n = int(input("enter number column2 : "))
		if n > 8:
			continue
		else: break
	while True:
		s = int(input("enter number row2 : "))
		if n > 8:
			continue
		else: break
	if n == t + 1 and s == p + 1:
		return "yes"
	if n == t - 1 and s == p -1:
		return "yes"
	if n == t - 1 and s == p + 1:
		return "yes"
	if n == t + 1 and s == p - 1:
		return "yes"
	if n == t and s == p + 1:
		return "yes"
	if n == t - 1 and s == p:
		return "yes"
	if n == t + 1 and s == p:
		return "yes"
	if n == t and s == p - 1:
		return "yes"
	else:
		return "no"

	
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 2
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 5
enter number row2 : 4
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 5
enter number row2 : 7
'no'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 2
enter number row2 : 3
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 3
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 1
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 3
enter number row2 : 1
'yes'
>>> chess_table()
enter number column : 3
enter number row : 2
enter number column2 : 4
enter number row2 : 2
'yes'
>>> 
