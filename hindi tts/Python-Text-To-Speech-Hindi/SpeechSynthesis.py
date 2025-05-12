from Utilities import tts

if __name__ == "__main__":
	message = input("Enter Message: ")

	# for i in message:
	# 	print(i)

	tts.text_to_speech(message, debug=True, use_pronunciation_dict=True)