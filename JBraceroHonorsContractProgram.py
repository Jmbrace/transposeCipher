

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
	flag = input("Enter 'e' to encrypt, or enter 'd' to decrypt").lower()
	if flag == 'e':
		encrypt()
	if flag == 'd':
		decrypt()


def encrypt():
	dist = int(input("Enter the transposition distance: "))
	text = input("Enter the clear text: ")
	cipher = build_cipher(dist)
	cypher_text = ""
	for char in text.lower():
		cypher_text += cipher[char]
	print(cypher_text)

def build_cipher(dist):
	cipher = {" ": " "}
	counter = 0
	for char in alphabet:
		index = getMappedIndex(counter, dist)
		cipher[char] = alphabet[index]
		counter += 1
	return cipher

def getMappedIndex(counter, dist):
	index = counter + dist
	while index > 25:
		index = index - 26
	return index

def getReverseMappedIndex(counter, dist):
	index = counter - dist
	while index < 0:
		index = index + 26
	return index

def build_reverse_cipher(dist):
	cipher = {" ": " "}
	counter = 0
	for char in alphabet:
		index = getReverseMappedIndex(counter, dist)
		cipher[char] = alphabet[index]
		counter += 1
	return cipher

def decrypt():
	dist = int(input("Enter the transposition distance: "))
	text = input("Enter the cypher text: ")
	cipher = build_reverse_cipher(dist)
	clear_text = ""
	for char in text.lower():
		clear_text += cipher[char]
	print(clear_text)


main()