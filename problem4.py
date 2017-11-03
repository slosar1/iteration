sentence = input("Please write a sentence:")
print(sentence)

message  = []
for letter in sentence:
	if(letter == " "):
		print(message)
