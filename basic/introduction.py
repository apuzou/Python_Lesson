# a = "test"
# b = a
# c = b

# print(c)

# num = 1
# name = "Mike"
# is_OK = True

# print(num,type(num))
# print(name,type(name))
# print(is_OK,type(is_OK))

# print("Hi","Mike",sep=",",end=".\n")
# print("Hi","Mike",sep=",",end=".\n")

# 数値計算
# import math

# result = math.sqrt(25)
# print(result)y = math.log2(10)
# print(y)

# print(help(math))

# 文字列
# print('hello.\nHow are you?')
# print(r'C:\name\name')

# print("########################")
# print("""\
# line1
# line2
# line3\
# """)
# print("########################")

# print("Hi" * 3 + "Mike")

# print("Py" "thon")
# print("Py" + "thon")

# prefix = "Py"
# print(prefix + "thon")

# s = "My name is Mike. Hi Mike."
# print(s)
# is_start = s.startswith("My")
# print(is_start)
# print(s.find("Mike"))
# print(s.rfind("Mike"))
# print(s.count("Mike"))
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.replace("Mike", "Nancy"))

# リスト
# scores = [82, 74, 60, 92, 70]
# print(scores)
# print(scores[2])
# print(scores[2:5])
# print(scores[2:])
# print(scores[:2])
# print(scores[:])
# print(scores[::2])
# print(len(scores))
# scores.append(100)
# print(scores)
# scores.insert(0, 60)
# print(scores)
# scores.pop()
# print(scores)
# scores.pop(0)
# print(scores)
# scores.remove(60)
# print(scores)
# scores.sort()
# print(scores)
# scores.reverse()
# print(scores)
# scores.clear()
# print(scores)

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# x = a + b
# print(x)
# print(a)
# print(b)
# a += b
# print(a)
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 10]
# x.extend(y)
# print(x)

# r = [1, 2, 3, 4, 5, 1, 2, 3]
# print(r.count(3))
# print(r.index(3))
# print(r.index(3, 3))

# s = "My name is Mike."
# to_split = s.split(" ")
# print(to_split)
# x = " ".join(to_split)
# print(x)

# i = [1, 2, 3, 4, 5]
# j = i
# j[0] = 100
# print("j =", j)
# print("i =", i)

# x = [1, 2, 3, 4, 5]
# y = x.copy()
# y[0] = 100
# print("y =", y)
# print("x =", x)

# print(help(list))

# 辞書
# 辞書はキーと値のペアを持つ
# scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}
# print(scores)
# print(scores["数学"])
# print(scores.keys())
# print(scores.values())
# print(scores.items())
# scores2 = {"数学": 90, "家庭科": 80}
# scores.update(scores2)
# print(scores)

# print(help(dict))

# タプル
# タプルは値を代入できない(読み込み専用として使用する)
# t = (1, 2, 3, 4, 5)
# print(t)
# print(type(t))

# print(help(tuple))

# 集合
# 集合は重複する値を持たない(重複する値は1つになる)
# a = {1, 2, 2, 3, 4, 5}
# print(a)
# print(type(a))
# b = {2, 3, 6, 7}
# print(a & b) # 積集合
# print(a | b) # 和集合
# print(a - b) # 差集合
# print(a ^ b) # 対称差集合

# print(help(set))

########################################################
# # 練習問題
# scores = {"数学": 82, "国語": 74, "英語": 60, "理科": 92, "社会": 70}

# # 理科と社会の点数の差
# diff = scores["理科"] - scores["社会"]
# print(f"理科と社会の点数の差: {diff}点")

# # 平均点
# scores_values = list(scores.values())
# avg_score = sum(scores_values) / len(scores_values)
# print(f"平均点: {avg_score}点")
########################################################