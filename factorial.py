def factorialRecursive(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorialRecursive(n-1)

def factorialNonRecursive(n):
	product=1
	for i in range(1,n+1):
		product*=i;
	return product		


def main():
	x=int(input("Enter Number: "))
	print(factorialRecursive(x))
	print(factorialNonRecursive(x))

if __name__ == '__main__':
	main()



