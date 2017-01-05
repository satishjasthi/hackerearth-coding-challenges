'''
Description: given a string S,print "YES" if S is a palindrom ,else "NO"
'''
s = raw_input("Please enter the string: \n")
l = list(s.lower())
if(len(l)%2 == 0):
	e = [True if(l[i] == l[-(i+1)]) else False for i,j in enumerate(l) ]
	print ("NO" if False in e else "YES" )
else:
	l.remove(l[(len(l) - 1)/2])
	o = [True if(l[i] == l[-(i+1)]) else False for i,j in enumerate(l) ]
	print ("NO" if False in o else "YES" )
