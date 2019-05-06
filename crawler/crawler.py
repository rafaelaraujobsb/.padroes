from selenium import webdriver

from servico.utils import set_proxy


browser = webdriver.Chrome(executable_path='./driver/chromedriver_v73', chrome_options=set_proxy())

browser.get('https://github.com/')

