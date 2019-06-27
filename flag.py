# Code by CW Coleman
# Base project format.
# 127.0.0.1 is locahost (the computer you are working on)
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

mc = Minecraft.create("127.0.0.1", 4711)
# This sets the x,y and z location to set blocks.
x, y, z = mc.player.getPos()        

# Clear with ait (air = 0)
air = 0
mc.setBlocks(x-15,y, z-15, x+15, y+20, z+15,air)
# b is a variable for the type of block
# create single blocks

# Create multiple blocks .  
# Notice 'w = 35,2' .  This is wool.

t = 50
d = 57
s = 1
g = 41
gg = 35,5
l = 22
c = 4
r = 35,14
ggg = 35,13
mc.setBlocks(x,y,z,x,y,z,t)
#Letter S
mc.setBlocks(x+10  ,y+1  ,z-5  ,x+10  ,y+1  ,z-3  ,d )
mc.setBlocks(x+10  ,y+3  ,z-3  ,x+10  ,y+1  ,z-3  ,d )
mc.setBlocks(x+10  ,y+3  ,z-3  ,x+10  ,y+3  ,z-5  ,d )
mc.setBlocks(x+10  ,y+3  ,z-5  ,x+10  ,y+5  ,z-5  ,d )
mc.setBlocks(x+10  ,y+5  ,z-5  ,x+10  ,y+5  ,z-3  ,d )
#Letter E
mc.setBlocks(x+10  ,y+1  ,z-1  ,x+10  ,y+1  ,z+1  ,g )
mc.setBlocks(x+10  ,y+5  ,z-1  ,x+10  ,y+5  ,z+1  ,g )
mc.setBlocks(x+10  ,y+3  ,z-1  ,x+10 ,y+3  ,z+0  ,g )
mc.setBlocks(x+10  ,y+1  ,z-1  ,x+10  ,y+5  ,z-1  ,g )
#Letter G

mc.setBlocks(x+10  ,y+1  ,z+3  ,x+10  ,y+1  ,z+6  ,l )
mc.setBlocks(x+10  ,y+3  ,z+6  ,x+10  ,y+1  ,z+6  ,l )
mc.setBlocks(x+10  ,y+3  ,z+5  ,x+10  ,y+3  ,z+5  ,l )
mc.setBlocks(x+10  ,y+1  ,z+3  ,x+10  ,y+5  ,z+3  ,l )
mc.setBlocks(x+10  ,y+5  ,z+3  ,x+10  ,y+5  ,z+6  ,l )

#behind text

mc.setBlocks(x+11  ,y+6  ,z-6  ,x+11  ,y+0  ,z-3  ,r )
mc.setBlocks(x+11  ,y+6  ,z-2  ,x+11  ,y+0  ,z+2  ,gg )
mc.setBlocks(x+11  ,y+6  ,z+3  ,x+11  ,y+0  ,z+7  ,ggg )

'''
mc.setBlocks(x+  ,y+  ,z-  ,x+  ,y+  ,z+  ,a )
'''




mc.setBlocks(x+15,y-1, z+15, x-15, y-1, z-15,c)

# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""
