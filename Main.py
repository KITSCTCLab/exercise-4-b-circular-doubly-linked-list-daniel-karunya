# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
flist=[]
for i in circular_linked_list:
    if i not in flist:
        flist.append(i)

print(len(flist))
for i in flist:
    print(i,end=" ")
