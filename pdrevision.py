import pandas as pd
data=pd.read_csv("url.csv")
print(data)
d=len(data)
print(d)
newrow={'fileno':d+1,'url':"www.hotstar.com",'data':'pqr'}
data=data.append(newrow,ignore_index=True)
data.to_csv("url.csv")
print(data)