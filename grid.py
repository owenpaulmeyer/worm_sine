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
        
        # self.setup_segments()
        self.worm = Worm(self, 2, 2)

    def increment_clock(self):
        self.clock += 1
        
        self.worm.advance_segments()
        
        if self.clock % 10 == 0:
            self.worm.cycle()

        

        
    def lookup_tile(self, y_pos, x_pos):
        tile = self.rows[y_pos-1][x_pos-1]
        return tile


    def make_row(self, idy):
        row = []
        for idx in range(1,self.col_size+1):
            rand = int(random(1,6))
            row.append(self.tile(rand,idx, idy))
        return row
    
    def tile(self,rand,idx, idy):
        sz = self.size
        sc = self.scale
        return Tile(self.random_genesis(rand), idx*sz, idy*sz, sz, sc)
    
    def draw_grid(self):
        for row_idx in range(0, self.row_size):
            for col_idx in range(0, self.col_size):
                tile = self.rows[row_idx][col_idx]
                tile.draw()
    
    def access(self, x, y):
        row = self.rows[y]
        return row[x]

    
    def change_pos(self, x, y):
        if x > 0 and x <= self.row_size and y > 0 and y <= self.col_size:
            if x != self.x_pos or y != self.y_pos:
                self.ready = True
                self.x_pos = x
                self.y_pos = y
    
    def set(self, y_pos, x_pos):
        if self.ready:
            rand = int(random(1,6))
            tile = self.random_tile(rand)
            existing = self.rows[y_pos-1][x_pos-1]
            while str(existing) == str(tile):
                rand = int(random(1,8))
                tile = self.random_tile(rand)
            self.rows[y_pos-1][x_pos-1].set(tile)
    
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
        
        
        
        
        
        
    