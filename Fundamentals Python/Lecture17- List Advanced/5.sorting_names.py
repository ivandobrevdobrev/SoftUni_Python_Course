names = input().split(", ")
sorted_list = sorted(names,key= lambda x:(-len(x),x))
print(sorted_list)

sorted_list = sorted(names,key=len,reverse= True)
print(sorted_list)