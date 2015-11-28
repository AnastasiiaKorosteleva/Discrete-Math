__author__ = 'anastasiiakorosteleva'
__author__ = 'anastasiiakorosteleva'

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

s=Stack()

#мы говорим, если встречаются символы скобок ( можно добавить и квадратные скобки), то записываем их в список,
# остальные символы игнорируем. Создаем стек в который записываем все открывающие скобки -- ({ -- далее с помощью счестчика index
# считаем совпадения открывающих и закрывающих скобок в функции matches, если все хорошо -- стек s должен быть isempty == true.

def parChecker(symbolString):
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "({"
    closers = ")}"
    return opens.index(open) == closers.index(close)

print(s.isEmpty())

print(parChecker('{{()}()}'))
print(parChecker('{()'))
