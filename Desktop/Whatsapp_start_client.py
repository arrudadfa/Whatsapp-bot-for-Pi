from selenium import webdriver

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('http://web.whatsapp.com')
print('Primeiramente escaneie o QR code.')