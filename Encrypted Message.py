# Jesse Wittenborn
# 2/15/2021-2/22/2022
# Encrypted Message

def main():
    message = input("What message would you like to encrypt")
	
    encodedMessage = []
    decodedMessage = ""
    for m in message:
        encodedMessage.append( ord(m))
   
	
    print (" Encoded Message: ")
    print (encodedMessage)
    for e in encodedMessage:
                 decodedMessage = decodedMessage + chr(e)
	 
	
        
	
    print (" Decoded Message: ")
    print (decodedMessage)
	 
	 
    for e in encodedMessage:
	        decodedMessage + chr(e)
main()
