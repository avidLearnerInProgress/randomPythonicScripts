#
def reverse(num):
  return str(num)[::-1]

def binaryToDecimal(n):
	convert=reverse(n)
	converted=0
	for i in range(0,len(convert),1):
		if convert[i]=='1':
			converted+=(2**i)
	print(converted)		

def convertToBinary(n):
	if n > 1:
		convertToBinary(n//2)
	print(n%2,end='')

binary=input("Enter Binary String:")
decimal=int(input("Enter Decimal Number:"))


def main():
	binaryToDecimal(binary)
	convertToBinary(decimal)

	
if __name__ == '__main__':
	main()



'''
Simpler way direct using functions:

dec=int(input("Enter Decimal Number:"))
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
'''