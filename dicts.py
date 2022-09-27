a = {'test': {'a': False},
     'execute': lambda x: print(x)}

text = 'hello world'
a['execute'](text)