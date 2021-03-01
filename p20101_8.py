import urllib.request
import json

def kleidi(dic):
    line = []
    for key in dix.keys():
        line.append(key)

    return line

def timh(symbolismos, symbols_comp=["EUR"]):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}&e=CCCAGG'\
            .format(symbolismos.upper(), ','.join(symbols_comp).upper())
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html)
    return data

arxeio = input("Enter file location: ")
arxeio1 = open(arxeio,'r')
arxeio1 = arxeio1.read()
arxeio1 = json.loads(arxeio1)
x=getKeys(arxeio1)
tmp={}

for i in x:
    temp1 = timh(i)
    temp[i] = temp1["EUR"]*arxeio1[i]

print('Your web-portofolio is: ')
print(arxeio1)
print('Which in euros is: ')
print(temp)
