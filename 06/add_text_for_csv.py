# 読み込むファイルパス
file_path = './members.csv'

#　リストの書き込み
# 書き込む文字列を入力
print("IDを入力してください")
id = input()
print("名前を入力してください")
name = input()
print("住所を入力してください")
addres = input()
print("電話番号を入力してください")
phone_namber = input()
#　書き込むテキストを結合
text = str(id) +','+ name +','+ addres +','+ str(phone_namber)
# 追記モードでファイルを開く
f = open(file_path, "a", encoding="UTF-8")
#　ファイルに書き込む
f.write(text + "\n")
#　ファイルを閉じる
f.close()

# ファイルの表示
# ファイルを開く
f = open(file_path, "r", encoding="UTF-8")
# ファイルを１行ごとのリストとして読み込む
lines = f.readlines()
# ファイルを閉じる
f.close()

# 各行を出力
for line in lines:
    print(line)
