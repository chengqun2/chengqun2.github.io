## Machine-learning
### Face-recognition
1. Making our image black and white because we don’t need color data to find faces.
2. We break up the image into small squares of 16x16 pixels each. Also called `Histogram of Oriented Gradients`.
3. Use `face landmark estimation` algorithm to solve `different directions look totally different` issue.
The basic idea is we will come up with 68 specific points (called landmarks) that exist on every face — the top of the chin, the outside edge of each eye, the inner edge of each eyebrow, etc.
4. Measure features of the face in 128 measurements for each person and save.
5. Looking at all the faces we’ve measured in the past, see which person has the closest measurements to our face’s measurements. 

### 算法:  朴素贝叶斯 VS 支持向量机
朴素贝叶斯的优点：
    原理简单，容易实现。
    适用于各种规模的数据集。
    运行速度快，适合实时预测。
    在某些情况下，准确性比其他分类器更好，需要更少的训练数据。
朴素贝叶斯的缺点：
    假设特征之间相互独立，这在实际中不一定成立。
    零概率问题：如果某个特征在训练集中没有出现过，会导致概率结果为零。
支持向量机的优点：
    可以处理非线性问题。
    对离群值敏感。
    在多分类问题上表现良好。
支持向量机的缺点：
    计算复杂度较高。
    需要调优参数。
    对大规模数据集不太适用。

### 分词器: HanLP分词 VS 二元组分词
二元组分词是一种简单快速的分词算法，适用于简单的分词任务和对实时性要求较高的场景；
HanLP 提供了更为复杂和高级的分词算法，能够克服二元组分词的一些局限性，在准确度和应用范围上有一定的优势。具体选择哪种算法取决于具体的应用需求和场景特点。


