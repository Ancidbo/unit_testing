import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
import csv, operator
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class ForgetPassword(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def forget_password(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.implicitly_wait(5)
      
        lista = []
        with open('registro.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
            # red lines
            # file = open('registro.csv') 
            # numline = len(file.readlines()) 
            # print (numline) 
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1
            else:
                # Share items
                drive.find