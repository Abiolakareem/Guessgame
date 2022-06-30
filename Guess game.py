import random
status='r' #to set whether the user wants to continue playing the game after exhausting their 3 attempts 
while status == 'r': #to quit or remain in the game. I latter realised I could use the quit() function. 
	score=0
	i=1

	while i<4: #to keep the game going up while attempts remain less than 3
		guess= input ('Guess a number between 1 - 3: ') 
		
# I would like to raise the below exception here but the code keeps blowing and I couldn't get it back to where it asks user for their guess so I had to comment it out

#		if guess !="1" or "2" or "3":
#			raise Exception ("Enter a number between 1 - 3: ")
#			break 
		num=random.randint(1,3)#to generate the random numbers against which the user input is compared. If the user guessed right, 1 point is awarded in score below, if the user guessed wrong attempt is reduced by 1
		if guess == str(num):
			score += 1
			print (f'You are correct {guess} is correct. Your score: {score}, Attempts left {4-i} ')

		else:
			if i==3: #if attempts is exhausted, we break out of the loop and game over. We 
				print(f'You are wrong, {guess} is incorrect, {num} is the correct answer. Game Over! You score: {score} ')
				break
			else:
				print(f'You are wrong, {guess} is incorrect. {num} is the correct answer. You have {3-i} attempts left') 
				i+=1
	status=input('Enter "R" to start again, otherwise enter anything to close the game ').lower()#User to decide whether to restart the game or quit after exhausting the three attempts 
		