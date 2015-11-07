__author__ = 'anastasiiakorosteleva'
def kmp(s1, s2):  #search s1 in s2
    i = 0
    j = 0
    l1 = len(s1)
    l2 = len(s2)
    offset = []
    # pre-process
    for o in range(1, l1+1):
        offset.append(0)
        _tmp = s1[:o]
        for _o in range(o-1, 0, -1):
            # prefix and sufix max match length
            if _tmp[:_o] == _tmp[o-_o:]:
                offset[o-1] = _o
                break
    while j < l1 :
        if i == l2:  # end when get the end
            return "No match"
        if s1[j] == s2[i]:
            i += 1
            j += 1
        else:
            if j:
                j = offset[j-1]
                i += j
            else:
                i += 1
    return i-l1

if __name__ == '__main__':
    print (kmp('ABCDABD', 'BBC ABCDAB ABCDABCDABDE') )
    print (kmp('ab', 'abababababababababeb') )
    print (kmp('abababeb', 'ecbabababababababab') )
