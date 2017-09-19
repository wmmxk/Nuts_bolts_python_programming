'''
This code is show how to group a rows of a data.frame and 
then retrieve subgroups

'''

import pandas as pd
raw_data = {'regiment': ['Night', 'Night', 'Day'],
            'preTestScore': ['1st', '2nd', '3rd'],
            'post': [1,2,3]}
df = pd.DataFrame(raw_data, columns=['regiment', 'preTestScore','post'])

groups_obj = df.groupby('regiment')


print(groups_obj.groups.keys())
print(groups_obj.groups.values())

// the .groups function return a dictionary with name of groups as keys and an array of indexes identifying the data items included in the group
groups_dict = groups_obj.groups

index_one_group = groups_dict['Night']

print(df.iloc[index_one_group,:])

//You can retrieve any of the constructed groups with get_group() passing as argument the value of the grouping factor
print(groups_obj.get_group('Day'))
