snake_case = input()
words = snake_case.split('_')
camel_case = words[0] + ''.join(word.title() for word in words[1:])
print(camel_case)