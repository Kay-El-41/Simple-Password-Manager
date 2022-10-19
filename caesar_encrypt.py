from cmath import exp
import json

s_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

import random

class Cipher:
    def __init__(self) -> None:
        self.Eshiftkey = (random.randint(1, 21))%26

    def caesar_cipher(self, forwhat:str, text:str, action:str) -> str:
        '''returns the input text into encrypted, or decrypted text
        don't forget to call add_key_function after encyrpting'''
        cipher_text=""
        if action == "D":
            self.Dshiftkey = int(self.cipher_get_key(forwhat))

        for letter in text:
            if letter in s_alphabet:
                look_list = s_alphabet
                index_x = look_list.index(letter)
            elif letter in c_alphabet:
                look_list = c_alphabet
                index_x = look_list.index(letter)
            else:
                cipher_text += letter

            if letter in s_alphabet or letter in c_alphabet:
                if action == 'E':
                    cipher_text += look_list[index_x + self.Eshiftkey]
                if action == 'D':
                    cipher_text += look_list[index_x - self.Dshiftkey]
                
        return cipher_text


    def cipher_get_key(self,forname:str):
        '''Get shift key for text decrypting,
        param = forname: WEBSITE NAME'''
        with open(file='data_saved/cipher_cache.json') as cache:
            return (json.load(cache)[forname]['load'])

    def cipher_add_key(self,forname:str):
        '''Save new shift key after encrypting
        param = forname: WEBSITE NAME'''
        new_data = {
            forname: {
                "load":self.Eshiftkey,
                }
        }
        try:
            with open(file='data_saved/cipher_cache.json') as cache:
                data = json.load(cache) # Load Data
                data.update(new_data) # Update Data
            with open(file='data_saved/cipher_cache.json', mode='w') as cache:
                json.dump(data, cache, indent=4) # Save Updated Data
        except FileNotFoundError:
             with open(file='data_saved/cipher_cache.json', mode='w') as cache:
                json.dump(new_data, cache, indent=4)
