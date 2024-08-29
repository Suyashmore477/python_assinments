l1=[]
max=0
n=int(input("enter the number of elements in list"))
print("enter the elements in list")
for i in range(0,n):
    
    l1.append(int(input()))
print(f"list={l1}")
for i in range(0,n):
    if l1[i]>max:
        max=l1[i]
print(f"maximum number in list is {max}")    
        
