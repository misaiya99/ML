#coding ="utf-8"
#KNN 算法测试
#
from  sklearn import  neighbors
from  sklearn import  datasets

KNN= neighbors.KNeighborsClassifier()
iris_data=datasets.load_iris()
print(iris_data)
KNN.fit(iris_data.data,iris_data.target)
pre=KNN.predict([[ 4.8,  3. ,  1.4,  0.1]])
pre1=KNN.predict([[ 5.9,  3. ,  5.1,  1.8]])
print("dad",pre)
print("2",pre1)
