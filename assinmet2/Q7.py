def filter_long_words(p1,p2):
    for i in range(0,p2):
        if len(p1[i])>p2:
            l2.append(p1[i])
  
    return l2       
n=int(input("enter no of words"))
l1=[]
l2=[]
print("enter the words")
for i in range(0,n):
    l1.append(str(input()))
print(f"list of words={l1}")
long_words=filter_long_words(l1,len(l1)) 
print(f"long words are={long_words}")  
        
        