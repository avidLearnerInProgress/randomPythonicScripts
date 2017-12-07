 def luhn_check(n):
	r=[int(ch) for ch in str(n)][::-1]
	return (sum(r[0::2])+sum(sum(divmod(d*2,10))for d in r[1::2])) % 10==0
 
if __name__ == "__main__":
    validity=luhn_check(input("Enter your credit card number:"))
    print(validity)