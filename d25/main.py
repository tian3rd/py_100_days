import pandas as pd

squirrel_df = pd.read_csv(
    '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

PFC = 'Primary Fur Color'

squirrel_color_lst = squirrel_df[
    squirrel_df[PFC].notnull()][PFC].unique().tolist()

# print(squirrel_color_lst)

squirrel_color_dic = {color: 0 for color in squirrel_color_lst}

for color in squirrel_df[squirrel_df[PFC].notnull()][PFC]:
    squirrel_color_dic[color] += 1

squirrel_color_count = {
    PFC: squirrel_color_lst, 'Count': squirrel_color_dic.values()}
squirrel_color_count_df = pd.DataFrame(squirrel_color_count)

# print(squirrel_color_count_df)

squirrel_color_count_df.to_csv('squirrel_color_count.csv')
