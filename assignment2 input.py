#ASSIGNMENT2
#--------------------------------------
#Q1
input_string = "Python is a case sensitive language"
#a)
print('Length of input string is:', len(input_string))
#b)
print('Reversed string is:',input_string[::-1])
#c)
print('New input string is:',input_string[10:26])
#d)
print('Changed string is:',input_string.replace("a case sensitive","object oriented"))
#e)
print('Index of "a" is:',input_string.find("a"))
#f)
print('New input string is:',input_string.replace(" ",""))
#___________________________________________________________________________________
#Q2
NAME='ARSH SHARMA'
SID='21103057'
DEPARTMENT='COMPUTER SCIENCE'
CGPA='9.9'
print(f'''Hey, {NAME} Here!
My SID is {SID}
I am from {DEPARTMENT} department and my CGPA IS {CGPA}''')
#_____________________________________________________________________________________
#Q3
a=56
b=10
#a)
print(a&b)
#b)
print(a|b)
#c)
print(a^b)
#d)
print(a<<2)
print(b<<2)
#e)
print(a>>2)
print(b>>4)
#_________________________________________________________________________________________
#Q4
print('Enter three numbers:')
number1=int(input('number1= '))
number2=int(input('number2= '))
number3=int(input('number3= '))
if (number1>number2):
    if(number1>number3):
     print('The greatest number is number1:',number1)
    else:
       print('The greatest number is number3: ',number3)
else:
    if (number2>number3):
       print('The greatest number is number2:',number2)
    else:  
      print ('The greatest number is number3:',number3)
#______________________________________________________________________________________________
#Q5
Statement=str(input('Enter a statement: '))
if 'name' in Statement:
 print('YES')
else:
 print('NO')
#python is a case sensitive language, so anything written other than 'name' would be given a no.
#____________________________________________________________________________________________
#Q6
lenght1 = int(input('lenght of first side: '))
lenght2 = int(input('lenght of second side: '))
lenght3 = int(input('lenght of third side: '))
if lenght1+lenght2>lenght3 and lenght2+lenght3>lenght1 and lenght3+lenght1>lenght2:
  print('yes')
else:
 print('no')
#_____________________________________________________________________________________________________________________________________________________________________________________________
