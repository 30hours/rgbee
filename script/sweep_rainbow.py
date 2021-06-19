import sys
import time
import pigpio
import math

def main(brightness = 1):

    pi = pigpio.pi()

    # get initial rgb
    initial_red = pi.get_PWM_dutycycle(17)
    initial_green = pi.get_PWM_dutycycle(27)
    initial_blue = pi.get_PWM_dutycycle(22)

    # fade to start
    start_red = brightness*(255/2)*(1+math.sin(0))
    start_green = brightness*(255/2)*(1+math.sin(math.radians(120)))
    start_blue = brightness*(255/2)*(1+math.sin(math.radians(240)))

    diff_red = start_red - initial_red
    diff_green = start_green - initial_green
    diff_blue = start_blue - initial_blue

    for factor in range(0, 101):
    
      pi.set_PWM_dutycycle(17, initial_red + diff_red*factor/100)
      pi.set_PWM_dutycycle(27, initial_green + diff_green*factor/100)
      pi.set_PWM_dutycycle(22, initial_blue + diff_blue*factor/100)
      time.sleep(0.01)

    while True:

      nMax = 1024
      nMin = 0

      for i in range(nMin, nMax):

        arg = 2*math.pi*i/nMax

        red = int((255/2)*(1+math.sin(arg)))
        green = int((255/2)*(1+math.sin(math.radians(120)+arg)))
        blue = int((255/2)*(1+math.sin(math.radians(240)+arg)))

        pi.set_PWM_dutycycle(17, brightness*red)
        pi.set_PWM_dutycycle(27, brightness*green)
        pi.set_PWM_dutycycle(22, brightness*blue)
        
        time.sleep(0.1)

if len(sys.argv) == 1:
    main()

if len(sys.argv) == 2:
    brightness = float(sys.argv[1])
    main(brightness/100)
