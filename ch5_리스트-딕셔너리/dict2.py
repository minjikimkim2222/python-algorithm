# 딕셔너리 모듈

import collections;

## 1. defaultdict
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
print(a) ## defaultdict(<class 'int'>, {'A': 5, 'B': 4})

a['C'] += 1
print(a) ## defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})

## 2. Counter
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
print(b) ## Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

ret_b = b.most_common(2)
print(ret_b) ## [(5, 3), (6, 2)]

## 3. OrderedDict
a = collections.OrderedDict({'banana' : 3, 'apple': 4, 'pear': 1, 'orange': 2})
print(a) ## OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])