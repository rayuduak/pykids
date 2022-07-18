#

#this is an example to show palindrome.
#write a pallindrome sample.
#session -https://prod.liveshare.vsengsaas.visualstudio.com/join?030A4E677E85A69050BE9821C9C7496A0A46
#yes I am here
def isPalindrome(s):
    return s == s[::-1]
    

s = "malayalam"
ans=isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
print(s)
print(s[::-1])

