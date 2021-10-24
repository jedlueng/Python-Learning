# https://leetcode.com/problems/jewels-and-stones/
#By jedlueng 7 September 2021 
import re

def numJewelsInStones(jewels, stones):
        #How many stone are also jewels
        #Case sensitive 
    jewels2 = [] 
    for i in jewels: 
        jewels2.append(i)
        jewels2.append('|')
    jewelsRegex = re.compile(r'{}'.format(jewels2))
    mo = len(jewelsRegex.findall(stones))
    return(mo)

m1 = 'aA' 
m2 = 'aAAbbbb'

numJewelsInStones(m1,m2)