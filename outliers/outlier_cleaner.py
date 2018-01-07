#!/usr/bin/python
import math


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    for i in xrange(len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], abs(net_worths[i]-predictions[i])/net_worths[i]))

    times_to_iterate = int(math.ceil(len(predictions)*.1))

    for i in xrange(times_to_iterate):
        a,b = max(enumerate(cleaned_data), key=lambda x: x[1][2])
        cleaned_data.pop(a)

    return cleaned_data

