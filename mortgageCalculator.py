term=(12)*int(input("Enter Mortgage Term in Years: "))
interest_rate=float(input("Enter Annual Interest: "))/12
loan=int(input("Enter Mortgage Loan: "))

temp=((1+interest_rate)**term);
temp1=(interest_rate*(temp));
temp2=temp-1;

mortgage=float((loan*temp1)/temp2);
print("MOnthly payment is:",mortgage);
