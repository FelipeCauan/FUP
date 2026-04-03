word = input()
result = ""

for characters in word:
    result = result + chr(ord(characters)+1)

print(result)
