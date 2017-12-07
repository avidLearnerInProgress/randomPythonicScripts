'''
   Q = 0.25;
   D = 0.10;
   N = 0.05;
   P = 0.01;
'''
def main():
	amount=float(input("Enter total amount: "));
	money=float(input("Enter money paid: "));
	change=float(amount-money);
	changeReturn(change);

def changeReturn(change):
	Q,D,N,P=0.25,0.10,0.05,0.01
	numQ=numD=numN=numP=0
	while change>0:
		if change>=Q:
			change-=Q
			numQ+=1

		elif change>=D:
			change-=D
			numD+=1

		elif change>=N:
			change-=N
			numN+=1

		else:
			change-=P
			numP+=1

	print("Quarters: ",numQ);
	print("Dimes: ",numD);
	print("Nickles: ",numN);
	print("Pennies: ",numP);

if __name__ == '__main__':
	main()




