__author__ = 'anastasiiakorosteleva'


def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
        else:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res

def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
        return merge(MergeSort(L), MergeSort(R))
 #это решение легко обощить для поиска всех сумм в массиве ( по-моему это задача о размене доллара ),
 # если не останавливать while return'ом, но вот я не уверена что сложность здесь не квадратная в худшем случае
def asd():
    A = [5, 6, 6, 7, 7, 9, 4, 5]
    x = 11

    B = MergeSort(A)

    m = x//2
    i = 0
    j = len(B)-1
    while B[i] <= m:
        j = len(B)-1
        while B[j] >= m:
            if x - B[j] == B[i]:
                return print((str(B[j]) + "+" + str(B[i]) ))

            j = j - 1
        i = i + 1
asd()



