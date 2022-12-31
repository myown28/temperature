#~~~ TEMOERATURE ~~~
#~~~ IMPORT ~~~
import os
import time

#~~~ CLASS & DEF ~~~

class celsius:
    def fahrenheit():
        print("Calsius ℃ to Fahrenheit ℉")
        try:
            a1 = float(input("Calsius ℃"))
        except ValueError:
            print("not-found")
           # continue
        else:
            print('not')
           # break
        a2 = float(a1) * float(1.8) + float(32)
        print(f"{a1}℃ is {a2}℉")

#~~~ MAIN-CODE ~~~
#while True:
#    try:
#      a1 = float(input('number'))
#    except ValueError:
#        print('not found')
#    else:
#        break

def clear():
    os.system('cls')

list1 = """1)Calsius ℃ 
2)Fahrenheit ℉
3)Kelvin\n"""

try:
    clear()
    a1 =  int(input(list1))
except ValueError :
    clear()
    print('not found\n')
except KeyboardInterrupt:
    clear()
    print('KeyboardInterrupt')
else:
    try:
      if a1 == int('1'):
         clear()
         print(list1)
         a2 = int(input("Calsius ℃ into\n"))
    except ValueError :
      clear()
      print('not found\n')
    except KeyboardInterrupt:
      clear()
      print('KeyboardInterrupt')
    else:
        try:
         if a2 == int('2'):
            clear()
            print("Calsius ℃ into Fahrenheit ℉")
            cf1 = input("Calsius = ")
            cf2 = float(cf1) * float(1.8) + float(32)
            print(f"{cf1}℃ is {cf2}℉")
        except ValueError :
            clear()
            print('not found\n')
        except KeyboardInterrupt:
            clear()
            print('KeyboardInterrupt')
        else:
            input('enter for exit')



        

