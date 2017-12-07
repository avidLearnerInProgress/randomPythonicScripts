# your code goes here

def findNextPrime(n):
	nextPrime=n;
	found=False;
	
	while not found:
		nextPrime+=1;
		#print(nextPrime);
		if isPrime(nextPrime):
			found=True;
	return nextPrime;
	
def isPrime(n):
	#print(n);
	for i in range(2,int(n/2),1):
		if n%i==0:
			return 0;
	return 1;

	
k=int(input("Enter Number"));
print(k);
print(findNextPrime(k));
	
	