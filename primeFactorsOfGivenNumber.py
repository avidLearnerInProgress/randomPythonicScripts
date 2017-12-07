#Prime factors of a given number

from math import sqrt;

def remove_duplicates(l):
    return list(set(l))

def primeFactors(n):
	l=[];
	e=[];
	while n%2==0:
		l.append(2);
		n/=2;

	for x in range(3,int(sqrt(n))+1,2):
		while n%x==0:
			l.append(int(x));
			n/=x;

	if n>2:
		l.append(int(n));

	e=remove_duplicates(l);

	for x in e:
		print(x,end=' ');

k=int(input("Enter number: "));
primeFactors(k);
