import gym
from gym.envs.registration import register
# import sys, tty, termios
from msvcrt import getch
#inkey=msvcrt.getch()

LEFT=0
DOWN=1
RIGHT=2
UP=3

arrow_keys={72:UP,
                  80:DOWN,
                  77:RIGHT,
                  75:LEFT}
while True:
    key=getch()
    #print(ord(key))
    if ord(key)==224:
        key=ord(getch())
        #print(key)
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break

    action=arrow_keys[key]
    state,reward,done,info=env.step(action)



    env.render()

    print("State ",state,"Action ",action, "Reward: ", reward, "Info: ",info)

    if done:
        print("Finished with reward",reward)
        break
