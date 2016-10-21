def multiply(*numbers):
	multiply=1
	for number in numbers:
		multiply *= number
	return (multiply)
		    
		
	

print(multiply(1))
print(multiply(2,3,-2))
print(multiply(5,6,7))