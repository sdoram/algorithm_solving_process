# https://www.acmicpc.net/problem/17254
N, M = 3, 5
input_list = [
    ["1", "0", "A"],
    ["2", "1", "P"],
    ["1", "2", "L"],
    ["2", "4", "E"],
    ["3", "0", "P"],
]
input_list2 = [
    ["1", "6", "B"],
    ["1", "1", "A"],
    ["1", "0", "L"],
    ["1", "3", "D"],
    ["2", "8", "G"],
    ["2", "6", "U"],
    ["2", "3", "Y"],
]
sorted_list1 = sorted(input_list, key=lambda x: [int(x[1]), int(x[0])])
sorted_list1 = sorted(input_list, key=lambda x: x[0])
print(sorted_list1)
sorted_list2 = sorted(input_list, key=lambda x: x[1])
print(sorted_list2)

sorted_list1 = sorted(input_list2, key=lambda x: [int(x[1]), int(x[0])])
# sorted_list1 = sorted(input_list2, key=lambda x: int(x[0]))
print(sorted_list1)
# sorted_list2 = sorted(input_list2, key=lambda x: int(x[1]))
# print(sorted_list2)

N, M = map(int, input().split())
print(
    "".join(
        [
            x[2]
            for x in sorted(
                [input().split() for _ in range(M)],
                key=lambda x: [int(x[1]), int(x[0])],
            )
        ]
    )
)
