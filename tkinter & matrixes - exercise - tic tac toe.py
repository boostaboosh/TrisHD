###tkinter e matrici - esercizio - gioco_game - tris_three in a row
##TRIS-HD

import tkinter

finestra=tkinter.Tk()#creo la finestra.
finestra.title("TRIS")
finestra["bg"]="white"
finestra.geometry("1280x720")#risoluzione HD
finestra.resizable(0,0)

vert1=tkinter.Label(None,bg="black").place(width=5,height=720,x=517,y=0)#usando 4 label formo la tavola da gioco del tris.
vert2=tkinter.Label(None,bg="black").place(width=5,height=720,x=759,y=0)
orri1=tkinter.Label(None,bg="black").place(width=720,height=5,x=280,y=237)
orri2=tkinter.Label(None,bg="black").place(width=720,height=5,x=280,y=479)


LP1=tkinter.Label(None,bg="white",fg="black",text="player 1:",font=("Verdana","20","bold")).place(width=280,height=50,x=0,y=0)#label che dice al player1 di inserire il nome nello spazio.
p1=tkinter.StringVar(value="")
P1=tkinter.Entry(None,bg="white",fg="black",textvariable=p1,font=("Verdana","20","bold")).place(width=280,height=50,x=0,y=70)#spazio per inserire il nome del player1. 

LP2=tkinter.Label(None,bg="white",fg="black",text="player 2:",font=("Verdana","20","bold")).place(width=280,height=50,x=1000,y=0)#label che dice al player2 di inserire il nome nello spazio.
p2=tkinter.StringVar(value="")
P2=tkinter.Entry(None,bg="white",fg="black",textvariable=p2,font=("Verdana","20","bold")).place(width=280,height=50,x=1000,y=70)#spazio per inserire il nome del player2.


vittoriep1=tkinter.IntVar(value=0)#contatore vittorie player1

LVP1=tkinter.Label(None,bg="white",fg="black",text="wins "+str(p1.get())+":",font=("Verdana","20","bold"))#label che dice vittorie                               ##+str(p1.get())+## dovrebbe prendere il nome inserito nell'entry P1 ma sembra farlo solo inizialmente quando l'entry è vuoto e poi non aggiornarsi.
LVP1.place(width=280,height=50,x=0,y=120)
VP1=tkinter.Label(None,bg="white",fg="black",textvariable=str(vittoriep1),font=("Verdana","40","bold"))#label che mostra il contatore di vittorie del player1.
VP1.place(width=280,height=100,x=0,y=180)

vittoriep2=tkinter.IntVar(value=0)#contatore vittorie player2

LVP2=tkinter.Label(None,bg="white",fg="black",text="wins "+str(p2.get())+":",font=("Verdana","20","bold"))#label che dice vittorie                               ##+str(p2.get())+## dovrebbe prendere il nome inserito nell'entry P2 ma sembra farlo solo inizialmente quando l'entry è vuoto e poi non aggiornarsi.
LVP2.place(width=280,height=50,x=1000,y=120)
VP2=tkinter.Label(None,bg="white",fg="black",textvariable=str(vittoriep2),font=("Verdana","40","bold"))#label che mostra il contatore di vittorie del player2.
VP2.place(width=280,height=100,x=1000,y=180)


board=[[0,0,0],[0,0,0],[0,0,0]]#la variabile board è la matrice grazie alla quale potremo verificare se è stato compiuto il tris.

def reset(buttons):#La funzione reset viene richiamata ogni volta che un giocatore vince una partita, essa "resetta" i valori iniziali dei text nei bottoni e riporta allo stato iniziale la matrice baord.
                   #Lascia invariati invece i contatori di vittorie e i nomi dei giocatori, diverso quindi dalla funzione resetgame.
    global board#in questo modo posso richiamare e modificare la variabile board anche da dentro le funzioni.
    board=[[0,0,0],[0,0,0],[0,0,0]]
    for k in (buttons):
        k.configure(text="")
    if s.get()=="X":#
        s.set("X")
    if s.get()=="O":#
        s.set("O")
    ##così se vince player 1 comincia il player 2 e viceversa
  
def win():#La funzione win verifica se é stato compiuto il tris, va quindi a vedere se i valori delle righe, delle colonne o delle diagonali siano uguali, a condizione però che i valori non siano tutti e tre 0, cioè la situazione iniziale.
    for rig in board:
        if rig[0] == rig[1] and rig [1] == rig[2] and rig[0] != 0:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != 0:
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[0][2] == board[1][1] and board[1][1]== board[2][0] and board[0][2] != 0:
        return True
    return False

def move(B,x,y):#funzione move che, avendo verificato che la casella/il bottone premuta/o non sia già stata premuta/o e quindi ha ancora il valore non modificato di 0, cambia il testo al bottone premuto;
                #X --> se è il primo turno oppure se il turno precedente era del giocatore O (player2); oppure O --> se il turno predente era del giocatore X (player1); assegna poi il valore stringa assegnato
                #al text del bottone al rispettivo posto del bottone nella matrice board (se il bottone board20 assume il valore X, il posto nella matrice board ad assunmere il valore X sarà il posto baord[2][0])
                #La funzione poi assegna alla variabile s il valore del simbolo assegnato al text del bottone, X oppure O, per fare in modo che al prossimo bottone premuto,
                #e quindi al prossimo richiamo della funzione move, il valore assegnato al text del bottone premuto e al rispettivo posto nella matrice board sia diverso dal valore assegnato in precedenza.
                #Ad esempio; se viene premuto un bottone, al primo turno, il suo text assume il valore di X assieme al rispettivo posto del bottone nella matrice ed assieme alla variabile s, al prossimo bottone premuto
                #la funzione vedrà che la variabile s vale X e quindi saprà che bisogna assegnare il valore O al text del bottone, al rispettivo posto del bottone nella matrice e alla variabile s.
                #Lo stesso procidimento vale per il prossimo botone premuto che quindi assumerà il valore di X poichè il precedente ha assunto il valore O. La successione continuerà quindi in questa maniera.
    if board[x][y]==0:
        if s.get()=="" or s.get()=="O":
            s.set("X")
            B.configure(text="X")
            board[x][y]="X"
        elif s.get()=="X":
            s.set("O")
            B.configure(text="O")
            board[x][y]="O"
        if win() == True:#se la funzione win risulta True, quindi vera, è avvenuta la vittoria di un giocatore, quindi si aggiunge 1  al contatore di vittorie del giocatore che ha fatto tris,
                         #player 1 se il valore di s, e quindi dell'ultimo bottone premuto, è X, player 2 se il valore di s invece vale O. Infine si esegue la funzione reset,
                         #che "resetta" la tavola da gioco.
            P1wins=int(vittoriep1.get())
            P2wins=int(vittoriep2.get())
            if s.get()=="X":
                vittoriep1.set(P1wins+1)
            elif s.get()=="O":
                vittoriep2.set(P2wins+1)
            reset(buttons)
        cas=0#variabile che aumenta di 1 ogni volta che aumenta di 1 ogni volta che viene occupata una casella
        for k in board:
            for h in k:
                if h!=0:
                    cas+=1 
        if cas == 9:#se tutte le caselle vengono occupate, e quindi se cas=9, si esegue la funzione reset,
                    #in questo modo si "resetta" automaticamente il tavolo di gioco anche in caso di pareggio, permettendo di continuare a giocare con gli stessi punteggi.
            reset(buttons)
                

def resetgame(buttons):#La funzione resetall restabilisce i valori iniziali.
    global board
    s.set("")
    board=[[0,0,0],[0,0,0],[0,0,0]]
    vittoriep1.set(0)
    vittoriep2.set(0)
    for k in (buttons):
        k.configure(text="")
    p1.set("")
    p2.set("")

s=tkinter.StringVar(value="") #Il valore iniziale di s è nullo ma esso andrà ad assunmere i valori di X e di O nel respettivo ordine grazie alla funzione move,
                              #serve quindi per poter sapere di chi è stato il precedente turno e di conseguenza anche per sapere chi ha vinto.

board00=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board00,0,0))#I bottoni sono 9, una per ogni casella del tris, i loro nomi sono in base al rispettivo posto nella matrice board.
#board00 per il posto board[0][0], board01 per il posto board[0][0] e cosi via. Font ci permette di cambiare lo stile e le misure del testo, Verdana lostile, 210 le misure in modo da riempire la casella e bold la caratterizzazione,
#bold perchè fa apparire più "grosse" le lettere, rendendo il gioco più chiaro. I command nei bottoni richiamano tutti la funzione move. Si utilizza lambda: dopo il command perchè se no non posso assegnare argomenti alla funzione
#all'interno di un widget.
board00.place(width=237,height=237,x=280,y=0)
board01=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board01,0,1))
board01.place(width=237,height=237,x=522,y=0)
board02=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board02,0,2))
board02.place(width=237,height=237,x=764,y=0)
board10=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board10,1,0))
board10.place(width=237,height=237,x=280,y=242)
board11=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board11,1,1))
board11.place(width=237,height=237,x=522,y=242)
board12=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board12,1,2))
board12.place(width=237,height=237,x=764,y=242)
board20=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board20,2,0))
board20.place(width=237,height=237,x=280,y=484)
board21=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board21,2,1))
board21.place(width=237,height=237,x=522,y=484)
board22=tkinter.Button(None,bg="white",fg="black",text="",font=("Verdana","210","bold"),command=lambda:move(board22,2,2))
board22.place(width=237,height=237,x=764,y=484)

buttons=[board00,board01,board02,board10,board11,board12,board20,board21,board22]#una lista contenente tutti i bottoni, serve per poter eseguire il resetall e il reset senza dover fare tkinter.configure per ogni singolo bottone.

breset=tkinter.Button(None,bg="white",fg="black",text="RESET GAME",font=("Verdana","20","bold"),command=lambda:resetgame(buttons))#bottone che richiama la funzione resetall che permette l'utente di "resettare" il gioco portando tutto ai valori iniziali.
breset.place(width=280,height=40,x=0,y=680)

finestra.mainloop()
