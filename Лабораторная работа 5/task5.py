import random
import string
from random import sample

def get_random_password() -> str:
    password = ""
    length_ = 8
    words_ = string.ascii_letters + string.digits
    pass_ = "".join(sample(words_, length_))
    return pass_

print(get_random_password())