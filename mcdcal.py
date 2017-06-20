menu = open("drinksmenu-cal.csv").read() # opens and read mcd nutritional info

rows = menu.split('\n')
final_data =[]
for row in rows: 
    split_list = row.split(',')
    final_data.append(split_list) # adds these elements to the final_data list

#print(final_data)

categories = []
for r in final_data: 
    final_datas = r[0] # each rows contains the first element from final data
    categories.append(final_datas) # add those first elements/cities to the cities list

#print(categories[0:5])

cat_slice = categories[1:len(categories)] # removes the category header

# code to count the number of categories in a list using a dictionary
category_counts = {}
for c in cat_slice:
    if c in category_counts:
        category_counts[c] = category_counts[c] + 1 
    else: 
        category_counts[c] = 1

print('\n',category_counts,'\n')

calories = []
for r in final_data:
    final_datas = r[2]
    calories.append(final_datas)

cal_slice = calories[1:len(calories)]

# print(cal_slice)

cal_int = []
for c in cal_slice:
    cal = int(c)
    cal_int.append(cal)

high_cal = [] # empty list of high calories
low_cal = [] 
for cal in cal_int:
    if cal > 150: 
        high_cal.append(cal) # add calories > 150 to high_cal list 
    else:
        low_cal.append(cal)

high_cal_single = []
for hc in high_cal:
    if hc in high_cal_single:
        pass # don't add cal if already in the list - avoids repeat cals
    else:
        high_cal_single.append(hc)

low_cal_single = []
for lc in low_cal:
    if lc in low_cal_single:
        pass # don't add cal if already in the list - avoids repeat cals
    else:
        low_cal_single.append(lc)



print("Range of High Calorie Drinks", '\n', sorted(high_cal_single),'\n')
print("Range of Low Calorie Drinks", '\n', sorted(low_cal_single),'\n')



items = []
for i in final_data:
    item = i[1]
    items.append(item)
item_slice = items[1:len(items)]

item_cal = dict(zip(item_slice, cal_int)) # pairs items and calories in a dictionary
# print(item_slice)

# hlatte = item_cal["Hazelnut Latte (Large)"]
# print("A Large Hazelnut Latte has",hlatte, "calories",'\n')

low_items = [k for k,v in item_cal.items() if v <= 150] # these items are less than 150 calories each
print("LOW CALORIE DRINKS",*low_items, sep='\n') # seperates each item per line

high_items = [k for k,v in item_cal.items() if v > 150] 
print('\n',"HIGH CALORIE DRINKS",*high_items, sep='\n') # seperates each item per line

print('\n',"USE calories(name of drink in quotes) TO GET IT'S CALORIES")  
def calories(drink_name, drinks_list = item_cal):  
    output = (drinks_list[drink_name])
    message = print("A",drink_name,"has", output, "calories!") 
    return(message)
    
    


