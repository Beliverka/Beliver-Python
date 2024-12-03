def F(n,x=2):
    if n<=1:
        return False
    if x*x>n:
        return True
    if n%x==0:
        return False
    return F(n,x+1)
n=int(input("Введите натуральное число n>1: "))
if F(n):
    print("YES")
else:
    print("NO")

