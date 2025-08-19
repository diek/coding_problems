# This does not work, because the when item removed,
# the index changes and the counter losses its place
def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print(L1)

# Much better to clone, make a copy
def removeDupsBetter(L1, L2):
    L1Start = L1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDupsBetter(L1, L2)
print(L1)
