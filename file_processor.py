file = "C:\\Users\\srratako\\OneDrive - Ciena Corporation\\Desktop\\Class Code\\data.txt"



# print all occurences....!

# count = 1

# with open(file) as file:
#     for line in file:
#         if 'V37628' in line:
#             print(count, line)
#         count += 1


# print only first occurences....!

count = 1

with open(file) as file:
    for line in file:
        if 'Vlan1993' in line: 
            print(line, 'in continue', sep='   :    ')
            count += 1
            continue
        print(line, "this wont print", sep="   :   ")
        if 'V37628' in line:
            print(count, line)
            break 
        count += 1
