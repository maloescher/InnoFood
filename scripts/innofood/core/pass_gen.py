import random
import string

def generate():
    alphabet = list(string.ascii_lowercase)
    password = ''
    for symbol in range(6):
        password = password + random.choice(alphabet)

    return password
