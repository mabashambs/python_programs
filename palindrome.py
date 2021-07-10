def palindrome(key):
      return key == key[::-1]
      
key = input()
ans = palindrome(key)
if ans:
      print("is palindrome")
else:
      print("not a palindrome")
