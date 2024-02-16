from string import ascii_uppercase

str_length = int(input())
letters = ascii_uppercase[0: str_length]

pos = 0
count = 1
lines = []
while pos < str_length:
        lines += [letters[pos: pos + count]]
        pos += count
        count += 1

out = []
height = len(lines)
for i in range(height):
    justify = 2*height - 1 if i != height - 1 else 0
    out.append(" ".join(lines[i]).rjust(justify))
print("\n".join(out))