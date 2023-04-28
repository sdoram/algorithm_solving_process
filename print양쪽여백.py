# a = int(input())
# b = a*2-1
# c = a*2
# # a*2-1 부터 시작해서 1까지 줄었다가 다시 a*2-1까지 늘어나는 별 찍기
# while b > 0:
#     print('{:^{}}'.format('*'*b, c))
#     b -= 2
# b = 3
# while b < c:
#     print('{:^{}}'.format('*'*b, c))
#     b += 2

# a = int(input())
# a = 5
# b = a*2-1
# c = a*2
# count = 0
# # a*2-1 부터 시작해서 1까지 줄었다가 다시 a*2-1까지 늘어나는 별 찍기
# while b > 0:
#     print(' '*count, '*'*b, sep='')
#     b -= 2
#     count += 1
# b = 3
# count -= 2
# while b < c:
#     print(' '*count, '*'*b, sep='')
#     b += 2
#     count -= 1

a = int(input())
count = 1
b = a-1
while count < a:
    print(' '*b, '*'*(count*2-1), sep='')
    count += 1
    b -= 1
while count > 0:
    print(' '*b, '*'*(count*2-1), sep='')
    count -= 1
    b += 1
