import pygame
import random
import time

pygame.init()

class Player:
	def __init__(self):
		self.x = 400
		self.y = 250
		self.body = [(self.x, self.y)]
		self.last_pos = self.body[0]
	
	def show(self, surface):
		global head_color, body_color
		for rect in self.body:
			pygame.draw.rect(surface, body_color, (rect[0], rect[1], 10, 10))
		pygame.draw.rect(surface, head_color, (self.x, self.y, 10, 10))
	
	def move(self, movement):
		global moving_speed, alive
		self.last_pos = self.body[-1]
		self.body = [(self.x, self.y)] + self.body[:-1]
		self.x += movement[0]*moving_speed
		self.y += movement[1]*moving_speed

		if (self.x, self.y) in self.body:
			alive = False

	def add(self):
		self.body.append(self.last_pos)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Snake")


head_color = (0, 0, 255)
body_color = (70, 150, 255)
food_color = (255, 0, 0)

facing = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
moving_speed = 10
alive = True

snake = Player()
borders = [
	pygame.Rect(0, 0, 800, 10),
	pygame.Rect(0, 0, 10, 500),
	pygame.Rect(0, 490, 800, 10),
	pygame.Rect(790, 0, 10, 500)
]

apple = pygame.Rect(random.randint(10, 780), random.randint(10, 480), 5, 5)

running = True

while running:

	snake.move(directions[facing])

	screen.fill((0, 0, 0))
	for box in borders:
		pygame.draw.rect(screen, (255, 255, 255), box)
		if box.colliderect((snake.x, snake.y, 10, 10)):
			alive=False

	if apple.colliderect((snake.x, snake.y, 10, 10)):
		snake.add()
		apple = pygame.Rect(random.randint(10, 780), random.randint(10, 480), 5, 5)

	pygame.draw.rect(screen, food_color, apple)

	snake.show(screen)
	running = alive

	for event in pygame.event.get():
		if event.type == pygame.QUIT or pygame.key.get_pressed()[27]:
			pygame.quit()
			exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT] and facing != 1: facing = 0
	elif keys[pygame.K_LEFT] and facing != 0: facing = 1
	elif keys[pygame.K_DOWN] and facing != 3: facing = 2
	elif keys[pygame.K_UP] and facing != 2: facing = 3

	# if keys[pygame.K_KP_0]: snake.add()

	pygame.display.flip()
	clock.tick(10)

time.sleep(1)

pygame.quit()
