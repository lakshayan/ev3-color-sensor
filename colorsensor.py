from time import sleep
import ev3dev.ev3 as ev3


rc = ev3.RemoteControl()
assert rc.connected


rm = ev3.LargeMotor('outD')
assert rm.connected

lm = ev3.LargeMotor('outA')
assert lm.connected

cl = ev3.ColorSensor()
assert cl.connected
cl.mode ='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')



speed = 900

ev3.Sound.speak('hello i am eva').wait()


def red_up_called(state):
    print ('RED up button pressed',state)
    if state == True:
        rm.run_forever(speed_sp = speed)
        lm.run_forever(speed_sp = speed)
    else:
        rm.stop()
        lm.stop()
    return
    

def red_down_called(state):
    print ('RED dow button pressed',state)
    if state == True:
        rm.run_forever(speed_sp = -speed)
        lm.run_forever(speed_sp = -speed)
    else:
        rm.stop()
        lm.stop()
    return

def blue_up_called(state):
    print ('BLUE up button pressed',state)
    if state == True:
        rm.run_forever(speed_sp = speed)
        lm.run_forever(speed_sp = -speed)
    else:
        rm.stop()
        lm.stop()
    return

def blue_down_called(state):
    print ('BLUE down button pressed',state)
    if state == True:
        rm.run_forever(speed_sp = -speed)
        lm.run_forever(speed_sp = speed)
    else:
        lm.stop()
        rm.stop()
    return

def beacon_called(state):
    print('BEACON button pressed',state)
    if state == True:
        ev3.Sound.speak(colors[cl.value()]).wait()
    return

rc.on_red_up = red_up_called
rc.on_red_down = red_down_called
rc.on_blue_up = blue_up_called
rc.on_blue_down = blue_down_called
rc.on_beacon = beacon_called


while True:
    rc.process()
    sleep(0.01)
    
