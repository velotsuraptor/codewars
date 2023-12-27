'''def quarter_of(month):
    # your code here'''

month = input('Enter month ')
quaters = {'first':[1,2,3], 'second':[4,5,6], 'third':[7,8,9], 'fortth':[10,11,12]}
for key in quaters:
    if month == key:
        print(key)