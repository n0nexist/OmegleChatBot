from datetime import datetime as dt 
import time

def delay(timeout=0.3):
    ''' Sleeps for a default of 0.3 seconds '''
    time.sleep(timeout)

def getmsg():
    ''' Gets the message body from the file message.txt '''
    try:
        f = open('message.txt','r')
        content = f.read()
        f.close()
        return content
    except Exception as e:
        utils.log('Error reading file message.txt','error')
        exit(1)

def skipChat(webdriver,driver,keys):
    ''' Sends 3 times the 'esc' button to the page, used to skip to the next chat '''
    for x in range(3):
        webdriver.ActionChains(driver).send_keys(keys.ESCAPE).perform()

def getTimestamp():
    ''' Gets the current timestamp in a conveniently readable format '''
    d = dt.now()
    return f'{d.day}/{d.month}/{d.year} {d.hour}:{d.minute}:{d.second}'

def log(text,lvl='info'):
    ''' Logs informations, warnings and errors '''
    print(f'{getTimestamp()}: [{lvl.upper()}] {text}')