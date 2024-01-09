#https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())
integer_list = map(int, input().split())
int_tuple = tuple(integer_list)
print(hash(int_tuple))
