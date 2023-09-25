from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def caeser(input_text, shift_no, direction):

	ans = ""

	for letter in input_text:
		if (letter == " "):
			ans += letter
			continue

		position_of_letter = alphabet.index(letter)

		temp_shift_no = shift_no

		if (direction == "decode"):
			if (position_of_letter - temp_shift_no < 0):
				temp_shift_no = abs(shift_no) % 25
				shift_position = 25 - temp_shift_no 
			else: 
				shift_position = position_of_letter - temp_shift_no

		if (direction == "encode"):
			# if (temp_shift_no > 25):
			temp_shift_no = shift_no % 25
			print(f"shift by: {temp_shift_no}")

			shift_position = position_of_letter + temp_shift_no

		# print(shift_position)
		ans += alphabet[shift_position]

	print(ans)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# encrypt(text, shift)

while (True):
	
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

	text = input("Type your message:\n").lower()

	shift = int(input("Type the shift number:\n"))

	caeser(text, shift, direction)		

	again = input("Would you like to go again? (y / n)")

	if (again == "n"):
		break
		


