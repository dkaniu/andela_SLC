def find_min_max(initial_list):

	result_list = []
	result_list.append(min(initial_list))
	result_list.append(max(initial_list))

	if (max(initial_list) == min(initial_list)):
		answer = [len(initial_list)]

	else:
		answer = result_list

	return answer
