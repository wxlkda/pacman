import pygame, sys
from pygame.locals import *
import random

vector = pygame.math.Vector2 #intialize a vector to handle most movement/position of things in this game

WINDOW_SIZE = WIDTH, HEIGHT = (784,1023) #set the window size/ height and width of the game
TITLE = "Pacman" #set the game title
FPS = 60 #set the current FPS to portray the game at
PLAYER_START = (13,26) #set the grid position of pacman

#intialize maze layout. Yes this was generated myself. Took some time
MAZE_LAYOUT = \
[
['2', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '44', '43', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '11', '1'],
['4', 'd2', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd2', '3'],
['4', 'd1', '40', '15', '15', '39', 'd1', '40', '15', '15', '15', '39', 'd1', '26', '25', 'd1', '40', '15', '15', '15', '39', 'd1', '40', '15', '15', '39', 'd1', '3'],
['4', 'd1', '26', '0', '0', '25', 'd1', '26', '0', '0', '0', '25', 'd1', '26', '25', 'd1', '26', '0', '0', '0', '25', 'd1', '26', '0', '0', '25', 'd1', '3'],
['4', 'd1', '28', '21', '21', '27', 'd1', '28', '21', '21', '21', '27', 'd1', '28', '27', 'd1', '28', '21', '21', '21', '27', 'd1', '28', '21', '21', '27', 'd1', '3'],
['4', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '3'],
['4', 'd1', '40', '15', '15', '39', 'd1', '40', '39', 'd1', '40', '15', '15', '15', '15', '15', '15', '39', 'd1', '40', '39', 'd1', '40', '15', '15', '39', 'd1', '3'],
['4', 'd1', '28', '21', '21', '27', 'd1', '26', '25', 'd1', '28', '21', '21', '39', '40', '21', '21', '27', 'd1', '26', '25', 'd1', '28', '21', '21', '27', 'd1', '3'],
['4', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '3'],
['6', '13', '13', '13', '13', '23', 'd1', '26', '37', '15', '15', '39', '0', '26', '25', '0', '40', '21', '21', '27', '25', 'd1', '24', '13', '13', '13', '13', '5'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '35', '22', '21', '27', '0', '28', '27', '0', '28', '21', '21', '39', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '25', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '26', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '25', '0', '30', '13', '13', '0', '0', '13', '13', '29', '0', '26', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['12', '12', '12', '12', '12', '27', 'd1', '28', '27', '0', '3', '0', '0', '0', '0', '0', '0', '4', '0', '28', '27', 'd1', '28', '12', '12', '12', '12', '12'],
['0', '0', '0', '0', '0', '0', 'd1', '0', '0', '0', '3', '0', '0', '0', '0', '0', '0', '4', '0', '0', '0', 'd1', '0', '0', '0', '0', '0', '0'],
['13', '13', '13', '13', '13', '23', 'd1', '40', '39', '0', '3', '0', '0', '0', '0', '0', '0', '4', '0', '40', '39', 'd1', '24', '13', '13', '13', '13', '13'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '25', '0', '32', '12', '11', '11', '11', '11', '11', '31', '0', '26', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '25', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '26', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '4', 'd1', '26', '25', '0', '40', '15', '15', '15', '15', '15', '15', '39', '0', '26', '25', 'd1', '3', '0', '0', '0', '0', '0'],
['2', '12', '12', '12', '12', '27', 'd1', '28', '27', '0', '28', '21', '21', '39', '40', '21', '21', '27', '0', '28', '27', 'd1', '28', '12', '12', '12', '12', '1'],
['4', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '3'],
['4', 'd1', '40', '15', '15', '39', 'd1', '40', '15', '15', '15', '39', 'd1', '26', '25', 'd1', '40', '15', '15', '15', '39', 'd1', '40', '15', '15', '39', 'd1', '3'],
['4', 'd1', '28', '21', '39', '25', 'd1', '28', '21', '21', '21', '27', 'd1', '28', '27', 'd1', '28', '21', '21', '21', '27', 'd1', '26', '40', '21', '27', 'd1', '3'],
['4', 'd1', 'd1', 'd1', '25', '25', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '0', '0', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', '3'],
['8', '15', '39', 'd1', '25', '25', 'd1', '40', '39', 'd1', '40', '15', '15', '15', '15', '15', '15', '39', 'd1', '40', '39', 'd1', '26', '25', 'd1', '40', '15', '7'],
['10', '21', '27', 'd1', '28', '27', 'd1', '26', '25', 'd1', '28', '21', '21', '39', '40', '21', '21', '27', 'd1', '26', '25', 'd1', '28', '27', 'd1', '28', '21', '9'],
['4', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', '26', '25', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', '3'],
['4', 'd1', '40', '15', '15', '15', '15', '38', '37', '15', '15', '39', 'd1', '26', '25', 'd1', '40', '15', '15', '38', '37', '15', '15', '15', '15', '39', 'd1', '3'],
['4', 'd1', '28', '21', '21', '21', '21', '21', '21', '21', '21', '27', 'd1', '28', '27', 'd1', '28', '21', '21', '21', '21', '21', '21', '21', '21', '27', 'd1', '3'],
['4', 'd2', 'd1', 'd1', 'd1', 'd1', 'd1 ', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd1', 'd2', '3'],
['6', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '13', '5']
]

#initialize the Helper class, which contains methods that are used to help in the making of this game (such as drawing text, drawing the maze, etc)
class Helper:
    def __init__(self):
        pass #dont need to past anything into the constructor

    def draw_text(self, font, size, text, color, xpos, ypos): #method to render text on the screen
        font = pygame.font.Font(font,size) #initialize the font object
        text = font.render(text, True, color) #render the fonder in pygame, returns a text object
        textRect = text.get_rect() #get the rect of the text object
        textRect.center = (xpos, ypos) #center the rect given the x and y position passed into the params
        self.screen.blit(text, textRect) #display the text on the screen


    def draw_maze(self): #method to draw the maze given a 2d array
        TILE_SIZE = 28 #initialize the tile size, which is a square
        for y, row in enumerate(MAZE_LAYOUT): #nexted for loop to draw the maze
            y += 3 #add an offset by units down to add an area for the score/time
            for x, tile in enumerate(row): #
                image = None #set the Image used to render each tile as None, for now
                if tile[0] != 'd': #if not a dot #while iterating through the 2d array, if the current tile does not start with a 'd', meaning it's a dot
                    if int(tile) % 2 == 0 and int(tile) != 0: #if the tile is not a black tile (background tile) or if the tile number is even
                        image = pygame.transform.flip(pygame.image.load(f"Maze Grid/maze_{int(tile) - 1}.png"), True, False) #it finds the file in the given directory, and flips it vertically
                    else:
                        image = pygame.image.load(f"Maze Grid/maze_{int(tile)}.png") #else it renders the same thing, but non flipped. The reason I did this flip thing was because I was too lazy to make 49 more sprites for the tiles

                elif tile[0] == 'd': #if it is a dot tile
                    image = pygame.image.load(f"Dot/dot_{tile[1]}.png") #look into the dots folder, and render the specified dot
                self.screen.blit(pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE)) #blit the current pygame.Image onto the screen



class Pacman: #intialize pacman class. If I had ghosts, I would create an AbstractPlayer class and inherit from there, but i dont
    def __init__(self, pos):
        self.grid_ind = pos #get the grid index of the pacman. Since I rendering the map using 28x28 tiles, I use this variable to keep track of which index/position the pacman is in the 2d array
        self.pos = self.get_pos() #method to get the pixel position
        self.speed = 7 #set the pacman speed
        self.direction = vector(-1,0) #set the default direction to go left (-1 on x axis, 0 on y [in pygame, going down is positive y and going right is positive x])
        self.stored_direction = None #keep track of the stored direction to handle when the pacman can go to the next grid
        self.able_to_move = True #a variable to check if the pacman can move to the next grid/tile
        self.score = '00000' #set the score, which is 0 by default

        #keep track of the animations used to render the pacman, This one is when pacman is facing down
        self.downAnimations = \
        [pygame.transform.scale(pygame.image.load(r"Pacmans/down1.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/down2.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/down3.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/down2.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/down1.png"), (30, 30))]

        self.upAnimations = [pygame.transform.flip(animation, False, True) for animation in self.downAnimations] # flip the down animations horizontally

        #keep track of the animations used to render the pacman, This one is when pacman is facing left
        self.leftAnimations = \
        [pygame.transform.scale(pygame.image.load(r"Pacmans/left_1.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/left_2.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/left_3.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/left_2.png"), (30, 30)),
        pygame.transform.scale(pygame.image.load(r"Pacmans/left_1.png"), (30, 30))]

        self.rightAnimations = [pygame.transform.flip(animation, True, False) for animation in self.leftAnimations] #flip the left animations vertically

        self.leftImage = 0 #keep track of the frame which is going to be used to check which image to redner from the animation list
        self.rightImage = 0
        self.upImage = 0
        self.downImage = 0


    def draw(self, surface): #method to draw the pacman onto the screen
        if self.upImage + 1 >= 9: #reset frame counter if the value exceed 9, or 3 frames
            self.upImage = 0
        if self.downImage + 1 >= 9:#reset frame counter if the value exceed 9, or 3 frames
            self.downImage = 0
        if self.leftImage + 1 >= 9:#reset frame counter if the value exceed 9, or 3 frames
            self.leftImage = 0
        if self.rightImage + 1 >= 9:#reset frame counter if the value exceed 9, or 3 frames
            self.rightImage = 0

        if self.direction == vector(0,-1): #if the current direction that it is facing is up, load the up animations and add 1 to the up counter
            surface.blit(self.upAnimations[self.upImage // 3], (int(self.pos[0]) - 14, int(self.pos[1]) - 14))
            self.upImage += 1

        if self.direction == vector(0,1): #if the current direction that it is facing is down, load the down animations and add 1 to the down counter
            surface.blit(self.downAnimations[self.downImage // 3], (int(self.pos[0]) - 14, int(self.pos[1]) - 14))
            self.downImage += 1

        if self.direction == vector(-1,0): #if the current direction that it is facing is left, load the left animations and add 1 to the left counter
            surface.blit(self.leftAnimations[self.leftImage // 3], (int(self.pos[0]) - 14, int(self.pos[1]) - 14))
            self.leftImage += 1

        if self.direction == vector(1,0): #if the current direction that it is facing is right, load the right animations and add 1 to the right counter
            surface.blit(self.rightAnimations[self.rightImage // 3], (int(self.pos[0]) - 14, int(self.pos[1]) - 14))
            self.rightImage += 1

    def update(self): #update the position of the current player

        if self.able_to_move: #if pacman can move
            self.pos += self.direction * self.speed #multiply the player speed by the direction and add it to the pacman pixel position

        if self.is_center_of_tile(): #if pacman is in the center of a tile
            if self.stored_direction != None: #if the previous/stored direction is not None
                self.direction = self.stored_direction #set the current direction to go in as the stored/previous direction
            self.able_to_move = self.can_move() #check if pacman can move using the method, can_move()

        if int(self.pos[0]) < 0 + 14: #if pacman's x position is less than 0, or pacman is
            self.pos[0] = WIDTH - 14 #make pacman go to the other side
        if int(self.pos[0]) > WIDTH - 14: #if pacman goes off the screen from the right side
            self.pos[0] = 0 + 14 #make it on the right side


        if self.is_center_of_tile(): #if pacman is in the centr of a tile, check if the tile is a dot
            if MAZE_LAYOUT[int(self.grid_ind[1]) - 3][int(self.grid_ind[0])] == "d1": #if it is a dot
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('Sounds/pacman_chomp.wav'))
                MAZE_LAYOUT[int(self.grid_ind[1]) - 3][int(self.grid_ind[0])] = "0" #set the tile position to a blank tile, which is 0
                self.score  = str(int(self.score) + 10).zfill(5) #add 10 to the score. .zfill() is a string method that returns an int with x leading zeroes

        self.grid_ind[0] = (self.pos[0] - (self.pos[0] % 28)) // 28 #set the grid position to be the pixel position - (pixel position / tile size)
        self.grid_ind[1] = (self.pos[1] - (self.pos[1] % 28)) // 28 #set the grid position to be the pixel position - (pixel position / tile size)

    def get_pos(self): #method to get the pixel position, which returns a vector containing the (grid position * tile size) + (tile size / 2)
        return vector((self.grid_ind[0] * 28) + 14, (self.grid_ind[1] * 28) + 14)

    def can_move(self): #check if the player can move. To do this, you want to check if the next tile in the direction you are going in is a wall. If it is, return False. By default, return True
        for wall in self.get_walls():
            if vector(self.grid_ind + self.direction) == wall:
                return False
        return True

    def is_center_of_tile(self): #method to check whether pacman is in the center of a tie
        if int(self.pos[0] + 14) % 28 == 0: #check if it is on a center of a tile on the x axis.
            if self.direction == vector(1, 0) or self.direction == vector(-1, 0) or self.direction == vector(0, 0): #check if the direction is either idle, left, or right, which add/take away pixels from the x axis
                return True #returns True
        if int(self.pos[1] + 14) % 28 == 0:
            if self.direction == vector(0, 1) or self.direction == vector(0, -1) or self.direction == vector(0, 0): #check if the direction is either idle, down, or up, which add/take away pixels from the y axis
                return True #return True if so
        return False #by default, return False

    def get_walls(self): #method to get the walls in the maze. This method returns a list of vectors which have the grid position of the wall
        walls = [] #initialize the walls variable
        for y, row in enumerate(MAZE_LAYOUT): #nexted for loop to iterate through the 2d array
            y += 3 #set an offset of 3 tiles
            for x, tile in enumerate(row):
                if tile[0] != 'd' and tile != '0': #if not a dot/blank tile
                    walls.append(vector(x,y)) #append the current grid position as a vector to the walls
        return walls #return walls

    def move(self, direction):
        self.stored_direction = direction

class Game(Helper): #Game class, which inherits from the helper class in order to get the helper functions
    def __init__(self):
        super().__init__() #call the class attributes of the parent class
        pygame.init() #initialize pygame
        self.screen = pygame.display.set_mode(WINDOW_SIZE) #create the current pygame window with the dimesnions of WINDOW_SIZE
        pygame.display.set_caption(TITLE) #set the caption of the current pygame window to TITLE
        self.clock = pygame.time.Clock() #attribute to handle the frames ticking for the game
        self.state = 'countdown' #attribute to keep track of the current state
        self.MUSICENDEVENT = pygame.event.custom_type() #create a custom music event to keep track of when music ends
        self.player = Pacman(vector(PLAYER_START)) #instantiate the player class, with the position of PLAYER_START
        self.time = 60 #attribute to keep track of how much time there's left

        #attributes used to count how many ms has passed:
        self.last = pygame.time.get_ticks()
        self.cooldown = 1000


    def run(self): #main game loop
        play_music = True #variavble to keep track of when to play the intro countdown music
        play_bg = True #variable to keep track of when to play the background siren music
        while True:

            if self.state == 'countdown': #if the current state of the game is the countdown phase,
                self.draw_text("emulogic.ttf", 30, "Score:", (255, 255, 255), WIDTH / 6 , HEIGHT / 17 - 40) #display the text "score" at the given x and y coordinates
                self.draw_text("emulogic.ttf", 30, "00000", (255, 255, 255), WIDTH / 6 - 10, HEIGHT / 17) #display "00000" as a placeholder for the score

                self.draw_text("emulogic.ttf", 30, "Time:", (255, 255, 255), (WIDTH / 4) * 3 , HEIGHT / 17 - 40) #display the text "time"
                self.draw_text("emulogic.ttf", 30, "60", (255, 255, 255), (WIDTH / 4) * 3 - 10, HEIGHT / 17) #display 60 as the placeholder for the time
                self.draw_maze() #draws the maze using one of the Parent's helper method
                if play_music: #if the countdown music variable is set to true
                    pygame.mixer.music.load('Sounds/pacman_beginning.wav') #load the music
                    pygame.mixer.music.set_endevent(self.MUSICENDEVENT) #create an end event for it, so the program knows what to do when the music stops
                    pygame.mixer.music.play() #play the music
                    play_music = False #set the variable to false

                self.player.draw(self.screen) #draws the player on the screen
                self.draw_text("emulogic.ttf", 30, "Ready!", (255, 255, 0), 312 + (166/2), 570) #draws the word ready on the screen under the ghost bax

                for event in pygame.event.get(): #event loop
                    if event.type == QUIT: #if the event type is QUIT, or if the user presses the x on the window, it quits the ggame and the program
                        pygame.quit()
                        sys.exit()
                    if event.type == self.MUSICENDEVENT: #if the event type is the music end event, meaning if the music stopped playing
                        self.state = 'playing' #it changes the game state to ' playing'

                pygame.display.update() #updates the display
                self.clock.tick(FPS) #renders the game at 60 FPS

            if self.state == 'playing': #if the game state is playing
                self.screen.fill((0,0,0)) #it fills the screen with black
                if play_bg: #if the bg music variable is set to True, it plays the siren in the background on infinite loop (hence the -1 passes into the parameter of play, into channel 0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sounds/playing_music.wav'), -1)
                    play_bg = False
                if MAZE_LAYOUT[int(self.player.grid_ind[1]) - 3][int(self.player.grid_ind[0])] == 'd2': # if the current tile is a big Dot
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('Sounds/eat_big.wav')) #it plays the "eat_big" sounds effect in channel 1
                    self.player.score  = str(int(self.player.score) + 10).zfill(5) #it updates the score, adding 10 to it
                    MAZE_LAYOUT[int(self.player.grid_ind[1]) - 3][int(self.player.grid_ind[0])] = "0" #it sets the till to be a blank tiole, or 0
                    self.time += 10 #it adds 10 to the oveall timer

                if self.player.score == '2430'.zfill(5): #if the player score is 02430, or the player has collected all the pellets
                    self.state = 'won' #it changes the game state to won

                if self.time == 0: #if the time runs out
                    self.state = 'time_out' #it changes the game state to time_out

                self.draw_maze() #method to draw the maze
                self.player.update() #updates the player and it's positon
                self.player.draw(self.screen) #draws the player and it's different animations on the screen
                self.draw_text("emulogic.ttf", 30, "Score:", (255, 255, 255), WIDTH / 6 , HEIGHT / 17 - 40) #displays the text "score" on the screen
                self.draw_text("emulogic.ttf", 30, self.player.score, (255, 255, 255), WIDTH / 6 - 10, HEIGHT / 17) #displays the attribute score on the screen

                self.draw_text("emulogic.ttf", 30, "Time:", (255, 255, 255), (WIDTH / 4) * 3 , HEIGHT / 17 - 40) #displays the text "time" on the screen
                self.draw_text("emulogic.ttf", 30, str(self.time), (255, 255, 255), (WIDTH / 4) * 3 - 10, HEIGHT / 17) #dsplays the actualy time on the screen

                now = pygame.time.get_ticks() #Small blurb of code to check whether 1000 ms (1 second) has passes. If it did, minus 1 from the timer
                if now - self.last >= self.cooldown: #check if the time right now - the last time is greater than or equal to the cooldown (1000 ms, 1 second)
                    self.last = now  #if it is, make the last time now
                    self.time -= 1 #minus 1 to the overall tiem

                for event in pygame.event.get(): #event loop
                    if event.type == QUIT: # if event type is QUIT, quit the game and program
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN: #if event type is keydown, or whenever the player pressses down on a key
                        if event.key == K_LEFT: #if the player presses the left key
                            self.player.move(vector(-1, 0)) #it stores the direction as a vector of -1 on the x axis, and 0 on the y axis
                        if event.key == K_RIGHT: #if the playe presses irght
                            self.player.move(vector(1, 0))#it stores the direction as a vector of 1 on the x axis, and 0 on the y axis
                        if event.key == K_UP: #if the player presses up
                            self.player.move(vector(0, -1)) #it stores the direction as a vector of 0 on the x axis, and -1 on the y axis
                        if event.key == K_DOWN: #if the player presses down
                            self.player.move(vector(0, 1)) #it stores the direction as a vector of 0 on the x axis, and 1 on the y axis

                pygame.display.update() #updates display
                self.clock.tick(FPS) #renders the game at 60 fps

            if self.state == 'time_out':
                pygame.mixer.stop()
                self.screen.fill((0,0,0))
                self.draw_text("emulogic.ttf", 30, "You ran out of time :(", (255, 255, 255), WIDTH //2 , HEIGHT // 2 - 60)
                self.draw_text("emulogic.ttf", 30, "You had a score of:", (255, 255, 255), WIDTH //2 , HEIGHT // 2)
                self.draw_text("emulogic.ttf", 30, str(int(self.player.score)), (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 40)

                self.draw_text("emulogic.ttf", 30, "press space to play again", (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 120)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.state = 'countdown' #attribute to keep track of the current state
                            self.player = Pacman(vector(PLAYER_START)) #instantiate the player class, with the position of PLAYER_START
                            self.time = 60 #attribute to keep track of how much time there's left
                            Game().run()


                pygame.display.update()
                self.clock.tick(FPS)

            if self.state == 'won':
                pygame.mixer.stop()
                self.screen.fill((0,0,0))
                self.draw_text("emulogic.ttf", 20, "You collected all the pellets :D", (255, 255, 255), WIDTH //2 , HEIGHT // 2 - 60)
                self.draw_text("emulogic.ttf", 30, "You had a score of:", (255, 255, 255), WIDTH //2 , HEIGHT // 2)
                self.draw_text("emulogic.ttf", 30, str(int(self.player.score)), (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 40)

                self.draw_text("emulogic.ttf", 30, "press space to play again", (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 120)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.state = 'countdown' #attribute to keep track of the current state
                            self.player = Pacman(vector(PLAYER_START)) #instantiate the player class, with the position of PLAYER_START
                            self.time = 60 #attribute to keep track of how much time there's left
                            Game().run() #start the game aain



                pygame.display.update()
                self.clock.tick(FPS)

            if self.state == 'won':
                self.screen.fill((0,0,0))
                self.draw_text("emulogic.ttf", 20, "You collected all the pellets :D", (255, 255, 255), WIDTH //2 , HEIGHT // 2 - 60)
                self.draw_text("emulogic.ttf", 30, "You had a score of:", (255, 255, 255), WIDTH //2 , HEIGHT // 2)
                self.draw_text("emulogic.ttf", 30, str(int(self.player.score)), (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 40)

                self.draw_text("emulogic.ttf", 40, "press space to play again", (255, 255, 255), WIDTH //2 , HEIGHT // 2 + 70)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            Game().run()

                pygame.display.update()
                self.clock.tick(FPS)

g = Game() #creates the game instance and runs it

g.run()
