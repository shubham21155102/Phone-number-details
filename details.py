import phonenumbers
from phonenumbers import timezone,geocoder,carrier

phoneNum=phonenumbers.parse("+91 6201060889")

timeZone=timezone.time_zones_for_number(phoneNum)

carrieR=carrier.name_for_number(phoneNum,'en')

Region=geocoder.description_for_number(phoneNum,'en')

print(phoneNum)
print(timeZone)
print(carrieR)
print(Region)