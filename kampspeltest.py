#Rondbaserat spel
#Spelaren attackerar på sin runda

#GUI
from tkinter import * 

#För att få olika skada
import random 

def huvudmeny():
	#Hur menyn som spelaren väljer med ska se ut

	print('Välkommen till spelet.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.')
	print('Vad är ditt namn?')

def introduktion():
	info=Label(fonster, text='Välkommen till spelet '+namn+'.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.\nDitt mål är att vinna motståndaren.')
	info.pack()

huvudmeny()
namn = input()
print('Hej '+namn+' vill du starta spelet?')
starta = input('JA/NEJ\n')
if starta.upper() == 'JA':
	running = True
else:
	running = False
	input('Tryck på ENTER för att avsluta...')

if running == True:
	fonster=Tk()
	fonster.title('Kampspel')
	fonster.resizable(width=False, height=False)
	fonster.geometry('1000x500')
	introduktion()
	fonster.mainloop()



	



