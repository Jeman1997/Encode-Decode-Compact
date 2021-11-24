alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def enorde(txt,shift,erd):
    otxt=''
    if erd.lower()=='decode':
        shift=shift*(-1)
    for x in list(txt):
        otxt=otxt+alp[alp.index(x)+shift]
    print(otxt)
    return
enorde(erd=input("Encode or decode:\n"),txt=input("Enter the message:\n"),shift=int(input("Enter the shift:\n")))