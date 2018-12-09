import collections as coll
import pandas as pd
import numpy as np
import time

count = 999
num_col = 100

start = time.time()
#Read Data Set 
df = pd.read_json('yelp_academic_dataset_review1K.json',lines = True).head(count)


df2 = df['text'].str.split(' ')

#Counts the frequencies of every word in the dataset
wcount_total = coll.Counter()
for i in range(0,count):
    for j in df2.iloc[i]:
        wcount_total[j] += 1

#List of most frequent words
top_words = sorted(wcount_total, key=wcount_total.get, reverse = True)[0:num_col]


#Count word frequencies by row
line_count = coll.Counter()
s = []
for k in range(0,count):
    for r in range(0,num_col):
        s.append(df2.iloc[k].count(top_words[r]))
        
freq_matrix = pd.DataFrame(np.array(s).reshape(-count,num_col),columns = top_words)

norm_freq_matrix = freq_matrix/freq_matrix.sum(axis=0)

end = time.time()
print(end - start)
print norm_freq_matrix
