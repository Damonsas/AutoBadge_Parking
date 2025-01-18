from turtle import pd
import pandas
df = pandas.read_excel('C:/Users/danhk/OneDrive/Bureau/Liste_Abonnés.xlsx') 
n = 3
# print (df.info)

# print (df.values)

# for i in df.values :
    # print (i [2])
    # if 'Non Affecté' == i [2]:
    #    print (i [0], i [2]) 

for i in df.values :
    if n == i [0]:
        print (i[0], i [2], i [3], i [5])