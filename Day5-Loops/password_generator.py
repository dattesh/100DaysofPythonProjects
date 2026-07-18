import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]
special_characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|",
    ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?",
    "`", "~"
]

password_length=int(input("how many length of password you want to generate?\t "))
alphabets =int(input("how many alphabets you want to add\t"))
num = int(input("How many numbers you want to add \t"))
special_char = int(input("How many special charcters \t"))

password_list=[]
for char in range(0,alphabets+1):
    password_list += random.choice(alphabet)

for char in range(0,special_char+1):
    password_list += random.choice(special_characters)
for char in range(0,num+1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password= ''
for char in password_list :
    password +=char

print(password)
#print(random.shuffle(password))