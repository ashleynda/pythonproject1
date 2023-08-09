# with open('account.txt', mode='w') as my_file:
#     my_file.write('001 esther 15\n')
#     my_file.write('002 moyin 13\n')
#     my_file.write('003 precious 16\n')
#     my_file.write('004 ashley 23\n')
#     my_file.write('005 grace 20\n')
# with open('account.txt', mode='r') as my_file:
#     print(my_file.read())

file_obj = open('account.txt', mode='r')
print(file_obj.readlines())
file_obj.seek(0)
print(file_obj.readlines())
file_obj.close()
