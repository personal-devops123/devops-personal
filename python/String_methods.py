String Methods
---------------
Syntax : Stringobject.methodname()
1. upper()
2. lower()
3. Swapcase()
4. title()
5. capitalize()
6. lstrip()
7. rstrip()
8. strip()
9. ljust()
10. rjust()
11.startswith()
12. endswith()
13. count()
14. find()
15. rfind()
16. index()
17. rindex()
18. replace()
19. split()
20. rsplit()
21. join()

String validation functions

22. islower()
23. isupper()
24. isalpha()
25. isdigit()
26. isalnum()
27. istitle()
28. isspace()

29. ord() : It return given character Ascci value
eg : print(ord('A'))

30. chr() : It reurns given Ascii code character.
eg: print(chr(65))

dir() : It displays gien object all properties and methods.
syntax :  dir(objectname)
eg : x="Tecnosoft"
      print(dir(x))

help() : It displays given method help
Syntax : help(objectname.methodname)

eg  :  x="tecnosoft"
print(help(x.count))
#___________________________________________________
>>> x="tecno"
>>> x.upper() #'TECNO'
>>>
>>> x="TECNO"
>>> x.lower() # 'tecno'
>>>
>>> x="TecNOsoFt"
>>> x.swapcase() # 'tECnoSOfT'
>>>
>>> x="hello good evening to all"
>>> x.title() # 'Hello Good Evening To All'
>>>
>>> x="hello good evening to all"
>>> x.capitalize() # 'Hello good evening to all'
_____________________________________________
>>> x="tecno"
>>> x.ljust(10,'*') # 'tecno*****'
>>>
>>> x.ljust(3,'*') # 'tecno'
>>>
>>> x.rjust(10,'*') # '*****tecno'
>>>
>>> x.ljust(10,'*').rjust(15,'*') #'*****tecno*****'
____________________________________________________________

>>> x="tecnosoft"
>>> x.startswith("tec") # True
>>> x.startswith("soft") # False
>>> x.endswith("soft") # True
>>>
>>> x="a1.py"
>>> x.endswith(".py") #True
>>>
__________________________________________________

>>> x="    tecno   soft     "
>>> x.lstrip() # 'tecno   soft     '
>>>
>>> x.rstrip() # '    tecno   soft'
>>>
>>> x.strip() # 'tecno   soft'
>>>
>>> x="tecnosoft"
>>> x.lstrip('t') # 'ecnosoft'
>>> x.lstrip('n') # 'tecnosoft'
>>> x.rstrip('t') #'tecnosof'
>>> x.strip('t') # 'ecnosof'
>>>
_______________________________________________________
>>> x="hello python python is simple python is easy"
>>> x.count("python") # 3
>>> x.count("o") # 4
>>> x.count("unix") #
______________________________________________
>>> x="hello python python is simple python is easy"
>>> x.find("python") # 6
>>> x.find("python",7) # 13
>>> x.find("python",14) # 30
>>> x.find("python",10,25) # 13
>>> x.rfind("python") # 30
>>> x.find("unix") # -1


>>> x="hello python python is simple python is easy"
>>> x.index("python") # 6
>>> x.index("python",7) # 13
>>> x.index("python",14) # 30
>>> x.index("python",10,25) # 13
>>> x.rindex("python") # 30
>>> x.index("unix") # ValueError: substring not found

Note : find and index methods are same but if the given element not found ,
the find() method returns "-1" whereas
index() method raise "ValueError" exception


>>> x="hello python python is simple python is easy"
>>>
>>> x.replace("python","tecno") # 'hello tecno tecno is simple tecno is easy'
>>>
>>> x.replace("python","tecno",1) # 'hello tecno python is simple python is easy'
>>>
>>> x.replace("python","tecno",2) # 'hello tecno tecno is simple python is easy'
>>>
>>> x.replace("python","") # 'hello   is simple  is easy'
>>>
>>> x.replace("python","",1) # 'hello  python is simple python is easy'
______________________________________________
>>> x="python is simple and easy to learn"
>>> y=x.split() # 
>>> y # ['python', 'is', 'simple', 'and', 'easy', 'to', 'learn']
>>> len(y) # 7
>>> a="101,Hari,Manager,90000,10"
>>> b=a.split(",")
>>> b # ['101', 'Hari', 'Manager', '90000', '10']
>>>
>>> b=a.split(",",1)
>>> b # ['101', 'Hari,Manager,90000,10']
>>>
>>> b=a.split(",",2)
>>> b # ['101', 'Hari', 'Manager,90000,10']
>>>

>>> a="101,Hari,Manager,90000,10"
>>> b=a.rsplit(",")
>>> b # ['101', 'Hari', 'Manager', '90000', '10']
>>> b=a.rsplit(",",1)
>>> b # ['101,Hari,Manager,90000', '10']
>>>
>>> b=a.rsplit(",",2)
>>> b # ['101,Hari,Manager', '90000', '10']
>>>


>>> x=['unix','python','aws','django','sql']
>>> y=":".join(x)
>>> print(y,type(y)) # unix:python:aws:django:sql <class 'str'>
>>>
>>> y="".join(x)
>>> y # 'unixpythonawsdjangosql'
>>>
>>> y="\n".join(x)
>>> print(y)
unix
python
aws
django
sql
>>>
___________________________________
>>> a="tecno"
>>> b="TECNO"
>>> c="TecNoSoFt"
>>> d="12345"
>>> x="abc123"
>>> y="abc123@"
>>> a.islower() # True
>>> b.islower() # False
>>> b.isupper() # True
>>> c.isalpha() # True
>>> x.isalpha() # False
>>>
>>> d.isdigit() #True
>>> x.isdigit() #False
>>> x.isalnum() # True
>>> c.isalnum() # True
>>> d.isalnum() #True
>>> y.isalnum() # False
>>>
    

>>> x="Hello Good Evening To All"
>>> x.istitle() # True
>>>
>>> x="Hello good Evening to All"
>>> x.istitle() # False
>>>

>>> x=" "
>>> x.isspace() # True
>>> x="\t"
>>> x.isspace() # True
>>> x="\n" 
>>> x.isspace() # True
>>>
>>> x="      \t \t      \n         "
>>> x.isspace() # True
>>>
>>> x="      \t \t  p    \n         "
>>> x.isspace() # False
>>>

#________________________________________________
