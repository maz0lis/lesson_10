import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

list_1 = [1 if x == 'human' else 0 for x in data['whoAmI']]
list_2 = [1 if x == 'robot' else 0 for x in data['whoAmI']]

df = pd.DataFrame({'whoAmI_human':list_1, 'whoAmI_robot':list_2})