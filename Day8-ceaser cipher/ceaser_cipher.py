alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]



#
# def encrypt(original_text,shift_amount):
#     cipher_text =""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)+shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text+=alphabet[shifted_position]
#
#     print(f"here is a result {cipher_text}")
#
# # encrypt(original_text=text,shift_amount=shift)
#
# def decrypt(original_text,shift_amount):
#     output_text =""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)-shift_amount
#         shifted_position %= len(alphabet)
#         output_text+=alphabet[shifted_position]
#
#     print(f"here is a result {output_text}")
#
# #decrypt(original_text=text,shift_amount=shift)

def ceaser(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text +=letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"here is a {encode_or_decode}d result {output_text}")

should_continue =True
while should_continue:
    direction=input('Type "encode" to encode. Type "decode to decrypt"').lower()
    text = input("Type your message").lower()
    shift=int(input("type the shift number\t"))

    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart=input('type "yes" if you want to do again or type "no"').lower()
    if restart == 'no':
        should_continue=False
        print("Good Bye")
