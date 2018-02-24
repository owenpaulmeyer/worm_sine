import traceback
import sys

class Segment:
    def __init__(self, orientation = None, percentage = None, enter_direction = None, exit_direction = None):
        self.orientation     = orientation
        self.percentage      = percentage
        self.enter_direction = enter_direction
        self.exit_direction  = exit_direction
        self.type            = 'segment' if orientation != None else None

    def advance(self, amount = 0.1):
        if self.orientation == tail:
            self.percentage += amount
        elif self.orientation == head:
            self.percentage += amount

class Worm:
    def __init__(self, tail, head):
        self.tail = tail
        self.head = head
    
    
    
class Tail:
    def __init__(self):
        self.type = 'tail'
class Head:
    def __init__(self):
        self.type = 'head'


class Bi_Directional:
    def __init__(self, dir1, dir2):
        self.direction1 = dir1
        self.direction2 = dir2
        self.decision = None
    def __hash__(self):
        return hash(self.decide().type)
    def __eq__(self, other):
        return self.get_type() == other.get_type()
    def enter(self):
        return self.decide().enter()
    def decide(self):
        if random(1) > 0.5:
            return self.direction1
        else:
            return self.direction2
    def __str__(self):
        return str(self.decide())
    def get_type(self):
        return self.decide().get_type()
class North:
    def __init__(self):
        self.type = 'N'
    def __hash__(self):
        return hash(self.type)
    def __eq__(self, other):
        result = None
        try:
            result = self.get_type() == other.get_type()
        except Exception, err:
            try:
                exc_info = sys.exc_info()

                # do you usefull stuff here
                # (potentially raising an exception)
                try:
                    raise TypeError("Again !?!")
                except:
                    pass
                # end of useful stuff
            finally:
                # Display the *original* exception
                traceback.print_exception(*exc_info)
                del exc_info
            
            
            
        return result
    def enter(self):
        return South()
    def __str__(self):
        return "North"
    def get_type(self):
        return self.type
class East:
    def __init__(self):
        self.type = 'E'
    def __hash__(self):
        return hash(self.type)
    def __eq__(self, other):
        result = None
        try:
            result = self.get_type() == other.get_type()
        except Exception, err:
            try:
                exc_info = sys.exc_info()

                # do you usefull stuff here
                # (potentially raising an exception)
                try:
                    raise TypeError("Again !?!")
                except:
                    pass
                # end of useful stuff
            finally:
                # Display the *original* exception
                traceback.print_exception(*exc_info)
                del exc_info
        return result
    def enter(self):
        return West()
    def __str__(self):
        return "East"
    def get_type(self):
        return self.type
class South:
    def __init__(self):
        self.type = 'S'
    def __hash__(self):
        return hash(self.type)
    def __eq__(self, other):
        result = None
        try:
            result = self.get_type() == other.get_type()
        except Exception, err:
            try:
                exc_info = sys.exc_info()

                # do you usefull stuff here
                # (potentially raising an exception)
                try:
                    raise TypeError("Again !?!")
                except:
                    pass
                # end of useful stuff
            finally:
                # Display the *original* exception
                traceback.print_exception(*exc_info)
                del exc_info
        return result
    def enter(self):
        return North()
    def __str__(self):
        return "South"
    def get_type(self):
        return self.type
class West:
    def __init__(self):
        self.type = 'W'
    def __hash__(self):
        return hash(self.type)
    def __eq__(self, other):
        result = None
        try:
            result = self.get_type() == other.get_type()
        except Exception, err:
            try:
                exc_info = sys.exc_info()

                # do you usefull stuff here
                # (potentially raising an exception)
                try:
                    raise TypeError("Again !?!")
                except:
                    pass
                # end of useful stuff
            finally:
                # Display the *original* exception
                traceback.print_exception(*exc_info)
                del exc_info
        return result
    def enter(self):
        return East()
    def __str__(self):
        return "West"
    def get_type(self):
        return self.type

north = North()
east  = East()
south = South()
west  = West()
east_west   = Bi_Directional(east, west)
north_south = Bi_Directional(north, south)

head        = Head()
tail        = Tail()
no_worm     = Segment()
simple_worm = Segment(tail, .3, north)