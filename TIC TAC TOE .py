def printboard(x,z):
    zero="x" if x[0] else("O" if z[0] else 0)
    one="x" if x[1] else("O" if z[1] else 1)
    two="x" if x[2] else("O" if z[2] else 2)
    three="x" if x[3] else("O" if z[3] else 3)
    four="x" if x[4] else("O" if z[4] else 4)
    five="x" if x[5] else("O" if z[5] else 5)
    six="x" if x[6] else("O" if z[6] else 6)
    seven="x" if x[7] else("O" if z[7] else 7)
    eight="x" if x[8] else("O" if z[8] else 8)
    
    print(f"{zero} | {one} | {two}")
    print("--|---|--")
    print(f"{three} | {four} | {five}")
    print("--|---|--")
    print(f"{six} | {seven} | {eight}")

def sum(a,b,c):
    return a+b+c
def win(x,z):
    w=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in w:
        if(sum(x[i[0]],x[i[1]],x[i[2]])==3):
            print()
            print(f"PLAYER >> {p1} << WON")
            return 1
        if(sum(z[i[0]],z[i[1]],z[i[2]])==3):
            print()
            print(f"PLAYER >> {[p2]} << WON")
            return 0
    return 2    

x=[0,0,0,0,0,0,0,0,0]
z=[0,0,0,0,0,0,0,0,0]
turn=1
print("************************************ welcome to the Tic Tac Toe game **************************************** ")

p1=input("enter the name of first player: ")
p2=input("enter the name of second player: ")
while (True):
    printboard(x,z)
    if turn ==1:
        print(f"{p1}'s turn ")
        value=int(input(" enter the value: "))
        
        x[value]=1
    else:
        print(f"{p2}'s turn")
        value=int(input(" enter the value: "))
        
        z[value]=1
    check=win(x,z)
    if(check!=2):
        print()
        print("------------------------------------- Thanks for playing Tic Tac Toe ----------------------------------------")
        break

    turn=1-turn
