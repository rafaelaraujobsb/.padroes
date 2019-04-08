import re
import os

from selenium import webdriver

def set_proxy(var_ambiente: str = 'http_proxy') -> webdriver.FirefoxProfile:
    """
    Configura o proxy do firefox.

    Params:
        var_ambiente: variável de ambiente com a configuração de proxy.
            exemplo: http://usuario:senha@host:porta

    Returns:
        webdriver.FirefoxProfile
    """
    USERNAME, PASSWORD, PROXY_HOST, PROXY_PORT = re.split(r'@|\:', os.environ['http_proxy'].replace('http://', ''))

    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", PROXY_HOST)
    profile.set_preference("network.proxy.http_port", PROXY_PORT)
    profile.set_preference("network.proxy.socks_username", USERNAME)
    profile.set_preference("network.proxy.socks_password", PASSWORD)

    profile.update_preferences()

    return profile

