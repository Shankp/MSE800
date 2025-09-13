
if __name__ == "__main__":
    data = ['a5','a2','b1', 'b3','c2']
    sorted_data = sorted(data, key=lambda x: (x[0], x[1:]))
    print(sorted_data)

#sorted(data, key=lambda x: (x[0], x[1:])) --> this lambda function creates keys to be used for sorting.
#Here x[0] will be used for sorting first, if the same values are available for te first value, 
#x[1:] will be used to do further sorting starting with the second value.