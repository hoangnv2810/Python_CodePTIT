s = input()
str = s[s.find("h") + 1:s.rfind("h")]
print(s[:s.find("h") + 1] + str.replace("h","H") + s[s.rfind("h"):])