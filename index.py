

li = [1,2,3,5]

for i in li:
    if i == 'hadi':
        break
    else:
        print(i)
username  = ''        
def login(username):
    username = input()
    if username != "":
        print('welcome')
    else:
        print('enter your username ')


login(username)