
text = eval(input())

print(eval({list: 'text[-1]', tuple: 'text[0]', set: 'len(text)'}[type(text)]))






