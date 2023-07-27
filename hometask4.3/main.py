import string
source = str("Should, I. subscribe? Yes qqqqq wwwww eeeee rrrrr ### ttttt yyyyy uuuuu iiiii ooooo ppppp aaaaa sssss ddddd fffff ggggg hhhhh jjjjjeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee111")
proc = ""
for char in source:
    if char not in string.punctuation:
        proc += char
source = ("#" + proc).title().replace(" ", "")
print(source[0:140])
