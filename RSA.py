p = 1061
q = 1283

n = p * q

phi = (p - 1) * (q - 1)
#print(phi)
def isPrime(num):
    prime = True
    if num>1:
        for i in range(2,num//2):
            if num%i==0:
                prime= False
                break
    if prime == True:
        return True
    else:
        return False



def gcd(a, b):
    while a != b:
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a



def E_gen(fi):

    for i in range(20,fi):
        if gcd(i, fi) == 1 and isPrime(i)==True:
            return i
            break

        else:
            continue



e=E_gen(phi)

#e = 21

def D_gen(fi):
    for d in range(10,fi):
        if (d*e)%fi == 1:
            return d
            break
        else:
            continue


d = D_gen(phi)

#d = 129421

print("Klucz publiczny to: " + str(e) + " oraz " + str(n))
print("Klucz prywatny  to: " + str(d) + " oraz " + str(n))

f = open("tekst.txt","r+")
txt = f.read()
txt = txt.replace(" ", "")

ciag = ""
for i in txt:
    ciag = ciag + str(ord(i)-97)

    ciag = ciag + " "

#print(ciag)

x = ciag.split(" ")
x = x[:len(x)-1]

#print(str(x))

for i in range( len(x)):
    x[i] = int(x[i])

print(str(x))

def szyfrowanie(lista):
    for i in range(len(lista)):
        lista[i] = (lista[i]**e)%n


    return lista

encrypted = szyfrowanie(x)
print(str(encrypted))


def deszyfrowanie(lista):
    for i in range(len(lista)):
        lista[i] =  (lista[i]**d)%n
        lista[i] = chr(lista[i]+97)
    listToStr = ''.join([str(elem) for elem in lista])
    return listToStr

decrypted = deszyfrowanie(encrypted)
print(str(decrypted))


