# 3. Explore different data types available in Python and demonstrate use of them
# Demonstrate use of the following Python data types
# - List
# - Dictionary
# - Set
# - Tuple
# Define each of the data types in Python and demonstrate a meaningful use of them.

######################### List #########################################

# List of programming languages
ProgLang = ["C", "Java", "Python", "C++", "C#",
            "JavaScript", "PHP", "VB.NET", "R", "SQL", "Go", "Perl"]

# Accessing elements of a list
print(ProgLang[3])  # Output: "C++"

# Modifying elements of a list
ProgLang[1] = "Visual FoxPro"
print(ProgLang)  # Output: ["C", "Visual FoxPro", "Python" ....]

# Adding an element to the end of the list
ProgLang.append("Smalltalk")
print(ProgLang)  # Output: [....'Go', 'Perl', 'Smalltalk']

# sort list
SortProgLang = sorted(ProgLang)
print(SortProgLang)  # Output:  ['C', 'C#', 'C++', 'Go' ....]

# print list len
print(len(SortProgLang))  # Output: 13

# show last item and second last item
print(ProgLang[-1], ProgLang[-2])  # Output:  Smalltalk Perl

# Remove last item From a List
del ProgLang[-1]
# Output: ['C', 'Visual FoxPro', 'Python', 'C++', 'C#', 'JavaScript', 'PHP', 'VB.NET', 'R', 'SQL', 'Go', 'Perl']
print(ProgLang)

######################### Dictionary #########################################

# Creating a dictionary
ProgLangD = {
    "Autocode": 1952,
    "Fortran": 1957,
    "BASIC": 1964,
    "PASCAL": 1970,
    "Perl": 1987,
    "Python": 1991,
    "Go": 2009,
    "Swift": 2014
}

# Accessing values using keys
print(ProgLangD["PASCAL"])  # Output: 1970

# Modifying a value
ProgLangD["Go"] = 2010
print(ProgLangD)  # Output: {.... 'Go': 2010, 'Swift': 2014}

# Adding a new key-value pair
ProgLangD["C#"] = 2000
# Output: {'Autocode': 1952, 'Fortran': 1957, 'BASIC': 1964, 'PASCAL': 1970, 'Perl': 1987, 'Python': 1991, 'Go': 2010, 'Swift': 2014, 'C#': 2000}
print(ProgLangD)

######################### set #########################################
# Creating a set
TypeSet = {"Decimal", "Binary", "Octal", "Hexadecimal", "Floating-point Literal", "Complex Literal"}

# print set 
print(TypeSet) # Output: {'Decimal', 'Floating-point Literal', 'Octal', 'Binary', 'Hexadecimal', 'Complex Literal'}

#Update a set
TypeSet.update(("NewType1","NewType2"))
print(TypeSet) # Output: {'Floating-point Literal', 'Decimal', 'NewType1', 'Complex Literal', 'Octal', 'NewType2', 'Binary', 'Hexadecimal'}

#Remove element
TypeSet.remove("NewType1")
print(TypeSet) # Output: {'Floating-point Literal', 'Decimal', 'Complex Literal', 'Octal', 'NewType2', 'Binary', 'Hexadecimal'}

#Remove all element
TypeSet.clear()
print(TypeSet) # Output: set()

#set union
TypeSet1 = {"Decimal", "Binary", "Octal", "Hexadecimal", "Floating-point Literal", "Complex Literal"}
TypeSet2 = {0,1,2,3,4,5,6,7,8,9}
print(TypeSet1|TypeSet2) # Output: {0, 1, 2, 3, 4, 5, 6, 'Hexadecimal', 7, 8, 9, 'Decimal', 'Floating-point Literal', 'Complex Literal', 'Binary', 'Octal'}

#set  Intersection
TypeSet3 = {0,1,2}
print(TypeSet2&TypeSet3) # Output: {0, 1, 2}

#set  Difference
print(TypeSet2-TypeSet3) # Output: {3, 4, 5, 6, 7, 8, 9}


######################### Tuple #########################################

TypeTuple = ("Decimal", "Binary", "Octal", "Hexadecimal", "Floating-point Literal", "Complex Literal")
print(TypeTuple)# Output: ('Decimal', 'Binary', 'Octal', 'Hexadecimal', 'Floating-point Literal', 'Complex Literal')

# print last element
print(TypeTuple[-1])# Output:Complex Literal

# Tuple allow duplicates
TypeTuple = ("Decimal", "Binary", "Octal", "Hexadecimal", "Floating-point Literal", "Complex Literal","Decimal")
print(TypeTuple) # Output:('Decimal', 'Binary', 'Octal', 'Hexadecimal', 'Floating-point Literal', 'Complex Literal', 'Decimal')