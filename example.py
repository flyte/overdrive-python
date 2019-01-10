from overdrive import Overdrive

def locationChangeCallback(addr, params):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("Location from {addr} : Piece={piece} Location={location} Clockwise={clockwise}".format(addr=addr, **params))

car = Overdrive("xx:xx:xx:xx:xx:xx")
car.setLocationChangeCallback(locationChangeCallback) # Set location change callback to function above
car.changeSpeed(500, 500) # Set car speed with speed = 500, acceleration = 500
car.changeLaneRight(500, 500) # Switch to next right lane with speed = 500, acceleration = 500
input() # Hold the program so it won't end abruptly
