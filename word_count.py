__author__ = 'kaniu'
def word_count(a):
	#convert the string into a list
	convert_list = a.split()
	convert_list.sort()

	#get a set to remove the dublicates
	set_list = set(convert_list)

	#return the set to a list
	unique_list = list(set_list)


	#use the occurrence of unique list as the key values for the other list
	for unique_item in unique_list:
		a = unique_item
		b = convert_list.count(unique_item)
		print(a, ':',  b)
