# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
print(circular_linked_list[0]," ",circular_linked_list[1]," ",circular_linked_list[2],ends="")
final_list = [circular_linked_list[0],circular_linked_list[1],circular_linked_list[2]]
for i in range (2,length_of_circular_linked_length):
  if circular_linked_linked[i] not in final_list:
    print(circular_linked_list[i],end = " ")
    final_list.append(circular_linked_list[i])
