def search_range_of_numbers(start_number, end_number):
    """[summary]
    Args:
        start_number ([int]): [beginning of the range]
        end_number ([int]): [end of range]

    Returns:
        [list]: [returns a list of lists from the range]
    """
    number_digits = []
    for i in range(start_number, end_number + 1): 
        single_list = [] 
        for x in str(i): 
            single_list.append(int(x))
        number_digits.append(single_list)
    return number_digits
    
def check_equal(lst):
    """[summary]
    Args:
        lst ([list]): [list of int]

    Returns:
        [boolean]: [returns true if there are two identical values next to each other]
    """
    last = lst[0]
    for num in lst[1:]:
        if num == last:
            return True
        last = num
    return False

def check_growing(lst):
    """[summary]
    Args:
        lst ([list]): [list of int]

    Returns:
        [boolean]: [returns true if no number decreases from left to right]
    """
    last = lst[0]
    for num in lst[1:]:
        if num < last:
            return False
        last = num
    return True

def search_range_key(list):
    """[summary]

    Args:
        list ([list]): [list number of digits]

    Returns:
        [int]: [takes a range as a list, returns the length of the list of ranges]
    """
    equal =[]
    for number_list in list:
        if check_equal(number_list) and check_growing(number_list):
            equal.append(number_list)
    answer = len(equal)
    return answer

def possible_solutions(start_number=265275, end_number=781584):
    """[summary]
        main function
    Args:
        start_number (int, optional): [beginning of the range]. Defaults to 265275.
        end_number (int, optional): [end of range]. Defaults to 781584.

    Returns:
        [str]: [answer string]
    """
    if len(str(start_number)) and len(str(end_number)) == 6:
        search_ranges = search_range_of_numbers(start_number=start_number, end_number=end_number)
        answer = search_range_key(search_ranges)
    return f"liczba kodów spełniająca warunki: {answer}" 


if __name__ == '__main__':
    print(possible_solutions())


        
    