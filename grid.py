from tiles import *
from ball import *

class Grid:
    def __init__(self, rs, cs, sc, sz, dir = west):
        self.clock = 0
        self.incr  = 0.2
        
        self.row_size = rs
        self.col_size = cs
        
        self.scale = sc
        self.size  = sz
        
        self.rows = []
        for row in range(0, self.row_size):
            idy = row + 1
            row = self.make_row(idy)
            self.rows.append(row)
        
        self.ready = True
        
        self.setup_segments()

    def increment_clock(self):
        self.clock += 1
        
        # print self.segment.percentage, self.next_segment.percentage
        self.advance_segments()
        
        
        if self.clock % 10 == 0:
            self.cycle()

    def advance_segments(self):
        self.segment.advance()
        self.next_segment.advance()
        return True
        

    def setup_segments(self):
        self.x_pos = 2
        self.y_pos = 2
        rand = random(1)
        if rand < .25:
            self.enter_direction = west
        elif rand < .5:
            self.enter_direction = east
        elif rand < .75:
            self.enter_direction = north
        else: self.enter_direction = south
        
        current_tile   = self.lookup_tile(self.y_pos, self.x_pos)
        exit_direction = current_tile.tile.exit_direction(self.enter_direction)
        self.segment   = Segment(tail, 0.0, self.enter_direction, exit_direction)

        (next_x, next_y), next_enter = self.next_location_enter_direction(exit_direction)
        self.next_x_pos              = next_x
        self.next_y_pos              = next_y
        self.next_enter_direction    = next_enter
        
        next_tile           = self.lookup_tile(self.next_y_pos, self.next_x_pos)
        next_exit_direction = next_tile.tile.exit_direction(self.next_enter_direction)
        self.next_segment   = Segment(head, 0.0, self.next_enter_direction, next_exit_direction)
        
    def lookup_tile(self, y_pos, x_pos):
        return self.rows[self.y_pos][self.x_pos]
    
    def lookup_next_location(self, x, y, exit_direction):
        stay = False
        x_pos = x
        y_pos = y
        # print 'lookup next location ', exit_direction, x_pos, y_pos
        if exit_direction == north:
            if y == 1:
                # stay = True
                y_pos = self.col_size
            else:
                y_pos -= 1
        elif exit_direction == east:
            if x == self.row_size:
                # stay = True
                x_pos = 1
            else:
                x_pos += 1
        elif exit_direction == south:
            if y == self.col_size:
                # stay = True
                y_pos = 1
            else:
                y_pos += 1
        elif exit_direction == west:
            if x == 1:
                # stay = True
                x_pos = self.row_size
            else:
                x_pos -= 1
        # print 'lookup output ', stay, x_pos, y_pos
        return (x_pos, y_pos), stay

    def next_location_enter_direction(self, exit_direction):
        
        next_enter_direction = None
        # print
        # print 'current_tile ', current_tile
        # print 'exit ', exit_direction
        (x_next, y_next), stay = self.lookup_next_location(self.x_pos, self.y_pos, exit_direction)
        # print 'after lookup ', x_next, y_next, stay
        # if not stay:
            # print 'not stay', exit_direction
            # next_enter_direction = exit_direction.enter()
            # print 'next enter ', next_enter_direction
        # else: next_enter_direction = exit_direction
        next_enter_direction = exit_direction.enter()
        # print 'next_loc ', x_next, y_next, next_enter_direction
        # print
        return (x_next, y_next), next_enter_direction
    def cycle(self):
                        
        self.set()
        
        rand = int(random(1,6))
        tile = self.random_tile(rand)
        
        self.x_pos = self.next_x_pos
        self.y_pos = self.next_y_pos
        self.enter_direction = self.next_enter_direction
        
        current_tile   = self.rows[self.y_pos-1][self.x_pos-1]
        exit_direction = current_tile.tile.exit_direction(self.enter_direction)
        self.segment   = Segment(tail, 0.0, self.enter_direction, exit_direction)

        (next_x, next_y), next_enter = self.next_location_enter_direction(exit_direction)
        self.next_x_pos = next_x
        self.next_y_pos = next_y
        self.next_enter_direction = next_enter
        
        next_tile           = self.rows[self.next_y_pos-1][self.next_x_pos-1]
        next_exit_direction = next_tile.tile.exit_direction(self.next_enter_direction)
        self.next_segment   = Segment(head, 0.0, self.next_enter_direction, next_exit_direction)
    
    def make_row(self, idy):
        row = []
        for idx in range(1,self.col_size+1):
            # print idx
            rand = int(random(1,6))
            row.append(self.tile(rand,idx, idy))
        return row
    
    def tile(self,rand,idx, idy):
        sz = self.size
        sc = self.scale
        return Tile(no_segment, self.random_genesis(rand), idx*sz, idy*sz, sz, sc)
    
    def draw_grid(self):
        for row_idx in range(0, self.row_size):
            for col_idx in range(0, self.col_size):
                tile = self.rows[row_idx][col_idx]
                if row_idx == self.y_pos - 1 and col_idx == self.x_pos - 1:
                    tile.draw(self.segment)
                elif row_idx == self.next_y_pos - 1 and col_idx == self.next_x_pos - 1:
                    tile.draw(self.next_segment)
                else: tile.draw()
    
    def access(self, x, y):
        row = self.rows[y]
        return row[x]

    
    def change_pos(self, x, y):
        if x > 0 and x <= self.row_size and y > 0 and y <= self.col_size:
            if x != self.x_pos or y != self.y_pos:
                # print 'ready'
                self.ready = True
                self.x_pos = x
                self.y_pos = y
    
    def set(self):
        # print self.ready
        if self.ready:
            rand = int(random(1,6))
            tile = self.random_tile(rand)
            existing = self.rows[self.y_pos-1][self.x_pos-1]
            while str(existing) == str(tile):
                rand = int(random(1,8))
                tile = self.random_tile(rand)
            self.rows[self.y_pos-1][self.x_pos-1].set(tile)
            # print 'not ready'
            # self.ready = False
    
    def set_tile(self, tile):
        self.rows[self.y_pos-1][self.x_pos-1].set(tile)
            
    def random_tile(self, rand):
        if rand==1:
            return tile_1
        elif rand==2:
            return tile_2
        # elif rand==3:
        #     return tile_3
        elif rand==4:
            return tile_4
        elif rand==5:
            return tile_5
        elif rand==6:
            return tile_6
        elif rand < 3:
            return tile_1
        else:
            return tile_2
        # else:
        #     return tile_6
    def random_genesis(self, rand):
        # if rand==1:
        #     return Tile1()
        # elif rand==2:
        #     return Tile2()
        # elif rand==3:
        #     return Tile3()
        # elif rand==4:
        #     return Tile4()
        # elif rand==5:
        #     return Tile5()
        # elif rand==6:
        #     return Tile6()
        # elif rand < 3:
        #     return Tile1()
        # else:
        #     return Tile2()
        # else:
        #     return Tile1()
        return tile_6
        
    def set_abunch(self):
        if self.ready and self.x_pos <= self.row_size - 1 and self.y_pos <= self.col_size - 1:
            for x in range(0,2):
                for y in range(0,2):
                    rand = int(random(1,8))
                    tile = self.random_tile(rand)
                    self.rows[self.y_pos-1+y][self.x_pos-1+x].set(tile)
                    self.ready = False
        
        
        
        
        
        
    