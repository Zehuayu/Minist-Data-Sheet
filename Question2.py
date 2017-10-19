#Output an image to the console




import Question1  # catch  the training set
import numpy as np

def Question1Image(no):
    myimage = Question1.train_images[no]
    myimage = np.array(myimage)
    return myimage



# print image to console
def printImage(myimage):
    for row in myimage:
        for col in row:
            print('.' if col<=127 else '$',end='')  #less than 128 
        print()

number = 3 #type a number in number
printImage(Question1Image(number))
