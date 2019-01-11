overdrive-python
================

Object interface for controlling Anki Overdrive with Python.

This project provides an API to control Anki Overdrive from Python.
Commands are mostly deciphered using information from [Anki Drive SDK](https://github.com/anki/drive-sdk) and [node-mqtt-for-anki-overdrive](https://github.com/IBM-Bluemix/node-mqtt-for-anki-overdrive).

This depends on [bluepy](https://github.com/IanHarvey/bluepy), so it only works on Linux systems.

Requirements
------------
* [Python 3.4+](https://python.org)
* [bluepy](https://github.com/IanHarvey/bluepy)
* Root permission (for scanning only)

Usages
------
To use this interface, start by initiating an Overdrive object with the desired Bluetooth MAC address:

```python
from overdrive import Overdrive

car = Overdrive("xx:xx:xx:xx:xx:xx")
```

For example, if your Overdrive Bluetooth MAC address is 00:11:22:33:44:55, use the following code:

```python
from overdrive import Overdrive

car = Overdrive("00:11:22:33:44:55")
```

After initialization, you can use the methods of the created object to control the car. For example, if you want to set the car moving, call `changeSpeed` function on the `car` object. The following code is an example with speed of 500 mm/sec and acceleration of 800 [mm/sec^2](https://en.wikipedia.org/wiki/Metre_per_second_squared):

```python
car.changeSpeed(500, 800)
```

Documentation
-------------

See `overdrive.py` file for available methods.

License
-------

This project is licensed under MIT license.
See `LICENSE` file for details.
