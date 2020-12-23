from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from tkinter import filedialog
import urllib.request
import datetime
import config
import pyautogui
import os



USERNAME = config.USERNAME
PASSWORD = config.PASSWORD


class AutoPoster:
	
	def __init__(self, page, text):
		"""
		Initializing Bot
		"""
		self.driver_path = os.getcwd()+r"\chromedriver.exe"
		self.path = "https://m.facebook.com/"
		self.page_id = page
		self.bot = webdriver.Chrome(options=self.__options(), executable_path=self.driver_path)
		self.image_path = os.getcwd()+r"\image"
		self.text = text
		self.__start(self.bot, self.path)


	def __start(self, bot, path):
		"""
		Starting Bot
		"""
		try:
			bot.get(path)
			WebDriverWait(bot, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="m_login_email"]')))
			print("Facebook Loaded")
			if self.__login(bot):
				print("Login Successful")
				sleep(10)
				bot.get(path)
				self.__post(bot, self.page_id)
			else:
				print("Login Failed")
		except:
			print("Failed")


	def __post(self, bot, page):
		bot.get(page)
		sleep(6)
		bot.find_element_by_css_selector("#u_0_1k > div:nth-child(1)").click()
		sleep(5)
		bot.find_element_by_id("uniqid_1").send_keys(self.text)
		sleep(3)
		pyautogui.click(x = 78, y = 418, clicks = 2, interval = 1)
		image = os.listdir(self.image_path)
		if len(image) == 0:
			print("No Image Found!")
		if len(image) == 1:
			if (image[0].endswith(".jpg")) or (image[0].endswith(".png")):
				self.__upload(bot, image[0])
				bot.refresh()
		pass


	def __upload(self, bot, image):
		"""
		Uploading Image
		"""
		image_found = self.image_path+f"\{image}"
		pyautogui.click(x = 206, y = 449)
		pyautogui.typewrite(image_found)
		pyautogui.click(x = 472, y = 479)
		sleep(3)
		bot.find_element_by_css_selector('#composer-main-view-id > div.acw > div > div > button').click()
		sleep(5)


	def __login(self, bot):
		"""
		Loging In the Bot
		"""
		try:
			username = bot.find_element_by_xpath('//*[@id="m_login_email"]')
			password = bot.find_element_by_xpath('//*[@id="m_login_password"]')
			bot.implicitly_wait(3)
			username.send_keys(USERNAME)
			bot.implicitly_wait(3)
			password.send_keys(PASSWORD)
			bot.implicitly_wait(3)
			bot.find_element_by_name('login').click()
			return True
		except:
			return False


	def __options(self):
		"""
		Configuring options of the Bot
		"""
		options = Options()
		options.add_argument("Cache-Control=no-cache")
		options.add_argument("--no-sandbox")
		options.add_argument("--dns-prefetch-disable")
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--disable-web-security")
		options.add_argument("--ignore-certificate-errors")
		options.page_load_strategy = 'none'
		options.add_argument("--ignore-certificate-errors-spki-list")
		options.add_argument("--ignore-ssl-errors")
		return options


fb = AutoPoster("https://m.facebook.com/groups/2002264246675285", "Bot is Posting in Groups")