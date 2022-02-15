import random
import Names_List
import time
from Names_List import maleFirstNames
from Names_List import femaleFirstNames
from Names_List import lastNames
'''
counter = 0
counter2 = 0
counter3 = 0
for x in maleFirstNames:
    print(counter)
    counter += 1
print("Done")

time.sleep(1.5)

for x in femaleFirstNames:
    print(counter2)
    counter2 += 1
print ("done again")

for x in lastNames:
    print(counter3)
    counter3 += 1
print ("Done finally")

print("The number of male first names is: ", counter)
print("The number of female first names is: ", counter2)
print("The number of last names is: ", counter3)
'''

#There are a total of 100 male first names [0:99]
#There are a total of 100 female first names [0:99]
#there are a total of 1000 last names [0:999]
counternum = 0
with open('newdatabase.txt', 'w') as f:
    for x in range(50):
        #print(counternum, ")")
        a = random.randint(0,99)
        #print(a)
        if ((a%2) == 0):
            firstname = maleFirstNames[a]
        else:
            firstname = femaleFirstNames[a]
        #print (firstname)
        f.write(str(counternum))
        f.write(") ")
        f.write(firstname)
        f.write(" ")
        counternum += 1
        b = random.randint(0,999)
        lastname = lastNames[b]
        f.write(lastname)
        f.write("\n")
        
f.close()


    