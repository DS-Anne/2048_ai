# author-Brandon Baker
# play2048.py - automatically plays 2048 by repeatedly sliding in the following pattern:
# up, right, down, left over and over again.
# Usage: play2048.py <file> - automatically plays 2048 and copies each round's score
# to the specified file.  If file doesn't exist, then the program makes it.  If no file
# given, plays without recording.   

import bs4, requests, sys, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def playGame(scoring = True):
	# Open browser with selenium
	browser = webdriver.Firefox()
	browser.get('https://gabrielecirulli.github.io/2048/')

	# TODO: while loop to repeatedly send key pattern while game is still going
	game = browser.find_element_by_class_name('game-container')
	while True:
		try:
			retryButton = browser.find_element_by_link_text('Try again')
			scoreElem = browser.find_element_by_class_name('score-container')
			#print('Score was: ' + scoreElem.text)
			if scoring == False:
				# Replay
				retryButton.click()
				continue
			else: 
				
				# Desired scoring file already exists so append scores.
				if os.path.isfile(fileName):
					scoreFile = open(fileName, 'a')
					scoreFile.write('\n' + 'Score was : ' + scoreElem.text.split()[0])
					scoreFile.close()
					retryButton.click()
					continue
				else:
					scoreFile = open(fileName, 'w')
					scoreFile.write('\n' + 'Score was : ' + scoreElem.text.split()[0])
					scoreFile.close()
					retryButton.click()
					continue
		except:
			#Do nothing.  Game is not over yet
			pass
		
		game.send_keys(Keys.UP)
		game.send_keys(Keys.RIGHT)
		game.send_keys(Keys.DOWN)
		game.send_keys(Keys.LEFT)

# Determine action from sys.argv
if len(sys.argv) == 1 :
	playGame(scoring = False)
elif len(sys.argv) == 2:
	fileName = sys.argv[1]
	playGame(scoring=True)
	
	