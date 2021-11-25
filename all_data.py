import pandas as pd
import glob

path = r'/Users/lidu/PycharmProjects/panda/test'  # use your path
all_files = glob.glob(path + "/*.csv")
print(all_files)

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.to_csv("all_data.csv", index=False)