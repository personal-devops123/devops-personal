Tuple
=====
1. It is same as list but the elements are immutable
2. The elements must enclose within ()
3. The elements are write protected.
4. Tuple gives good performance over list.

1. Creating a tuple
===================
1. a=(10,20,30,40,50,60)
2. b=(10,2.3,'unix')
3. days=('mon','tue','wed','thu','fri','sat','sun')
4. x=(10) # integer
5. y=(10,) # tuple
6. x=10,20,30,40 # tuple

1. Accessing elements
====================
1. print(a) # (10,20,30,40,50)
print(type(a)) # tuple

2. a[2] # 30
   a[-1] # 60
   a[:] # (10,20,30,40,50,60)
   a[::2] # (10,30,50)
   a[::-1] # (60,50,40,30,20,10)

3. a[2]=300   X TypeError
4. del a[1]  X
5. a.append(100)  X

6. for  i  in  x :
        print(i)

7.   for  i,j  in  enumerate(x) :
            print(i+1,":",j)

8. x=('unix','perl','python')

list()
-----

1. x=list(x)
print(type(x)) # 'list'

2.x[1]='Aws'
x.append('data science')

tuple()
-------
x=tuple(x)
type(x) # 'tuple'

#_________________________________________________________________
Set
===
1. It is also collection of elements.
2. The elements must enclose within {}.
3. It is an unordered list
4. It doesn't support item indexing,item assignment and item deletion.
5. It holds unique values i.e it eleminates duplicates.
6. It is mutable object.
7. It allows to do mathematical operations like union,intersect,minus and
symmetric difference.


1)  Creating a set
------------------
1. a={10,20,30,40,50,60}

(or)

a=set([10,20,30,40,50,60])

2. b=set()  # Empty set
 
2) Accessing elements
----------------------
1. print(a)  #  {40, 10, 50, 20, 60, 30}

print(type(a)) # <class 'set'>


3) Set methods
===============
1. add()

a.add(100)
a.add(10)
a.add(10)
a.add(10)
a.add(30)
a.add(300)
a.add(30)
a.add(30)
a.add(30)
print(a) # {100, 40, 10, 300, 50, 20, 60, 30}

2. pop() : It deletes and returns first element from the unorderd list



>>> a.pop()  # 100
>>> a.pop() # 40

3. remove() : It removes given element,if element not found raises
KeyError Exception

>>> a.remove(50)

>>> a.remove(50) # KeyError: 50

4. discard() : It also removes gien element,if element not found it
won't show any error
>>> a.discard(300)
>>> a.discard(300)

5. copy() : To copy set
>>> b=a.copy()

6. clear() : It removes all elements
>>> b.clear()
>>> print(b) # set()

Set  Operations
===============
a={10,30,40,60}
b={10,20,40,50}

1. union(|)
c=a|b  # a.uion(b)
print(c)  #  set([10,30,40,60,20,50])

2. intesect ( & )
c=a&b # a.intersection(b)
print(c) # set([10,40])

3. minus(-)

1. c=a-b # a.difference(b)
print(c) # set([30,60])
2. c=b-a # b.difference(a)
print(c) # set([20,50])

4. Symmetric difference( ^)
c=a^b # a.symmetric_difference(b)
print(c) # set([30,60,20,50])

How to eleminate duplicat values from a list
----------------------------------------------
x=[10,20,30,20,30,40,10,20,50,40,30,20,30,40,50,10]
>>> x=sorted(list(set(x)))
>>> print(x)
[10, 20, 30, 40, 50]

___________________________________________
frozenset  :  It is same as set but the elements are immutable.frozenset() is
the funtion to create frozenset.


>>> a=frozenset([10,20,30,40,50,60])
>>> type(a) # <class 'frozenset'>
>>> print(a) # >>> a=frozenset([10,20,30,40,50,60])

1. a[2]=300  X
2. a.add(100)  X
3. a.pop() X


#_________________________________________________________
Dictionary
==========
1. It is a group of key pair values
2. The elements must enclose within {}
3. It is mutable object.
4. Keys must be unique.
5. Dictionary gives good performance over list.
6. Using key ,we can retrive its value but not vice verse

1. Creating a dictionary
=========================
>>> d1={'ap':'hyd','tn':'chennai','kn':'bangalore'}
>>> d2={'unix':3000,'python':50000,'aws':90000}
>>> d3={10:'acc',20:'it',30:'sales'}
>>> d4={'A':65,'B':66,'C':67,'D':68}
>>> d5={} # empty dictionary

2. Accessing key pair values
============================
1.print(d1)#{'ap': 'hyd', 'tn': 'chennai', 'kn': 'bangalore'}
print(type(d1)) # <class 'dict'>
>>> d1['tn'] # 'chennai'
>>> d2['python'] # 50000
>>> d3[20] # 'it'

3. Adding key pairs
===================
d1['up']='lucknow'
d2['sql']=3000

4. Modifying key pairs
======================
d1['ap']='amaravathi'
d2['unix']=5000

5. Deleting key pairs
=====================
del  d1['tn']
del  d2['aws']
del    d3  #  It deletes a dictionary
print(d3)  X NameError


6. Dictionary methods
=====================
1. keys() : returns only keys
>>> d1.keys()  # ['ap', 'tn', 'kn']

2.values() : returns only  values
>>> d1.values() # ['amaravthi', 'chennai', 'bangalore']

3.items() :  returns keys and values
>>> d1.items() # [('ap', 'amaravthi'), ('tn', 'chennai'),
                    ('kn', 'bangalore')]


for   i   in  d1.keys() :
      print("Capital of ",i,"is : ",d1[i])

for   i,j   in  d1.items() :
       print("Capital of ",i,"is : ",j)

4. get() : It return given key value if not found no error,
and it allows to set default value.

d1.get('tn') # chennai
d1.get('up') # no error
d1.get('up','lucknow') # lucknow,it takes default value
d1.get('ap','amaravathi') # hyd,it takes its original value

5. pop() : It returns and deletes given key pair value, not found
raises KeyError exception.
d1.pop('kn') # bangalore

6. popitem() : It returns and deletes last key pair
d1.popitem()

7. update() : To append a dictionary

a={1:10,2:20}
a.update(d1)
print(a) # {1:10,2:20,'ap':'hyd','tn':'chennai', 'kn':'bangalore'}

8. copy() : To copy a dictionary
x=d1.copy()

9. clear() : To removes all key pairs
d1.clear()
print(d1) # {}


#_______________________________









