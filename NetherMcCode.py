from colorama import init
from colorama import Fore, Back, Style

init()

print ( Fore.BLACK)
print( Back.CYAN )

what = input( "Что будем делать? (1.С ада в мир; 2. С мира в ад): " )

print( Back.YELLOW )

x = float( input("Введите x координату: ") )
z = float( input("Введите z координату: ") )

print( Back.GREEN )

if what == "1":
	c = x * 8
	d = z * 8
	print("x: " + str(c))
	print("z: " + str(d))
	print("Программа создана: H1KC_YT#1155")
elif what == "2":
	c = x / 8
	d = z / 8
	print("x: " + str(c))
	print("z: " + str(d))
	print("")
	print("Программа создана: H1KC_YT#1155")
else:
	print("Вы вписали не допустимый символ! Введите либо 1(С ада в мир) либо 2(С мира в ад)")

input()

