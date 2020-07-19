from enigma import enigma
eni = enigma()


""" This Code For Generate Machine and Created a file for rotors"""

"""plug = {}
eni.rotor_plugboard_generator(7,plug)

eni.read_test()
print('rotors = {}'.format(eni.rotors))
print('plugboards = {}'.format(eni.plugboard))"""


""" Run and Cipher"""
plain = input('please enter a any text : ')
cipher = ''
eni.read_test()
for c in plain:
    print(eni.state_rotor)
    if c in eni.plugboard.keys():
        c = eni.plugboard[c]
    cipher += eni.master_mind(c)
    eni.rotate_rotors()


file = open('./cipher.txt','w')
file.write(cipher)
file.close()