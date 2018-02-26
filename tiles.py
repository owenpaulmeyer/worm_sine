from ball import *
from collections import deque

def bounding_box(x, y, size):
    stroke(1)
    strokeWeight(1)
    rect(x, y, size, size)
class Tile:
    def __str__(self):
        return self.x_pos + ', ' + self.y_pos + ', ' + str(self.segment)
    def __init__(self, t, x = 0, y = 0, sz = 20, sc = 1):
        self.x_pos = x
        self.y_pos = y
        self.tile = t
        self.size = sz
        self.scale = sc
        self.segments = deque([])

    def set_segment(self, segment):
        self.segments.append(segment)
        # print 'set ', segment
        
    def drop_segment(self):
        if len(self.segments) > 0:
            print 'B: ', self.segments
            self.segments.popleft()
            print 'A: ', self.segments

    def draw(self):
        # print 'drawin'
        # if len(self.segments) > 0:
        #     print '>>>>'
        #     for segment in self.segments:
        #         print str(segment)
        noFill()
        self.tile.drawFunction(self.x_pos, self.y_pos, self.size, self.scale, self.segments)
        

        
    def __str__(self):
        return str(self.tile)
    
    def set(self, newTile):
        self.tile = newTile


class Tile1:
    def __init__(self):
        self.type = "t1"

    def __str__(self):
        return "T1"
          
    def __hash__(self):
        return hash((self.type))

    def __eq__(self, other):
        return (self.type) == (other.type)
    
    def exit_direction(self, enter_dir):
        exits = {
                north: west,
                east:  south,
                south: east,
                west:  north
                }
        return exits[enter_dir]
        
    def draw_f_1(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_west_2_north_curve(x, y, size, scale)
    def draw_f_2(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_south_2_east_curve(x, y, size, scale)
    def draw_f_3(self, x, y, size, scale):
        set_light(2 * scale)
        return make_south_2_east_curve(x, y, size, scale)
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        return make_west_2_north_curve(x, y, size, scale)
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x1'
        # print ': ' + str(self) + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_1(x_loc, y_loc, size, scale)
        
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        
        for segment in segments:
            make_worm(segment, x_loc, y_loc, size, scale)

tile_1 = Tile1()

class Tile2:
    def __init__(self):
        self.type = "t2"

    def __str__(self):
        return "T2"
    
    def exit_direction(self, enter_dir):
        exits = {
                north: east,
                east:  north,
                south: west,
                west:  south
                }
        return exits[enter_dir]
         
    def draw_f_1(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_east_2_north_curve(x, y, size, scale)
    def draw_f_2(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_south_2_west_curve(x, y, size, scale)
    def draw_f_3(self, x, y, size, scale):
        set_light(2 * scale)
        return make_south_2_west_curve(x, y, size, scale)
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        return make_east_2_north_curve(x, y, size, scale)
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x2'
        # print ': ' + str(self) + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_1(x_loc, y_loc, size, scale)
        
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        
        for segment in segments:
            make_worm(segment, x_loc, y_loc, size, scale)

tile_2 = Tile2()

class Tile3:
    def __init__(self):
        self.type = "t3"

    def __str__(self):
        return "T3"

    def exit_direction(self, enter_dir):
        exits = {
                north: south,
                east:  west,
                south: north,
                west:  east
                }
        return exits[enter_dir]
     
    def draw_f_1(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_h_line(x, y, size, scale)
    def draw_f_2(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_v_line(x, y, size, scale)
    def draw_f_3(self, x, y, size, scale):
        set_light(2 * scale)
        return make_v_line(x, y, size, scale)
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        return make_h_line(x, y, size, scale)
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x3'
        # print ': ' + self + segments
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_1(x_loc, y_loc, size, scale)
        
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        
        for segment in segments:
            make_worm(segment, x_loc, y_loc, size, scale)
tile_3 = Tile3()

class TileT:
    def __init__(self):
        self.type = "tt"
        self.south_north = None
        self.west_east   = None
        rand = random(1)
        if rand < .25:
            self.south_north = north
            self.west_east   = west
        elif rand < .55:
            self.south_north = north
            self.west_east   = east
        elif rand < .75:
            self.south_north = south
            self.west_east   = west
        else:
            self.south_north = south
            self.west_east   = east
        

    def __str__(self):
        return "T4"
    
    def exit_direction(self, enter_dir):
        exits = {
                north: self.west_east,
                east:  self.south_north,
                south: self.west_east,
                west:  self.south_north
                }
        return exits[enter_dir]
    
    def draw_f_1(self, x, y, size, scale):
        ran = random(1)
        if ran < 0.25:
            fill(255)
        elif ran < 0.5:
            fill(0,255,0)
        elif ran < 0.75:
            fill(255,0,0)
        else: col = fill(0,0,255)
        # noStroke()
        half = size / 2
        ellipse(x + half, y + half, half/4, half/4)
        noFill()
        set_dark(4 * scale)
        # f1, g1 = make_west_2_north_curve(x, y, size, scale) # west to north
        # f2, g2 = make_east_2_north_curve(x, y, size, scale) # east to north
        n1 = lambda g: g
        return n1, n1
    def draw_f_2(self, x, y, size, scale):
        set_dark(4 * scale)
        # f1, g1 = make_south_2_east_curve(x, y, size, scale) # south to east
        f2, g2 = make_south_2_west_curve(x, y, size, scale) # south to west
        n1 = lambda g: g
        return n1, n1
    def draw_f_3(self, x, y, size, scale):
        set_light(2 * scale)
        # f1, g1 = make_south_2_east_curve(x, y, size, scale)
        # f2, g2 = make_south_2_west_curve(x, y, size, scale)
        n1 = lambda g: g
        return n1, n1
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        # f1, g1 = make_west_2_north_curve(x, y, size, scale)
        # f2, g2 = make_east_2_north_curve(x, y, size, scale)
        n1 = lambda g: g
        return n1, n1
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'xT'
        # print ': ' + str(self)
        # print ': ' + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        
        self.draw_f_1(x_loc, y_loc, size, scale)
        
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        for segment in segments:
            make_worm(segment, x_loc, y_loc, size, scale)
tile_t = TileT()

class Tile4:
    def __init__(self):
        self.type = "t4"
        self.south_north = None
        self.west_east   = None
        rand = random(1)
        if rand < .25:
            self.south_north = north
            self.west_east   = west
        elif rand < .55:
            self.south_north = north
            self.west_east   = east
        elif rand < .75:
            self.south_north = south
            self.west_east   = west
        else:
            self.south_north = south
            self.west_east   = east
        

    def __str__(self):
        return "T4"
    
    def exit_direction(self, enter_dir):
        exits = {
                north: self.west_east,
                east:  self.south_north,
                south: self.west_east,
                west:  self.south_north
                }
        return exits[enter_dir]
    
    def draw_f_1(self, x, y, size, scale):
        ran = random(1)
        if ran < 0.25:
            fill(255)
        elif ran < 0.5:
            fill(0,255,0)
        elif ran < 0.75:
            fill(255,0,0)
        else: col = fill(0,0,255)
        # noStroke()
        half = size / 2
        ellipse(x + half, y + half, half/4, half/4)
        noFill()
        set_dark(4 * scale)
        f1, g1 = make_west_2_north_curve(x, y, size, scale)
        f2, g2 = make_east_2_north_curve(x, y, size, scale)
        return f1, f2
    def draw_f_2(self, x, y, size, scale):
        set_dark(4 * scale)
        f1, g1 = make_south_2_east_curve(x, y, size, scale)
        f2, g2 = make_south_2_west_curve(x, y, size, scale)
        return f1, f2
    def draw_f_3(self, x, y, size, scale):
        set_light(2 * scale)
        f1, g1 = make_south_2_east_curve(x, y, size, scale)
        f2, g2 = make_south_2_west_curve(x, y, size, scale)
        return f1, f2
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        f1, g1 = make_west_2_north_curve(x, y, size, scale)
        f2, g2 = make_east_2_north_curve(x, y, size, scale)
        return f1, f2
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x4'
        # print ': ' + str(self) + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        
        self.draw_f_1(x_loc, y_loc, size, scale)
        
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        for segment in segments:
            make_worm(segment, x_loc, y_loc, size, scale)
tile_4 = Tile4()

class Tile5:
    def __init__(self):
        self.type = "t5"

    def __str__(self):
        return "T5"
    
    def exit_direction(self, enter_dir):
        exits = {
                north: south,
                east:  west,
                south: north,
                west:  east
                }
        return exits[enter_dir]
    
    def exit_direction(self, enter_dir):
        exits = {
                north: south,
                east:  west,
                south: north,
                west:  east
                }
        return exits[enter_dir]

    def draw_f_1(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_v_line(x, y, size, scale)
    def draw_f_2(self, x, y, size, scale):
        set_light(2 * scale)
        return make_v_line(x, y, size, scale)
    def draw_f_3(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_h_line(x, y, size, scale)
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        return make_h_line(x, y, size, scale)
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x5'
        # print ': ' + str(self) + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_1(x_loc, y_loc, size, scale)
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        for segment in segments:
            enter_direction = segment.enter_direction
            exit_direction = segment.exit_direction
            if segment.type != None:
                if segment.enter_direction == south or enter_direction == north:
                    stroke(11,14,211, 160)
                    strokeWeight(2.6)
                    make_v_line(x_loc, y_loc, size, scale, segment.orientation, segment.percentage, segment.enter_direction)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        # make_worm(segment, x_loc, y_loc, size, scale)
        for segment in segments:
            if segment.type != None:
                if segment.enter_direction == east or segment.enter_direction == west:
                    stroke(11,14,211, 160)
                    strokeWeight(2.6)
                    make_h_line(x_loc, y_loc, size, scale, segment.orientation, segment.percentage, segment.enter_direction)
tile_5 = Tile5()

class Tile6:
    def __init__(self):
        self.type = "t6"

    def __str__(self):
        return "T6"
    
    def exit_direction(self, enter_dir):
        exits = {
                north: south,
                east:  west,
                south: north,
                west:  east
                }
        return exits[enter_dir]
    
    def exit_direction(self, enter_dir):
        exits = {
                north: south,
                east:  west,
                south: north,
                west:  east
                }
        return exits[enter_dir]
        
    def draw_f_1(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_h_line(x, y, size, scale)
    def draw_f_2(self, x, y, size, scale):
        set_light(2 * scale)
        return make_h_line(x, y, size, scale)
    def draw_f_3(self, x, y, size, scale):
        set_dark(4 * scale)
        return make_v_line(x, y, size, scale)
    def draw_f_4(self, x, y, size, scale):
        set_light(2 * scale)
        return make_v_line(x, y, size, scale)
    def drawFunction(self, x_loc, y_loc, size, scale, segments):
        # print 'x6'
        # print ': ' + str(self) + str(segments)
        noFill()
        strokeCap(SQUARE)
        
        f, g = self.draw_f_1(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_1(x_loc, y_loc, size, scale)
        self.draw_f_2(x_loc, y_loc, size, scale)
        
        for segment in segments:
            if segment.type != None:
                if segment.enter_direction == east or segment.enter_direction == west:
                    stroke(11,14,211, 160)
                    strokeWeight(2.6)
                    make_h_line(x_loc, y_loc, size, scale, segment.orientation, segment.percentage, segment.enter_direction)
        
        f, g = self.draw_f_3(x_loc, y_loc, size, scale)
        make_gradient(f, g)
        self.draw_f_3(x_loc, y_loc, size, scale)
        
        self.draw_f_4(x_loc, y_loc, size, scale)
        # make_worm(segment, x_loc, y_loc, size, scale)
        for segment in segments:
            if segment.type != None:
                if segment.enter_direction == north or segment.enter_direction == south:
                    stroke(11,14,211, 160)
                    strokeWeight(2.6)
                    make_v_line(x_loc, y_loc, size, scale, segment.orientation, segment.percentage, segment.enter_direction)
tile_6 = Tile6()

def make_h_line(x, y, size, scale, orientation = None, percentage = None, enter_direction = None):
    x1, y1, x2, y2 = line_args_h(x, y, size, scale, orientation, percentage, enter_direction)
    line(x1, y1, x2, y2)
    f = lambda g: line(x1, y1 + g, x2, y2 + g)
    g = lambda g: line(x1, y1 - g, x2, y2 - g)
    return f, g
def make_v_line(x, y, size, scale, orientation = None, percentage = None, enter_direction = None):
    x1, y1, x2, y2 = line_args_v(x, y, size, scale, orientation, percentage, enter_direction)
    line(x1, y1, x2, y2)
    f = lambda g: line(x1 + g, y1, x2 + g, y2)
    g = lambda g: line(x1 - g, y1, x2 - g, y2)
    return f, g
def line_args_h(x, y, size, scale, orientation = None, percentage = None, enter_direction = None):
    if orientation == None:
        return (x, y+(size/2), x+(size), y+(size/2))
    elif orientation == tail:
        if enter_direction == east:
            return (x, y+(size/2), x+(size)-(size*percentage), y+(size/2))
        elif enter_direction == west:
            return (x+(size*percentage), y+(size/2), x+(size), y+(size/2))
    elif orientation == head:
        if enter_direction == east:
            return (x+(size)-(size*percentage), y+(size/2), x+(size), y+(size/2))
        elif enter_direction == west:
            return (x, y+(size/2), x+(size*percentage), y+(size/2))
    
def line_args_v(x, y, size, scale, orientation = None, percentage = None, enter_direction = None):
    if orientation == None:
        return (x+(size/2), y, x+(size/2), y+(size))
    elif orientation == tail:
        if enter_direction == south:
            return (x+(size/2), y, x+(size/2), y+(size)-(size*percentage))
        elif enter_direction == north:
            return (x+(size/2), y+(size*percentage), x+(size/2), y+(size))
    elif orientation == head:
        if enter_direction == south:
            return (x+(size/2), y+(size)-(size*percentage), x+(size/2), y+(size))
        elif enter_direction == north:
            return (x+(size/2), y, x+(size/2), y+(size*percentage))


def make_worm(segment, x, y, size, scale):
    if segment.type == None: return
    percentage = segment.percentage
    orientation = segment.orientation
    enter_direction = segment.enter_direction
    exit_direction  = segment.exit_direction
    stroke(11,14,211, 160)
    strokeWeight(2.6)
    if enter_direction == north:
        if exit_direction == east:
            make_north_2_east_curve(x, y, size, scale, orientation, percentage)
        elif exit_direction == west:
            make_north_2_west_curve(x, y, size, scale, orientation, percentage)
    elif enter_direction == east:
        if exit_direction == north:
            make_east_2_north_curve(x, y, size, scale, orientation, percentage)
        elif exit_direction == south:
            make_east_2_south_curve(x, y, size, scale, orientation, percentage)
    elif enter_direction == south:
        if exit_direction == east:
            make_south_2_east_curve(x, y, size, scale, orientation, percentage)
        elif exit_direction == west:
            make_south_2_west_curve(x, y, size, scale, orientation, percentage)
    elif enter_direction == west:
        if exit_direction == north:
            make_west_2_north_curve(x, y, size, scale, orientation, percentage)
        elif exit_direction == south:
            make_west_2_south_curve(x, y, size, scale, orientation, percentage)
    
def make_curve(x, y, size, scale, curve_args, orientation = None, percentage = None):
    ellipseMode(RADIUS)
    (x, y, w, h, r1, r2) = curve_args(x, y, size, scale, orientation, percentage) 
    arc(x, y, w, h, r1, r2)
    f = lambda g: arc(x, y, w - g, h - g, r1, r2)
    g = lambda g: arc(x, y, w + g, h + g, r1, r2)
    return f, g

def make_west_2_north_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, west_2_north_args, orientation, percentage)
def make_north_2_west_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, north_2_west_args, orientation, percentage)
    
def make_south_2_east_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, south_2_east_args, orientation, percentage)    
def make_east_2_south_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, east_2_south_args, orientation, percentage)
    
def make_east_2_north_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, east_2_north_args, orientation, percentage)    
def make_north_2_east_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, north_2_east_args, orientation, percentage)
    
def make_south_2_west_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, south_2_west_args, orientation, percentage)    
def make_west_2_south_curve(x, y, size, scale, orientation = None, percentage = None):
    return make_curve(x, y, size, scale, west_2_south_args, orientation, percentage)
    
# west / north
def west_2_north_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == None:
        return (x, y, size/2 , size/2, 0, HALF_PI)
    elif orientation == tail:
        return (x, y, size/2 , size/2, 0, HALF_PI-(HALF_PI*percentage))
    elif orientation == head:
        return (x, y, size/2 , size/2, HALF_PI-(HALF_PI*percentage), HALF_PI)
def north_2_west_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == tail:
        return (x, y, size/2 , size/2, HALF_PI * percentage, HALF_PI)
    elif orientation == head:
        return (x, y, size/2 , size/2, 0, HALF_PI-(HALF_PI-(HALF_PI * percentage)))
    
# south / east
def south_2_east_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == None:
        return (size+x, size+y, size/2, size/2, PI, PI+HALF_PI)
    elif orientation == tail:
        return (size+x, size+y, size/2, size/2, PI+(HALF_PI*percentage), PI+HALF_PI)
    elif orientation == head:
        return (size+x, size+y, size/2, size/2, PI, PI+(HALF_PI*percentage))
def east_2_south_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == tail:
        return (size+x, size+y, size/2, size/2, PI, PI+HALF_PI-(HALF_PI*percentage))
    elif orientation == head:
        return (size+x, size+y, size/2, size/2, PI+(HALF_PI-(HALF_PI*percentage)), PI+HALF_PI)
    
# east / north
def east_2_north_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == None:
        return (x+size, y, size/2 , size/2, HALF_PI, PI)
    elif orientation == tail:
        return (x+size, y, size/2 , size/2, HALF_PI+(HALF_PI * percentage), PI)
    elif orientation == head:
        return (x+size, y, size/2 , size/2, HALF_PI, PI-(HALF_PI-(HALF_PI*percentage)))
def north_2_east_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == tail:
        return (x+size, y, size/2 , size/2, HALF_PI, PI-(HALF_PI*percentage))
    elif orientation == head:
        return (x+size, y, size/2 , size/2, HALF_PI+(HALF_PI-(HALF_PI*percentage)), PI)
    
# south / west
def south_2_west_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == None:
        return (x, size+y, size/2, size/2, PI+HALF_PI, TAU)
    elif orientation == tail:
        return (x, size+y, size/2, size/2, PI+HALF_PI, TAU-(HALF_PI*percentage))
    elif orientation == head:
        return (x, size+y, size/2, size/2, PI+HALF_PI+(HALF_PI-(HALF_PI*percentage)), TAU)
def west_2_south_args(x, y, size, scale, orientation = None, percentage = None):
    if orientation == tail:
        return (x, size+y, size/2, size/2, PI+HALF_PI+(HALF_PI*percentage), TAU)
    elif orientation == head:
        return (x, size+y, size/2, size/2, PI+HALF_PI, PI+HALF_PI+(HALF_PI*percentage))
    

def set_dark(w):
    stroke(0)
    strokeWeight(w)
def set_light(w):
    stroke(255)
    strokeWeight(w)

def make_gradient(f, g):
    strokeWeight(8)
    gradient(f)
    gradient(g)

def gradient(f, a = 220):
  noFill()
  strokeWeight(3)
  radius = 5
  # r = radius
  rate = .7
  
  # while r < 15:
  for r in range(radius, 24, 2):
    r += 1
    cp = color(0, a)
    stroke(cp)
    f(r)
    a *= rate

def drange(st, en, step):
    count = st
    rng = [st]
    while count < en:
        count += step
        rng.append(count)
    return rng


    
        
   