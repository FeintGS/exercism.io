def slices(series, length):
    if length <= 0:
        raise ValueError("Argument must be a positive integer >= 1")
    elif length > len(series):
        raise ValueError("Argument must not exceed length of series")

    slices = []
    for i in range(length, len(series)+1):
        slices.append(series[i-length : i])
    return slices
