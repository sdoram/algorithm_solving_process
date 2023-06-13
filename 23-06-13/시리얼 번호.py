# https://www.acmicpc.net/problem/1431

# 길이 순 정렬
# 수의 합이 작은 것
# 사전 순
serial_list = ["ABCD", "145C", "A", "A910", "Z321"]
serial_list = ["34H2BJS6N", "PIM12MD7RCOLWW09", "PYF1J14TF", "FIPJOTEA5"]

serial_list = []
for _ in range(int(input())):
    serial_list.append(input())
serial_list = sorted(serial_list)
serial_list = sorted(
    serial_list, key=lambda serial: sum([int(s) for s in serial if s.isdigit()])
)
serial_list = sorted(serial_list, key=len)
print("\n".join(serial_list))


serial_list = []
for _ in range(int(input())):
    serial_list.append(input())
serial_list = sorted(
    serial_list,
    key=lambda serial: (
        len(serial),
        sum([int(s) for s in serial if s.isdigit()]),
        serial,
    ),
)
print("\n".join(serial_list))
