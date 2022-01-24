"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
 Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
 Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]


"""

t=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list=[]
def flaten(t):
    for i in t:
        if type(i) == list:
            flaten(i)
        else:
            new_list.append(i)

flaten(t)
print(new_list)


"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

param_list=[[1, 2], [3, 4], [5, 6, 7]]
new_param_list=[]

def arr(x):
    a=len(x)
    for i in range(a):
        b=x[a-i-1]
        b.reverse()
        new_param_list.append(b)

arr(param_list)
print(new_param_list)
