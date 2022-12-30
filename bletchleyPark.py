import enchant

#reference list to decrypt the message
alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

encryptedString = str(input("enter the message you would like to decrypt: "))

results = [] #list to store the decryption key, the resulting message, and its score

def decode(message, rule):
    newMessage = ""

    for i in range(0, len(message)):

        for j in range(0, len(alphabet)):

            if message[i] == alphabet[j]:
                 encryptedIndex = (j + rule) % 26 #decryption formula
                 newMessage = newMessage + alphabet[encryptedIndex] #add the decrypted word to the newMessage string
    return newMessage


for i in range(0, 25):
    score = 0
    finalMessage = ""

    stringSeperate = list(encryptedString.split(' '))#seperates the message based on words

    for j in range(0, len(stringSeperate)):
        decodedMessage = decode(stringSeperate[j], i) # 3 -> qeb -> the

        d = enchant.Dict("en_US") #checks if the resulting word is real
        isWord = d.check(decodedMessage)
        if isWord == True:
            score += 1

        finalMessage = f"{finalMessage} {decodedMessage}"

    tmpList = [i, finalMessage, score]
    results.append(tmpList)

#sorts the list by score
'''results = sorted\
(
results,
key=lambda t: t[2],
reverse=True
)'''

print(results)