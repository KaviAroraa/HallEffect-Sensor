
# f = open('email.txt', 'r')
# f2 = open('names.txt', 'r')
#
# emails = f.readlines()
# names = f2.readlines()
#
# for i in range(len(emails)):
#     print(emails[i][0:-1] + ':' + names[i][0:-1])
#
# f.close()
# f2.close()

# f = open('abc.txt', 'w')
# a = [1,2,3,4,5]
# for i in range(len(a)):
#     f.writelines(str(a[i]))
#     f.writelines('\n')
# f.close()
#
# def add():
#     f = open('items.txt', 'a')
#     L = []
#     item = input("Enter item: ")
#     quantity = input("Enter quantity: ")
#     price = input("Enter price: ")
#     L = [item, quantity, price]
#     for i in L:
#         f.writelines(i + ' ')
#     f.close()
# def show():
#     f = open('items.txt', 'r')
#     x = f.readlines()
#     final = 0
#     for i in x:
#         a = i.split()
#         total = int(a[1])*int(a[2])
#         print('Value of', a[0],'ís', total)
#         final += total
#     print('Total value:', final)
#     f.close()
# add()
# show()

# L = []
# Sum = 0
# for i in range(0,1000):
#     if i%3 == 0 or i%5 == 0:
#         if i not in L:
#             L.append(i)
# for j in L:
#     Sum += j
#
# print(Sum)

#Find sum of even valued terms of fibonacci series till 4 mil
sum = 0
a = 0
b = 1
while sum < 4000000:
    sum = a+b
    a = b
    b = sum

    print(sum, end = '')
