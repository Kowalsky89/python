from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as ec
#from selenium.webdriver.support.ui import WebDriverWait
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--ignore-ssl-errors')
#driver = webdriver.Chrome(chrome_options=options)
browser = webdriver.Chrome('D:\Temp\SE\chromedriver_win32\chromedriver.exe')
browser.implicitly_wait(5) #пятисекундная задержка. Если Selenium не находит элемент, он ждет, чтобы все загрузилось и пытается снова
browser.maximize_window()
browser.get('https://kazan.hh.ru/account/login?backurl=%2F&hhtmFrom=main')
login_link = browser.find_element("xpath","//button[contains(text(),'Войти с паролем')]")
login_link.click()
sleep(1)
usrnm_inpt = browser.find_element("xpath",'//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/fieldset/input')
usrnm_inpt.send_keys("login")
passd_inpt = browser.find_element("xpath",'//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/fieldset/input')
passd_inpt.send_keys("pass")
login_bttn = browser.find_element("xpath",'//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]')
login_bttn.click()
sleep(1)
browser.get('https://kazan.hh.ru/search/vacancy?area=113&professional_role=113&professional_role=114&professional_role=116&resume=3bc08a60ff073f22b30039ed1f5a4639356244&schedule=remote&search_field=name&search_field=company_name&search_field=description&forceFiltersSaving=true&clusters=true&enable_snippets=true&order_by=salary_desc&from=cluster_schedule&showClusters=false')
sleep(1)
for i in range(1, 51):
    otklik = browser.find_element("xpath","//*[contains(text(),'Откликнуться')]")
    otklik.click()
    #if len(browser.find_elements("xpath","//div[contains(text(),'Чтобы откликнуться на эту вакансию, поменяйте види')]"))>0: #!!!OK!!!
    #//p[contains(text(),'Для отклика на эту вакансию необходимо ответить на')] #окошечко
    #//body/div[@id='HH-React-Root']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/textarea[1]  # text 1
    #//body/div[@id='HH-React-Root']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[4]/div[2]/textarea[1]  # text 2
    #//body/div[@id='HH-React-Root']/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[11]/div[2]/textarea[1] # text 8
    #if len(browser.find_elements("xpath","//div[contains(text(),'Сопроводительное письмо')]"))>0:
    #    print('Sopr exists')
    #    sopr_inpt = browser.find_element("xpath",'//*[@id="RESPONSE_MODAL_FORM_ID"]/div/div/textarea')
    #    #//*[@id="RESPONSE_MODAL_FORM_ID"]/div/div/textarea
    #    #/html[1]/body[1]/div[12]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/textarea[1]
    #    text_inpt.send_keys("Для отклика на эту вакансию был написан тестировочный Selenium-бот на Python. Если интересно - код будет выкладываться на гитхаб.")
    #    otklik = browser.find_element("xpath","//*[contains(text(),'Откликнуться')]")
    #    otklik.click()
    if len(browser.find_elements("xpath","//p[contains(text(),'Для отклика на эту вакансию')]"))>0: # работодатель предлагае
        print('Element exists')
        #for i in range(3, 12):
        text_inpt = browser.find_element("xpath",'//*[@id="HH-React-Root"]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/div[2]/textarea[1]')
        text_inpt.send_keys("Для отклика на эту вакансию был написан тестировочный Selenium-бот на Python. Если интересно - код будет выкладываться на гитхаб.")
        sleep(1)
        otklik = browser.find_element("xpath","//*[contains(text(),'Откликнуться')]")
        otklik.click()
        browser.get('https://kazan.hh.ru/search/vacancy?area=113&professional_role=113&professional_role=114&professional_role=116&resume=3bc08a60ff073f22b30039ed1f5a4639356244&schedule=remote&search_field=name&search_field=company_name&search_field=description&forceFiltersSaving=true&clusters=true&enable_snippets=true&order_by=salary_desc&from=cluster_schedule&showClusters=false')
sleep(10)
browser.close()
