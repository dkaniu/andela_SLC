__author__ = 'kaniu'
def data_type(input_to_test):
	test_result = input_to_test
	if type(input_to_test) == None:
		test_result = 'no value'
	if isinstance(input_to_test, str):
		test_result = len(input_to_test)
	if isinstance(input_to_test, int):
		if input_to_test == 100:
			test_result = 'equal to 100'
		elif input_to_test > 100:
			test_result = 'more than 100'
		else:
			test_result = 'less than 100'
	if isinstance(input_to_test, float):
		test_result = 'float'
	if isinstance(input_to_test, list):
		if len(input_to_test) < 3:
			return None
		else:
			test_result = input_to_test[2]
	if isinstance(input_to_test, bool):
		test_result = input_to_test
	return test_result
