import numpy as np

class Unit: 
    def __init__(self, _location, _master, _type, _attack,
                 _defense, _mobility):
        #The province id where this unit currently sits on
        self.location = _location
        #Which civ this unit belongs to 
        self.master = _master
        #Ex) club infantry, tercio, great war infantry, etc
        self.type = _type
        self.attack = _attack
        self.defense = _defense
        #How many tiles the unit can move per turn
        self.mobility = _mobility
        #Represents how degraded/not a unit is. Strength decreases as units enter combat
        self.strength = 100 #TODO -- strengh shouldn't really be injected in, more modified as time goes on

#TODO -- The same principle from the province class may apply here
#The idea here is, that data classes seem to be used for relatively small, modular units of data that do things
#in the program. But when we work with very large, overlappping and all-encompassing units, 
#a database seems more approprate
#While not fitting the case as well, this seems to fit the look. 
class Civ:
    def __init__(self, _name, _manpower, _econ, _tech):
        self.name = _name
        self.manpower =_manpower
        self.econ = _econ
        self.tech = _tech
        self.wars = np.array()


#TODO -- honestly thnking about deleting this class
#TODO -- and just delegating everything to an excel spreadsheet w/ pandas (would double as 'map')
class Province:
    def __init__(self, _pid, _controller, _terrain, _econ, _manpower):
        #Unique province id
        self.pid = _pid
        #Who owns this province
        self.controller = _controller
        self.terrain = _terrain
        self.econ = _econ
        self.manpower = _manpower
        self.city = None
        
class Game:
    civs = np.array()
    turn_no = 0

class City:
    def __init__(self, _controller, _name):
        self.controller = _controller
        self.name = __name__

