#Rondbaserat spel
#Spelaren attackerar på sin runda

#GUI
from tkinter import * 
#För att få olika attacker
import random 
#Bakgrundsmusik
from winsound import * 
#Slutmeddelande
import tkinter.messagebox

def heal_wav():
	return PlaySound('heal.wav', SND_FILENAME)

def attack_wav():
	return PlaySound('attack.wav', SND_FILENAME)

def slag():
	global troll_hp
	attack_wav()
	slag = random.randint(18, 25)
	troll_hp = troll_hp - slag
	trollhp=Label(toolframe, text='Trollets liv:'+str(troll_hp)+'')
	trollhp.grid(row=1, column=1)
	trollatk = random.randint(0,60)
	global spelare_hp
	spelare_hp = spelare_hp - trollatk
	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)
	if spelare_hp <= 0:
		info2.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du förlorade :(')
		hp.grid_forget()
		hpdead=Label(toolframe, text='Ditt liv:'+str(dead)+'')
		hpdead.grid(row=0, column=1)
	elif troll_hp <= 0:
		trollhp.grid_forget()
		trollhpdead=Label(toolframe, text='Trollets liv:'+str(dead)+'')
		trollhpdead.grid(row=1, column=1)
		info.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du vann :)')

	return troll_hp
	return spelare_hp

def superslag():
	global troll_hp
	attack_wav()
	superslag = random.randint(10, 35)
	troll_hp = troll_hp - superslag
	trollhp=Label(toolframe, text='Trollets liv:'+str(troll_hp)+'')
	trollhp.grid(row=1, column=1)
	trollatk = random.randint(0,70)
	global spelare_hp
	spelare_hp = spelare_hp - trollatk
	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)
	if spelare_hp <= 0:
		info2.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du förlorade :(')
		hp.grid_forget()
		hpdead=Label(toolframe, text='Ditt liv:'+str(dead)+'')
		hpdead.grid(row=0, column=1)
	elif troll_hp <= 0:
		trollhp.grid_forget()
		trollhpdead=Label(toolframe, text='Trollets liv:'+str(dead)+'')
		trollhpdead.grid(row=1, column=1)
		info.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du vann :)')

	return troll_hp
	return spelare_hp

def hela():
	global spelare_hp
	heal_wav()
	heal = random.randint(70,90)
	spelare_hp = spelare_hp + heal
	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)
	trollatk = random.randint(15,115)
	spelare_hp = spelare_hp - trollatk
	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)
	if spelare_hp <= 0:
		info2.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du förlorade :(')
		hp.grid_forget()
		hpdead=Label(toolframe, text='Ditt liv:'+str(dead)+'')
		hpdead.grid(row=0, column=1)
	elif troll_hp <= 0:
		trollhp.grid_forget()
		trollhpdead=Label(toolframe, text='Trollets liv:'+str(dead)+'')
		trollhpdead.grid(row=1, column=1)
		info.grid(row=0, column=2)
		tkinter.messagebox.showinfo('Information', 'Du vann :)')

	return spelare_hp
	return troll_hp

def klar_namn():
	namn.grid_forget()
	inloggning.grid_forget()
	klar.grid_forget()
	start=Label(frame, text='Hej '+namn.get()+' vill du starta spelet?\nDu måste slå ner trollet för att vinna spelet!\nDu har tre attacker att välja på.\nVarje spelare har 100hp och vinnaren är den som får ner den andra till 0.\nTrollet slår dig hårdare då du helar.')
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

	hp=Label(toolframe, text='Ditt liv:'+str(spelare_hp)+'')
	hp.grid(row=0, column=1)

	trollhp=Label(toolframe, text='Trollets liv:'+str(troll_hp)+'')
	trollhp.grid(row=1, column=1)

	atk1=Button(toolframe, text='Slag',padx=20,pady=10,background='gray',command=lambda:slag())
	atk1.grid(row=0, column=0)

	atk2=Button(toolframe, text='Superslag',padx=20,pady=10,background='gray',command=lambda:superslag())
	atk2.grid(row=1, column=0)

	atk3=Button(toolframe, text='Hela',padx=20,pady=10,background='gray',command=lambda:hela())
	atk3.grid(row=2, column=0)

	close=Button(toolframe, text='Stäng av',padx=5,pady=5,background='red',command=lambda:root.destroy())
	close.grid(row=2,column=1)

	root.mainloop()
	#Gav upp med att försöka lägga in riddare och troll som skilt
	#Lade till dem till bilden istället.

spelare_hp = 100
troll_hp = 100
dead = 0

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

info=Label(toolframe, text='Du vann!',background='green',font=("Courier", 20))
info.grid(row=0, column=2)
info.grid_forget()

info2=Label(toolframe, text='Du förlorade',background='red',font=("Courier", 20))
info2.grid(row=0, column=2)
info2.grid_forget()












          



