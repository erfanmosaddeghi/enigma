from enigma import enigma

eni = enigma()

count = int(input("Please Enter count rotors: "))

plugboard = {'a':'d','e':'y'}

eni.setup(count,plugboard)