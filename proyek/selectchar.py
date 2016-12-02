import sys, pygame, config, game, highscore, titlescreen

class selectChar:

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
							pygame.quit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						mx, my = pygame.mouse.get_pos()
						if my < 345 and mx < 420:
							game.Game.char = 1
							self.singlePlayer()
						elif my < 345 and mx > 420:
							game.Game.char = 2
							self.singlePlayer()
						elif my > 345 and mx < 420:
							game.Game.char = 3
							self.singlePlayer()
						elif my > 345 and mx > 420:
							game.Game.char = 4
							self.singlePlayer()


	def withinBoundary(self, x1, x2, y1, y2):
		if pygame.mouse.get_pos()[0] >= x1 and pygame.mouse.get_pos()[0] <= x2 and pygame.mouse.get_pos()[1] >= y1 and pygame.mouse.get_pos()[1] <= y2:
			return True
		return False

	def singlePlayer(self):
		g = game.Game(self.c.SINGLE)

	def selectchar(self):
  		#imagePath = self.c.IMAGE_PATH + "loading.png"
		#img = pygame.image.load(imagePath).convert()
		#self.screen.blit(img,(0,0))
		preloader = pygame.image.load(self.c.IMAGE_PATH + "char.png").convert()
		self.screen.blit(preloader,(0,0))
		pygame.display.flip()

	def multiplayer(self):
		g = game.Game(self.c.MULTI)

	def instructions(self):
		print "Instructions clicked!"

	def highScores(self):
		h = highscore.Highscore()
		h.displayScore()

	def clearBackground(self):
		bg = pygame.Surface(self.screen.get_size())
		bg = bg.convert()
		bg.fill((0,0,0))
		self.blit(bg,(0,0))