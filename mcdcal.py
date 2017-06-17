f = open("drinksmenu-cal.csv","r") # opens mcd nutritional info menu as read only
menu = f.read() # reads it in assigned to menu

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

cat_slice = categories[1:len(categories)-1] # removes the category header

# code to count the number of categories in a list using a dictionary
category_counts = {}
for c in cat_slice:
    if c in category_counts:
        category_counts[c] = category_counts[c] + 1 
    else: 
        category_counts[c] = 1

print(category_counts)

calories = []
for r in final_data:
    final_datas = r[2]
    calories.append(final_datas)

cal_slice = calories[1:len(calories)-1]

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

print(high_cal)
print(low_cal)
