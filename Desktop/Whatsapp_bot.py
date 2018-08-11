#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Whatsapp_start_client import driver

def run():
    name = input('Entre o nome de usuário ou o nome do grupo : ')
    msg = input('Entre a mensagem a ser enviada : ')
    count = int(input('Quantidade de mensagens : '))

    user = driver.find_element_by_class_name('jN-F5')
    user.clear()
    user.send_keys(name)
    user.send_keys(Keys.RETURN)

    msg_box = driver.find_element_by_class_name('_2S1VP')
    msg_box.clear()
    for i in range(count):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.RETURN)
    
#driver.quit()