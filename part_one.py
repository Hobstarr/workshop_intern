print('Welcome to the workshop!')
print('This will be reasonably interactive')
print('Please enter the word password below to continue')
print('')

word_check = input('enter here: ')
if word_check == 'password':
    print('')
    print('Well Done!')
    print('')
    print("Now let's create a virtual environment")
    print("Please install requirements file - 'secret_req.txt'")
    print("You've made it to part_two.py")
    exit()

else:
    print("I'm sorry that wasn't the correct word, please try again!")
    exit()