from gpiozero import LED,Button
from time import sleep
from random import uniform

led=LED(4)
i=5
player1=0
player2=0
right_button=Button(15)
left_button=Button(14)
left_name=input('left player name is ')
right_name=input('right player name is ')
led.on()
sleep(uniform(5,10))
led.off()
def pressed(button):
	global player1,player2
	if button.pin.number==14:
		player1+=1 
		print(left_name+' won the game')
	else:
		player2+=1
		print(right_name+' won the game')
	exit()
while i>0:
	i-=1
	led.on()
	sleep(uniform(1,2))
	led.off()
	right_button.when_pressed=pressed
	left_button.when_pressed=pressed
	sleep(2)
print("Game over")
if player1>player2:
	print(left_name+' won the game')
else:
	print(right_name+' won the game')
