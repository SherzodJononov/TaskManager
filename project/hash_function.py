
# Hash function

numberlist = ['0','1','2','3','4','5','6','7','8','9']
symbollist = ['.' , ',' , '/' , '~' , '!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' , ')' , '-' , '=' , '+' , '*' , '_']
smallletterlist = ['a','b','c','d','e','f','g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
bigletterlist = ['A','B','C','D','E','F','G','H', 'I','J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

oursymbols = numberlist + symbollist + smallletterlist + bigletterlist

def onesymbol(symbol):
    try:
        x = 0
        for i in range(len(oursymbols)):
            if oursymbols[i] == symbol:
                x = i
                break
        return x
    except:
        print("Try again")

def Hash(password):
    try:
        H = []
        H.append(0)

        for i in range(1,len(password)):
                H.append(H[i-1] + onesymbol(password[i])**2 % len(oursymbols))

        x = ''
        for i in range(len(H)):
            x = x + str(H[i])

        return x
    except:
        print("Try again")
