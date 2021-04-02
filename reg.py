import numpy as np
from scipy.optimize import minimize, differential_evolution

height_weigth = np.array([
                         [182, 82],
                         [169, 70],
                         [159, 48],
                         [192, 87],
                         [185, 100],
                         [166, 50],
                         [170, 51],
                         [180, 69],
                         [155, 44],
                         [201, 138]])
 
gender = np.vstack([1, 1, 0, 1, 1, 0, 0, 0, 0, 1])

'''def loss(arr, hw, g):
    *a, b = arr
    a = np.vstack(a)
    y0 = np.dot(hw, a) + b
    diff = np.mean(np.abs(y0 - g))
    return diff'''

def loss(arr, hw, g):
    a = arr[0:2]
    b = arr[2]
    c = arr[-2:]
    a = np.vstack(a)
    c = np.vstack(c)
    y0 = b + np.dot(hw, a) + np.dot(hw**2, c)
    diff = np.mean(np.abs(y0 - g))
    return diff

def main():
    bounds = [(-100, 100), (-100, 100), (-100, 100), (-100, 100), (-100, 100)]
    res = differential_evolution(loss, bounds, args=(height_weigth, gender), workers=4)
    #res = minimize(loss, [0, 0, 0, 0, 0], args=(height_weigth, gender), method='COBYLA')
    print(res)

if __name__ == '__main__':
    main()
