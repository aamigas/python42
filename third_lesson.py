# price = {'Молоко' : 2, 'Масло' : 5, 'Мука' : 7}
# a = input()
# print(price.get(a, 'Not in shop'))

l = [11, 17, 7, 14, 49, 5, 7]

i = 0
for x in l:
    i+=1
    if x % 7 == 0:
        print(x, i-1)

