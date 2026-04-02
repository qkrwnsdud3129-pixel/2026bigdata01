def entrance_fee(ages) -> int:
    """
    Calculates the admission fee for the amusement park.
    Parameters :
        ages : List of Ages
    Returns:
        int: The total calculated entry fee.
    """
    kid, adult, senior = 5000, 10000, 7000
    total_free = 0
    for age in ages:
        if age >= 65:
            total_free = total_free + senior
        elif age >= 19:
            total_free = total_free + adult
        else:
            total_free = total_free + kid
    return total_free
