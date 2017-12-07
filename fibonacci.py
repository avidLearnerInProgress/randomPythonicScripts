def fibonacci(n):
	if n==0:
		return 0;
	if n==1 or n==2:
		return 1;
	else:
		return (fibonacci(n-1)+fibonacci(n-2));

#Enter max k as 30 to get faster results 
#Otherwise it will produce results slowly
k=int(input("Enter nth digit upto which fibonacci has to be generated:"));
for iterator in range(1,k+1):
	print(str(iterator)+"->"+str(fibonacci(iterator)));
	#print(iterator+" "+fibonacci(ans));


