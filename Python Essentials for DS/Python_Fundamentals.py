# ==============================
# 1. STRINGS (Immutable)
# ==============================
s = "hello world"

# Access / Traversal
print(s[0])          # 'h'
print(s[-1])         # 'd'
for c in s:
    pass
for i, c in enumerate(s):
    pass

# Slicing
print(s[1:4])        # 'ell'
print(s[::-1])       # reverse
print(s[:5])         # 'hello'
print(s[6:])         # 'world'

# Transformations
print(s.lower())
print(s.upper())
s2 = "  hello  "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())
print(s.replace("world", "python"))
print(s.split(" "))
print(" ".join(["hello", "world"]))

# Search
print(s.find("world"))
print(s.index("world"))
print("world" in s)
print(s.startswith("hello"))
print(s.endswith("world"))

# Frequency / Counting
print(s.count('l'))
from collections import Counter
print(Counter(s))

# Sorting / Reordering
print("".join(sorted(s)))
print(sorted(s))

# Conversion
print(list(s))
print(int("123"))
print(str(123))

# Key Interview Patterns
# Palindrome check
print(s == s[::-1])
# Sliding window (example: longest substring without repeating chars)
# Two pointers (already done in palindrome)
# Hash map frequency (Counter above)


# ==============================
# 2. LISTS (Dynamic Arrays)
# ==============================
arr = [1, 2, 3]

# Creation
arr2 = [0] * 5
arr3 = list(range(5))

# Access
print(arr[0])
print(arr[-1])
print(arr[1:3])

# Add Elements
arr.append(4)
arr.extend([5, 6])
arr.insert(0, 0)

# Remove Elements
arr.pop()
arr.pop(0)
arr.remove(3)
del arr[0]

# Search
print(2 in arr)
print(arr.index(2))
print(arr.count(2))

# Sorting
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x: -x)
sorted_arr = sorted(arr)

# Reverse
arr.reverse()
arr[::-1]

# Useful built-ins
print(min(arr))
print(max(arr))
print(sum(arr))
print(len(arr))

# Transformations
squares = [x**2 for x in arr if x > 0]

# Stack Operations
stack = []
stack.append(1)   # push
stack.pop()       # pop

# Key Interview Patterns
# Two pointers (example: pair with sum target)
l, r = 0, len(arr)-1
target = 2
while l < r:
    if arr[l] + arr[r] == target:
        break
    elif arr[l] + arr[r] < target:
        l += 1
    else:
        r -= 1

# Sliding window (max sum subarray of size k)
k = 3
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

# Prefix sum
prefix = [0] * len(arr)
if arr:
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

# Binary search
def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# Partitioning (quick select style) – not shown


# ==============================
# 3. DICTIONARIES (Hash Maps)
# ==============================
d = {}

# Creation
d = {'a': 1, 'b': 2}
from collections import defaultdict
dd = defaultdict(int)
from collections import Counter
c = Counter('abracadabra')

# Access
print(d['a'])
print(d.get('c', 0))

# Insert / Update
d['c'] = 3
d.update({'d': 4})

# Delete
del d['a']
d.pop('b')

# Iteration
for k in d:
    pass
for k, v in d.items():
    pass
for v in d.values():
    pass

# Membership
print('c' in d)

# Frequency Counting
freq = {}
for x in [1, 2, 2, 3]:
    freq[x] = freq.get(x, 0) + 1

# Sorting
sorted_items = sorted(d.items(), key=lambda x: x[1])

# Useful Conversions
list(d.keys())
list(d.values())
list(d.items())

# Key Interview Patterns
# Frequency map (above)
# Prefix sum map (e.g., two-sum)
# Graph adjacency list
adj = defaultdict(list)
adj[0].append(1)

# Memoization (DP)
cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


# ==============================
# 4. SETS (Hash Sets)
# ==============================
s_set = set()
s_set = {1, 2, 3}

# Add / Remove
s_set.add(4)
s_set.remove(2)
s_set.discard(5)   # no error if missing
s_set.pop()        # arbitrary removal

# Membership
print(1 in s_set)

# Set Operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)      # union
print(s1 & s2)      # intersection
print(s1 - s2)      # difference
print(s1 ^ s2)      # symmetric difference

# Useful
print(len(s_set))
print(sorted(s_set))

# Key Interview Patterns
# Duplicate detection: if x in seen: ...
# Membership check O(1)
# Graph visited tracking: visited = set()


# ==============================
# 5. DEQUE (Double Ended Queue)
# ==============================
from collections import deque
dq = deque()

# Operations
dq.append(1)
dq.appendleft(2)
dq.pop()
dq.popleft()

# Key Uses
# BFS: queue = deque([start])
# Sliding window: maintain deque of indices
# Monotonic queue: for max/min in sliding window


# ==============================
# 6. HEAP / Priority Queue
# ==============================
import heapq
h = []

# Min heap (default)
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappush(h, 2)
print(heapq.heappop(h))   # 1

# Max heap (push -x)
heapq.heappush(h, -3)
heapq.heappush(h, -1)
heapq.heappush(h, -2)
print(-heapq.heappop(h))  # 3

# Heapify existing list
heapq.heapify(arr)

# Key Uses
# Top K problems: use heap of size k
# Dijkstra: priority queue
# Median finder: two heaps


# ==============================
# 7. COUNTER (Frequency Map)
# ==============================
from collections import Counter
cnt = Counter(['a', 'b', 'a', 'c'])
print(cnt.most_common(2))   # [('a', 2), ('b', 1)]
cnt['a'] += 1                # increment count


# ==============================
# 8. Key Algorithmic Manipulations
# ==============================
# Frequency Counting (manual)
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

# Two Pointer
l, r = 0, len(arr)-1
while l < r:
    # do something
    l += 1
    r -= 1

# Sliding Window
l = 0
for r in range(len(arr)):
    # expand window
    # while condition invalid: shrink from left
    pass

# Prefix Sum
prefix = [0] * len(arr)
if arr:
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

# Binary Search
target = 5
l, r = 0, len(arr)-1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        break
    elif arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1