import pandas as pd
import requests
data = {
    'name':['A', 'B', 'C', 'D', 'E'],
    'age':[25, 30, 35, 40, 45],
    'address':['Pune', 'Mumbai', 'Delhi', 'Bangalore', 'Chennai']
}
print('student details')
df = pd.DataFrame(data)
print(df)

print('print data from API')
response =requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())