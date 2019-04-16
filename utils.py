import numpy as np

def preprocess(data):
        cropped = data[34:194, :, :]
        reduced = data[0:-1:2, 0:-1:2]
        grayscale = np.sum(reduced, axis=2)
        bw = np.zeros(grayscale.shape)
        bw[grayscale != 233] = 1
        return np.expand_dims(bw, axis=2)
