sample_list = ["yamada",100,"taro",True]

#このリストの中身は xx と xx と xx です。
def output_list(text):
    text=[str(a) for a in text]
    text="と".join(text)
    print("このリストの中身は" + text + "です")

#このリストの中身は「xx」と「xx」と「xx」と「xx」です。
def output_list2(text):
    text=["「"+str(a)+"」" for a in text]
    text="と".join(text)
    print("このリストの中身は" + text + "です")

output_list(sample_list)
output_list2(sample_list)