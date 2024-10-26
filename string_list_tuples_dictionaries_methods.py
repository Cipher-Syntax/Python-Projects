print("==================================================================")
print("                         [STRING METHODS]                         ")
print("==================================================================")

# User is prompted to enter a sentence
sentence = input("Enter a Sentence: ")

    # This is function that will force the user to enter a word or sentence
    #       if the user did not enter a sentence this function will continue
    #       for infinite amount of times.
while sentence == "":
    print("Please enter a word or sentence...")
    sentence = input("Enter a Sentence: ")
    
# Converting Sentence into Uppercase or Lowercase
    # The method upper() and lower() to uppercase and lowercase using
    #       the variable sentence followed by dot (.) then the method.
    #       sentence.upper()        or          sentence.lower()
uppercase = sentence.upper()
lowercase = sentence.lower()
print(f"\nUppercase: {uppercase}")  # Displays the result
print(f"Lowercase: {lowercase}")    # Displays the result
print("==================================================================")
   
# Replacing a word in the sentnce with another word
    # The user will be asked to input the sentence the want to replace
word = input("Enter a word to replace in the sentence: ")
word_to_replace = input(f"Enter a word to replace with '{word}': ")
    # The user then will be asked to input what they want the word/sentence to
    #   be replaced with.
replaced_sentence = sentence.replace(word, word_to_replace)
    # dislays the updated sentence or word
    
    # This will print the result of the relaced sentence.
    # If word is not found in the sentence it will display word not found in the sentence
if word in sentence:
    print(f"\nReplaced Sentence: {replaced_sentence}")
    print("==================================================================")
else:
    print(f"\nWord '{word}' not found in the sentence")
    print("==================================================================")
    
# Finding the first occurence of a specific word or character
    # The user inputs a word or character, and the method find() will find the first occurence
    #       using the replaced_sentence.find(find_word)
find_word = input("Enter a word or character to find the First Occurence: ")
first_ocurence = replaced_sentence.find(find_word)
    # The index of the first occurence is printed or a message will appear if the
    #       word is not found
if first_ocurence != -1:
    print(f"The first occurence of '{find_word}' is at index: {first_ocurence}")
    print("==================================================================")
else:
    print(f"'{find_word}' is not found in the sentence")
    print("==================================================================")


print("==================================================================")
print("                         [LIST METHODS]                           ")
print("==================================================================")

# The user inputs a list of items separated by commas
print("Enter several items separated by comma(e.g.,shopping list, movies, etc.)\n")
    
items = input("Enter the items: ")
items = [item.strip() for item in items.split(',')]
# Append New Items
    # The user is prompted to enter a new item to add in the list
    #       using the method append().
    #       variable then the method append() followed by dot(.)
    #       items.append(new_item)
new_item = input("Enter new item to add: ")
items.append(new_item)
print(f"\nList after Appending new item: {items}" ) # Print the results
print("==================================================================")

# Remove Items
    # The user will be asked of the specified item they want to remove
    #       using the method remove() 
    #       variable then the method append() followed by dot(.)
    #       items.remove(remove_item)
remove_item = input("Enter the item to remove from the list: ")
if remove_item in items:
    items.remove(remove_item)
    print(f"\nList after Removing item: {items}") # Display the result
    print("==================================================================")
else:
    print(f"'{remove_item}' is not in the list") # Display this result if word is not found
    print("==================================================================")

# Sort the list in alphabetical or reverse order
    # Sort the items in alphabetical and reverse order using the method sort()
    #       then displays the result
items.sort()
print(f"List in alphabetical order: {items}")

items.sort(reverse = True)
print(f"List in reverse order: {items}")
print("================================================================")


print("==================================================================")
print("                         [TUPLE METHODS]                          ")
print("==================================================================")

#   The coordinates will be diplayed
coordinates = (1, 4, 2, 5, 3)
print(f"Tuple of coordinates: {coordinates}")

    # The user is asked to enter an index between 0 - 4 to access and element in the tuple
index = int(input("Enter an index to access elements in the tuple (0 - 4): "))
print(f"\nElement at index {index} is: {coordinates[index]}")
print("==================================================================")

# Slice the tuple to obtain portion of it
    # The user provides a starting and ending index to slice the tuple
    #       then print the results using, coordinates[starting_index:ending_index]
starting_index = int(input("Enter starting index for the slicing (0 - 4): "))
ending_index = int(input("Enter ending index for the slicing (0 - 4): "))

print(f"\nSliced tuple from index {starting_index} to {ending_index} is: {coordinates[starting_index:ending_index]}")

print("==================================================================")


print("==================================================================")
print("                     [DICTIONARY METHODS]                         ")
print("==================================================================")

# The initial student grades will be printed
print("==================================================================")
student_grades = {"Ah-lannour": 1.0, "Albriane": 1.25, "Francis": 1.50}
print(f"Dictionary of Student Grades: {student_grades}")
print("==================================================================")

# Add new key-value pair
    # The user inputs a new student and grade
new_student = input("Enter the name of the new student you want to add: ")
new_grade = float(input("Enter the grade of the new student: "))

student_grades[new_student] = new_grade

print(f"\nDictionary after adding new student: {student_grades}") # Prints the result along with the new student
print("==================================================================")

# Update existing key-value pair
    # The user selects the student whose grade they want to update
update_student = input("Enter name of the student you want to update: ")

    # if the student the user selects exist in the dictionary, their grade is updated
    #       if not the message student not found in the dictionary will be printed
if update_student in student_grades:
    update_grade = float(input("Enter the new grade for the student: "))
    student_grades[update_student] = update_grade
    print(f"\nDictionary after updating {update_student}: {student_grades}")
    print("==================================================================")
else:
    print(f"\nStudent '{update_student}' not found in the dictionary.")
    print("==================================================================")

# Remove a key-value pair from the dictionary
    # The user specifies a student to removed from the dictionary
remove_student = input("Enter name of the student you want to remove: ")

    # if the student the user selects exist in the dictionary, their grade is deleted
        #       using the method del()
        #       if not the message student not found in the dictionary will be printed
if remove_student in student_grades:
    del student_grades[remove_student]
    print(f"\nDictionary after deleting {update_student}: {student_grades}")
    print("==================================================================")
else:
    print(f"\nStudent '{remove_student}' not found in the dictionary.")
    print("==================================================================")

# Retrieve and print the value asscociated with specific key
    # The user inputs a studentt name to retrieve their grade
find_student = input("Enter name of the student whose grade you want to find: ")

    # if the student the user selects exist in the dictionary, their grade is retrieved
    #       if not the message student not founnd in the dictionary will be printed
if find_student in student_grades:
    print(f"\nThe grade of {find_student}: {student_grades[find_student]}")
    print("==================================================================")
else:
    print(f"\nStudent '{find_student}' not found in the dictionary.")
    print("==================================================================")
    
print("==================================================================")