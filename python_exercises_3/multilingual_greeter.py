"""
Add a function called language_input that gives the user an option to choose 1 of at least 3 languages.
Ask the user for his name in the chosen language.
Greet the user in the chosen language.
"""

# language input
def language_selection():
	global selection
	selection = int(input("Enter 1 for English, 2 for Spanish, 3 for French"))


language_selection()

# get name input with language specific prompt based off language selection
def name_input():
	global name
	if selection == 1:
		name = input("Please enter your name")
	elif selection == 2:
		name = input("Por favor ingrese su nombre")
	elif selection == 3:
		name = input("Veuillez saisir votre nom")

name_input()

# print greeting based off language selection
def greet():
	if selection == 1:
		print("Hello " + str(name))
	elif selection == 2:
		print("Hola " + str(name))
	elif selection == 3:
		print("Bonjour " + str(name))

greet()
