# https://www.acmicpc.net/problem/2309

# 7개를 합쳐서 100이 되는 경우 찾기


# def dwarf(dwarfs, find_dwarf):
#     copy_list = dwarfs[::]
#     for _ in copy_list:
#         num1 = copy_list.pop()
#         for num2 in copy_list:
#             if find_dwarf == num1 + num2:
#                 dwarfs.remove(num1)
#                 dwarfs.remove(num2)
#                 return sorted(dwarfs)
# print(*dwarf(dwarf_list, not_dwarf), sep="\n")


dwarf_list = [20, 7, 23, 19, 10, 25, 15, 8, 13]
# dwarf_list = []
# for _ in range(9):
#     dwarf_list.append(int(input()))
# not_dwarf = sum(dwarf_list) - 100


def dwarf(dwarfs):
    copy_list = dwarfs[::]
    not_dwarf = sum(dwarfs) - 100
    for _ in copy_list:
        num1 = copy_list.pop()
        for num2 in copy_list:
            if not_dwarf == num1 + num2:
                dwarfs.remove(num1)
                dwarfs.remove(num2)
                return sorted(dwarfs)


answer = dwarf(dwarf_list)
for a in answer:
    print(a)
# 타입에러가 어디서 나는거야;
