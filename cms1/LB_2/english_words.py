text = input()
counter = 0
unique_array = []

for i in text:
    if i not in unique_array:
        unique_array.append(i)

print(len(unique_array))
a=text.split()
print(len(set(text)))