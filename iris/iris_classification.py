from sklearn import datasets
import numpy as np
from sklearn import svm
clf = svm.LinearSVC()
iris = datasets.load_iris()
clf.fit(iris.data, iris.target)
'''
print np.unique(iris.target)'''
print clf.predict([[ 5.0,  3.6,  1.3,  0.25]])