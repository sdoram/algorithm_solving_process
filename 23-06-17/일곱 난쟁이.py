# https://www.acmicpc.net/problem/2309
# # num_list = sorted([20, 7, 23, 19, 10, 15, 25, 8, 13])
# num_list = sorted([6, 7, 8, 9, 11, 12, 13, 14, 40])
# num_list = sorted([20, 7, 23, 19, 10, 11, 13, 8, 12])
# num_list = sorted([1, 1, 1, 1, 1, 1, 1, 94, 95])
# num_list = sorted([6, 14, 40, 7, 13, 8, 12, 9, 11])
# num_list = sorted([1, 2, 8, 9, 11, 12, 55, 56, 57])
# num_list = sorted([50, 40, 30, 20, 10, 1, 2, 3, 4])
# num_list = sorted([3, 4, 5, 6, 7, 10, 15, 20, 40])
# # num_list = [int(input()) for _ in range(9)]
# print(sum(num_list))
# for num in num_list:
#     find_num = sum(num_list) - 100 - num
#     if find_num in num_list and num != find_num:
#         # print(num, find_num)
#         num_list.pop(num_list.index(num))
#         num_list.pop(num_list.index(find_num))
#         break
# for num in num_list:
#     print(num)
# # [print(num) for num in num_list]


num_list = sorted([int(input()) for _ in range(9)])
for num in num_list:
    find_num = sum(num_list) - 100 - num
    if find_num in num_list and num != find_num:
        num_list.pop(num_list.index(num))
        num_list.pop(num_list.index(find_num))
        break
[print(num) for num in num_list]
