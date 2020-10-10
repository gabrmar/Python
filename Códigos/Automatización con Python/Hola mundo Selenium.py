from selenium import webdriver

# El driver del navegador que se quiera usar debe estar en el PATH que lleva a Python 

# Para usar Firefox
browser = webdriver.Firefox()
# Para Usar Chrome 
#browser = webdriver.Chrome()
browser.get('http://seleniumhq.org/')