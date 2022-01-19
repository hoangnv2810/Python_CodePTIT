s = input()
tmp = s[s.find('h')+1:s.rfind('h')]
a = s[:s.find('h')+1] + tmp.replace('h', 'H') + s[s.rfind('h'):]
print(a)