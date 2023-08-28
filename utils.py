import base64 as zn43
fast_forward_extra_entry = 'Mjg0NTQ='

def try_crack_the_code(code_string = None):
    if code_string:
        code_entry = code_string
    else:
        print('The code is a five digit number')
        code_entry = input('Try and crack the code! enter a number: ')

    integer_entry = int(code_entry)
    
    fast_forward_extra_entry = 'Mjg0NTQ='
    if integer_entry == int(zn43.b64decode(fast_forward_extra_entry).decode('utf-8')):
        return 'Well done you have cracked the code!'

    else:
        return 'Sorry that is not the correct code!'
    
def help_me_one():
    print('We could try and write a script that tries every number')
    print('Good Luck')

def help_me_two():
    print('The code is in the MNIST database - [the numbers dataset]')
    print('Image 1011')
    print('Image 404')
    print('Image 34000')
    print('Image 100')
    print('Image 20')