#Rondbaserat spel
#Spelaren attackerar på sin runda

#GUI
from tkinter import * 

#För att få olika attacker
import random 

#Bakgrundsmusik
import winsound

def slag():
	global troll_hp
	troll_hp = troll_hp - random.randint(18, 25)
	return troll_hp

def superslag():
	global troll_hp
	troll_hp = troll_hp - random.randint(10, 35)
	return troll_hp

def hela():
	global spelare_hp
	spelare_hp = spelare_hp + random.randint(20, 25)
	return spelare_hp

def klar_namn():
	namn.grid_forget()
	inloggning.grid_forget()
	klar.grid_forget()
	start=Label(frame, text='Hej '+namn.get()+' vill du starta spelet?\nDu måste slå ner trollet för att vinna spelet!\nDu har tre attacker att välja på.\nVarje spelare har 100hp och vinnaren är den som får ner den andra till 0.')
	start.grid(padx=20,pady=20)
	startknapp.grid(padx=10,pady=10)

#Rensar skärmen och ändrar storleken och mera
def rensa():
	startknapp.grid_forget()
	root.resizable(width=False, height=False)
	root.geometry('1000x650')
	root.title('Kampspel')
	#Animerad bakgrund
	#Fick hitta ett sätt att undvika .grid och .pack eftersom de inte går ihop
	bg_bild = PhotoImage(file = 'bakgrund.gif') 
	x = Label(image=bg_bild)
	x.grid(row=0, column=0)

	atk1=Button(toolframe, text='Slag',padx=20,pady=10,background='gray',command=lambda:slag())
	atk1.grid()

	atk2=Button(toolframe, text='Superslag',padx=20,pady=10,background='gray',command=lambda:superslag())
	atk2.grid()

	atk3=Button(toolframe, text='Hela',padx=20,pady=10,background='gray',command=lambda:hela())
	atk3.grid()

	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)

	trollhp=Label(toolframe, text='Trollets liv:'+str(troll_hp)+'')
	trollhp.grid(row=1, column=1)

	root.mainloop()
	#Gav upp med att försöka lägga in riddare och troll som skilt
	#Lade till dem till bilden istället.

spelare_hp = 100
troll_hp = 100

if spelare_hp > 100:
	spelare_hp = 100

if troll_hp > 100:
	troll_hp = 100

root=Tk()
root.title('Information')
root.resizable(width=False, height=False)

frame = Frame(root)
frame.grid()

toolframe = Frame(root)
toolframe.grid()
		
inloggning=Label(frame, text='Vad heter du?')
inloggning.grid()
namn=Entry(frame)
namn.grid(padx=100, pady=5)
klar=Button(frame, text='Klar',command=lambda:klar_namn())
klar.grid()

startknapp=Button(frame,text='START!',command=lambda:rensa())
startknapp.grid()
startknapp.grid_forget()









          



