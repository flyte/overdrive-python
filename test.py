#!/usr/bin/env python
# coding: utf-8

from overdrive import Overdrive
car = Overdrive('f7:27:7e:4d:2a:aa')  # X52


def locationChangeCallback(addr, params):
    params['addr'] = addr
    print('Location from {addr} : Piece={piece} Location={location} Speed={speed} Clockwise={clockwise}'.format(**params))

car.setLocationChangeCallback(locationChangeCallback)

def transitionChangeCallback(addr, params):
    params['addr'] = addr
    print('Transition from {addr} From={piecePrev} To={piece} Offset={offset}'.format(**params))

car.setTransitionCallback(transitionChangeCallback)

car.changeSpeed(500, 800)

while True:
    inpt = input('[ to change lane to left, ] to change lane to right, enter to stop.\n')
    if inpt == '[':
        car.changeLaneLeft(500, 800)
    elif inpt == ']':
        car.changeLaneRight(500, 800)
    else:
        break

car.changeSpeed(0, 800)
car.disconnect()
