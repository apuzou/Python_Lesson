# python のコードスタイル
'''下記記述は誤ったコードスタイルを含みます'''

# ;は不要
x = 1;
y = 2;

# インデントはスペース4つ
if x == 1:
print("x is 1")
else:
    print("x is not 1")

# ８０文字以内に収める
x = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# 不要な()を削除
if(x):
    print("x is true")

# クラス名はPascalCase
class myClass:

# メソッド名・変数名はsnake_case
def my_method(self):
    print("my_method")

# クラスの改行は2行
class myClass1:
    def my_method(self):
        print("my_method")


class myClass2:

# joinを使用してリストを結合(パフォーマンス向上)
long_word = []
for word in ['ndinvd', 'jfkdnfo', 'nruhfowe']:
    long_word.append("{}kenrfenf".format(word))
new_long_word = ''.join(long_word)

# TODO(name): ここにタスクを記述

# ファイルを開くときはwithを使用
with open('data.csv', 'r') as csv_file:
    for line in csv_file:
        print(line)
# ファイルを閉じる
csv_file.close()
