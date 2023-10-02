str = "apple"

count = 0
l={}
for i in str:
    if i not in l:
        l[i]=count+1
 

print(l)
