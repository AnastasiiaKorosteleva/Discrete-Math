__author__ = 'anastasiiakorosteleva'
__author__ = 'anastasiiakorosteleva'
 #Для двух стеков -- первого и второго, Первый стек будет добавлять элемент во второй, стек 2 удаляет элемент из стека 1. Если
 # первый стек пуст, то переносятся из второго в первый. Элементы из первого стека переносятся в обратном порядке, а второй
 #  остается пустым. Время зависит от входа.
class Queue:

    def __init__(self, n):
        self.leftStack = [0 for x in range(n)]
        self.i_left = 0
        self.rightStack = [0 for x in range(n)]
        self.i_right = 0


    def ISempty(self):
        return self.i_left == self.i_right


    def Whatsize(self):
        if self.i_right > self.i_left:
            return self.i_right + self.i_left
        else:
            return self.i_left - self.i_right


    def enqueue(self, e):
        if self.i_left == len(self.leftStack):
            print ("I Am Full")
        else:
            self.leftStack[self.i_left] = e
            self.i_left += 1


    def dequeue(self):
        if self.i_right == 0:
            if self.i_left == 0:
                return 'I Am Empty'
            else:
                while self.i_left != 0:
                    self.rightStack[self.i_right] = self.leftStack[self.i_left - 1]
                    self.i_left -= 1
                    self.i_right += 1
        self.i_right -= 1
        return self.rightStack[self.i_right]


q=Queue(2)
print(q.dequeue())

q.enqueue('mama')
q.enqueue('yomayo')
q.enqueue(4)

print(q.Whatsize())



