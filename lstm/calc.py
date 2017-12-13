import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\cheng\dev\data\C.csv')
col_names=list(df.columns.values)
print(col_names)
df['label'] = (df.Close > df.Close.shift(1)).astype(int)
# print(df.head())
nums = [1, 5, 10, 20, 50]
ma_names=['MA'+str(num) for num in nums]
print(ma_names)

for num in nums[1:]:
    df['MA'+str(num)] = df['Close'].rolling(window=num).mean()

df['MA1'] = df['Close']

df['15'] = (df['Close'] > df['MA5']).astype(int)

for i in nums:
    for j in nums:
        if i == j:
            continue
        df[str(i)+'-'+str(j)] = (df['MA'+str(i)]>df['MA'+str(j)]).astype(int)

for col_name in col_names:
    df.drop(col_name, axis=1, inplace=True)

df_lable= df[['label']].copy()
df.drop('label', axis=1, inplace=True)
matrix = df.as_matrix()
print(type(matrix))
print(matrix.shape)

matrix_lable = df_lable.as_matrix()
print(matrix_lable.shape)

np.save(r'C:\Users\cheng\dev\data\features.npy', df)
np.save(r'C:\Users\cheng\dev\data\label.npy', df_lable)
# print(df.head(10))
# df.to_csv(r'C:\Users\cheng\dev\data\C_processed.csv')