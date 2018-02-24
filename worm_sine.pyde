from grid import *
from ball import *

def boundry(x, y, size, scl):
        stroke(0)
        strokeWeight(1)
        rectMode(CORNER)
        rect(0 + x, 0 + y, size * scl, size * scl)


def setup():
    background(200)
    # noCursor()
    global rs, cs, sz, sc, mod, grid
    size(450,450,P2D)
    # size(500,500)
    smooth(8)
    frameRate(1000)
    
    rs = 5
    cs = 5
    sz = 64
    sc = 4.5
    
    mod = sz

    grid = Grid(rs,cs,sc,sz)
    
    tc = Tile(tile_t, 250, 250, sz, sc)
    tc.draw()
    
    tile = tc.tile
    # print tile.exit_direction(north)
    #
    
    
    
    # print 'enter ', grid.enter_direction
    # print grid.x_pos, grid.y_pos
    # print
    # print 'next enter ', grid.next_enter_direction
    # print grid.next_x_pos, grid.next_y_pos
    # grid.draw_grid()
    print no_worm.type
    print simple_worm.type


        
    
    
clock = 0
def draw():
    global clock
    background(200)
    # fill(200,60)
    # rect(0,0,500,500)
    global mod, grid
    grid.increment_clock()
    
    # x = mouseX / mod
    # y = mouseY / mod
    # grid.change_pos(x,y)
    # grid.set()
    grid.draw_grid()