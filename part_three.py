print('Here we go:')
print("Let's look at our first dataset")

input_answer = input('Shall we look at our first dataset? Y/n - ')

if input_answer != 'Y':
    print("Exiting..... please enter Y if you'd like to see the dataset")
    exit()

else:
    print('Installing packages:')
    from keras.datasets import mnist
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    print('Loading MNIST dataset')
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    print('Feel free to look through this dataset')
    print('When finished, please continue on to the task')
    image_n = None
    while image_n != 'exit':
        image_n = input("Please choose a value 0-59999, 'exit', or 'continue' - ")
        
        if image_n in (str(x) for x in list(range(60000))):
            print(f'displaying image {image_n}:')
            print(f'displaying image {image_n}:')
            image_n = int(image_n)
            plt.imshow(x_train[image_n])
            plt.show()

        elif image_n == 'exit':
            print('Goodbye')
            exit()

        elif image_n == 'continue':
            print('Goodbye')
            break

        else:
            print('Please enter a valid entry')

    
