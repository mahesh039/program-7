def pal(s):
    s=s.lower()
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return pal(s[1:-1])
my_input=input ("enter a sring:")
if pal(my_input):
    print(f"{my_input}'is a palindrome")
else:
    print(f"{my_input}'is ot a palindrome")