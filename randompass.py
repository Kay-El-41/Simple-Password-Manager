import random

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*']

class RandomPassword():
    def __init__(self) -> None:
        self.lett_count=random.randint(2,4)
        self.sym_count=random.randint(2,4)
        self.num_count=random.randint(2,4)
        self.pass_list=[]
        self.pass_Text=""

    def generate_random_password(self) -> str:
        '''Generate a random password'''
        for i in range(0,self.lett_count):
            self.pass_list.append(random.choice(alphabets))
        for i in range(0,self.sym_count):
            self.pass_list.append(random.choice(symbols))
        for i in range(0,self.num_count):
            self.pass_list.append(random.choice(numbers))
        random.shuffle(self.pass_list)
        for i in self.pass_list:
            self.pass_Text+=i
        return self.pass_Text