import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation
import os, sys
import scipy as SciPy

reconstructed_model = keras.models.load_model("my_model")

def get_result(result):
    if result[0][0] == 1:
        return('a')
    elif result[0][1] == 1:
        return ('b')
    elif result[0][2] == 1:
        return ('c')
    elif result[0][3] == 1:
        return ('d')
    elif result[0][4] == 1:
        return ('e')
    elif result[0][5] == 1:
        return ('f')
    elif result[0][6] == 1:
        return ('g')
    elif result[0][7] == 1:
        return ('h')
    elif result[0][8] == 1:
        return ('i')
    elif result[0][9] == 1:
        return ('j')
    elif result[0][10] == 1:
        return ('k')
    elif result[0][11]
    
     == 1:
        return ('l')
    elif result[0][12] == 1:
        return ('m')
    elif result[0][13] == 1:
        return ('n')
    elif result[0][14] == 1:
        return ('o')
    elif result[0][15] == 1:
        return ('p')
    elif result[0][16] == 1:
        return ('q')
    elif result[0][17] == 1:
        return ('r')
    elif result[0][18] == 1:
        return ('s')
    elif result[0][19] == 1:
        return ('t')
    elif result[0][20] == 1:
        return ('u')
    elif result[0][21] == 1:
        return ('v')
    elif result[0][22] == 1:
        return ('w')
    elif result[0][23] == 1:
        return ('x')
    elif result[0][24] == 1:
        return ('y')
    elif result[0][25] == 1:
        return ('z')

if __name__ == '__main__':
    if len(sys.argv) > 0:
        testFileCase = sys.argv[1]
        testFileNum = sys.argv[2]

        modelPath = os.path.join('/home/dai/Downloads/ReadAlphabet/','my_model') 

        reconstructed_model = keras.models.load_model(modelPath)
        
        testFilePath = r'/home/dai/Downloads/ReadAlphabet/'

        if testFileCase == 'a':
            FilePath = os.path.join(testFilePath, 'aa')
        elif testFileCase == 'b':
            FilePath = os.path.join(testFilePath, 'bb')
        elif testFileCase == 'c':
            FilePath = os.path.join(testFilePath, 'cc')

        filename = os.path.join(FilePath, '{}.png'.format(testFileNum))

        test_image = image.load_img(filename, target_size = (32,32))
        plt.imshow(test_image)
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)

        result = reconstructed_model.predict(test_image)
        result = get_result(result)
        print ('Predicted Alphabet is: {}'.format(result))
