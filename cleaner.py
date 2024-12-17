def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    only_digits = []
    for element in data:
        #remove whitespace
        element = element.strip()
        if element.strip().isdigit() == True: 
                element = element.strip()
        #if element is a digit append to only_digits list
                only_digits.append(int(element))

    return only_digits
   
    
def filter_outliers(data: list) -> list:
    """
    Filter all outliers from list of integers

    Args:
        data (list[int]): list of integers representing heart rate samples.

    Returns:
        list[int]: list of integers, with all outliers removed

    """
    new_data = []
    for element in data:
        if element > 30 and element < 250: 
                new_data.append(element)
    return new_data