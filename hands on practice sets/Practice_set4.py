# fruit_name = input("Enter any seven fruits name you want separated with comma eg. ,").strip()
# if fruit_name.count(",")!= 6:
#    print("Invalid input \nEnter the correct number of items 7")
# else :
#     fruit_list = fruit_name.split(",")

#     for fl in fruit_list:
#         print(fl)



# marks = []
# for index in range (0,5):
#     try:
#       mark = int(input(f"Enter marks of student {index + 1}: "))
#       marks.append(mark)
#     except ValueError:
#        print("Invalid input ")
#        exit()
      
# count=1      
# for mark in marks:
#    print(f"The marks of student {count} is {mark}")
#    count+=1



# list_numbers = [2,4,4,6]

# sum_of_numbers = 0

# for i in list_numbers:
#     sum_of_numbers+=i

# print(sum_of_numbers)

num_list = (0,23,0, 34, 0,35,0)

zeroes =num_list.count(0)
print(zeroes)
