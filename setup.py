from enigma import enigma

eni = enigma()

count = int(input("Please Enter count rotors: "))

plugboard = {}

eni.setup(count,plugboard)