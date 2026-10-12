import pandas as pd

data ={
    'Roll No':[1,2,3,4,5],
    'Name':['ifham','sameer','shahid','nadeem','danish'],
    'Marks':[98,82,77,96,88]
}

#print original dataframe
df = pd.DataFrame(data)
print(df)

# lets sort the rows based on marks obtained
print("")
#df2 = df.sort_values(by='Marks',ascending=False)#in decreasing order
df2 = df.sort_values(by='Marks')#in increasing order


print(df2)