import time
import pywhatkit #libreria per sendwhatmsg
import datetime




class Notifica():
    def __init__(self):
        super(Notifica, self).__init__()


    def invia_messaggio(self, messaggio):

        self.id_gruppo = 'LS72HItDQxE09q7Qb49wZ2'
        now = datetime.datetime.now()

        try:

            # parametri: id gruppo, messaggio, ora minuto
            # invia messaggio su whatsapp web
            pywhatkit.sendwhatmsg_to_group(self.id_gruppo, 'Quote Giornaliere:\n' + messaggio, now.hour, (now.minute + 2))
            print("invio riuscito!")
            #time.sleep(20)
            #os.system("taskkill /im brave.exe /f") #arresta un programma in base al nome. Es: per chrome: os.system("taskkill /im chrome.exe /f")

        except:
            print(("invio non riuscito!"))




            '''phone_num (required) - Phone number of target with country code
message (required) - Message that you want to sendwhatmsg
time_hour (required) - Hours at which you want to send message in 24 hour format
time_min (required) - Minutes at which you want to send message
wait_time (optional, val = 20) - Seconds after which the message will be sent after opening the web
print_wait_time (optional, val = True) - Will print the remaining time if set to true
tab_close (optional, val = False) - True if you want to close the tab after sending the message'''