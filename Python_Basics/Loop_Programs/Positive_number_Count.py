numbers = input ("Enter numbers in list but separated with ','(Commas) this : ")
numbers_list = [i.strip() for i in  numbers.split(",")]
# pos_nums = []
count =0
length = len(numbers_list)
for num in range(0,length):
       if num >0:
            #   pos_nums.append(num)
              count +=1
# for num in pos_nums:
#        print(num )
print(f"Total positive numbers in the above list is {count}")