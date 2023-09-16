'''
Omegle Chat Bot by n0nexist.github.io
github download: github.com/n0nexist/omegleChatBot
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import utils

utils.log('Started omegleChatBot by n0nexist')
message = utils.getmsg() # get the message from message.txt
msglines = len(message.split('\n'))
utils.log(f'Read {msglines} lines from message.txt')
utils.log('Starting chrome driver...','progress')

browser = webdriver.Chrome()

utils.log('Starting chatbot...','progress')

browser.get('https://omegle.com')

utils.delay()

chatButton = browser.find_element(By.ID, "chattypetextcell") # Click the Text Chat button
chatButton.click()

utils.delay()

checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"][style*="font-size: 1.5em; width: 1em; height: 1em; float: left; margin-right: 0.5em;"]')
for checkbox in checkboxes: # Click all checkboxes to accept terms of service
    checkbox.click()

utils.log('Accepting terms of service','progress')

acceptAndContinue = browser.find_element(By.CSS_SELECTOR, 'input[type="button"][style*="font-size: 1.5em; pointer-events: auto;"]')

utils.log('Everything is ready to start. press enter to continue.')
input()

utils.log('Starting to generate the chats...','progress')
acceptAndContinue.click() # Click the button that accepts the terms of service and starts generating chats

utils.log('Chatbot started!','success')

msgcounter = 0

def detect_captcha():
    try: # Is there a captcha on the page?
        checkbox_element = browser.find_element(By.CLASS_NAME,'recaptcha-checkbox-border')
        utils.log('The chatbot got blocked by a captcha. solve it and then press enter.','warning')
        input()
    except:
        pass

while True:
    utils.delay(1) # Wait for the whole page to load

    detect_captcha()        

    try: # Try to type on the textarea
        textarea = browser.find_element(By.CSS_SELECTOR, '.chatmsg')
        textarea.send_keys(message)
        textarea.send_keys(Keys.ENTER)
        utils.delay()
        msgcounter+=1
        utils.log(f'Sent {msgcounter} messages in total')
    except: # If the user skipped us before we could type, then it was probably another chatbot
        utils.log('Message wasn\'t sent, we probably encountered another chatbot','warning')

    utils.log(f'Skipping to next person...')
    utils.skipChat(webdriver,browser,Keys) # Press 'esc' 3 times to skip to another chat

while True:
    pass # Keep the program open