import csv
import json
from functools import reduce
from deepmerge import always_merger, merge_or_raise
class NestedDict(dict):
    """Creat nested dict class."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def list2dict(a,b):
    rlt = {}
    if not a:
        rlt[b] = a
        return rlt
    rlt[b] = [a]
    return rlt
def csv2json(file_path):
    rlt = {}
    with open(file_path,encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
        rows[0].append([])
        first_row = rows[0][::-1]
        base_dict = reduce(list2dict, first_row)
        print(base_dict)
        #print(rows)
        for i in range(1,len(rows)):
            row = rows[i]
            for j in range(0,len(row)):
                if row[j]=='':
                    row[j] =rows[i-1][j]
            row.append([])
            print(reduce(list2dict, row[::-1]))
            row_dict = reduce(list2dict, row[::-1])




        print(rows)
def merge_dict(d1,d2):
    dd ={}
    for key in a.keys() :
        if key in b.keys():
            a[key].extend(b[key])
            print(a)


if __name__ == "__main__":
    a = {'机器学习': [{'线性模型': [{'线性回归': []}]}]}
    b = {'机器学习': [{'神经网络': []}]}
    #print({key:(a.get(key).extend(b.get(key))) for key in a.keys()|b.keys()})

    b['机器学习'].(a['机器学习'])
    #print(b)
    print(merge_dict(a, b))
    #csv2json('eigin.csv')
    # a=list2dict(1,3)
    # print(reduce(list2dict,[6,4,5,]))



# a={
#     "机器学习":[
#         {
#             "线性模型":[]
#         },{
#             "神经网络":[{
#                 "神经元模型":[]
#             }]
#         },{
#             "强化模型":[]
#         }]
# }
# def find(key):
#     pass
#     #return output
#
# path=find('感知机')
# print(path)
# # '机器学习。神经网络。多层网络。感知机‘
# path = find('贝叶斯模型')
# print(path)
# #'不存在关键字：贝叶斯模型'
