import statistics

def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    for y in range(0,len(data), n):
        window = data[y: y + n]
        maximums.append(max(window))
    return maximums

def window_average(data: list, n: int) -> list:
    avg = []
    for y in range (0,len(data), n):
        window = data[y:y + n]
        averages = sum(window) / len(window)
        avg.append((round(window_average, 2)))
    return avg


def window_stddev(data: list, n: int) -> list:
    if data == []:
        return data
    stdevs = []
    for y in range(0, len(data), n):
        window = data[y:y + n]
        if len(window) > 1:
            std_dev = statistics.stdev(window)
            stdevs.append(round(std_dev, 2))
        else:
            stdevs.append(0)
    return stdevs