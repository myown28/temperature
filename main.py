#~~~ IMPORT ~~~
import os
import time

#~~~ DEF ~~~
def clear1():
    os.system('cls')

#~~~ LIST ~~~
list1 = """1)Calsius °C 
2)Fahrenheit °F
3)Kelvin K
4)Rankine °R
5)Réaumur °Re\n"""

#~~~ MAIN-CODE ~~~
while True:
    try:
        clear1()
        a1 = int(input(list1))
        if a1 == int('1'):
            clear1()
            print(list1)
            a2 = int(input("Calsius °C into\n"))
            if a2 == int('1'):
                clear1()
                print("Calsius °C into Calsius °C")
                cf1 = float(input("Calsius = "))
                cf2 = cf1
                print(f"{cf1}°C is {cf2}°C")
                input('enter for exit')
            elif a2 == int('2'):
                clear1()
                print("Calsius °C into Fahrenheit °F")
                cf1 = float(input("Calsius = "))
                cf2 = float(cf1) * float(1.8) + float(32)
                print(f"{cf1}°C is {cf2}°F")
                input('enter for exit')
            elif a2 == int('3'):
                clear1()
                print("Calsius °C into kelvin K")
                cf1 = float(input("Calsius = "))
                cf2 = float(cf1) + float(273.15)
                print(f"{cf1}°C is {cf2} K")
                input('enter for exit')
            elif a2 == int('4'):
                clear1()
                print("Calsius °C into Rankine °R")
                cf1 = float(input("Calsius = "))
                cf2 = float(cf1) * float(1.8) + float(491.67)
                print(f"{cf1}°C is {cf2}°R")
                input('enter for exit')
            elif a2 == int('5'):
                clear1()
                print("Calsius °C into Reaumur °Re")
                cf1 = float(input("Calsius = "))
                cf2 = float(cf1) / float(1.25)
                print(f"{cf1}°C is {cf2}°Re")
                input('enter for exit')
        elif a1 == int('2'):
            clear1()
            print(list1)
            a2 = int(input("Fahrenheit °F into\n"))
            if a2 == int('1'):
                clear1()
                print("Fahrenheit °F into Calsius °C")
                cf1 = float(input("Fahrenheit = "))
                cf2 = (float(cf1) - float(32)) / float(1.8)
                print(f"{cf1}°F is {cf2}°C")
                input('enter for exit')
            elif a2 == int('2'):
                clear1()
                print("Fahrenheit °F into Fahrenheit °F")
                cf1 = float(input("Fahrenheit = "))
                cf2 = cf1 
                print(f"{cf1}°F is {cf2}°F")
                input('enter for exit')
            elif a2 == int('3'):
                clear1()
                print("Fahrenheit °F into Kelvin K")
                cf1 = float(input("Fahrenheit = "))
                cf2 = (float(cf1) + float(459.67)) * (float(5) / float(9))                
                print(f"{cf1}°F is {round(cf2, 3)} K")
                input('enter for exit')
        else:
            print('not found')
            time.sleep(1)

    except ValueError:
        print('not found error')
        time.sleep(1.5)
    except KeyboardInterrupt:
        print('not found error')
        time.sleep(1.5)

