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


A = [1, 3, 5, 7, 2, 0, 7, 8]
B = [2, 4, 6]

#print(merge(A, B))

def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        L = A[:len(A) // 2]
        R = A[len(A) // 2:]
        return merge(MergeSort(L), MergeSort(R))

print(MergeSort(A))