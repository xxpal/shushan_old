# P298 - 给定一个成绩单（字典），找出最大最小值，并求出平均成绩，成绩自己定义。

scores = {'张三': 66, '李四': 83, '王五': 96, 'xx': 53}
# max_score = max(scores.values())
# print(max_score)
# min_score = min(scores.values())
# print(min_score)

# values = list(scores.values())
# max = values[0]
# min = values[0]
# for i in range(len(values)):
#     if values[i] > max:
#         max = values[i]
#     if values[i] < min:
#         min = values[i]
# print(max)
# print(min)

values = list(scores.values())
print(values)
max1 = 0
min1 = 0

for i in range(len(values)):
    if values[i] > max1:
        max1 = values[i]
    if values[i] < min1:
        min1 = values[i]

print(max1)
print(min1)

max2 = max(scores.values())
print(max2)
print(min(list(scores.values())))








