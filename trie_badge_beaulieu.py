import sys
from turtle import pd
import pandas

df = pandas.read_excel('C:/Users/danhk/OneDrive/Bureau/Liste_Abonnés.xlsx') 

# for i in df.values :
    # if n == i [0]:
        # print (i[0], i [2], i [3], i [5])

print ("trie_badge_beaulieu:", sys.argv[1])

found = False   
for i in df.values : 
    if int(sys.argv[1]) == i [0]:
        found = True
        print (i[0], i[3], i[5])
         

if not found :
    print ("not used")

