N = int(input())
customer = list(map(int, input().split()))

print(len(customer) - len(set(customer)))