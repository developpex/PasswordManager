import string
from random import choice, randint, shuffle
import pyperclip

class Password:
    def __init__(self, length_letters=None, length_nums=None, length_syms=None):
        self.letters = string.ascii_letters
        self.numbers = string.digits
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        self.length_letters = length_letters or randint(6, 8)
        self.length_nums = length_nums or randint(2, 4)
        self.length_syms = length_syms or randint(2, 4)

    def generate(self) -> str:
        password_list = (
            [choice(self.letters) for _ in range(self.length_letters)] +
            [choice(self.numbers) for _ in range(self.length_nums)] +
            [choice(self.symbols) for _ in range(self.length_syms)]
        )
        shuffle(password_list)
        return "".join(password_list)