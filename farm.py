import pyautogui, cv2, msvcrt, random
from time import sleep

# Functions
def wait():
    sleep(round(random.uniform(.8, 3), 2))
    
# Main Function
cont = 0

# Random clicks location
# Varia de acordo com a largura da imagem
def random_left(width):
    objx = random.randint(0,width)
    return objx

# Varia de acordo com a altura da imagem
def random_top(height):
    objy = random.randint(0,height)
    return objy

while 1:

    print ('Running: ' + str(cont))
    
    # Vitoria
    victory = pyautogui.locateOnScreen('vitoria.PNG', grayscale=True, confidence=.7)
    if(victory):
        pyautogui.click((victory.left + random_left(victory.width))
                        ,(victory.top + random_top(victory.height))
                        , clicks=2, interval=1.5)
    wait()

    #Vender Runa
    btn_vender = pyautogui.locateOnScreen('ok.PNG', grayscale=True, confidence=.7)
    if(btn_vender):
        pyautogui.click((btn_vender.left + random_left(btn_vender.width))
                        ,(btn_vender.top + random_top(btn_vender.height)))
        
    wait()

    # OK = Runa, Mons, Perg, event
    btn_ok = pyautogui.locateOnScreen('ok.PNG', grayscale=True, confidence=.7)
    if(btn_ok):
        pyautogui.click((btn_ok.left + random_left(btn_ok.width))
                        ,(btn_ok.top + random_top(btn_ok.height)))           
    wait()

    # Repetir 
    btn_repetir = pyautogui.locateOnScreen('repetir.PNG', grayscale=True, confidence=.9)
    if(btn_repetir):
        pyautogui.click((btn_repetir.left + random_left(btn_repetir.width))
                        ,(btn_repetir.top + random_top(btn_repetir.height)))
    wait()

    cont += 1

    ## Reseta a posição das imagens ##
    victory = None
    btn_vender = None
    btn_ok = None
    btn_repetir = None

    # ESC para sair
    if msvcrt.kbhit():
        if ord(msvcrt.getch()) == 59:
            break
