z=[]
x=(1,2,3,4,5,6,7,8,9,0)
def names():
    while True:
        y = input('write your name : ').strip()
        if not y:
            print('you must enter your name')
            continue
        if not all(c.isalpha() or c == ' ' for c in y):
            print('name must contain letters only')
            continue
        z.append(y)
        return y


while True :
   value = names()

   try:
        num = int(value)
        if num in x:
          print('u may forgot to add ur name ')
          continue
        else:
          print('thnks')
          break
   except ValueError:
        print('thnks')
        break
