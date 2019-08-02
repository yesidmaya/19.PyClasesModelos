# -*- codign: utf-8 -*-
#v=4.5

class Lamp:
    _LAMPS = ['''

    #########::::::::::########
    ##########::::::::#########
    ###########::::::##########
    ###########,---.###########
    ##########/`---'\##########
    #########/       \#########
    ########/         \########
    #######:`-._____.-':#######
    ######::::: ( ) |::::######
    #####:::::: ) ( o:::::#####
    ####::::: .-(_)-. :::::####
    ###:::::: '=====' ::::::###
    ###########################

    ''',
    '''
         _________
        d         b
       d           b
      d             b
     d               b
    d                 b
     -----------------
            fff
          .'   '.
         ^       ^.'--.
         b       d     ,
          czzzzzd       ..oOo

    '''] # variable clase

    def __init__(self, isTurned_on): # __init__ -> es el constructor de la clase y self -> metodo de instancia
        self._is_turned_on = isTurned_on # Recibimos el parámetro is_turned_on que lo guarda en una variable de instancia self. _is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
    
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(isTurned_on = False)

    while True:
        command = str(input('''
            Que deseas hacer?

            [p]render la lampara
            [a]pagar la lampara
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == "__main__":
    run()