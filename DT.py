import  math
import  numpy as np
import copy
import  operator
def splitDataSet(dataset, feat, value):
    retDataSet = []
    for featVec in dataset:
        if featVec[feat] == value:
            reducedFeatVec = featVec[:feat]
            reducedFeatVec.extend(featVec[feat + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
def shang(data1):
    label={}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in label.keys():
            label[currentLabel] = 0
        label[currentLabel] += 1

    num_shang=0.0
    for key in label:
        pro =float(label[key]/len(data1))
        if pro !=0:
            num_shang += -pro*math.log(pro,2)
    return num_shang
def best_feature(dataset):
    '''
    :param data: 传入数据，计算信息增益
    :return: 返回最好的分裂特征的标签
    '''
    #特征长度为
    f_length=len(dataset[0])-1
    #类别：
    class1=[x[-1] for x in dataset]
    bestInfoGain=0.0
    bestFeat=-1
    num_class=set(class1)
    base_shang=shang(dataset)

    for i in range(f_length):
        featValues = [example[i] for example in dataset]
        #某个求属性可能的值
        uniqueFeatValues = set(featValues)
        newEntropy = 0.0
        for value in uniqueFeatValues:
            #返回分割的子集,得到由i 的特征值等于 value 的子集（value所在列剔除）
            subDataSet = splitDataSet(dataset, i, value)
            #计算子集上的熵

            prob = len(subDataSet) / float(len(dataset))
            newEntropy += prob *  shang(subDataSet)
        if (base_shang - newEntropy)>bestInfoGain:
            bestInfoGain=base_shang - newEntropy
            bestFeat = i
    return bestFeat
def classify(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
        sortedClassCount =sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
    return  sortedClassCount[0][0]
features=['no surfacing','flippers']
def growDT(dataset,features):
    classList = [example[-1] for example in dataset]
    print("bestFeatLabel",classList[0])
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:  # no more features
        return classify(classList)

    I = best_feature(dataset)
    print(I)+
    bestFeatLabel = features[I]
    DT = {bestFeatLabel: {}}
    print(bestFeatLabel)
    #value=dataset[:][I]
    value = [example[I] for example in dataset]
    uni_value=set(value)
    #del (features[I])
    for values in uni_value:
        subDataSet = splitDataSet(dataset, I, values)
        DT[bestFeatLabel][values] = growDT(subDataSet,features)
    #features.insert(I, bestFeatLabel)

    return DT

if __name__ =="__main__":
    dataset = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    best_feature(dataset)
    tree=growDT(dataset,features)
    print(tree)