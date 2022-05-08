import requests as req
import json 
import time
data=[]
c=[]
data = req.get("https://api.wazirx.com/api/v2/tickers")
data =data.json()
for i in data.keys() :
    c.append(i)
c.sort()
def recent_message () :#take the messages fro the bot
  data=req.get("https://api.telegram.org/bot5399857746:AAGgH9vTOa25xEYF9LP8tzzsTnRh6qSzsEM/getUpdates")
  data=data.json()
  data=data["result"]
  message=data[-1]["message"]["text"]
  return message

def send_response (msg) :
  data=req.get("https://api.telegram.org/bot5399857746:AAGgH9vTOa25xEYF9LP8tzzsTnRh6qSzsEM/getUpdates")
  data=data.json()
  data=data["result"]
  data=data[-1]["message"]["from"]["id"]
  par={
      "chat_id":data,
       "text":msg
  }
  send=req.get("https://api.telegram.org/bot5399857746:AAGgH9vTOa25xEYF9LP8tzzsTnRh6qSzsEM/sendMessage" , data=par)
def ptr (a) :
    a=a.split("</h2>")
    # print(a)
    a=". ".join(a)
    # print(a)
    a=a.split(". ")
    a="#".join(a)
    a=a.split("&#36;")
    a="$".join(a)
    a=a.split("#")
    return(a)
def coin_forcast (c) :
    d=[]
    c=c.split(" ")
    c="-".join(c).lower()
    url="https://tradingbeasts.com/price-prediction/"+c
    count=0
    data=req.get(url)
    data=str(data.text)
    data=data.split('<h2 class="coin-header">')
    data= data[1:6]
    if data==[] :
      return "No coin found"
    for i in data :
        app=ptr(i)
        d.append(app)
    return d
def send_pred(lit) :
  if lit=="No coin found" :
    send_response(lit)
    return 
  msg=""
  for i in lit :
    for j in i :
      msg=msg+j+"\n"
    send_response(msg)
    msg=""
def ask_coin () :
  send_response("Enter Your Coin Full Name :-")
  msg=check_msg()
  data=coin_forcast(msg)
  send_pred(data)
def check_msg() :
  data=req.get("https://api.telegram.org/bot5399857746:AAGgH9vTOa25xEYF9LP8tzzsTnRh6qSzsEM/getUpdates")
  data=data.json()
  data=data["result"]
  data=data[-1]["message"]["message_id"]
  data1=data
  while data==data1:
    data1=req.get("https://api.telegram.org/bot5399857746:AAGgH9vTOa25xEYF9LP8tzzsTnRh6qSzsEM/getUpdates")
    data1=data1.json()
    data1=data1["result"]
    data1=data1[-1]["message"]["message_id"]
  msg=recent_message()
  return msg
def check_written () :
  data=recent_message()
  data1=data
  while data==data1 :
    data1=recent_message()
  return True
def search_coin (a):
  d=[]
  for i in c :
    if data[i]['base_unit']==a :
        d.append(i)
  send_response("enter your coin currency as shown:-")
  for i in d :
    send_response(i)
  if check_written() :
    if recent_message().lower() in d :
      return recent_message().lower()
    else :
      return "No coin found"
def coin_info(id) :
  id=search_coin(id)
  print(id)
  a=["","","","",""]
  a[0]=('NAME : '+data[id]['name'])
  a[1]=('HIGH : '+data[id]['high'])
  a[2]=('LOW : '+data[id]['low'])
  a[3]=('BUY : '+data[id]['sell'])
  a[4]=('SELL : '+data[id]['buy'])
  show(a)
  return
def show (a) :
  c=""
  for i in a :
    c=c+i+"\n"
  send_response(c)
  return
def ask_dec() :
  send_response("For the information of the coins type 'info'\nFor the prediction type 'pred' ")
  while 1>0:
    if check_written() :
      if recent_message()=="info" :
        send_response("enter your coin 3 digit code:")
        if check_written() :
          coin=recent_message()
          coin_info(coin)
      elif recent_message()=="pred" :
        print("1")
        ask_coin()
      else :
        return
    send_response("same Again 'info' or 'pred' :-")
while 1>0 :
  ask_dec()
  if recent_message()=="/help" :
    send_response("Enter your problem ")