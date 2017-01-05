'''
Description:
given a string return the string by reversing it case state ie converting
uppercase letter to lowercase and vice versa.
'''

s = raw_input()
l = list(s)
l = [l[i].upper() if(l[i].islower()) else(l[i].lower()) for i,j in enumerate(l)]
print "".join(l)
