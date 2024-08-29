l1=[]
n=int(input("enter no elements in list"))
print("enter list elements")

for i in range(0,n):
    x=int(input())
    l1.append(x)

print(f"list={l1}")
print(f"alterante elements in list are={l1[::2]} ")    