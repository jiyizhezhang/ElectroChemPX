import numpy as np

def one_hot_encode(X):
    encoded_X = X[:, 0:2].copy()  # Copy the first two columns

    solv = []
    elec = []

    for i in range(0, len(X)):
        solv_index = np.argmax(X[i, 2:6])
        solv_code = np.zeros_like(X[i, 2:6])
        solv_code[solv_index] = 1

        elec_index = np.argmax(X[i, 6:8])
        elec_code = np.zeros_like(X[i, 6:8])
        elec_code[elec_index] = 1

        solv.append(solv_code)
        elec.append(elec_code)

    solv = np.array(solv)
    elec = np.array(elec)

    encode_X = np.hstack((encoded_X, solv, elec))

    return encode_X


def one_hot_encode2(X):
    encoded_X = X[:, 0:5].copy()  # Copy the first two columns

    solv = []

    for i in range(0, len(X)):
        solv_index = np.argmax(X[i, 5:9])
        solv_code = np.zeros_like(X[i, 5:9])
        solv_code[solv_index] = 1

        solv.append(solv_code)

    solv = np.array(solv)

    encode_X = np.hstack((encoded_X, solv))

    return encode_X