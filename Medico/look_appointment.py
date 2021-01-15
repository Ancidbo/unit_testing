import unittest
import csv, operator
import smtplib
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class LookAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_look_appointment(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('data.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1        
            else:
                correo = linea [0]
                contrasenia = linea [1]
                # cie10 = linea [2]
                estudio = linea [3]
                # tipo_cita = linea [4]
                # costo = linea [5]
                # fecha = linea [6]
                # hora_i = linea [7]
                # hora_f = linea [8]
                # telefono = linea [9]

            # Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)

                # button look_appointment
                driver.find_element_by_xpath('/html/body/app-root/div/app-medico/div[1]/div[1]/div[1]/button[2]').click()

        # Appointment History
                search = driver.find_element_by_xpath('//*[@id="listaCitas_filter"]/label/input')
                search.clear()
                search.send_keys(estudio) 

                # Button
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
        
                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Buscar cita'))                
