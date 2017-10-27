for stumber in range(1,1000+1):
	if stumber %3==0:
		print("Burrito")
	elif stumber %5==0:
		print("Cheeto")
	elif stumber %3==0 and stumber %5==0:
		print("BurritoCheeto")
	elif stumber %7==0:
		print("Veto")
	elif stumber %3==0 and stumber %7==0:
		print("BurritoCheeto")
	elif stumber %5==0 and stumber %7==0:
		print("CheetoVeto")
	elif stumber %3==0 and stumber %5==0 and stumber %7==0:
		print("BurritoCheetoVeto")
	else:
		print(stumber)
