def num_finder(list_1,list_2):
  	
  	# Initialize variable away that holds missing digit to zero
	away = 0
	
	# If list_1 is smaller, find and show the missing number
	if len(list_1) < len(list_2):
		absent = (set(list_2) - set(list_1))
		away = absent.pop()
		return away
	
	# If list_2 is smaller, find and show the missing number 
	elif len(list_2) < len(list_1):
		absent = (set(list_1) - set(list_2))
		away = absent.pop()
		return away
	
	else:
	  return 0


