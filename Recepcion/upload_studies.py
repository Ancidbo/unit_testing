import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.support.select import Select
import csv, operator
import time
# DOM interaction
#from selenium.webdriver.support.select import Select


#Cases of test
class UploadStudies(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        

    #unit tests  
    def test_upload_studies(self):
        driver = self.driver
        driver.get('https://semindigital.com/')
        driver.maximize_window()
        driver.implicitly_wait(1)
      
        lista = []
        with open('data_patients.csv') as data:
            entrada = csv.reader(data)
            lista = list (entrada)
           
        x=0
        for linea in lista:
        #print(linea)
        #print ("Iteracion " , x)
            if(x==0):
                x=x+1
            else:
                # nombre_paciente = linea [0]
                # apellido_p_paciente = linea[1]
                # apellido_m_paciente = linea [2]
                correo_paciente = linea [3]
                # telefono_cel_paciente = linea [4]
                fecha_nacimiento_paciente = linea [5]               
                # sexo_paciente = linea[6]
                correo = linea [7]
                # tipo_sangre_paciente = linea[8]
                # curp_paciente = linea [9]
                # calle_paciente = linea [10]
                # colonia_paciente = linea [11]
                # numero_inte_paciente = linea [12]
                # numero_ext_paciente = linea [13]
                # cp_paciente = linea [14]
                # municipio_paciente = linea [15]
                # localidad_paciente = linea [16]
                # estado_paciente = linea [17]
                # telefono_casa_paciente = linea [18]
                # telefono_ofi_paciente = linea [19]
                # telefono_cel_paciente = linea[20]
                # entidad_nac_paciente = linea [21]
                # entidad_act_paciente = linea [22]
                # nivel_socioe_paciente = linea [23]
                # tipo_vivienda_paciente = linea [24]
                # discapacidad_paciente = linea [25]
                # grupo_etni_paciente = linea [26]
                # reli_paciente = linea [27]
                # ocupacion_paciente = linea [28]
                # tipo_domicilio_paciente = linea [29]
                # numero_exp_paciente = linea [30]
                contrasenia = linea [31]
                nombre_estudio = linea [32]
                fecha_r_estudio = linea [33]


            #Login
                email = driver.find_element_by_id ('email')
                password = driver.find_element_by_id('password')
                
                self.assertTrue(email.is_enabled() 
                and password.is_enabled())

                email.send_keys(correo)
                password.send_keys(contrasenia)
                
                driver.find_element_by_xpath('//*[@id="login"]/div/div/div[2]/form/div[3]/div/div/button').click()
                driver.implicitly_wait(1)

                # Button patient
                driver.find_element_by_xpath('/html/body/app-root/div/app-citas/app-navop/div/div[1]/div[2]/nav/ul/li[2]').click()
                time.sleep(4)

                # search patient
                search_patient = driver.find_element_by_css_selector('#lista_filter > label > input[type=search]')
                search_patient.clear()
                search_patient.send_keys(correo_paciente)
                
                # Click table
                driver.find_element_by_xpath('/html/body/app-root/div/app-pacientes/div/div/div/div/table/tbody').click()
                time.sleep(1)
                # Click upload studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[2]/div[2]/button[4]').click()

                # Study name patient
                study_name_patient = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[1]')
                study_name_patient.clear()
                study_name_patient.send_keys(nombre_estudio)
                
                # Date of realization
                date_realization_studie = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[2]')
                date_realization_studie.clear() 
                date_realization_studie.send_keys(fecha_r_estudio) 

                # Select file 
                upload_studies_file = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[4]')
                upload_studies_file.send_keys('C:\\Users\\Semin\\Desktop\\recepcion\\RecetaMedica.pdf')

                # Select the DICOM file
                upload_studies_dicom = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/form/input[5]')
                upload_studies_dicom.send_keys('C:\\Users\\Semin\\Desktop\\recepcion\\rayosx.jpg')
                time.sleep(1)

                # Button upload
                button_upload = driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[2]/button[2]')
                self.assertTrue(button_upload.is_displayed())
                button_upload.click()
                time.sleep(2)

                # Close table updload studie
                driver.find_element_by_xpath('/html/body/ngb-modal-window[2]/div/div/div[1]/button').click()

                # Close table
                driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/div[1]/button').click()
                
                #  Get out
                driver.find_element_by_xpath('//*[@id="body"]/header/div/div[2]/a/div').click()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output= 'reportes',report_name= 'Subir_Estudios_Paciente'))