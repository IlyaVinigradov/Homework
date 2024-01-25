"""
Необходимо написать программу, которая будет считывать со стандартного ввода строку, 
далее будет приводить ее к нижнему регистру, а также будет заменять символы “!”, “%”, “#”, “@” на пустую 
строку. В итоге нужно будет вывести в первой строке число замененных символов, а во второй 
преобразованную строку.

входные данные:
Hello World!@#%

выходные данные:
4
hello world
"""

user_input = input().lower()
count = 0

count += user_input.count('!')
user_input = user_input.replace('!', '')
count += user_input.count('%')
user_input = user_input.replace('%', '')
count += user_input.count('#')
user_input = user_input.replace('#', '')
count += user_input.count('@')
user_input = user_input.replace('@', '')

print(count)
print(user_input)