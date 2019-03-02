from sklearn.decomposition import PCA
import numpy as np
import cv2


def rescale(img):
    height, width, depth = img.shape
    W = 900
    scaling = W / width
    X, Y = img.shape[1] * scaling, img.shape[0] * scaling

    return int(X), int(Y)
    j

def main():
    for num in range(1,3):
        print(num)
        image = cv2.imread(str(num) + '.jpg')
        copy = image.copy()
       
        h, w, d = image.shape
        img1 = np.reshape(image, (h, w * d))

        fit = PCA(350).fit(img1)
        img2 = fit.transform(img1)
        print(np.sum(fit.explained_variance_ratio_))
        x = fit.inverse_transform(img2)
        x = np.reshape(x, (h, w, d))
        result = np.uint8(x)
        resultCopy = result.copy()
        cv2.imwrite('quantizedImages/op-' + str(num) + '.jpg', result)

        copy = cv2.resize(copy, (rescale(image)))
        cv2.imshow("Original", copy)
        resultCopy = cv2.resize(resultCopy, (rescale(image)))
        cv2.imshow("Compressed", resultCopy)
        cv2.waitKey() 
