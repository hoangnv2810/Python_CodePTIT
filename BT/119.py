f = open("pi_digits.txt")
contents = f.read()
print(contents.rsplit())

f.close()

with open("pi_digits.txt") as file:
    cn = file.read()

print(cn)