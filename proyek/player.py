import pygame, character, config, bomb, game, tile


# RFCT NEEDED
class Player(character.Character):
	lives = 3
	score = 0
	currentBomb = 1
	maxBombs = 1
	power = 1			# bomb power
	speed = 1			# player movement speed
	tempmaxBombs = 1
	temppower = 1
	templives = 3

	def __init__(self, name, imageName, id, point):
		character.Character.__init__(self, name, "players/"+imageName, point)
  		#character.Character.__init__(self, name, "players/p_2_", point)
		self.c = config.Config()
		self.id = id
		self.instance_of = 'player'

	# reset all stats if death is true
	def reset(self,death):
		character.Character.reset(self,True)
		if death:
			self.currentBomb = self.maxBombs = 1
			self.power = 1
			self.speed = 1

	def deployBomb(self):
		if self.currentBomb > 0:
			self.currentBomb -= 1
			b = bomb.Bomb(self)
			return b
		return None

	def gainPower(self,power):
		if power == self.c.BOMB_UP:
			self.currentBomb += 1
			if self.maxBombs < 9:
				self.maxBombs += 1
				self.tempmaxBombs += 1
		elif power == self.c.LIFE_UP:
			if self.lives < 9:
				self.lives += 1
				self.templives += 1
		elif power == self.c.POWER_UP:
			if self.power < 9:
				self.power += 1
				self.temppower += 1
 		elif power == self.c.POWER_PLUS:
			if self.power < 9:
				self.power = 9
   		elif power == self.c.TIME_UP:
			game.Game.timeplus = True
		elif power == self.c.WALL_PASS:
			tile.wpass = True
			t = tile.Tile(self.c.WALL_PASS)
			t.setAttributes()
		elif power == self.c.ARMOR:
			game.Game.armor = True
		elif power == 10:
			self.power = 9
			self.lives = 9
			self.maxBombs = 9
		elif power == 11:
			self.power = self.temppower
			self.lives = self.templives
			self.maxBombs = self.tempmaxBombs

	def setScore(self,score):
		self.score += score
		if self.score < 0:
			self.score = 0

	# RFCT - this was a bad idea
	def loseLifeAndGameOver(self):
		self.lives -= 1
		return self.lives <= 0