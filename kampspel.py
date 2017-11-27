#Rondbaserat spel
#Spelaren attackerar på sin runda

#GUI
from tkinter import * 

#För att få olika attacker
import random 

def huvudmeny():
	#Hur menyn som spelaren väljer med ska se ut

	print('Välkommen till spelet.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.')
	print('Vad är ditt namn?')
	return

#Rensar skärmen och ändrar storleken och mera

def rensa():
	startknapp.pack_forget()
	info.pack_forget()
	fonster.resizable(width=False, height=False)
	fonster.geometry('1000x700')
	fonster.title('Kampspel')
	#Animerad bakgrund
	canvas = Canvas(fonster)
	canvas.grid(row = 0, column = 0)
	photo = PhotoImage(file = 'bakgrund.gif') 
	canvas.pack(expand = YES, fill = BOTH)
	#Ena hörnet av bilden i nordväst
	canvas.create_image(0, 0, image=photo, anchor=NW)
	fonster.mainloop()
	return

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
	fonster.title('Information')
	fonster.resizable(width=False, height=False)
	fonster.geometry('400x100')

	info=Label(fonster, text='Välkommen till spelet '+namn+'.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.\nDitt mål är att vinna motståndaren.')
	info.pack()

	startknapp=Button(fonster, text='START!',command=lambda:rensa())
	startknapp.pack()

	fonster.mainloop()



	