test_dict = {'I' : 2, 'am' : 2, 'great' : 2, 'at' : 2, 'go-karting' : 1 }
K = 2
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1
print("Frequency of K is: " + str(res))