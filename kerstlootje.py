names = []

while True:
    question = input('Type de namen van de deelnemers. Type \'1\' als je klaar bent ')
    names.append(question)
    if '1' in names:
        names.remove('1')
    if question == '1':
        if len(names) > 1:
            print(names)
            break
        else:
            print('Er is maar 1 deelnemer opgegeven!')


my_list=sorted(names)
 
duplicates=[]
for i in my_list:
     if my_list.count(i)>1:
         if i not in duplicates:
             duplicates.append(i)
 
print(duplicates)