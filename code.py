n = int(input("Inserisci il numero da scomporre: "))
x = 2 # divisore
i = n 
a = 0 # n volte scomposto
while i > 0:
	if n == x and a == 0:
		print( str(n) + " è un numero primo")
		i = 0
	else:
		if i % x == 0:
			i //= x # divisione senza virgola
			print(x)
			x = 2
			a += 1
		else:
			x += 1