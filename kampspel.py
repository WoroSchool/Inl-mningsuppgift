#Rondbaserat spel
#Spelaren attackerar på sin runda

#GUI
from tkinter import * 

#För att få olika skada
import random 

def huvudmeny():
	#Hur menyn som spelaren väljer med ska se ut

	print('Välkommen till spelet.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.')

def namn():
	a = int(Entry.get(x))
	namn.configure(text='Ditt namn är: ' +str(a))

huvudmeny()

fonster=Tk()
fonster.title('Kampspel')
fonster.resizable(width=False, height=False)
fonster.geometry('1000x500')

#Introduktion

info=Label(fonster, text='Välkommen till spelet.\nDet är ett rondbaserat kampspel där du strider mot en motståndare.\nDitt mål är att vinna motståndaren.')
info.pack()

namn=Label(fonster, text='Vad heter du?\n')
namn.pack()

#Vad vill du heta?

x=Entry(fonster, width=12)
x.pack()

knapp=Button(fonster,text='Klart',command=lambda:namn())
knapp.pack()

fonster.mainloop()

