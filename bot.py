# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

#importar chrome
from  webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def pesquisar_city(bot, city):
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregando...')
    
    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(city)
    bot.wait(1000)
    bot.enter()

def extrair_dados(bot):
    cont=0
    while True:
        cont +=1
        dia_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[1]', By.XPATH).text
        temp_max = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[1]', By.XPATH).text
        temp_min = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[2]', By.XPATH).text
        
        print(f'Dia: {dia_semana}')
        print(f'Temperatura:\nMax= {temp_max} / Min = {temp_min}')
        print('-------------------------')
        
        if cont==8:
            break


def main():
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

   
    bot.browser = Browser.CHROME

   
    bot.driver_path =ChromeDriverManager().install()

    bot.browse("https://www.google.com")

    try:
        pesquisar_city(bot,'clima manaus')
        bot.wait(1000)
        extrair_dados(bot)
    
    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')
        
    finally:
        bot.wait(3000)

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
