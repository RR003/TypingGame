import pygame
import levels
import FreeTypeLevel
import time

pygame.init()
# make the screen
(width, height) = (1030, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
running = True
char_objects = []
# Generate text
font = pygame.font.SysFont('Calibri', 25)
str = FreeTypeLevel.TypeChallenge()
strSplit = str.split()
numOfWords = len(strSplit)

print(str)
ListOfLetters = [letter for letter in str]
ListOfNums = []
for letter in ListOfLetters:
    number = ord(letter)
    ListOfNums.append(number)
print(len(ListOfLetters))
pygame.display.flip()

level = 9

class Letters():
    def __init__(self, char, x, y, color=(255, 255, 255)):
        self.char = char
        self.x = x
        self.y = y
        self.color = color

    def char_display(self):
        txt = font.render(self.char, True, self.color)
        screen.blit(txt, (self.x, self.y))

    def become_green(self):
        self.color = (0, 255, 0)

    def become_red(self):
        self.color = (255, 0, 0)


def str_to_object(string):
    global char_objects
    x_cor = 30
    y_cor = 30
    for let in string:
        obj = Letters(let, x_cor, y_cor)
        char_objects.append(obj)
        x_cor += 20
        if x_cor > 1030:
            x_cor = 30
            y_cor += 60


def display_chars():
    global screen
    for char in char_objects:
        char.char_display()
    pygame.display.flip()


def main():
    global running
    str_to_object(str)
    display_chars()
    index = 0
    ListOfKeys = [0]
    start = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                a = event.key

                if (index == 0 and start == 0):
                    start = time.time()
                    timer.countdown(60)




                if (a > 100000):
                    ListOfKeys.append(a)
                else:
                    if ListOfLetters[index].isupper():

                        if (ListOfKeys[-1] > 1000000 and a == ListOfNums[index] + 32):
                            char_objects[index].become_green()
                            ListOfKeys.append(a)
                            index += 1
                        else:
                            char_objects[index].become_red()

                    elif a == ListOfNums[index]:
                        ListOfKeys.append(a)
                        char_objects[index].become_green()
                        index += 1

                        if (index == len(ListOfLetters) - 1):
                            end = time.time()
                            totalTime = levels.ElapsedTime(end,start)
                            print(totalTime)
                            wpm = FreeTypeLevel.wpm(totalTime, numOfWords)
                            print(wpm)
                            if level > 0 and level < 9:
                                levels.checkAdvancement(totalTime, levels.limits(level))

                            break
                    else:
                        char_objects[index].become_red()
            display_chars()

            if event.type == pygame.QUIT:
                running = False
main()