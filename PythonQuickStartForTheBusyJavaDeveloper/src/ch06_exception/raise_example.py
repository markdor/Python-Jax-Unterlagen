def ensure_value_in_range(value, lower_bound, upper_bound):
    if value < lower_bound or value > upper_bound:
        raise ValueError("out of bounds")
    pass