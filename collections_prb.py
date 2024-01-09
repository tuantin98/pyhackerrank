#https://www.hackerrank.com/challenges/collections-counter
from collections import Counter
X = int(input())
int_input = map(int, input().split())
int_list = list(int_input)
X_counter = Counter(int_list)
N = int(input())
result = 0
for i in range(N):
    shoe_map = map(int, input().split())
    shoe = list(shoe_map)
    if X_counter.get(shoe[0]) > 0 :
        int_list.remove(shoe[0])
        result = result + shoe[1]
        X_counter = Counter(int_list)
print(result)