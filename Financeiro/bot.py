from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui
from botcity.core import DesktopBot
import time
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
   
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    pyautogui.hotkey('win','d')
    bot = DesktopBot()
    bot.browse("http://192.168.1.221:8080/monitor/#!/")
    time.sleep(1)
    if not bot.find( "UsuarioLogin", matching=0.97, waiting_time=10000):
        not_found("UsuarioLogin")
    bot.click()
    pyautogui.write('BOT_CAISP')
    bot.tab()   
    time.sleep(1)
    pyautogui.write('caisp@123')
    bot.enter()
    time.sleep(1)
    if not bot.find( "Doc.Recebidos", matching=0.97, waiting_time=10000):
        not_found("Doc.Recebidos")
    bot.click()
    time.sleep(1)
    if not bot.find( "CT-eRecebidos", matching=0.97, waiting_time=10000):
      not_found("CT-eRecebidos")
    bot.click()
    time.sleep(1)
    if not bot.find( "Pesquisa_Avancada", matching=0.97, waiting_time=10000):
        not_found("Pesquisa_Avancada")
    bot.click()
    time.sleep(1)
    if not bot.find( "Calendario", matching=0.97, waiting_time=10000):
        not_found("Calendario")
    bot.click()
    if not bot.find( "Ultimo7dias", matching=0.97, waiting_time=10000):
        not_found("Ultimo7dias")
    bot.click()
    if not bot.find( "MaisCNPJ", matching=0.97, waiting_time=10000):
        not_found("MaisCNPJ")
    bot.click()
    if not bot.find( "Click", matching=0.97, waiting_time=10000):
        not_found("Click")
    bot.click()
    time.sleep(1)
    CNPJ="52.443.149/0001-49;43.945.907/0001-36;41.220.962/0001-33;39.345.125/0001-99;29.860.722/0001-06;16.783.178/0001-96;13.128.655/0001-91;46.475.657/0001-06;32.780.426/0001-00;21.216.843/0001-08;15.570.190/0001-50;41.281.249/0001-08;21.900.268/0001-50;40.061.514/0001-71;29.171.540/0001-10;42.642.147/0001-25;16.754.821/0001-53;28.665.247/0001-46;16.754.805/0001-60;16.896.725/0001-40;48.359.263/0001-18;17.732.180/0001-07;19.900.698/0001-20;39.524.754/0001-86;36.519.979/0001-56;45.357.933/0001-79;31.519.152/0001-29;46.018.507/0001-73;33.214.837/0001-92;17.732.193/0001-78;19.785.770/0001-15;46.060.037/0001-06;16.784.334/0001-33;31.532.117/0001-40;36.086.968/0001-20"
    time.sleep(1)
    pyautogui.write(CNPJ)
    time.sleep(4)
    pyautogui.click(1688,725)
    time.sleep(1)
    bot.scroll_down(clicks=6)
    time.sleep(1)
    if not bot.find( "PesquisaFinal", matching=0.97, waiting_time=10000):
        not_found("PesquisaFinal")
    bot.click()
    time.sleep(2)
    if not bot.find( "Emitende", matching=0.97, waiting_time=10000):
        not_found("Emitende")
    bot.click_relative(-49, 12)
    time.sleep(1)
    if not bot.find( "SelecionarRelative", matching=0.97, waiting_time=10000):
        not_found("SelecionarRelative")
    bot.click_relative(187, 82)
    #if not bot.find( "SelecionarTODOS", matching=0.97, waiting_time=10000):
        #not_found("SelecionarTODOS")
    #bot.click()
    bot.scroll_up(clicks=1)
    if not bot.find( "BaixarXML", matching=0.97, waiting_time=10000):
        not_found("BaixarXML")
    bot.click()
    time.sleep(1)
    if not bot.find( "DesmarcaProcEventos", matching=0.97, waiting_time=10000):
        not_found("DesmarcaProcEventos")
    bot.click_relative(-30, 5)
    if not bot.find( "Download", matching=0.97, waiting_time=10000):
        not_found("Download")
    bot.click_relative(172, 24)
    time.sleep(1)
    pyautogui.click(1814,212)
    time.sleep(1)
    bot.scroll_up(clicks=10)
    time.sleep(5)
    if not bot.find( "Deslogar", matching=0.97, waiting_time=10000):
        not_found("Deslogar")
    bot.click()
    time.sleep(1)
    if not bot.find( "Sair", matching=0.97, waiting_time=10000):
        not_found("Sair")
    bot.click()
    time.sleep(1)
    pyautogui.hotkey('alt','f4')
    time.sleep(1)
    pyautogui.hotkey('win','r')
    time.sleep(1)
    pyautogui.write(r'C:\Users\TI2\Downloads')
    time.sleep(1)
    bot.enter()
    pyautogui.click(831,614)
    time.sleep(1)
    bot.type_down()
    time.sleep(1)
    if not bot.find( "Extrair", matching=0.97, waiting_time=10000):
        not_found("Extrair")
    bot.click()
    if not bot.find( "Extrairaqui", matching=0.97, waiting_time=10000):
        not_found("Extrairaqui")
    bot.click()
    time.sleep(10)
    pyautogui.hotkey('win','d')
    time.sleep(1)
    pyautogui.hotkey('win','r')
    time.sleep(1)
    pyautogui.write(r'C:\Users\TI2\AppData\Roaming\Microsoft\Windows\Start Menu\CORPORATIVO.lnk')
    bot.enter()
    if not bot.find( "Login", matching=0.97, waiting_time=20000):
        not_found("Login")
    bot.click_relative(-47, -72)
    bot.kb_type('bot.financeiro')
    bot.tab()
    bot.kb_type('caisp@123')
    bot.enter()
    

    


    
    
   
    
  
    ...


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()