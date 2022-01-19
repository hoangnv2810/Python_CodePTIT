s = input()
id1 = s[:s.find("h")+1]
id2 = s[s.rfind("h"):]
str = s[s.find("h")+1:s.rfind("h")]
if s.count("h") >= 2:
    print(id1 + str[::-1] + id2)
else:
    print(s.count("h"))