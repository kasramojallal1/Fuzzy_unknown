import pandas as pd
import numpy as np
import random
import math
from colorama import Fore, Style
import matplotlib.pyplot as plt

K = 3
m = 2

file_list = ['data1.csv', 'data2.csv', 'data3.csv', 'data4.csv']
data_frames = []

data1_df = pd.read_csv("data1.csv")
number_column_data1 = len(data1_df.columns)
column_list_data1 = []
for i in range(number_column_data1):
    column_list_data1.append(str(i + 1))

data1_df = pd.read_csv("data1.csv", names=column_list_data1)



clusters = []

for i in range(K):
    rand_cluster = []
    for j in range(number_column_data1):
        rand_cluster.append(random.randint(200, 300))
    clusters.append(rand_cluster)

print(clusters)

arr_data1 = data1_df.to_numpy()


count1 = 0
for iteration in range(100):

    arr_belongs = []

    for value in arr_data1:
        belong = []

        for i in range(K):
            value_sum = 0
            for j in range(K):
                value_sum += (math.dist(value, clusters[i]) / math.dist(value, clusters[j])) ** (2 / (m - 1))

            belong.append(1 / value_sum)

        arr_belongs.append(belong)


    sum_belongs = [0 for i in range(K)]
    for value in arr_belongs:
        for i in range(K):
            sum_belongs[i] += value[i]

    for i in range(K):
        new_arr = [0 for p in range(number_column_data1)]
        for j in range(len(arr_belongs)):
            for k in range(number_column_data1):
                new_arr[k] += arr_belongs[j][i] * arr_data1[j][k]

        for t in range(number_column_data1):
            new_arr[t] = new_arr[t] / sum_belongs[i]

        clusters[i] = new_arr


    print(str(count1) + Fore.YELLOW + str(clusters) + Style.RESET_ALL)
    count1 += 1



cost = 0
for j in range(len(arr_data1)):
    my_sum = 0
    for i in range(K):
        my_sum += ((arr_belongs[j][i]) ** m) * math.dist(arr_data1[j], clusters[i])

    cost += my_sum

print(cost)

