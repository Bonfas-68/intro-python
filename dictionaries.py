customer = {
    "name": "John Smith",
    "age":30,
    "is_verified": True
}
customer['age'] = 32
customer['name'] = "bonfas"
print(customer["name"], customer['age'])
print(customer.get("name"))


##########################
##Challenge one on dictionary to translate 1 to one
"""phone = input("Phone: ")
numbers = {
   "1": "one" ,
   "2": "two" ,
   "3":"three"
}
output = ""
for ch in phone:
    output += phone.get(ch, "!") + " "
print(output)"""

# Emoji converter
message = input('>')
words = message.split(' ')
emojis =  {
    ":)":"😀",
    ":(":"😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + ""
print(output)