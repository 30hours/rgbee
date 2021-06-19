import sys
import time
import pigpio

def main(color, brightness = 1):

    pi = pigpio.pi()
    
    rgb = hex_to_rgb(color)

    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]

    pi.set_PWM_dutycycle(17, red * brightness)
    pi.set_PWM_dutycycle(27, green * brightness)
    pi.set_PWM_dutycycle(22, blue * brightness)


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
