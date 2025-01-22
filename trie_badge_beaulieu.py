import sys
from turtle import pd
import pandas

df = pandas.read_excel('C:/Users/danhk/OneDrive/Bureau/Liste_Abonnés.xlsx') 
# n = 7575

# for i in df.values :
    # if n == i [0]:
        # print (i[0], i [2], i [3], i [5])


print ("trie_badge_beaulieu:", sys.argv[1])

for i in df.values : 
    if int(sys.argv[1]) == i [0]:
         print (i[0], i[3], i[5])
else :
    if int(sys.argv[1]) != i[0]:
        print ("not used") 
  #  else :
        # print ("(sys.argv[1]) is not a number")
