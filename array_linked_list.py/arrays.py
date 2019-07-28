

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity
        pass


# Double the size of the given array
def resize_array(array):
    #double capacity in new array
    new_capacity = array.capacity * 2
    #create new array storagew in similar fashion to above
    new_storage = [None] * new_capacity
    #populates new array with old values
    for i in range(array.capacity):
        new_storage[i] = array.storage[i]
    #changes old storage to new    
    array.storage = new_storage
    #changes old capacity to new
    array.capacity = new_capacity    
    


# Return an element of a given array at a given index
def array_read(array, index):
    if index > array.count:
        print('Error. Element' + str(index) + ' is out of range.') 
        return None
    return array.storage[index]  


# Insert an element in a given array at a given index
def array_insert(array, value, index):
    # Throw an error if array is out of the current count
    if index > array.count:
        print("Error, index" + str(index) + "out of range")
        return  None
    if array.capacity <= array.count:
        resize_array(array)
    # Resize the array if the number of elements is over capacity

    # Move the elements to create a space at 'index'
    # Think about where to start!
    for i in range(array.count, index, -1):
        array.storage[i] = array.storage[i - 1]
    array.storage[index] = value  
    array.count += 1
    # Add the new element to the array and update the count


# Add an element to the end of the given array
def array_append(array, value):
    array_insert(array, value, array.count + 1)
    # Hint, this can be done with one line of code
    # (Without using a built in function)



# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(array, element):
    removed = False
    for i in range(array.count):
        if removed:
            array.storage[i - 1] = array.storage[i]
        elif array.storage[i] == element:
            removed = True   

    if removed:
        array.count -= 1
        array.storage[array.count] = None
    else:
        print('Error, element' + str(element) + 'not found')    


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop(array, index):
    if index > array.count:
        print("Error, index" + str(index) + "is out of range")
        return None

    return_value = array.storage[index]
    for i in range(index + 1, array.count):
        array.storage[i -1] = array.storage[i]

    array.count -= 1  
    array.storage[array.count]      

    return return_value


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.storage[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
array_pop(arr, 0)
array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
array_insert(arr, "STRING2", 1)
array_insert(arr, "STRING3", 2)
array_print(arr)
