scores = {
    "kimura" : 90,
    "takahashi" : 100,
    "yamamoto" : 70,
    "tanaka" : 85,
    "sakamoto" : 55
}
# 1.合計点
total = 0
for score in scores.values():
    total += score
print("全員の合計は" + str(total) + "点です")

# 2.平均点(lenバージョン)
avg = 0
len = len(scores)
avg = total/len
print("平均点は" + str(avg) + "点です") 

# 3.辞書の追加
scores["nakata"] = 95
total = 0
print(scores)

# 3.合計点
for score in scores.values():
    total += score
print("中田さんを足した全員の合計は" + str(total) + "点です")

# 3.平均点（関数作成バージョン）
def count_keys(score):
    count = 0
    for i in enumerate(score):
        count += 1
    return count
scorekey_number = count_keys(scores)
avg = total/scorekey_number
print("中田さんを足した平均点は" + str(avg) + "点です")
