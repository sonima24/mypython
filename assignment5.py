
#task1=create a dictionary of student marks
dictionary= {'Alice':'75','Bob':'55','Charlie':'80','David':'95'}
name = (input("Enter the student's name: "))
if name in dictionary:
    print(dictionary[name])
else:
    print('Student not found')

'''
#task2= demonstrate list slicing
original_list= [1,2,3,4,5,6,7,8,9,10]
print(original_list)
extract_first=original_list[:5]
print(extract_first)
extract_first.reverse()
print(extract_first)
'''