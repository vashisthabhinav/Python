
f = open('sample.txt')
t = f.read()
if 'Abhinav' in t:
    print('Abhinav is present')
else:
    print('Abhinav is not present')
f.close()


def game():
    return 480

score = game()
with open('Highscore.txt') as f:
    Highscore =  f.read()

if int(Highscore)<score or Highscore=='':
    with open('Highscore.txt','w') as f:
        f.write(str(score))
else:
    pass