import random
import pickle

class enigma:

    def __init__(self):
        self.alphabet_en = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet_en_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet_sign = ".:;’~`?,!@#$%^&*()[]{}'<>/\-_=+ 0123456789۰۱۲۳۴۵۶۷۸۹"
        self.alphabet_fa = "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        self.alphabets = self.alphabet_en + self.alphabet_fa + self.alphabet_sign + self.alphabet_en_big
        self.plugboard = {}
        self.count_rotors = ''
        self.rotors = []
        self.state_rotor = 0
        self.state_rotate = 0


    def reflector(self,character):
        """
        this is method for reflected characters
        this is work change character
        a <=> z
        b <=> y
        """
        return self.alphabets[len(self.alphabets) - self.alphabets.find(character) - 1]

    def rotor_plugboard_generator(self,count,dictionary):
        """
        this method for generate rotors by count input
        """
        if dictionary != None:
            self.plugboard.update(dictionary) # this just plugboard

        rotors = []
        for i in range(count):
            i = list(self.alphabets)
            random.shuffle(i)
            i = ''.join(i)
            rotors.append(i)

        with open('rotor_state.enigma','wb') as file:
            pickle.dump((rotors,self.plugboard),file)
            file.close()

    # just Testing for read file
    def read_test(self):
        with open('rotor_state.enigma','rb') as file:
            items = pickle.load(file)
            file.close()
            self.rotors = items[0]
            self.plugboard.update(items[1])

    
    def master_mind(self,x):
        """
        this is important method for enigma encode & decode ..
        """
        #print(f'rotors = > {self.rotors}')
        #print(f'plugboards = > {self.plugboard}')
        character = ''
        #print(character,'\n')

        character = self.rotors[0][self.alphabets.find(x)]
        #print(f'character of rotor[0] = {character}')
        
        for i in range(1, len(self.rotors)):
            character = self.rotors[i][self.alphabets.find(character)]
            #print(f'character of rotor[{i}] = {character}')

        character = self.reflector(character)
        #print(f'character reflector = {character}')

        for j in range(len(self.rotors),0,-1):
            character = self.alphabets[self.rotors[j-1].find(character)]
            #print(f'character of rotor[{j-1}] = {character}')

        #print(f'i = {i}, len rotors = {len(self.rotors)}')
        return character


    def rotate_rotors(self):
        """
        this method for rotate rotors
        """
        self.rotors[0] = self.rotors[0][1:] + self.rotors[0][0]
        self.state_rotate += 1
        if self.state_rotate % (len(self.alphabets) * (self.state_rotor + 1)) == 0:
            self.state_rotate = 0
            self.state_rotor += 1
            
            
            if self.state_rotor >= len(self.rotors):
                self.state_rotor = 0

            self.rotors[self.state_rotor] = self.rotors[self.state_rotor][1:] + self.rotors[self.state_rotor][0]
            

    def run(self,plain):
        """
                This Method for Run enigma machine 
                submit settings and options for start
        """
        cipher = ''
        self.read_test()
        for c in plain:
            print(self.state_rotor)
            if c in self.plugboard.keys():
                c = self.plugboard[c]
            cipher += self.master_mind(c)
            self.rotate_rotors()


        file = open('./cipher.txt','w')
        file.write(cipher)
        file.close()


    def setup(self,count_rotor,plugboard):
        """
                THIS METHOD FOR SETUP ENIGMA MACHINE &
                SAVE FILE FOR ENIGMA
        """
        self.rotor_plugboard_generator(count_rotor,plugboard)
        self.read_test()
        print('rotors = {}'.format(self.rotors))
        print('plugboards = {}'.format(self.plugboard))