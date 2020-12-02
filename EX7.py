from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_user = input()
        if input_user == stopper:
            mixer.music.stop()
            break


def logs(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{datetime.now()} : {msg}\n")


if __name__ == '__main__':
    watersecs = 40*60
    eyessecs = 30*60
    pesecs = 45*60
    init_water = time()
    init_eyes = time()
    init_pe = time()
    while True:
        if time() - init_water > watersecs:
            print("Enter \"Drank\" to stop the alarm\n")
            musicloop('water.mp3', "Drank")
            init_water = time()
            logs("Drank Water")
        if time() - init_eyes > eyessecs:
            print("Enter \"EyDone\" to stop the alarm\n")
            musicloop('water.mp3', "EyDone")
            init_eyes = time()
            logs("Did eyes exercise")
        if time() - init_pe > pesecs:
            print("Enter \"ExDone\" to stop the alarm\n")
            musicloop('water.mp3', "ExDone")
            init_pe = time()
            logs("Did physical exercise")
