#Twilio registration details

#Give your info here or comment below details till  " Passwd = input('Enter the Password') "  and directly get the details from your webpage or excel sheet

FirstName = input('Enter the FirstName :')
LastName = input('Enter the LastName :')
EmailAddr = input('Enter the EmailAddress :')
Passwd = input('Enter the Password it should 14 + Characters :')
print('Please Wait...')
browser = webdriver.Chrome(executable_path='C:/chromedriver.exe')

def twlo():

    
     
     browser.get("https://www.twilio.com/")
     time.sleep(30)
     doc = browser.find_elements_by_xpath('/html/body/nav/div/ul[2]/li[2]/a')[0]
     doc.click()
     time.sleep(8)
     doc1 = browser.find_elements_by_xpath('//*[@id="FirstName"]')[0]
     doc1.click()
     time.sleep(2)
     doc1.send_keys(FirstName)
     time.sleep(2)
     doc2 = browser.find_elements_by_xpath('//*[@id="LastName"]')[0]
     doc2.click()
     time.sleep(2)
     doc2.send_keys(LastName)
     time.sleep(2)
     doc3 = browser.find_elements_by_xpath('//*[@id="EmailAddr"]')[0]
     doc3.click()
     time.sleep(2)
     doc3.send_keys(EmailAddr)
     time.sleep(2)
     doc4 = browser.find_elements_by_xpath('//*[@id="Passwd"]')[0]
     doc4.click()
     time.sleep(2)
     doc4.send_keys(Passwd)
     time.sleep(2)
     doc5 = browser.find_elements_by_xpath('//*[@id="Tos"]')[0]
     doc5.click()
     time.sleep(2)
     doc6 = browser.find_elements_by_xpath('//*[@id="signup-button"]')[0]
     doc6.click()
     time.sleep(2)
     print('Check your Email id for twilio verification link ')
     print('If it is done come to www.twilio.com and click login ')
     print('Enter your registered twilio account Email ID and Password ')
     print('Now go to your Dashboard and get a number for you account also your ACCOUNT SID and AUTH TOKEN ')

try:

     twlo()

except:

     print('Low Internet connection')
     print('Reconnecting and running the code again')
     twlo()
