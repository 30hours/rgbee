import pigpio

def main():

    pi = pigpio.pi()

    # turn off initially
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(27, 0)
    pi.set_PWM_dutycycle(22, 0)

    # set pull down
    pi.set_pull_up_down(17, pigpio.PUD_DOWN)
    pi.set_pull_up_down(27, pigpio.PUD_DOWN)
    pi.set_pull_up_down(22, pigpio.PUD_DOWN)
    
    # set PWM frequency
    freq=800
    pi.set_PWM_frequency(17, freq)
    pi.set_PWM_frequency(27, freq)
    pi.set_PWM_frequency(22, freq)

main()
