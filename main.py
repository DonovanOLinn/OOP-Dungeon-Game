from tkinter import N
import random

CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),
  ]


class Game:
    def __init__(self, CELLS):
        self.CELLS = CELLS
        self.token_dict = {}
        self.my_player = Player()
        self.my_monster = Monster()
        self.my_egg1 = Egg()
        self.my_egg2 = Egg()
        self.my_egg3 = Egg()
        self.my_basket = Basket()
        self.my_door = Door()
        self.game_playing = True
        self.drawMap()
        
    def drawMap(self):
        divider = '----------------------------------------'
        n = 0
        for i in range(0,5):
            i = n
            j = i + 5
            print(self.CELLS[i:j])
            print(divider)
            n += 5
        self.setVariables()

    def setVariables(self):
        random_list = []
        while len(random_list) != 7:
            random_number = random.randint(0,len(self.CELLS)-1)
            if random_number not in random_list:
                random_list.append(random_number)
        self.token_dict[self.my_player] = self.CELLS[random_list[0]]
        self.token_dict[self.my_monster] = self.CELLS[random_list[1]]
        self.token_dict[self.my_egg1] = self.CELLS[random_list[2]]
        self.token_dict[self.my_egg2] = self.CELLS[random_list[3]]
        self.token_dict[self.my_egg3] = self.CELLS[random_list[4]]
        self.token_dict[self.my_basket] = self.CELLS[random_list[5]]
        self.token_dict[self.my_door] = self.CELLS[random_list[6]]
        self.Navigation()

    def Navigation(self):
        while self.game_playing:
            print(f'This is your current location: {self.token_dict[self.my_player]}')
            move = input("Where would you like the player to move?\n")
            if move == 'debug':
                self.locationDebug()
            else:
                for i in range(len(self.CELLS)):
                    if self.CELLS[i] == self.token_dict[self.my_player]:
                        if move == 'up':
                            self.token_dict[self.my_player] = self.CELLS[i-5]
                            self.checkOverlap()
                            self.monsterNavigation()
                            break
                        if move == 'down':
                            j = i + 5
                            if j > len(self.CELLS)-1:
                                j = j - len(self.CELLS)
                            self.token_dict[self.my_player] = self.CELLS[j]
                            self.checkOverlap()
                            self.monsterNavigation()
                            break
                        if move == 'left':
                            self.token_dict[self.my_player] = self.CELLS[i-1]
                            self.checkOverlap()
                            self.monsterNavigation()
                            break
                        if move == 'right':
                            j = i + 1
                            if j > len(self.CELLS)-1:
                                j = j - len(self.CELLS)
                            self.token_dict[self.my_player] = self.CELLS[j]
                            self.checkOverlap()
                            self.monsterNavigation()
                            break
                    
    def monsterNavigation(self):
        monster_random_move = random.randint(0,3)
        for i in range(len(self.CELLS)):
            if self.CELLS[i] == self.token_dict[self.my_monster]:
                if monster_random_move == 0:
                    self.token_dict[self.my_monster] = self.CELLS[i-5]
                    self.checkOverlap()
                    break
                if monster_random_move == 1:
                    j = i + 5
                    if j > len(self.CELLS)-1:
                        j = j - len(self.CELLS)
                    self.token_dict[self.my_monster] = self.CELLS[j]
                    self.checkOverlap()
                    break
                if monster_random_move == 2:
                    self.token_dict[self.my_monster] = self.CELLS[i-1]
                    self.checkOverlap()
                    break
                if monster_random_move == 3:
                    j = i + 1
                    if j > len(self.CELLS)-1:
                        j = j - len(self.CELLS)
                    self.token_dict[self.my_monster] = self.CELLS[j]
                    self.checkOverlap()
                    break


    def locationDebug(self):
        print(f'player location: {self.token_dict[self.my_player]}')
        print(f'monster location: {self.token_dict[self.my_monster]}')
        print(f'egg1 location: {self.token_dict[self.my_egg1]}')
        print(f'egg2 location: {self.token_dict[self.my_egg2]}')
        print(f'egg3 location: {self.token_dict[self.my_egg3]}')
        print(f'basket location: {self.token_dict[self.my_basket]}')
        print(f'door location: {self.token_dict[self.my_door]}')

    def checkOverlap(self):
        if self.token_dict[self.my_player] == self.token_dict[self.my_basket]:
            print('Basket overlap achieved!')
            self.my_player.basket = True
            self.my_egg1.canPick = True
            self.my_egg2.canPick = True
            self.my_egg3.canPick = True
            self.token_dict[self.my_basket] = ('none','none')

        if self.token_dict[self.my_player] == self.token_dict[self.my_monster]:
            self.Endgame()

        if self.token_dict[self.my_player] == self.token_dict[self.my_egg1]:
            if self.my_egg1.canPick == True:
                print('Egg1 overlap achieved!')
                self.my_player.eggs += 1
                self.token_dict[self.my_egg1] = ('none', 'none')

        if self.token_dict[self.my_player] == self.token_dict[self.my_egg2]:
            if self.my_egg2.canPick == True:
                print('Egg2 overlap achieved!')
                self.my_player.basket = True
                self.my_player.eggs += 1
                self.token_dict[self.my_egg2] = ('none', 'none')

        if self.token_dict[self.my_player] == self.token_dict[self.my_egg3]:
            if self.my_egg3.canPick == True:
                print('Egg3 overlap achieved!')
                self.my_player.basket = True
                self.my_player.eggs += 1
                self.token_dict[self.my_egg3] = ('none', 'none')

        if self.my_player.eggs == 3:
            if self.token_dict[self.my_player] == self.token_dict[self.my_door]:
                self.my_door.canLeave = True
                self.Endgame()
        
    def Endgame(self):
        if self.my_door.canLeave == True:
            print('Congratulation! You managed to escape without being eaten by the monster. Good job!')
            self.game_playing = False
        if self.my_door.canLeave == False:
            print('The monster has caught up to you! YA DEAD')
            self.game_playing = False

    
class Player:
    def __init__(self):
        self.basket = False
        self.eggs = 0
        self.door = False
        self.monster = False
        pass

class Monster:
    pass

class Egg:
    def __init__(self):
        self.canPick = False

class Basket:
    def __init__(self):
        self.hasBasket = False

class Door:
    def __init__(self):
        self.canLeave = False


my_game = Game(CELLS)
