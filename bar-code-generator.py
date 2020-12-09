#!pip install python-barcode

from barcode import *
from barcode.writer import ImageWriter

def BarCodeGenerator(code, bar_type):
	"""
	Bar Code Generator

	Assintotic: O(11) >> O(1)
	"""
	if bar_type == 0: EAN8(code, writer=ImageWriter()).save('ean-8')
	if bar_type == 1: EAN13(code, writer=ImageWriter()).save('ean-13')
	if bar_type == 2: EAN14(code, writer=ImageWriter()).save('ean-14')
	if bar_type == 3: UPCA(code, writer=ImageWriter()).save('upc-a')
	if bar_type == 4: JAN(code, writer=ImageWriter()).save('jan')
	if bar_type == 5: ISBN10(code, writer=ImageWriter()).save('isbn-10')
	if bar_type == 6: ISBN13(code, writer=ImageWriter()).save('isbn-13')
	if bar_type == 7: ISSN(code, writer=ImageWriter()).save('issn')
	if bar_type == 8: Code39(code, writer=ImageWriter()).save('code-39')
	if bar_type == 9: Code128(code, writer=ImageWriter()).save('code-128')
	else:             PZN(code, writer=ImageWriter()).save('pzn')

def BarCodeDescription(with_description=True):
	types = {'EAN-8' : 'Numbers Only (7 digits + 1 check digit)'
		, 'EAN-13' : 'Numbers Only (12 digits + 1 check digit)'
		, 'EAN-14' : 'Numbers Only (13 digits + 1 check digit)'
		, 'UPC-A' : 'Numbers Only (10 digits + 1 check digit)'
		, 'JAN' : 'Numbers Only (45 or 49 +  10 digits + 1 check digit)'
		, 'ISBN-10' : 'Numbers Only (9 digits + 1 check digit)'
		, 'ISBN-13' : 'Numbers Only (978 or 979 + 8 digits + 1 check digit)'
		, 'ISSN' : 'Numbers Only (3 prefix digits + 6 digits + 2 issues digits + 1 check digit + 2 sequence digits)'
		, 'Code 39' : 'UpperCase Letters, Numbers, Space and Symbols [- . $ / + %] (variable length)'
		, 'Code 128' : 'All ASCII chars (variable length)'
		, 'PZN' : 'Numbers Only (6 digits + 1 check digit)'}

	return list(types.items()) if with_description else list(types.keys())

##############

# Informations and Execution

types_with_description = BarCodeDescription(True)
print('*** Types and Descriptions ***\n')
for type in types_with_description: print(type)
print('\n')

types_without_description = BarCodeDescription(False)
print('*** Types ***\n')
for type in types_without_description: print(type)
print('\n')

BarCodeGenerator('12345678', 0)
BarCodeGenerator('1234567890123', 1)
BarCodeGenerator('12345678901234', 2)
BarCodeGenerator('12345678901', 3)
BarCodeGenerator('4512345678901', 4)
BarCodeGenerator('1234567890', 5)
BarCodeGenerator('9784567890123', 6)
BarCodeGenerator('123456', 7)
BarCodeGenerator('123456789', 8)
BarCodeGenerator('123456789', 9)
BarCodeGenerator('1234567', 10)  
