# set
# 삽입, add
s = set()
s.add("apple")
s.add("banana")
s.add("cheery")
print(s) # {'banana', 'cheery', 'apple'}

# 삭제, remove
s.remove("apple")
print(s) ## {'cheery', 'banana'}

# 임의 삭제, pop
item = s.pop()
print(item, s)

# 전체 삭제, clear
s.clear()
print(s)

