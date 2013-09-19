combo = { }

for i in range(1,7):
	for j in range(1,7):
		roll= i+j
		combo.setdefault( roll, 0 )
		combo[roll] += 1

for n in range(2,13):
	print ("%d %.2f%%" % ( n, combo[n] ))
	
ans = (2+3j)*(4+5j)
print (ans)
print (complex(3,2))
print (abs(-2.345))
print (pow(3,3,2))
print (round(2.3333,3))