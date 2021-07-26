# imports
import requests
import time

# Set up
from win10toast import ToastNotifier # notifier
toaster = ToastNotifier()
URL = "https://www.newworld.com/es-es/support/server-status"
SERVER = "Machina"
changed = False # first time call
print("We will notify you when there is a change in your world, to finish press CTRL + C")

# Start of ouroboro
while True :
  
 r = requests.get(url = URL) # call the page
 
 txt = r.content.decode('utf-8') # server response as string
 indice = txt.find(SERVER) # search the server in the response
 status_substr = txt[indice-200:indice].find("up") # if find up index then is server up, down also can be used
 up = status_substr > 0 # -1 if changed
 if up != changed: # status changed after last change
  notif =  "Status Changed:" + SERVER +" "+ str(up) 
  toaster.show_toast("NEW WORLD SERVER", notif)
  changed = up
  print("Notification sended",changed)
 time.sleep( 5 ) # check every 5 secs