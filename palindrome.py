#!\usr\bin\env python3
# -*- coding:utf-8 -*-
def is_palindrome(n):
    s = str(n)
    i = len(s)-1
    k = 0
    while i > k:
        if s[i] != s[k]:
            return False
        i -= 1
        k += 1
    return True

output=filter(is_palindrome,range(0,1000))
print(list(output))
