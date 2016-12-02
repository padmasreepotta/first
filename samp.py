import string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''

p = raw_input("Enter a string: ")
print("%s",p)
q = ""
for i in p:
   if i not in punctuations:
       q=q+i
print(q)
q=q.lower()
print q

s=reversed(q)
print s
if list(q)==list(s):
   print "its a palindrome"
else:
   print "not a palindrome"
   
