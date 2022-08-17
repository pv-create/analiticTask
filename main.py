# тут буду писать решения своих задач к курсу по аналитике данных

import pandas as pd
import numpy as np

StudentsPerfomance = pd.read_csv('StudentsPerformance.csv')
# print(StudentsPerfomance.describe())
# print(StudentsPerfomance.dtypes)
# print(StudentsPerfomance.groupby('gender').aggregate({'writing score' : 'mean'}))
print(StudentsPerfomance.query("gender == 'female'"))

# print(StudentsPerfomance.size)
# print(StudentsPerfomance.loc[StudentsPerfomance.gender == 'female'])
# mean=StudentsPerfomance['writing score'].mean()
# print(StudentsPerfomance.loc[StudentsPerfomance['writing score']>mean])
# print(StudentsPerfomance.loc[StudentsPerfomance.lunch == 'free/reduced'].describe())
# print(StudentsPerfomance.describe())
score_collums=[i for i in list(StudentsPerfomance) if 'score' in i]
# print(StudentsPerfomance[score_collums])
print(StudentsPerfomance.filter(like='score'))
