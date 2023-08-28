from utils import try_crack_the_code, help_me_one, help_me_two
print('You will be trying to crack a code')

print(try_crack_the_code())
################### try_crack_the_code takes a 5 digit number
################### It then outputs two different strings,
################### when you guess correctly, you will
################### get the correct string.
################### - Part 5 requires the correct code to access.

print('')
print('')
print('Please open up this python file')
print('You can edit it how you like')
print('Your aim is to crack the code')

help_me = input('Do you need help? Y/n - ')
if help_me != 'Y':
    exit()
    
else:
    help_me_one()

    help_me_more = input('Do you need more help? Y/n - ')
    if help_me_more != 'Y':
        exit()

    else:
        help_me_two()
        exit()