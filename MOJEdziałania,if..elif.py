'''
    Equals: a == b  (równe)
    Not Equals: a != b (nie równe)
    Less than: a < b  (mniejsze od a)
    Less than or equal to: a <= b (mniejsze bądź równe a)
    Greater than: a > b (większe od a)
    Greater than or equal to: a >= b (większe bądź równe a)

Przykład w ćwiczenie.py
    PRZYKŁADY: 
'''

a = 33
b = 200
    if b > a:
    print("b is greater than a")



a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error 

'''
elif - The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
'''

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

'''
else - The else keyword catches anything which isn't caught by the preceding conditions.
'''

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

'''
Data Types
'''

Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: list, tuple, range

x = str("Hello World") 	sts	
x = int(20) 	int 	
x = float(20.5) 	float 	
x = complex(1j) 	complex 	
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple 	
x = range(6)

'''
Numbers
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

'''
Operators
'''

+ 	Addition 	x + y 	
- 	Subtraction 	x - y 	
* 	Multiplication 	x * y 	
/ 	Division 	x / y 	
% 	Modulus 	x % y 	
** 	Exponentiation 	x ** y 	
// 	Floor division 	x // y


'''
Lists
'''

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Ostatni item

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #Drugi item od końca

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #item od 2 do 5

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #Drugi item

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #len - ile jest liczb

#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

