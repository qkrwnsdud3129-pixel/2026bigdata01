def entrance_fee(ages: list) -> int:
    """
    Calculates the total admission fee for a group based on their ages.

    Args:
        ages (list): A list of ages for the visitors.

    Returns:
        int: The total calculated entry fee for the amusement park.
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
