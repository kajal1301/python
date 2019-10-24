#regular expressions
import re

mystr = """Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map"""
# findall, search, split,   sub, finditer
#findall= it returns the specific string matches
#search= it returns a match object
print(r"\n")    #this prints \n as output. r is known as raw string
patt= re.compile(r"map")
#meta characters
matches = patt.finditer(mystr)
for match in matches:
    print(match) 
    print(mystr[448:552])
patt= re.compile(r".")   #it matches everything

matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt = re.compile(r'^Tata') #
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt = re.compile(r'iin$')  # $ indicates ends with
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt = re.compile(r'ai{2}') #{} indicates that i comes two times
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt = re.compile(r'(ai){1}')   #this tells that string 'ai' comes only once
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt = re.compile(r'ai{1}|t') # | is either symbol. either 'ai' or 't'
matches = patt.finditer(mystr)
for match in matches:
    print(match) 
#special characters
patt= re.compile(r"\ATata")     # string begins with "tata"
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt= re.compile(r"\bmap")     # string begins or ends with given word
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt= re.compile(r"27\b")     # there is an ending with 27
matches = patt.finditer(mystr)
for match in matches:
    print(match) 

patt= re.compile(r"\d{5}-\d{4}")     # \d= digits \d{5}-\d{4} means 5 digits-4digits
matches = patt.finditer(mystr)
for match in matches:
    print(match) 
