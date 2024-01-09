#https://www.hackerrank.com/challenges/python-power-mod-power
a = int(input())
b = int(input())
m = int(input())
def powmod(x,y,z):
    result = x**y
    result = result % z
    return result
print(a**b)
print(powmod(a,b,m))