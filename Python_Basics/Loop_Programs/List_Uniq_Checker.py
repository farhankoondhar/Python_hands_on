item = input("Enter elements in the list but separate with commas : ")
item_List = [i.strip() for i in item.split(",")]
unique_Items = set()
item_Listlen = len(item_List)
for i in range(item_Listlen):
    if item_List[i] in unique_Items:
        print("The Duplicate item : ",item_List[i])
        break
    unique_Items.add(item_List[i])
print(unique_Items)