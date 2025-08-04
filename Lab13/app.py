import math


def calculate_circle_area(radius:float) -> float:
    """Calculates the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * (radius**2)


calculate_circle_area("maia")
