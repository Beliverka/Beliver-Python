def F(n):
    if n==0:
        return 0
    else:
        return n%10+F(n// 0)
N = int(input("Введите натуральное число N: "))
result = F(N)
print(f"Сумма цифр числа {N} равна {result}.")

