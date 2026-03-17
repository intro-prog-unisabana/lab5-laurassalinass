from utils import flip
from utils import count_letters
print("Please type your message")
mensaje= input ("")
numero= count_letters(mensaje,"a")
cambio= flip(mensaje)+ str(numero)
print("Your enconded message is:", cambio)