# Engineering_4_Repository

## Dice Roller
#Automatic Dice Roller
#Written by [Lucas Miller]  #With help from pythonfiddle.com

from random import randint

print ("Automatic Dice Roller")

doubles = 0            #Im using two dice, I found a cool code online that rolls two dice and also asks to re roll.
num1 = randint(1,6)    # im trying to recreate and use its resources, I thought it would be fun.
num2 = randint(1,6)

print ("Do you want to roll? (Y)es or (No)")  #I have it aks if you want to roll again or not
answer = raw_input()
while answer.lower()[0] == ("y"):
        print ("You rolled a" , num1, "and a" , num2, "The total of these dice is:" num1 + num2)
        while num1 == num2:
                print "Nice! you rolled a double!"
        print ("Roll again? (Y)es or (N)o")
        answer = raw_input()
        
### Reflection 
In this assignment I treid a slighly different code for the porject. I got it to work for about 5 minutes, however it stopped working after that and im trying to fix it. I thought I'd put my code in anyways for a grade and advice. I decided to make two variable, num1 and num2 and these depict the two different dice. Each one is rolled at the same time and each gives a number. My code is suppsoed to display them and add them together to get the sum of the two. It also asks to re roll afterwards. The main issue that I think im having/ had is the second dice rolling and them adding, the first time I did it it only printed the first number, I then messed with it for a little while and relaized I didnt have brackets and qoutations in the right places, so I got it to work from that. Im still working out the bugs and trying to get it working again. 
