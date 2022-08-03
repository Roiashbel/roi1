input_line = input("入力")
moji= len(input_line)
one_line = "++"
three_line = "++"
for i in range(moji):
    one_line += "+"
    three_line += "+"
print(one_line)
print("+" + input_line + "+")
print(three_line)

