# Write a program to replace 'yt' in 'Python' with the string entered by the user.
# Create a string named language with the value "Python".
# Take string as an input for ch variable.
# Use the replace() method to replace "yt" with user-entered string stored in ch.
# Print the new string.
language = input("Enter the language:")
ch = input("Enter a remove key:")
lang = language.replace("yt", ch)
print(lang)
