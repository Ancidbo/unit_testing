import unittest
import csv, operator
import smtplib
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.select import Select

#unit tests
#Cases of test
class Billing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_billing(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.implicitly_wait(10) 

        lista = []
        with open('data_billing.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1        
            else:
                empresa = linea [0]
                sucursal = linea [1]
                nombre = linea [2]
                apellido_p = linea[3]
                apellido_m = linea [4]
                rfc = linea [5]
                cantidad_p = linea [6]
                telefono = linea [7]
                email_p = linea [8]
                uso_cfdi = linea [9]
                forma_pago = linea [10]
                metodo_pago = linea [11]
                descripcion = linea [12]
                nombre_paciente = linea [13]
                num_expe = linea [14]
                num_folio = linea [15]
                estudios = linea [16]
                observaciones = linea [17]
                correo = linea [18]
                contrasenia = linea [19] 
                
            # Login
                email = driver.find_element_by_id ('email')
                email.clear()
                password = driver.find_element_by_id('password')
                password.clear()
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(2)

                # button refunds
                button = driver.find_element_by_xpath('/html/body/app-root/div/app-citas/div[1]/div[1]/div[4]/button[6]')
                self.assertTrue(button.is_enabled())
                button.click()
                time.sleep(2)
                
                # button new refunds
                button1 = driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[2]')
                self.assertTrue(button1.is_enabled())
                button1.click()

            # new_refunds

                # Company               
                select_company = driver.find_element_by_xpath('//*[@id="empresa"]')
                select_company.send_keys(empresa)

                # Branch office
                select_office = driver.find_element_by_xpath('//*[@id="sucursal"]')
                select_office.send_keys(sucursal)

                # name
                name = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[1]')
                name.clear()
                name.send_keys(nombre)

                # Last name
                last_name = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[2]')
                last_name.clear()
                last_name.send_keys( apellido_p)
                
                # Mother's last name
                mother_last_name = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[3]')
                mother_last_name.clear()
                mother_last_name.send_keys( apellido_m)

                # RFC
                rfc1 = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[4]')
                rfc1.clear()
                rfc1.send_keys(rfc)

                # Amount paid
                amount_paid = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[5]')
                amount_paid.clear()
                amount_paid.send_keys(cantidad_p)

                # Cell phone
                cell_phone = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[6]')
                cell_phone.clear()
                cell_phone.send_keys(telefono)

                # Email -------------------------->verificar<---------------------
                correo_email = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[7]')
                correo_email.send_keys(email_p)
        
                # CDFI use
                select_cdfi = driver.find_element_by_id('cfdi_uso')
                select_cdfi.send_keys(uso_cfdi)

                # method of payment
                select_method_payment = driver.find_element_by_id('forma_pago')
                select_method_payment.send_keys(forma_pago)

                # pay method
                select_pay_method = driver.find_element_by_id('metodo_pago')
                select_pay_method.send_keys(metodo_pago)

                # Description
                description = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[8]')
                description.send_keys(descripcion)

                # Name of patient
                name_patient = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[9]')
                name_patient.clear()
                name_patient.send_keys(nombre_paciente)

                # File number
                file_number = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[10]')
                file_number.clear()
                file_number.send_keys(num_expe)

                # Folio number
                folio_number = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[11]')
                folio_number.clear()
                folio_number.send_keys(num_folio)

                # applied studies
                applied_studies = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[12]')
                applied_studies.clear()
                applied_studies.send_keys(estudios)

                # Observations
                observations = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[1]/form/input[13]')
                observations.clear()
                observations.send_keys(observaciones)

                # Button save
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[2]/button[2]').click()

                #Button return table
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/div[2]/button[1]').click()

                #Button return 
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/button[1]').click()

                # Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()
if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Facturación'))
