import os

def main():
    with open('/Users/mugki/Desktop/twitch earnings /algorithms/ed.txt','r') as f :
        z=f.read().split('\n')
        #print(z)  
    inp = input('Name:').lower()
    os.system('cls||clear')
    print("inp output:"+inp)
    try:
        #foundarr = []
        for x in z:
            d = x.split(' ')[1].lower()
            if inp in (d):
                b = x.split(' ')
                #ell = 'Rank: '+b[0]+"\n",'Name: '+b[1]+"\n","Earnings: "+('$'+b[3])+"\n"
                #foundarr.append(ell)
                print('Rank: '+b[0]+"\n",
                'Name: '+b[1]+"\n",
                "Earnings: "+('$'+b[3])+"\n")
    except:
        print('none found')
    input('press any to continue')
    main()


main()