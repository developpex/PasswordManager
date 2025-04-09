import pytest
from logic.generator import Password

def test_generated_password_length():
    password = Password(length_letters=5, length_nums=3, length_syms=2).generate()
    assert len(password) == 10

def test_generated_password_has_letters():
    password = Password(length_letters=5, length_nums=0, length_syms=0).generate()
    assert any(char.isalpha() for char in password)

def test_generated_password_has_digits():
    password = Password(length_letters=0, length_nums=5, length_syms=0).generate()
    assert any(char.isdigit() for char in password)

def test_generated_password_has_symbols():
    password = Password(length_letters=0, length_nums=0, length_syms=5).generate()
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    assert any(char in symbols for char in password)
