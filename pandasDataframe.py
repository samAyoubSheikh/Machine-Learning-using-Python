import pandas as pd

list = [
    [1,'sameer',21],
    [2,'ifham',25],
    [3,'shahid',23]
    ]


n = pd.DataFrame(list , columns=["Roll No","Name","Age"])
print(n)