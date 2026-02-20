# # if文
# x = 10

# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# else:
#     print('positive')

# a = 5
# b = 10

# if a > 0:
#     print('a is positive')
#     if b > 0:
#         print('b is positive')

# # 比較・論理演算子
# a = 10
# b = 20

# # aがbと等しい
# a == b
# # aがbより大きい
# a > b
# # aがbより小さい
# a < b
# # aがb以上
# a >= b
# # aがb以下
# a <= b
# # aがbではない
# a != b
# # aもbも真であれば真
# if a > 0 and b > 0:
#     print('a and b is positive')
# # aがbまたはbがc
# if a > 0 or b > 0:
#     print('a or b is positive')

# # "in" "not in" "not"
# x = 1
# y = [1, 2, 3,]

# if x in y:
#     print('x is in y')

# if 100 not in y:
#     print('x is not in y')

# is_ok = True

# if not is_ok:
#     print('Hello')
# else:
#     print('World')

# is_ok = [1, 2, 3, 4]

# if len(is_ok):
#     print('OK')
# else:
#     print('NG')

# # while文
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# # break
# count = 0
# while True:
#     if count >= 5:
#         break
#     print(count)
#     count += 1

# # continue
# count = 0
# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#     count += 1

# # while else文
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

# # input関数
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# # for文 range break continue else
# n = 7
# for i in range(n):
#     if i % 2 == 0:
#         continue
#     if i == 9:
#         break
#     print(i)
# else:
#     print('done')

# # enumerate関数
# fruits = ['apple', 'banana', 'cherry']
# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# # zip関数
# days = ['mon', 'tue', 'wed']
# fruits = ['apple', 'banana', 'cherry']
# prices = [100, 200, 300]
# for day, fruit, price in zip(days, fruits, prices):
#     print(day, fruit, f'¥{price}')

# # 辞書 for文
# d = {'x': 100, 'y': 200, 'z': 300}
# for k, v in d.items():
#     print(k, ':', v)

# # 関数定義 引数 戻り値
# def what_is_this(color):
#     if color == 'red':
#         return 'This is apple'
#     elif color == 'yellow':
#         return 'This is banana'
#     else:
#         return "I don't know"

# result = what_is_this(input('Enter color:'))
# print(result)

# # キーワード引数
# def menu(entree = 'beef', drink = 'wine'):
#     print(entree, drink)

# menu()
# menu(entree = 'chicken', drink = 'beer')
# menu(drink = 'coffee')

# # デフォルト引数 注意点
# # デフォルト引数に参照渡しを使用すると、バグの原因になるので、注意が必要
# # デフォルト引数にはNoneを使用する
# def test_func(x, l = None):
#     if l is None:
#         l = []
#     l.append(x)
#     return l

# # y = [1, 2, 3]
# # r = test_func(100, y)
# # print(r)

# r = test_func(100)
# print(r)
# r = test_func(100)
# print(r)

# # 位置引数のタプル化
# def say_something(word, *args):
#     print(word)
#     for arg in args:
#         print(arg)

# say_something('Hi', 'Mike', 'Nancy')

# # キーワード引数の辞書化
# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)

# d = {
#     'entree': 'beef',
#     'drink': 'wine',
#     'dessert': 'ice'
# }
# menu(**d)

# # Docstring
# def example_func(param1, param2):
#     """
#     This is an example function.
#     Args:
#         param1: The first parameter.
#         param2: The second parameter.
#     Returns:
#         The result of the function.
#     """
#     return param1 + param2

# print(example_func.__doc__)

# # 関数内関数
# def outer(a, b):
#     def plus(c, d):
#         return c + d

#     r1 = plus(a, b)
#     r2 = plus(b, a)
#     print(r1 + r2)

# outer(1, 2)

# # クロージャー
# def outer(a, b):
#     def inner():
#         return a + b
#     return inner

# f = outer(1, 2)
# r = f()
# print(r)

# def circle_area_func(pi):
#     def circle_area(radius):
#         return pi * radius * radius
#     return circle_area

# ca1 = circle_area_func(3.14)
# ca2 = circle_area_func(3.141592)

# print(ca1(10))
# print(ca2(10))

# # デコレーター
# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper

# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# @print_info
# @print_more
# def add_num(a, b):
#     return a + b

# r = add_num(10, 20)
# print(r)

# # ラムダ
# l = ['Mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

# def change_words(words, func):
#     for word in words:
#         print(func(word))

# # def sample_func(word):
# #     return word.capitalize()
# # ↓これと同じ
# # sample_func = lambda word: word.capitalize()
# # ↓これと同じ
# change_words(l, lambda word: word.capitalize())

# # ジェネレーター
# def counter(num = 10):
#     for _ in range(num):
#         yield 'run'

# def greeting():
#     yield 'Good morning'
#     yield 'Good afternoon'
#     yield 'Good night'

# g = greeting()
# c = counter(10)
# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# print(next(g))

# # リスト内包表記
# t = (1, 2, 3, 4, 5)
# t2 = (10, 20, 30, 40, 50)

# # r = []
# # for i in t:
# #     if i % 2 == 0:
# #         r.append(i)
# # ↓これと同じ
# r = [i for i in t if i % 2 == 0]
# print(r)

# r = [i * j for i in t for j in t2]
# print(r)

# # 辞書内包表記
# w = ['mon', 'tue', 'wed']
# f = ['apple', 'banana', 'cherry']

# # d = {}
# # for x, y in zip(w, f):
# #     d[x] = y
# # ↓これと同じ
# d = {x: y for x, y in zip(w, f)}
# print(d)

# # 集合内包表記
# s = {i for i in range(10) if i % 2 == 0}
# print(s)

# # ジェネレータ内包表記
# # def g():
# #     for i in range(10):
# #         yield i
# # ↓これと同じ
# g = (i for i in range(10) if i % 2 == 0)

# for x in g:
#     print(x)

# # 名前空間とスコープ
# # global変数
# # local変数
# """
# Test Test #############
# """
# animal = 'cat'

# def f():
#     """Test func doc"""
#     print(f.__name__)
#     print(f.__doc__)

# f()
# print('global:', globals())

# # 例外処理
# l = [1, 2, 3]
# i = 5
# # del l

# try:
#     () + l
# except IndexError as ex:
#     print("don't worry: {}".format(ex))
# except NameError as ex:
#     print(ex)
# except Exception as ex:
#     print('other: {}'.format(ex))
# else:
#     print('done')
# finally:
#     print('clean up')

# 独自例外処理
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'banana', 'cherry']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as ex:
    print('This is my fault. Go next')
else:
    print('done')