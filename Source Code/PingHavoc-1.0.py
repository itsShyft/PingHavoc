import pyautogui
import colorama
import os
from time import sleep
from builtins import int
colorama.init()

version = None
message = None
amount = None
pingEveryone = None
getSettingsFailed = None
messageCount = 0
version = '1.0'

print(colorama.Fore.RED, 'DISCLAIMER: I AM NOT RESPONSIBLE FOR ANY PUNISHMENT YOU RECIEVE FOR SPAMMING!' ,colorama.Fore.RESET)
print('Thanks for downloading PingHavoc!')
print('You are running version ' + version)

print(' ')
message = input('What message would you like to spam? Do not include @everyone, that will be covered in a later step. ')
amount = int(input('How many times would you like the message to be sent? This must be a positive number without decimals. '))
pingEveryone = input('Would you like an @everyone ping to be included in the message? YOU MUST ANSWER yes OR no (Case Sensetive) ')

os.system('cls')
print('Spamming will begin in 10 SECONDS.')
print('YOU MUST CLICK INTO THE MESSAGE BOX ON DISCORD AS IF YOU WERE ABOUT TO TYPE SOMETHING!')
print('If nothing happens after 10 seconds, check the program again for error messages.')
sleep(10)
if pingEveryone == 'no':
    print(' ')
    for int in range(amount):
        if messageCount == 10:
            print(' ')
            print('Bypassing Discord anti-spam filter. This may take 8-10 seconds.')
            print(' ')
            sleep(8)
            messageCount = 0
        pyautogui.write(message)
        pyautogui.press('enter')
        messageCount = messageCount + 1
        print('Message Sent')
elif pingEveryone == 'yes':
    print(' ')
    for int in range(amount):
        if messageCount == 10:
            print(' ')
            print('Bypassing Discord anti-spam filter. This may take 8-10 seconds.')
            print(' ')
            sleep(8)
            messageCount = 0
        pyautogui.write('@everyone ' + message)
        pyautogui.press('enter')
        messageCount = messageCount + 1
        print('Message Sent')
else:
    print(colorama.Fore.RED, 'ERROR: You must enter either yes or no for whether you want to ping everyone. PLEASE RESTART THE PROGRAM.', colorama.Fore.RESET)
    sleep(999)

print(colorama.Fore.GREEN, 'Spamming Successful! Thanks for using PingHavoc!', colorama.Fore.RESET)
sleep(999)