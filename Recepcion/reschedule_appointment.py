import unittest
import csv, operator
import random
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class RescheduleAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_reschedule_appointment(self):
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
                sucursal = linea [2]
                sala = linea [3]
                prueba = linea [4]
                sala_rea = linea [8]
                hora_ini = linea [9]
                hora_fin = linea [10]
                modificar_es = linea [11]
                reagendar_cita = linea [12]
                
            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)

            #schedule appointment
                # Select branch
                select_branch = Select(driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[1]/div[1]/div[1]/select')) 
                select_branch.select_by_visible_text(sucursal)

                # Select hall
                select_hall = Select(driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[1]/div[1]/div[2]/select')) 
                select_hall.select_by_visible_text(sala)
                time.sleep(2)

                 # Select the box in the table
                driver.find_element_by_css_selector('#calendar > div.fc-view-container > div > table > tbody > tr > td > div > div > div:nth-child(2) > div.fc-content-skeleton > table > tbody > tr:nth-child(1) > td:nth-child(6) > a').click()

                # Click on Reschedule
                driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[2]/div/div/div[3]/button[2]').click()

                # Branch office
                select_branch_office = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[1]/select')) 
                select_branch_office.select_by_visible_text(sucursal)

                # Hall
                select_hall = Select(driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/select')) 
                select_hall.select_by_visible_text(sala_rea)

                # Appointment date
                appointment_date = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[1]')
                appointment_date.send_keys(reagendar_cita)

                # Start Time
                start_time = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[2]')
                start_time.clear()
                start_time.send_keys(hora_ini)
                
                # Final hour
                final_time = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/form/input[3]')
                final_time.send_keys( hora_fin)

                # Reschedule button
                reschedule_button = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]')
                self.assertTrue(reschedule_button.is_displayed())
                reschedule_button.click()
                time.sleep(2)

                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[1]').click()
                time.sleep(2)
                
                # # Get out System
                # driver.find_element_by_xpath('/html/body/app-root/div/app-citas/app-navop/div/header/div/div[2]/a/div').click()


if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Reagendar_cita'))
