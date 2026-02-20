# from step_up_package import utils
# from step_up_package.talk import human, animal

# r = utils.say_twice('hello')
# print(r)

# print(human.sing())
# print(human.cry())

# print(animal.sing())
# print(animal.cry())

# 組み込み関数
# pythonのドキュメントを参照すると良い

# # 標準ライブラリ

# s = "dnfojwrnfourwfhnwlkf"

# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)

# d = {}
# for c in s:
#     d.setdefault(c, 0)
#     d[c] += 1
# print(d)

# from collections import defaultdict
# d = defaultdict(int)
# for c in s:
#     d[c] += 1
# print(d)

# d = defaultdict(int)
# for c in s:
#     d[c] += 1
# print(d)

# # サードパーティライブラリ
# # pyPIから検索する
# # 例：コマンドライン pip install termcolor
# from termcolor import colored
# print(colored('Hello!', 'red'))
# print(colored('Hello!', 'red', 'on_cyan'))
# print(colored('Hello!', 'red', 'on_cyan', attrs=['bold']))

# # __name__ と __main__
# # モジュールの中でテストを行いたい場合は、if __name__ == '__main__': を使用する
# # (step_up_package/utils.py 参照)
# from step_up_package import utils

# print("step_up: ", utils.say_twice('hello'))

# # クラスの定義 オブジェクト指向プログラミング
# class Person(object):
#     def __init__(self, name):
#         self.name = name

#     def say_something(self):
#         print(f'hello, my name is {self.name}')
#         self.run(10)

#     def run(self, num):
#         print('run' * num)

#     def __del__(self):
#         print('good bye')

# person = Person('Seita')
# person.say_something()

# del person

# # クラスの継承
# class Car(object):
#     def run(self):
#         print('run')

# class ToyotaCar(Car):
#     pass

# class TeslaCar(Car):
#     def auto_run(self):
#         print('auto run')

# car = Car()
# car.run()

# toyota_car = ToyotaCar()
# toyota_car.run()

# tesla_car = TeslaCar()
# tesla_car.run()
# tesla_car.auto_run()

# # メソッドのオーバーライド
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')

# class ToyotaCar(Car):
#     def run(self):
#         print('fast')

# class TeslaCar(Car):
#     def __init__(self, model="Model S", enable_auto_run=False):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
#     def run(self):
#         print('super fast')
#     def auto_run(self):
#         print('auto run')

# car = Car()
# car.run()

# print("########################")
# toyota_car = ToyotaCar("Prius")
# print(toyota_car.model)
# toyota_car.run()
# print("########################")

# tesla_car = TeslaCar("Model S")
# print(tesla_car.model)
# tesla_car.run()
# tesla_car.auto_run()

# # プロパティを使った属性の設定
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')

# class ToyotaCar(Car):
#     def run(self):
#         print('fast')

# class TeslaCar(Car):
#     def __init__(self, model="Model S",
#                 enable_auto_run=False,
#                 password="1234"):
#         super().__init__(model)
#         self._enable_auto_run = enable_auto_run
#         self.password = password

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.password == "1234":
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError("Password is incorrect")

#     def run(self):
#         print('super fast')
#     def auto_run(self):
#         print('auto run')

# tesla_car = TeslaCar("Model S", password="4321")
# tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)

# ダックタイピング
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age

#     def drive(self):
#         if self.age >= 18:
#             print('ok')
#         else:
#             raise Exception("No drive")

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

# baby = Baby()
# adult = Adult()

# class Car(object):
#     def __init__(self, model=None):
#         self.model = model

#     def ride(self, person):
#         person.drive()

# car = Car()
# # car.ride(baby)
# car.ride(adult)

# # 抽象クラス
# import abc
# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age

#     @abc.abstractmethod
#     def drive(self):
#         pass

# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         raise Exception("No drive")

# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError

#     def drive(self):
#         print("ok")

# baby = Baby()
# # baby.drive()
# adult = Adult()
# adult.drive()

# # 多重継承
# class Person(object):
#     def talk(self):
#         print('talk')

# class Car(object):
#     def run(self):
#         print('run')

# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print('fly')

# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()

# # クラス変数
# class Person(object):
#     kind = 'human'

#     def __init__(self, name):
#         self.name = name

#     def who_are_you(self):
#         print(self.name, self.kind)

# a = Person('A')
# b = Person('B')
# a.who_are_you()
# b.who_are_you()

# print("########################")
# class T(object):
#     def __init__(self):
#         self.words = []

#     def add_word(self, word):
#         self.words.append(word)

# c = T()
# c.add_word('add one')
# c.add_word('add two')
# c.add_word('add three')
# print(c.words)

# d = T()
# d.add_word('add four')
# d.add_word('add five')
# d.add_word('add six')
# print(d.words)

