from selenium import webdriver

from servico.utils import set_proxy

browser = webdriver.Firefox(executable_path='./driver/geckodriver', firefox_profile=set_proxy())

browser.get('https://www.google.com/')

