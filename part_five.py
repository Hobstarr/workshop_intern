import base64 as zn43
from utils import fast_forward_extra_entry

pass_code = input('Please enter the code: ')

if pass_code != zn43.b64decode(fast_forward_extra_entry).decode('utf-8'):
    print("Incorrect, I'm sorry that wasn't the code")

else: 
    print("Correct, that was the code, let's get on to some Machine Learning")
