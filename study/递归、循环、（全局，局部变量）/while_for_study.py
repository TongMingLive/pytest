# arr = ["a","b","c"]
#
# print('------------ while -------------')
#
# i = 0
# while(i<len(arr)):
#     print(arr[i])
#     i += 1
#
# print('------------ for range -------------')
#
# for a in range(0,len(arr)):
#     print(arr[a])
#
# print('------------ for each -------------')
#
# for a in arr:
#     print(a)
#
# print('------------ while test -------------')
#
# input_num = int(input('请输入一个整数：'))
# # i = 1
# #
# # while input_num > i:
# #     print(i)
# #     i += 1
# # else:
# #     print(input_num)
#
# while input_num > 0:
#     print(' '*input_num,'*'*input_num)
#     input_num -= 1

num1 = [1,2,3,4,5,5,0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print('num1：',num1)
print('temp：',temp)