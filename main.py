import string #imports string module

def caesar(text, shift, alphabets): #defining a function for a caesar cipher
  def shift_alphabet(alphabet):
    return alphabet[shift:] + alphabet[:shift] #shifts the alphabet by the shift number
  shifted_alphabets = tuple(map(shift_alphabet, alphabets)) #creates a tuple of shifted alphabets by applying the shift_alphabet function to each element in the alphabets list
  final_alphabet = ''.join(alphabets)
  final_shifted_alphabet = ''.join(shifted_alphabets) #lines 7 and 8 joins the alphabets and shifted_alphabets tuples into two final strings
  table = str.maketrans(final_alphabet, final_shifted_alphabet) #creates a translation table that maps each character in final_alphabet to its shifted character in final_shifted_alphabet
  return text.translate(table)
print('Enter any message:') #asking the user for their message
text = input()

print('Enter a number to shift it by:') #asking for a shift numbere
shift = int(input()) #turns the input into an integer
shift %= 26 #converts the input into a shift value within the range of 0-25

encrypted_text = caesar(text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]) #using the caesar function

print('Encrypted Text:', encrypted_text) #printing the encrypted text
print()

text = encrypted_text #sets the new text variable to the encrypted_text
shift = 26 - shift #calculates the shift value needed to decrypt the text

decrypted_text = caesar(text, shift, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]) #using the caesar function

print('Decrypted Text:', decrypted_text) #printing the decrypted text
print()