from turtle import pd
import pandas
df = pandas.read_excel('C:/Users/danhk/OneDrive/Bureau/Liste_Abonnés_test.xlsx') 

# print (df.info)

# print (df.values)
i = 'non affecté'

for i in df.values :
    print (i [2])
