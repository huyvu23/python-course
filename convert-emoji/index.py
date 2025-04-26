message = input(">")
words = message.split(' ')
emoji = {
    ":)" : "😊",
    ":(" : "😔",
    ":D" : "😊"
}
for word in words:
    if word in emoji:
        message = message.replace(word, emoji[word])
print(message)
# Output: Hello 😊, how are you? 😊