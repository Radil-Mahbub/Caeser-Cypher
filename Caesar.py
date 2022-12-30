class CaesarCipher:
    alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, message, rule):
        self.message = message
        self.rule = rule


    def userInputs(self):
        self.message = str(input("Enter the message you would like to use: ")).lower()
        self.rule = int(input("Enter your encryption key = "))


    def encode(self):
        newMessage = []

        for i in range(0, len(self.message)):
            if self.message[i] == ' ':
                newMessage.append(' ')

            else:
                for j in range(0, len(self.alphabet)):
                    if self.message[i] == self.alphabet[j]:
                        encryptedIndex = (j - self.rule) % 26
                        newMessage.append(self.alphabet[encryptedIndex])

        for i in range(0, len(newMessage)):
            print(newMessage[i], end= '')


cipher1 = CaesarCipher('DEFAULT', 0)
cipher1.userInputs()
cipher1.encode()