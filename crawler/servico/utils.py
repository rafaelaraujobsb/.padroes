import re
import os
import zipfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import servico.proxy_config as proxy_config

def set_proxy(headless: bool, var_ambiente: str = 'http_proxy') -> Options:
    """
	Configura o proxy do chrome.

	Params:
	    var_ambiente: variável de ambiente com a configuração de proxy.
			exemplo: http://usuario:senha@host:porta
		headless: para rodar o selenium no servidor.

	Returns:
	    Options
	"""
	option = Options()
	option.add_argument("--start-maximized")   

	if headless:     
	    option.headless = headless
	else:
	    USUARIO, SENHA, HOST, PORTA = re.split(r'@|\:', os.environ['http_proxy'].replace('http://', ''))

	    file = './servico/proxy_auth_plugin.zip'
	    with zipfile.ZipFile(file, 'w') as zp:
		zp.writestr("manifest.json", proxy_config.MANIFEST_JSON)
		zp.writestr("background.js", proxy_config.BACKGROUND_JS %(HOST, int(PORTA.replace('/','')), USUARIO, SENHA))
	    
	    option.add_extension(file)

	return option

