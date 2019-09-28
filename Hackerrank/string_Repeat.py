 #s = string which is considere reapeted infinity 
    #n = the firts number of letter to be considered fot counting number of
    #ocurrences of character 'a' in a infinite string


def reapetedstring(s,n):
    len_str = len(s)

    num_strs = n//len_str

    remainder = n %len_str

    count1 = 0

    count2 = 0

    for i in range(len_str):
        if s[i] =='a':
            count1 += 1
        if s[i]== 'a' and i<remainder:
            count2 += 1
    
    total = count1* num_strs + count2

    return total

print(reapetedstring('aba', 10))
   