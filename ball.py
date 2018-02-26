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
    def __init__(self, grid, x_pos, y_pos):
        self.grid = grid
        self.setup_segments(x_pos, y_pos)
    
    def setup_segments(self, x_pos, y_pos):
        self.tail_x_pos = x_pos
        self.tail_y_pos = y_pos
        rand = random(1)
        
        if rand < .25:
            enter_direction = west
        elif rand < .5:
            enter_direction = east
        elif rand < .75:
            enter_direction = north
        else:
            enter_direction = south

        current_tile   = self.grid.lookup_tile(y_pos, x_pos)
        exit_direction = current_tile.tile.exit_direction(enter_direction) 

        tail_segment = Segment(tail, 0.0, enter_direction, exit_direction)                       
        current_tile.set_segment(tail_segment)   

        (next_x, next_y), next_enter = self.next_location_enter_direction(exit_direction)
        self.head_x_pos              = next_x
        self.head_y_pos              = next_y
        next_enter_direction         = next_enter
        
        next_tile           = self.grid.lookup_tile(self.head_y_pos, self.head_x_pos)
        next_exit_direction = next_tile.tile.exit_direction(next_enter_direction)
        
        head_segment = Segment(head, 0.0, next_enter_direction, next_exit_direction)
        next_tile.set_segment(head_segment)
    
    def cycle(self):
        print 'CYC'
                        
        self.grid.set()
        
        self.tail_x_pos = self.head_x_pos
        self.tail_y_pos = self.head_y_pos
        self.enter_direction = self.next_enter_direction
        
        current_tile   = self.grid.lookup_tile(self.y_pos, self.x_pos)
        exit_direction = current_tile.tile.exit_direction(self.enter_direction)
        
        tail = Segment(tail, 0.0, self.enter_direction, exit_direction)
        current_tile.set_segment(tail)

        (next_x, next_y), next_enter = self.next_location_enter_direction(exit_direction)
        self.next_x_pos = next_x
        self.next_y_pos = next_y
        self.next_enter_direction = next_enter
        
        next_tile           = self.grid.lookup_tile(self.y_pos, self.x_pos)
        next_exit_direction = next_tile.tile.exit_direction(self.next_enter_direction)
        
        head = Segment(head, 0.0, self.next_enter_direction, next_exit_direction)
        next_tile.set_segment(head)
    
    
    def next_location_enter_direction(self, exit_direction):
        next_enter_direction = None
        (x_next, y_next), stay = self.lookup_next_location(self.tail_x_pos, self.tail_y_pos, exit_direction)
        if not stay:
            next_enter_direction = exit_direction.enter()
        else: next_enter_direction = exit_direction
        next_enter_direction = exit_direction.enter()
        return (x_next, y_next), next_enter_direction
    
    def lookup_next_location(self, x, y, exit_direction):
        stay = False
        x_pos = x
        y_pos = y
        if exit_direction == north:
            if y == 1:
                # stay = True
                y_pos = self.grid.col_size
            else:
                y_pos -= 1
        elif exit_direction == east:
            if x == self.grid.row_size:
                # stay = True
                x_pos = 1
            else:
                x_pos += 1
        elif exit_direction == south:
            if y == self.grid.col_size:
                # stay = True
                y_pos = 1
            else:
                y_pos += 1
        elif exit_direction == west:
            if x == 1:
                # stay = True
                x_pos = self.grid.row_size
            else:
                x_pos -= 1
        return (x_pos, y_pos), stay
    
    def advance_segments(self):
        self.tail.advance()
        self.head.advance()
        return True
    
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

head           = Head()
tail           = Tail()
no_segment     = Segment()
# simple_segment = Segment(tail, .3, north)