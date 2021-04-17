import os.path
import glob
import os
import csv
import pathlib
import pandas as pd

###os.pathを使ってファイル名を保存
# file_path = "../Best_Score_0423"
# print(os.path.basename('../Best_Score_0423/*'))

### pathlibを使う
### 拡張子も取得する．
### この方法だと，png以外の画像ファイルには適用されない
# csvfile = '../Best_Score_0423/filename.csv'
# p_temp = pathlib.Path('../Best_Score_0423').glob('*.png')
# for p in p_temp:
#     print(p.name)

### 上記の方法で，csvにファイル名を書き込む
# csvfile = '../Best_Score_0423/filename.csv'
# p_temp = pathlib.Path('../Best_Score_0423').glob('*.png')
# for p in p_temp:
#     print(p.name)
    # with open(csvfile, 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(p.name)
# with open(csvfile, 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(p.name)
# print(csvfile.read())

### os.pathを使って，csvにファイル名を保存する
### 画像ファイルがあるディレクトリに.pyファイルを置く必要がある．
csv_file = 'filelist.csv'

file_list = []
for file in os.listdir():
    is_file = os.path.isfile(file) #ファイルか
    not_py_file = os.path.basename(__file__) != file #このpyファイルではないか
    not_csv_file = csv_file != file #生成したcsvファイルはでは無いか
    if is_file and not_py_file and not_csv_file:
        if not file.startswith("."): #隠しファイルは除く
            only_file_name = os.path.splitext(file)[0]
            only_file_name_list = only_file_name.split('_')
            file_list.append(only_file_name_list)

with open(csv_file, "w", newline="") as f:
    csv_writer = csv.writer(f)
    for r in file_list:
        csv_writer.writerow(r)
## csvファイルを読み込んで，スコアが高い順に並べ替える
df = pd.read_csv('filelist.csv',index_col=0, header=None, squeeze=True).to_dict()
print(df)
print(len(df))
score_sorted = sorted(df.items(), key=lambda x:x[1], reverse=True)
print(score_sorted)

# with open(csv_file, 'w', newline="") as csv:
#     data = csv.reader(csv, header=None)
# data_dict = {rows[0] : rows[1] for rows in data}
# print(data_dict)

# data = pd.read_csv('filelist.csv', header=None)
# print(data)
# data_dict = {rows[0] : rows[1] for rows in data}
# print(data_dict)

# score_sorted = sorted(data.items(), key=lambda x:x[1])
# print(score_sorted)
### 上記の方法で，辞書型リストにファイル名を保存する．
# csv_file = 'filelist.csv'

# file_list = []
# for file in os.listdir("."):
#     is_file = os.path.isfile(file) #ファイルか
#     not_py_file = os.path.basename(__file__) != file #pyファイルではないか
#     if is_file and not_py_file:
#         file_list.append(file)
#
# with open(csv_file, "w", newline="") as f:
#     csv_writer = csv.writer(f)
#     for r in file_list:
#         csv_writer.writerow(r)

### globを使ってファイル名を取得する方法
# files = glob.glob('../Best_Score_0423/*')
# print(files)