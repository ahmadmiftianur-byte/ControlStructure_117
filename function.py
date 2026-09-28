"""
def ahmi (mi):
    print(mi)
    return 

ahmi("Ganteng")
ahmi(mi="Tampan")
ahmi("67")
"""
"""
def kontrakan (pintu):
    pintu.append([1,2,3,4,5]);
    print("ini adalah pintu kontrakan",pintu)
    return
pintu = [10, 20, 30, 40, 50];
kontrakan (pintu);
print("ini adalah pintu rumah",pintu)
"""
"""
def orang (anggota):
    anggota = ["ahmi", "tampan", "ganteng"];
    print("ini adalah anggota orang",anggota)
    return
anggota = ["ronaldo", "tampan", "ganteng"];
orang(anggota);
print("sepakbola    adalah",anggota)
"""
"""
def aldo(name, age):
    print("nama:", name)
    print("umur:", age)
    return

aldo(20, name ="febi")
aldo(age = 20, name = "ronaldo")
aldo(30, "ahmi")
"""
def convert_temperature(value, unit):
	"""Convert a temperature. unit = 'C' (from Celsius) or 'F' (from Fahrenheit)."""
    unit = unit.upper()              # accept 'c' and 'f' too

    if unit == 'C':
        return (value * 9 / 5) + 32  # Celsius -> Fahrenheit
    elif unit == 'F':
        return (value - 32) * 5 / 9  # Fahrenheit -> Celsius
    else:
        return None                  # invalid unit


# --- Testing ---
print(convert_temperature(100, 'C'))   # 212.0
print(convert_temperature(212, 'F'))   # 100.0
print(convert_temperature(37, 'C'))    # 98.6
print(convert_temperature(50, 'K'))    # None (invalid unit)

"""
def printinfo( arg1, *vartuple ): 
	print ("Output is: ")
	print (arg1)
	for var in vartuple: 
			print (var) 
	return; 
printinfo( 10, 0 ); 
printinfo( 70, 60, 50 ); 
"""
"""
sum = lambda arg1, arg2: arg1 + arg2;
print ("Value of total : ", sum( 10, 20 )) 
print ("Value of total : ", sum( 20, 20 ) )
"""
"""
def sum( arg1, arg2 ):
    total = arg1 + arg2;
    print ("Inside the function : ", total)
    return total;
sumdata = sum( 10, 20 );
"""