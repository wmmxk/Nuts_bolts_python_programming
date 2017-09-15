import pandas as pd

mylist = []
def times100(x):
#     mylist.append([x[0],x[1]])
     return((x[0]*2,x[1]))
rectangles = [
            { 'height': 40, 'width': 10 },
                { 'height': 20, 'width': 9 },
                    { 'height': 3.4, 'width': 4 }
                    ]

rectangles_df = pd.DataFrame(rectangles)
print(rectangles_df)

print(rectangles_df.apply(times100,axis=1))


rectangles_df['times'] = rectangles_df.apply(times100,axis=1)
