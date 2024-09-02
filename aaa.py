def isSubstring(s1,s2):
    return s2 in s1

print(isSubstring("Hello World", "Hello"))
print(isSubstring("Hello World", "World"))
print(isSubstring("Hello World", "HELLO"))
