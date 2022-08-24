# a=2%5//3+2**3*2-1
# print(a)

# 12345
# aaaa
# 123
# bb
# 1
n=int(input("enter the number:"))
i=0
while i<=n:
    j=1
    while j<=n-i:
        if i==1:
            print("a",end="")
        elif i==3:
            print("b",end="")
        else:
            print(j,end="")
        j+=1
    print()
    i+=1
    
    