import re
str = "$50 each. $100, $999"
lst = re.findall(r"\$\d+", str.lower())
print("lst:", lst)


print("find:", str.find("$"))
print("split:", str.split("$"))

lst = [[1, 2], [3, 4], [5, 6]]
for u, v in lst[::-1]:
    print("u:", u, "v:", v)

for i in range(10, -1, -1):
    print("i:", i)

num = "0010"
print("int:", int(num))

print("or:", 10 or 1)

print("test:", []+[[2, 3], [4, 5]])

s = set([1, 2, 3, 4, 5])
print("set:", s)

s = set()
s.add(1)
s.add(3)
print("s:", s)

num = -10
print("str:", str(num))

str = "$50 each. $100, $999"
lst = re.findall(r"\$\d+", str.lower())
print("lst:", lst)

print("bin:", bin(0))
