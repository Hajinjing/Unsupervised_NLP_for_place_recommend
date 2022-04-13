import glob
import pandas as pd

data_paths = glob.glob('./crawling_data/*')
print(data_paths)
df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.columns = ['title', 'contents']
    df = pd.concat([df, df_temp], ignore_index=True,
              axis='rows')
df.info()
df.to_csv('./crawling_data/tour_all.csv',
          index=False)
