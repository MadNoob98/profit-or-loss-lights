### Control LED lights based on Profit/Loss on Binance Account


### Set Variables

balance = 
updated_balance = 
profit_loss = 


### Import all the stuff you need
from blinkstick import blinkstick

from binance.client import Client
client = Client(api_key, api_secret)



### Import binance balance





### Calculate if it has gone up or down

if updated_balance == balance
	print "Balance same, skipping"
elif  
 updated_balance > balance
   profit_loss = "P"
   updated_balance = balance	
elif
  updated_balance < balance
    profit_loss = "L"
	updated_balance = balance
	
	
### Change colour of lights based on P/L

if profit_loss == "P"
	led = blinkstick.find_first():
    led.set_color(name="green")
else 
	led = blinkstick.find_first():
    led.set_color(name="red")
	