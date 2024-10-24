s='абсолютно любое название строки'
z=s.count('о')
s=s.replace('а','о')
k=s.count('о')
print(k-z,len(s))