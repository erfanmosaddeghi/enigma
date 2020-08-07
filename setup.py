from enigma import enigma

eni = enigma()

count = int(input("Please Enter count rotors: "))

plugboard = {'a':'d','e':'y','آ':'s','r':'ب'}

eni.setup(count,plugboard)