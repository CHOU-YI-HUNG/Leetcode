

def lenofLastWord(s):
    return len(list(filter(None,s.split(" ")))[-1])

s = "Hello World"
print(lenofLastWord(s))
s="   fly me   to   the moon  "
print(lenofLastWord(s))
s="luffy is still joyboy"
print(lenofLastWord(s))