#RegEx - Regular Expressions
"""
^  Matches the beginning of a line
$  Matches the end of the line
.  Matches any character
\s Matches whitespace
\S Matches any non-whitespace character

*  Repeats a character zero or more times 
*? Repeats a character zero or more times (non-greedy)
+  Repeats a character one or more times
+? Repeats a character one or more times (non-greedy)

[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character NOT in the listed set
[A-Z0-9] The set of characters can include a range

( Indicates where string extraction is to start
) Indicates where string extraction is to end

#Using re.search() like find
import re

hand = open('ring.txt')
for line in hand:
    line = line.rstrip()
    if re.search('the', line):
        print(line)


#Using re.search() like startswith()

hand = open('ring.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)  
"""
#Matching and Extracting Data
import re
x='My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)        
y = re.findall('[AEIOU]+',x)
print(y)

#Warning Greedy Matching
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)

#Non-greedy Matching
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

#Fine-Tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
atpos = x.find('@')
print(atpos)
sppos = x.find(' ',atpos)
print(sppos)
host = x[atpos+1 : sppos]
print(host)

#ou
words = x.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#Ou ou
y=re.findall('@([^ ]*)',x)
print(y)

#Ou ou ou
y=re.findall('^From .*@([^ ]*)',x)
print(y)
