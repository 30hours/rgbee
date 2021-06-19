import sys
import time
import pigpio

def main(color, brightness = 1):

    pi = pigpio.pi()
    
    # get initial rgb
    initial_red = pi.get_PWM_dutycycle(17)
    initial_green = pi.get_PWM_dutycycle(27)
    initial_blue = pi.get_PWM_dutycycle(22)

    rgb = hex_to_rgb(color)

    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    red = red * brightness
    green = green * brightness
    blue = blue * brightness

    diff_red = red - initial_red
    diff_green = green - initial_green
    diff_blue = blue - initial_blue

    for factor in range(0, 101):
    
      pi.set_PWM_dutycycle(17, initial_red + diff_red*factor/100)
      pi.set_PWM_dutycycle(27, initial_green + diff_green*factor/100)
      pi.set_PWM_dutycycle(22,  initial_blue + diff_blue*factor/100)
      time.sleep(0.002)


def hex_to_rgb(hex_string):

    r_hex = hex_string[0:2]
    g_hex = hex_string[2:4]
    b_hex = hex_string[4:6]
    
    return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)

if len(sys.argv) == 2:
    color = sys.argv[1]
    main(color)

if len(sys.argv) == 3:
    color = sys.argv[1]
    brightness = float(sys.argv[2])
    main(color, brightness/100)
