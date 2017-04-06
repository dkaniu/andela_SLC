class BinarySearch(list):
  def __init__(self, a, b):
    super(BinarySearch, self).__init__()
    for item in range(1, a+1):
      self.append(item * b)
      self.a = len(self)

def search(self, search_value):
  first_item = 0
  last_item = len(self) - 1
  counter = 0

  while first_item <= last_item:
		mid = (first_item + last_item)//2
		if self[mid] == search_value:
			search_value = mid
		else:
			counter = counter + 1
      if search_value < self[mid]:
      	last_item = mid - 1
      else:
      	first_item = mid + 1

  return {"counter" : counter, "index": search(search_value)}
