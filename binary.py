
def b_search(array, item):
    """
    used for sorting ascending numerical arrays
    """
    while True:
        mid_index = len(array)//2 #gets middle of array
        if array[mid_index] == item: #if array middle is itme then return index
            print(array[mid_index])
            return mid_index
        elif array[mid_index] > item: # if array middle is bigger than item, set array to itself left side
            array = array[:mid_index]
        elif array[mid_index] < item: # if array middle is bigger than item, set array to itself right side
            array = array[mid_index:]
        print(array)
# add not found error
listt = []

for i in range(0, 1000):
    listt.append(i)

found = b_search(listt, int(input("item\n> ")))
