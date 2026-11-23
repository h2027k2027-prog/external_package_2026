import pandas as pd
data = {
    'name':['A', 'B', 'C', 'D', 'E'],
    'age':[25, 30, 35, 40, 45],
    'address':['Pune', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai']
}
print('student details')
df = pd.DataFrame(data)
print(df)