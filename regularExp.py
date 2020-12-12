#Operations on regular expressions
import re
print('Operations on regular expressions')
str = "we need to inform him with the latest information"


#1. Find a word in a string
print('\nFind a word in a string')
if re.search("inform", str):
      print("there is inform")

      
#2. Find all words in a string
print('\nFind all words in a string')
allinform = re.findall("inform",str)
for i in allinform:
      print(i)

      
#3. generate an iterator
print("\nGenerate an iterator")
for i in re.finditer("inform",str):
       print(i.span())

       
#4. Match words with the particular pattern
print('\nMatch words with the particular pattern')
str1 = "pat mat rat sat"
allstr = re.findall("[smrp]at",str1)
for i in allstr:
      print(i)

      
#5. Match series of range of characters
print('\nMatch series of range of characters')
Somestr = re.findall("[m-p]at",str1)
print("[m-p]")
for i in Somestr:
      print(i)

      
#6. carriage symbol return
Somestr1 = re.findall("[^j-q]at",str1)
print("\ncarriage symbol")
for i in Somestr1:
      print(i)

      
#7. Replace a particular string
print("\nReplace a particular string ")
fruits = "pat mat rat sat"
print(fruits)
regex = re.compile("[r]at")
fruits = regex.sub("pair",fruits)
print(fruits)


#8. Solving the backslash problems
print("\nSolving the backslash problems")
randstr = "here is \\drogba"
print(randstr)
print(re.search(r"\\drogba",randstr))

#9. Match a single character
print('\nMatch a single character')
randstr1 = '''keep
the
blue flag
flying high
Chelsea
'''
print(randstr1)
regex = re.compile("\n")
randstr1 = regex.sub("_",randstr1)
print(randstr1)

#Other whitespaces
##\b: backspace
##\f: formfeed
##\r: carriage return
##\t: tab
##\v: vertical tab

randstr2 = "12345"
print("Matches:",len(re.findall("\d",randstr2)))
print("Matches:",len(re.findall("\d{4}",randstr2)))
nums= " 123 1234 12345 123456 1234567"
print("Matches:",re.findall("\d{1,4}",nums))

#applications of reg exp
##\w -> [a-zA-Z0-9_]
##\W -> [^a-zA-Z0-9]
##\s -> [\f\n\r\t\v]
##\S -> [^\f\n\r\t\v]
#10. phone number validation
phn = "412-121-3233"
if re.search("\w{3}-\w{3}-\w{3}",phn):
      print("Valid phone number")

#11. Full name valid
print("Full name valid")
if re.search('\w{2,20}\s\w{2,20}',"Aafaq rashid"):
      print("valid fullname")
