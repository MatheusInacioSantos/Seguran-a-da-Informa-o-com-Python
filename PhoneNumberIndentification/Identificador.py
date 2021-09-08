import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato: +5516993759329: ') # Telefone do google +16502230000 - California

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))