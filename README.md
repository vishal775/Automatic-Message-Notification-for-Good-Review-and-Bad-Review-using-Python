# Automatic-Message-Notification-for-Good-Review-and-Bad-Review-using-Python
Send message to the reviewer whether review is good, if not send alert notification that your account is going to be blocked if done again

!!!  IMPORTANT NOTES  !!!


	1) To message to other phone numbers Before running this code go to www.twilio.com and create a account with your PHONE NUMBER and get a TRIAL NUMBER (from other countries to message) for your account by your choice.
	2) Account details will be sent through zip file
	3) kindly get the important (name, last name and email id in your webpage itself inorder to register for twilio account)
	4) Download Chrome Driver by checking the version of the chrome you are using 
	5) After Download extract in Local Disc C if possible or any other Local Disc.
	6) Now get the whole PATH of chromediver.exe in extracted directory and paste it in "User-Agent": "YOUR CHROMEDRIVER.EXE PATH" in the code


!!!  REQUIRED PYTHON PACKAGES   !!!


	import requests
	from bs4 import BeautifulSoup
	from selenium import webdriver
	from twilio.rest import Client
	import pickle
	from textblob import TextBlob
	from better_profanity import profanity


Do check all the libraries are installed properly if you are using offline software for python (like IDLE, Pycharm etc.,)

** If you need to change the number that you want to send message then you have go to the twilio account webpage change it **

