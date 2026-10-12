import pandas as pd

data =[
    [1,"madiha",76],
    [2,"danish",73],
    [3,"nadeem",70],
    [4,"ilham",56],
    [5,"Gurpreet",90],
    [6,"Iqra",95],
    [7,"ifham",88],
    [8,"sameer",89],
    [9,"rabia",82],
    [10,"shahid",65]
]

df = pd.DataFrame(data,columns=["Roll No","Name","Marks"])
print(df)
#now i want to rank the students based on marks obtained for that 

#df["Rank"] creates an extra column. ascending = false means highest marks will get rank 1
df["Rank"] = df["Marks"].rank(ascending=False)
print(df)