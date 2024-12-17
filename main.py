"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    file= open(filename)
    for line in file:
        data.append(line)

    #filter out all nondigits
    data = filter_nondigits(data)

    #filter all outliers
    data = filter_outliers(data)
    
    #calculate window_max

    maximums = window_max(data, 6)

    #calculate window_average
    avg = window_average(data, 6)

    #calculate window_stddev
    stdevs = window_stddev(data, 6)
    
    #save the plots

    plt.savefig(maximums, 'images/maximums.png')
    plt.savefig(avg, 'images/averages.png')
    plt.savefig(stdevs, 'images/stdevs.png')
    plt.close()
    #return all 3 lists
    return maximums, avg, stdevs


if __name__ == "__main__":
    run("data/data1.txt")
