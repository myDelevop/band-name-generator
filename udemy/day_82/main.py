from morse_code import MorseCode

sentence = input("Please insert the sentence you want to convert in Morse Code")

mc = MorseCode()

print(mc.encode_sentence(sentence))
