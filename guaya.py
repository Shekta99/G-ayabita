import random
import sys

def dado():
    return(random.randint(1,6))

def jugador1(jug1,jug2,mesa,dad):
    if dad==1:
        print 'Jugador1'
        print 'Dado=1'
        print 'mesa='+str(mesa+mini())
        print 'jugador1='+str(jug1-mini())+'\n'
        com(jug1-mini(),1)
        jugador2(jug1-mini(),jug2,mesa+mini(),dado())
    elif dad==6:
        print 'Jugador1'
        print 'Dado=6'
        print 'mesa='+str(mesa+mini())
        print 'jugador1='+str(jug1-mini())+'\n'
        com(jug1-mini(),1)
        jugador2(jug1-mini(),jug2,mesa+mini(),dado())
    elif dad==5:
        print 'Jugador1'
        print 'Dado=5'
        if mesa-mini()>=0:
            print 'mesa='+str(mesa-mini())
            print 'jugador1='+str(jug1+mini())+'\n'
            jugador2(jug1+mini(),jug2,mesa-mini(),dado())
        else:
            print 'mesa='+str(mesa)
            print 'jugador1='+str(jug1) +'\n'
            jugador2(jug1,jug2,mesa,dado())
    elif dad==2:
        print 'Jugador1'
        print 'Dado=2'
        if dado()>2:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador1='+str(jug1+mini()) +'\n'
                jugador2(jug1+mini(),jug2,mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador1='+str(jug1) +'\n'
                jugador2(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador1='+str(jug1-mini())+'\n'
            com(jug1-mini(),1)
            jugador2(jug1-mini(),jug2,mesa+mini(),dado())
    elif dad==3:
        print 'Jugador1'
        print 'Dado=3'
        if dado()>3:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador1='+str(jug1+mini())+'\n'
                jugador2(jug1+mini(),jug2,mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador1='+str(jug1)+'\n'
                jugador2(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador1='+str(jug1-mini())+'\n'
            com(jug1-mini(),1)
            jugador2(jug1-mini(),jug2,mesa+mini(),dado())
    elif dad==4:
        print 'Jugador1'
        print 'Dado=4'
        if dado()>4:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador1='+str(jug1+mini())+'\n'
                jugador2(jug1+mini(),jug2,mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador1='+str(jug1)+'\n'
                jugador2(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador1='+str(jug1-mini())+'\n'
            com(jug1-mini(),1)
            jugador2(jug1-mini(),jug2,mesa+mini(),dado())
            
            
            
def jugador2(jug1,jug2,mesa,dad):
    if dad==1:
        print 'Jugador2'
        print 'Dado=1'
        print 'mesa='+str(mesa+mini())
        print 'jugador2='+str(jug2-mini())+'\n'
        com(jug2-mini(),2)
        jugador1(jug1,jug2-mini(),mesa+mini(),dado())
    elif dad==6:
        print 'Jugador2'
        print 'Dado=6'
        print 'mesa='+str(mesa+mini())
        print 'jugador2='+str(jug2-mini())+'\n'
        com(jug2-mini(),2)
        jugador1(jug1,jug2-mini(),mesa+mini(),dado())
    elif dad==5:
        print 'Jugador2'
        print 'Dado=5'
        if mesa-mini()>=0:
            print 'mesa='+str(mesa-mini())
            print 'jugador2='+str(jug2+mini())+'\n'
            jugador1(jug1,jug2+mini(),mesa-mini(),dado())
        else:
            print 'mesa='+str(mesa)
            print 'jugador2='+str(jug2)+'\n'
            jugador1(jug1,jug2,mesa,dado())
    elif dad==2:
        print 'Jugador2'
        print 'Dado=2'
        if dado()>2:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador2='+str(jug2+mini())+'\n'
                jugador1(jug1,jug2+mini(),mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador2='+str(jug2)+'\n'
                jugador1(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador2='+str(jug2-mini())+'\n'
            com(jug2-mini(),2)
            jugador1(jug1,jug2-mini(),mesa+mini(),dado())
    elif dad==3:
        print 'Jugador2'
        print 'Dado=3'
        if dado()>3:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador2='+str(jug2+mini())+'\n'
                jugador1(jug1,jug2+mini(),mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador2='+str(jug2)+'\n'
                jugador1(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador2='+str(jug2-mini())+'\n'
            com(jug2-mini(),2)
            jugador1(jug1,jug2-mini(),mesa+mini(),dado())
    elif dad==4:
        print 'Jugador2'
        print 'Dado=4'
        if dado()>4:
            if mesa-mini()>=0:
                print 'mesa='+str(mesa-mini())
                print 'jugador2='+str(jug2+mini())+'\n'
                jugador1(jug1,jug2+mini(),mesa-mini(),dado())
            else:
                print 'mesa='+str(mesa)
                print 'jugador2='+str(jug2)+'\n'
                jugador1(jug1,jug2,mesa,dado())
        else:
            print 'mesa='+str(mesa+mini())
            print 'jugador2='+str(jug2-mini())+'\n'
            com(jug2-mini(),2)
            jugador1(jug1,jug2-mini(),mesa+mini(),dado())
    

def mini():
    return(100)

def com(apues,n):
    if apues<=0:
        print 'game over jugador'+str(n)+'\n'
        sys.exit(0)


def main():
    print 'hola mi guayabita::'
    jugador1(600,600,1000,dado())


main()


