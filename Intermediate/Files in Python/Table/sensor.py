words = ['donkey' , 'Don-key', 'DON_KEY', 'abcd']

with open('sample.txt') as f:
    content = f.read().lower()
for word in words:
    content = content.replace(word,'!@#$%^')
    with open('sample.txt','w') as f:
        f.write(content)

