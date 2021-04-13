from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

audience = ['iamarshadmalik']


class InstaBot:
    def __init__(self, username, password, message):
        self.username = username
        self.password = password
        self.message = message
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)

        self.bot.find_element_by_xpath(
            '//html/body/div[3]/div/div/div/div[3]/button[2]').click()
        time.sleep(2)

        self.bot.get('https://www.instagram.com/direct/inbox/')
        time.sleep(2)

        self.bot.get('https://www.instagram.com/direct/new/')
        time.sleep(2)

        for i in audience:

            self.bot.find_element_by_name('queryBox').send_keys(i)
            time.sleep(2)

            self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[2]/div[2]/div[1]').click()
            time.sleep(2)

            self.bot.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div').click()
            time.sleep(2)

            send = self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            send.send_keys(self.message)
            time.sleep(1)

            send.send_keys(Keys.RETURN)
            time.sleep(2)


ed = InstaBot('_nkvii', '$hahidali786', 'fk u')
ed.login()
