# https://www.acmicpc.net/problem/1371
# alpha_dict = {}
# while True:
#     try:
#         alphabet = input()
#         for a in alphabet:
#             alpha_dict[a] = alpha_dict.get(a, 0) + 1
#     except EOFError:
#         print(
#             "".join(
#                 sorted(
#                     [
#                         k
#                         for k, v in alpha_dict.items()
#                         if v == max(alpha_dict.values()) and k != " "
#                     ]
#                 )
#             )
#         )
#         break
alpha_list = [0] * 26
while True:
    try:
        word = input()
        for w in word:
            if ord(w) != 32:
                alpha_list[ord(w) - 97] += 1
    except EOFError:
        print(
            "".join(
                sorted(
                    [
                        chr(i + 97)
                        for i, a in enumerate(alpha_list)
                        if a == max(alpha_list)
                    ]
                )
            )
        )
        break
