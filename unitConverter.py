
#!/usr/bin/python3

#temperature converter
'''
1: kelvin to celsius
2. kelvin to fahrenheit
3. celsius to kelvin
4. celsius to fahrenheit
5. fahrenheit to celsius
6. fahrenheit to kelvin
'''

def kelvin_to_fahrenheit(value):
	convert=value
	const=273.15
	return float((1.8*(convert-const))+32)

def kelvin_to_celsius(value):
	convert=value
	const=273.15
	return float(convert-const)

def celsius_to_kelvin(value):
	convert=value
	const=273.15
	return float(convert+const)

def celsius_to_fahrenheit(value):
	convert=value
	return float((1.8*convert)+32)

def fahrenheit_to_kelvin(value):
	convert=value
	const=459.67
	return float((convert+const)*(5/9))

def fahrenheit_to_celsius(value):
	convert=value
	return float((5/9)*(convert-32))


#{u'IDR': 11612.0, u'BGN': 1.4349, u'ILS': 3.4861, u'GBP': 0.5938, u'DKK': 5.4762, u'CAD': 1.0901, u'JPY': 101.92, u'HUF': 222.66, u'RON': 3.2359, u'MYR': 3.2101, u'EUR': 0.73368, u'SEK': 6.6471, u'SGD': 1.2527, u'HKD': 7.7519, u'AUD': 1.0845, u'CHF': 0.89582, u'KRW': 1024.9, u'CNY': 6.2377, u'TRY': 2.0888, u'HRK': 5.5751, u'NZD': 1.1707, u'THB': 32.6, u'LTL': 2.5332, u'NOK': 5.9652, u'RUB': 34.122, u'INR': 58.509, u'MXN': 12.893, u'CZK': 20.131, u'BRL': 2.2178, u'PLN': 3.0544, u'PHP': 43.721, u'ZAR': 10.356}


#currency converter
#Using forex-python package to convert currency from one system to another
'''
1. from 3-digit code to another 3-digit code
2. from bitcoin to 3-digit code
3. from 3-digit code to bitcoin
'''

from forex_python.converter import CurrencyRates

def currency_converter(from_code,to_code,amount):
	c=CurrencyRates()
	if amount%1==0:
		output=c.convert(from_code,to_code,amount)
	else:
		output=c.convert(from_code,to_code,Decimal(amount))
	return output

from forex_python.bitcoin import BtcConverter
def bitcoin_to_curr(amount,to_code):
	output=b.convert_btc_to_cur(amount,to_code)
	return output

def curr_to_bitcoin(amount,from_code):
	output=b.convert_to_btc(amount,from_code)
	return output


#mass converter
'''
1. lb(pound) to gram
2. lb to oz (ounce)
3. lb to kg
4. gram to lb
5. gram to oz
6. gram to kg
7. oz to lb
8. oz to gram
9. oz to kilogram
10. kg to lb
11. kg to oz
12. kg to gram
'''

def lb_to_gram(weight):
	const=453.59237
	return float((weight*const))

def lb_to_oz(weight):
	return float(weight*16)

def lb_to_kg(weight):
	return float(lb_to_gram(weight)*1000))

def gram_to_lb(weight):
	const=453.59237
	return float(weight/const)

def gram_to_oz(weight):
	const=28.34952
	return float(weight/const)

def gram_to_kg(weight):
	return float(weight*1000)

def oz_to_gram(weight):
	const=28.34952
	return float(weight*const)

def oz_to_lb(weight):
	return float(weight*16)

def oz_to_kg(weight):
	return float(oz_to_gram*1000)

def kg_to_lb(weight):
	const=0.45359237
	return float(weight/const)

def kg_to_oz(weight):
	const=0.02834952
	return float(weight/const)

def kg_to_gram(weight):
	return float(weight/1000)




def main():



if __name__ == '__main__':
	main()	
