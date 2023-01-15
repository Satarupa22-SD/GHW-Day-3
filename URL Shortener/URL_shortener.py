import pyshorteners
user_link = input('Enter Your URL:\n  ')
shorts = pyshorteners.Shortener()
i = shorts.tinyurl.short(user_link)
print(i)