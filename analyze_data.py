# Name: Faye(Lifei) Wang
# Date: 02/12/2025

import pandas as pd
import numpy as np

# 读取 CSV 文件
file_path = "/Users/faye/Documents/hw-5110/hw4-fayewang1617/Iris.csv"
df = pd.read_csv(file_path)

# 归一化 (Normalization)
df_normalized = df.copy()
df_normalized.iloc[:, :-1] = (df.iloc[:, :-1] - df.iloc[:, :-1].min(axis=0)) / (df.iloc[:, :-1].max(axis=0) - df.iloc[:, :-1].min(axis=0))

# 保存归一化后的 CSV 文件
normalized_file_path = "/Users/faye/Documents/hw-5110/hw4-fayewang1617/Iris_Normalized.csv"
df_normalized.to_csv(normalized_file_path, index=False)


# 标准化 (Standardization)
df_standardized = df.copy()
df_standardized.iloc[:, :-1] = (df.iloc[:, :-1] - df.iloc[:, :-1].mean(axis=0)) / df.iloc[:, :-1].std(axis=0)

# 保存标准化后的 CSV 文件
standardized_file_path = "/Users/faye/Documents/hw-5110/hw4-fayewang1617/Iris_Standardized.csv"
df_standardized.to_csv(standardized_file_path, index=False)

