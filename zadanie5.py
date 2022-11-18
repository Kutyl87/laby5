def find_the_average(array):
    return [sum(array)/len(array) for elem in array]


def try_to_convert_elements(array):
    try:
        temporary_array = [int(elem) for elem in array]
        return find_the_average(temporary_array)
    except ValueError:
        return "Wrong type of the data"
    
def try_elements(list_of_arrays):
    new_array  = []
    for array in list_of_arrays:
        try:
            new_array.append(find_the_average(array))
        except ZeroDivisionError:
            new_array.append("You cannot divide by 0")
        except TypeError:
            new_array.append(try_to_convert_elements(array))
    return new_array



print(try_elements([[1,2,3],[4,5,6],[7,8,9],[],[3,4,5],["12",1,2],[],["12a",1,2]]))

