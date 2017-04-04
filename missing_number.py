def missing_number(first_list, second_list):
	answer_to_return = 0
	a = len(first_list)
	b = len(second_list)
	if (not first_list and not second_list) or (a == b) :
		answer_to_return = 0
	else:
		first_list.sort()
		second_list.sort()


		if(a > b):
			answer_to_return = first_list[-1]
		else:
			answer_to_return = second_list[-1]
	return answer_to_return
