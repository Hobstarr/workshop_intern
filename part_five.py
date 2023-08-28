import base64 as zn43
from utils import fast_forward_extra_entry
import time

pass_code = input('Please enter the code: ')

if pass_code != zn43.b64decode(fast_forward_extra_entry).decode('utf-8'):
    print("Incorrect, I'm sorry that wasn't the code")

else: 
    print("Correct, that was the code, let's get on to some Machine Learning")
    print('')
    print('')
    print()
    
    print('Installing packages:')
    from keras.datasets import mnist
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.ensemble import RandomForestClassifier
    sns.set_style('whitegrid')

    print('Loading MNIST dataset')
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    print('Data Processing...')
    x_train = np.reshape(x_train/255, (60000, 784))
    x_test = np.reshape(x_test/255, (10000, 784))

    print('Loading Model...')
    forest_clf = RandomForestClassifier()

    print('Training Model...')
    forest_clf.fit(x_train, y_train)

    print('...Done')
    print('')
    print('')
    print('Feel free to look through this dataset again')
    print('This time we will also make some predictions about what we see')
    print('We can continue past this to get some statistics about our model.')

    image_n = None
    while image_n != 'exit':
        image_n = input("Please choose a value 0-59999, 'exit', or 'continue' - ")
        
        if image_n in (str(x) for x in list(range(60000))):
            print(f'displaying image {image_n}:')
            image_n = int(image_n)
            plt.imshow(x_train[image_n].reshape(28,28))
            plt.title(f'Label: {y_train[image_n]}, Prediction: {forest_clf.predict(x_train[image_n].reshape(1,-1))[0]}')
            plt.axis('off')
            plt.show()

        elif image_n == 'exit':
            print('Goodbye')
            exit()

        elif image_n == 'continue':
            print('Goodbye')
            break

        else:
            print('Please enter a valid entry')

    print('')
    print('')
    print("How accurate was the model?")
    print("Let's check the accuracy...")
    
    preds = forest_clf.predict(x_train)
    correct_preds = [int(x == y) for x,y in zip(preds, y_train)]
    accuracy = np.sum(correct_preds) / len(correct_preds)
    print(f'The model achieved an accuracy of {accuracy:.2f}...')
    time.sleep(1)
    print(f'Is this good? What does this mean?...')
    time.sleep(3)
    print(f'...')
    time.sleep(3)
    print(f'Well... it achieved an accuracy of 100%... it must be good?')
    exit()