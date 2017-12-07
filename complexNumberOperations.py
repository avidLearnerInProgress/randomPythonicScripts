class complexNumber:
	def __init__(self,real1,img1,real2,img2):
		self.real1=real1
		self.img1=img1
		self.real2=real2
		self.img2=img2

	def addRealPart(self):
		return self.real1+self.real2

	def addImaginaryPart(self):
		return self.img1+self.img2

	def subRealPart(self):
		return self.real1-self.real2

	def subImaginaryPart(self):
		return self.img1-self.img2

	def multiplyRealPart(self):
		#(x+yi)(u+vi) = (xu-yv)+(xv+yu)i
		return ((self.real1*self.real2)-(self.img1*self.img2)) 

	def multiplyImaginaryPart(self):
		return((self.real1*self.img2)+(self.real2*self.img1))

	def divideRealPart(self):
		#a=(((s1.rel)*(s2.rel))+((s1.img)*(s2.img)))/(pow(s2.rel,2)+pow(s2.img,2));
		#b=(((s2.rel)*(s1.img))-((s1.rel)*(s2.img)))/(pow(s2.rel,2)+pow(s2.img,2));
		return ((self.real1*self.real2)+(self.img1*self.img2))/((self.real2**2)+(self.img2**2))
	
	def divideImaginaryPart(self):
		return ((self.real2*self.img1)-(self.real1*self.img2))/((self.real2**2)+(self.img2**2))



def main():
	x,y=input("Enter real and imaginary part of first Number:").split()
	w,z=input("Enter real and imaginary part of second Number:").split()

	x1,y1=int(x),int(y)
	x2,y2=int(w),int(z)

	a=complexNumber(x1,y1,x2,y2)

		#Addition
	addReal=a.addRealPart() 
	addImg=a.addImaginaryPart()
	print(str(addReal)+" + "+str(addImg)+" i")

		#Subtraction
	subReal=a.subRealPart()
	subImg=a.subImaginaryPart()
	print(str(subReal)+" + "+str(subImg)+" i")

		#Multiplication
	multiplyReal=a.multiplyRealPart()
	multiplyImg=a.multiplyImaginaryPart()
	print(str(multiplyReal)+" + "+str(multiplyImg)+" i")

		#Division
	divideReal=a.divideRealPart()
	divideImg=a.divideImaginaryPart()
	print(str(divideReal)+" + "+str(divideImg)+" i")


if __name__ == '__main__':
	main()









