try:
    import numpy as np
    np_response = np.round(5.2)

finally:
    if np_response == 5:
        print('Well done installed correctly')
        print("Let's look at part_three.py")
        
    else:
        print("Sorry you haven't installed the requirements file")
        print("Please ensure you have created a virtual environment")
        print("and installed 'secret_req.txt' requirements file.")
        exit()