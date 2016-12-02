import sys, pygame, config, highscore, titlescreen, player, game

class Shop:
	def __init__(self):
		self.c = config.Config()
		exitMain = False

		while not exitMain:
			pygame.init()
			self.screen = pygame.display.set_mode((840,690))
			pygame.display.set_caption("Bomberman")

			imagePath = self.c.IMAGE_PATH + "char.png"
			img = pygame.image.load(imagePath).convert()
			self.screen.blit(img,(0,0))

			pygame.mixer.music.load(self.c.AUDIO_PATH + "title.mid")
			pygame.mixer.music.play()

			clock = pygame.time.Clock()
			pygame.mouse.set_visible(True)
			pygame.display.flip()
			userInteracted = False

			while not userInteracted:
				clock.tick(self.c.FPS)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						userInteracted = True
						exitMain = True
						pygame.quit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							userInteracted = True
							exitMain = True
							g = game.Game()
							g.victory()

					if event.type == pygame.MOUSEBUTTONDOWN:
						mx, my = pygame.mouse.get_pos()
						if my < 384 and mx < 514:
							game.Game.char = 1
							self.singlePlayer()
						elif my < 384 and mx > 514:
							game.Game.char = 2
							self.singlePlayer()
						elif my > 384 and mx < 514:
							game.Game.char = 3
							self.singlePlayer()
						elif my > 384 and mx > 514:
							game.Game.char = 4
							self.singlePlayer()
				self.updateDisplayInfo()
				self.drawInterface()


	def withinBoundary(self, x1, x2, y1, y2):
		if pygame.mouse.get_pos()[0] >= x1 and pygame.mouse.get_pos()[0] <= x2 and pygame.mouse.get_pos()[1] >= y1 and pygame.mouse.get_pos()[1] <= y2:
			return True
		return False

	def singlePlayer(self):
		game.Game(self.c.SINGLE)

	def updateDisplayInfo(self):
		self.printText(player.Player.score,(65,653))
		self.printText(player.Player.lives,(775,653))
		self.printText(player.Player.maxBombs,(630,653))
		self.printText(player.Player.power,(700,653))

	def drawInterface(self):
		player  = pygame.image.load(self.c.IMAGE_PATH + "screen/player.png").convert()
		life = pygame.image.load(self.c.IMAGE_PATH + "screen/life.png").convert()
		bomb = pygame.image.load(self.c.IMAGE_PATH + "screen/bomb.png").convert()
		power = pygame.image.load(self.c.IMAGE_PATH + "screen/power.png").convert()
		clock = pygame.image.load(self.c.IMAGE_PATH + "screen/clock.png").convert()

		self.screen.blit(player,(40,650))
		self.screen.blit(clock,(365,650))
		self.screen.blit(bomb,(590,647))
		self.screen.blit(power,(670,650))
		self.screen.blit(life,(740,652))

	def printText(self,text,point):
		font = pygame.font.Font("lucida.ttf",20)
		label = font.render(str(text)+'  ', True, (255,255, 255), (0, 0, 0))
		textRect = label.get_rect()
		textRect.x = point[0]
		textRect.y = point[1]
		self.screen.blit(label, textRect)