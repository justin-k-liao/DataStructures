
from linkedlist import MatthewLL

ll = MatthewLL()
ll.add(4)
ll.add(7)
ll.add(3)
ll.add(2)

regularList = [4, 7, 3, 2]

for i in range(len(regularList)):
    print(ll.index(i) == regularList[i])

#bonus

try:
    ll.index(4)
except ValueError:
    print('yay, we caught the value Error!')

