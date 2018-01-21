from sklearn import datasets
from sklearn import neighbors, metrics
from sklearn.neighbors import KNeighborsClassifier as kNN
import matplotlib.pyplot as plt


Digits = datasets.load_digits()
Imglabels = [x for x in list(zip(Digits.images, Digits.target)) if x[1] == 7 or x[1] == 3]
for ind, (image, label) in enumerate(Imglabels[:4]):
    plt.subplot(2, 4, ind + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: label')
    plt.show()

num = len(Digits.images) #calculates number
imgs = Digits.images.reshape((num, -1))
labs = Digits.target

y_trainset, x_trainset = labs[:int(num*.7)].reshape(-1,), imgs[:int(num*.7)]
y_testset, x_testset= labs[int(num*.7):].reshape(-1,), imgs[int(num*.7):]

neighbor = kNN(n_neighbors=3)
neighbor.fit(x_trainset, y_trainset)

new_val = neighbor.predict(x_testset)

print("kNN classifirer reports: \n", neighbor, metrics.classification_report(y_testset, new_val))
print("Confusion matrix is: \n", metrics.confusion_matrix(y_testset, new_val))
