import random

#Διαβάζω διάσταση πίνακα
dim = int(input("Enter the dimensions:"))
#Επειδή ΄θέλουμε τετράδες από άσσους άρα πρέπει το τετράγωνο να είναι τουλάχιστον 4χ4
while (dim<=3):
    print("Enter a number larger than 3")
    dim = int(input("Enter the dimensions:"))
dimensions=dim**2
#Πρέπει να γεμ΄ίζω τις μισές θέσεις με 1 οπότε βρίσκω τις μισές θέσεις
if dimensions % 2 == 1:
	theseis = round(dimensions/2)+1
else:
	theseis = round(dimensions/2)
SumOfOnes=0
for i in range(100):
	table = []
    #Μετρητές για τα 1 και τα 0
	pl1 = 0
	pl0 = 0
    #Όσες είναι οι πλευ΄ρες τόσες θα είναι και οι λίστες (π.χ αν η πλευρά είναι 3 , θέλει 3 λίστες με 3 στοιχεία η κάθε μία μέσα κ.ο.κ)
	for j in range(dim):
		lis = []
		for k in range(dim):
			arithmos = random.randint(0,1)
			if (arithmos == 1 and pl1 < theseis):
				lis.append(arithmos)
				pl1 = pl1 + 1
			elif (arithmos == 0 and pl0 < dimensions-theseis):
				lis.append(arithmos)
				pl0 = pl0 + 1
			elif (pl0 == dimensions-theseis):
				lis.append(1)
			elif (pl1 == theseis):
				lis.append(0)
		table.append(lis)
#Ψάχνουμε τις οριζόντιες τετράδες, θέλουμε μετρητή για ΣΥΝΕΧΟΜΕΝΟΥΣ άσσους και μετρητή για τετράδα

	horizontal = 0
	for i in range(dim):
		cons1 = 0
		horizontalcons1=0
		for j in range(dim):
			if table[i][j]==1:
				cons1 += 1
				if cons1>=4:
					horizontalcons1=cons1-3
			else:
				cons1=0
		horizontal=horizontal+horizontalcons1

	vertical = 0
	for i in range(dim):
		cons1=0
		verticalcons1=0
		for j in range(dim):
			if table[j][i]==1:
				cons1 += 1
				if cons1>=4:
					verticalcons1=cons1-3
			else:
				cons1=0
		vertical=vertical+verticalcons1

	diagonal=0
	for i in range(dim):
		for j in range(dim):
            #Για να μην βγει εκτος table range
			if (i<dim-3 and j<dim-3):
				if (table[i][j]==1 and table[i+1][j+1]==1 and table[i+2][j+2]==1 and table[i+3][j+3]==1):
					diagonal=diagonal+1
			if (i<dim-3 and j>dim-3):
				if (table[i][j]==1 and table[i+1][j-1]==1 and table[i+2][j-2]==1 and table[i+3][j-3]==1):
					diagonal=diagonal+1
	SumOfOnes = SumOfOnes + diagonal + vertical + horizontal

OnAverage = SumOfOnes/100
print(*table, sep="\n")
print(OnAverage)
print(horizontal, vertical, diagonal)
