import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("dataset3-movies-cornell.csv")
# df_train = df.sample(frac=.81)
# print(df_train.shape)
# print(df.shape)
df['sentence'] = df['sentence'].str[0:-3]
print(df.head())
train_dev, test = train_test_split(df, test_size=0.1)
train, dev = train_test_split(train_dev, test_size=.1)
# print("train_dev", train_dev.shape)
# print("test", test.shape)
# print("train", train.shape)
# print("dev", dev.shape)
#
train_dev.to_csv("datasets/cornell/train_dev.tsv", sep="\t", index=False)
test.to_csv("datasets/cornell/test.tsv", sep="\t", index=False)
train.to_csv("datasets/cornell/train.tsv", sep="\t", index=False)
dev.to_csv("datasets/cornell/dev.tsv", sep="\t", index=False)
