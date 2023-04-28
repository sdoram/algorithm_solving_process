# 뒤집기
# 완성은 했는데 가독성이 너무 떨어지는 것 같다.
# bin_str = '0001100'
# bin_str = '11111'
# bin_str = '00000001'
# bin_str = '11001100110011000001'

bin_str = input()
zero_str_list = []
one_str_list = []
num_list = []
for num in range(len(bin_str)):
    if num != 0 and bin_str[num-1] != bin_str[num] and bin_str[num-1] == '0':
        zero_str_list.append(num_list)
        num_list = []
    elif num != 0 and bin_str[num-1] != bin_str[num] and bin_str[num-1] == '1':
        one_str_list.append(num_list)
        num_list = []
    if num == len(bin_str)-1 and bin_str[num] == '0':
        zero_str_list.append(num_list)
    elif num == len(bin_str)-1 and bin_str[num] == '1':
        one_str_list.append(num_list)
    num_list.append(bin_str[num])

print(len(one_str_list) if len(one_str_list) <
      len(zero_str_list) else len(zero_str_list))
