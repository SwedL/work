
from collections import ChainMap

dic1 = {'red':1,'white':4}
dic2 = {'red':9,'black':8}
chain = ChainMap(dic1,dic2)
print(chain)

new_dic={'blue':10,'yellow':12}
chain=chain.new_child(new_dic)

print(chain)

chain.maps = reversed(chain.maps)
print(chain)

