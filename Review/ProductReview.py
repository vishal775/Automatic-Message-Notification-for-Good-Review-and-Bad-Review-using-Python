#comments are for your references
#Before running this code go to www.twilio.com and create a account with your PHONE NUMBER and get a TRIAL NUMBER (from other countries to message) for your account by your choice.
#We have already created an account for twilio in the name of 'Surya123 S'
#account details will be sent through whatsapp as screenshot
#kindly get the important (name, last name and email id in your webpage itself inorder to register for twilio account)

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from twilio.rest import Client
import pickle
from textblob import TextBlob
from better_profanity import profanity

count=0

#Web scrapping for using ID
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Choose the webpage and copy the webpage URL and paste it in site = "webpage URL" given below

site = "https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/dp/B085J1CPD1/ref=sr_1_1?dchild=1&keywords=OnePlus+8T+5G+%28Lunar+Silver+12GB+RAM%2C+256GB+Storage%29&qid=1606552466&sr=8-1"

# Download Chrome Driver by checking the version of the chrome you are using 
# After Download extract in Local Disc C if possible or any other Local Disc.
# Now get the whole PATH of chromediver.exe in extracted directory and paste it in "User-Agent": "YOUR CHROMEDRIVER.EXE PATH"

headers = {
     "User-Agent": "C:/chromedriver.exe"
}

response=requests.get(site,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')

def Review():

     #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     #To get review from webscrapping in a webpage leave it as it is
     #Use your ID in place of (id="productTitle") given below
     censored=soup.find(id="productTitle").get_text()
     #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     #To get review from user enable 'censored' below and disable above webscrapping 'censored'
     #censored=input("Enter the Review :")
     text = profanity.censor(censored) #checks any abuse or faulty  words are been used in the given review sentence
     #print(text) #Review sentence for reference
     if '*' in text:
          return 'The text is Negative'

     else:
          obj=TextBlob(text)
          sentiment = obj.sentiment.polarity
          #print(sentiment) to get the sentiment value in integers
          if sentiment < 0:
               return 'The text is Negative'
          elif sentiment == 0:
               return 'The text is Neutral'
          elif sentiment > 0 and sentiment <= 1:
               return 'The text is Positive'
          
     return censored

def msg(messcont): #Twilio account details '+16143899653' this is the number given to you from twilio

     num='+91'+'YOUR_PHONE_NUMBER'
     client = Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")
     client.messages.create(from_='YOUR_TRIAL_NUMBER',
                           to=num,
                           body='!! IMPORTANT !!: '+messcont)
     
for i in range(0,3):

     login='login successfull' #get your user login credintials from your webpage and return only login successfull 

     if login=='login successfull':

          try:
               check = Review() #Returns the sentiment of text

               if check == 'The text is Neutral' or check == 'The text is Positive':
                    Gen='\nYour Review is Genuine'
                    print(Gen)
                    try:
                         msg(Gen) #Message sent to your twilio registered number !! you can have this if you need else comment it !!
                         print('Message sent ')
                    except:
                         exec(open("F:/Review/Twiliocheck.py").read()) # give the file location where Twiliocheck.py located
                    break

               elif check == 'The text is Negative':
                    count+=1
                    print('Fake Review')
                    if count == 1:
                         Send='Your account has only 2 chances left due to FAKE REVIEW'
                         print(Send)
                         try:
                              msg(Send) #Message sent to your twilio registered number
                              print('Message sent ')
                         except:
                              exec(open("F:/Review/Twiliocheck.py").read()) # give the file location where Twiliocheck.py located
                    elif count ==  2:
                         Send='Your account has only 1 chances left due to FAKE REVIEW'
                         print(Send)
                         try:
                              msg(Send) #Message sent to your twilio registered number
                              print('Message sent ')
                         except:
                              exec(open("F:/Review/Twiliocheck.py").read()) # give the file location where Twiliocheck.py located
                    else:
                          Send='Your account is  blocked due to FAKE REVIEW'
                          print(Send)
                          try:
                               msg(Send) #Message sent to your twilio registered number
                               print('Message sent ')
                          except:
                              exec(open("F:/Review/Twiliocheck.py").read()) # give the file location where Twiliocheck.py located

               else:
                    print('!!Error From Code!!') #first check the ID is given properly for webscrapping

          except:
               print('!!Error From Code!!') #first check the ID is given properly for webscrapping

     else:
          print('!! Account not available !!') #No account availabe login failure
