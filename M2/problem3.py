a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")

    p_arr = []                                  # UCID: krs
                                                # Date: 9/21/23
    
    for item in arr:                            # For-loop to iterate through elements of array.
        if isinstance(item, (int, float)):     
            p_arr.append(abs(item))             # Take the absolute value and append it to new positive array.
        else:
            p_arr.append(str(abs(int(item))))   # Convert to integer, take the absolute value, and convert back to string and append.
    
    print(p_arr)

    print(type(p_arr[0]))    # type() of the output data to ensure the result is positive AND the same datatype as the input value


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)