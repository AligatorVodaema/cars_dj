from typing import Tuple
from cars.models import *
from typing import List


def get_and_zip_car_values(value1: str, value2: str) -> List[Tuple, ]:
    """Get from db all cars with filer (is_reserved, is_published),
    extract 2 list values and zip them for form-menu"""
    
    cars_query_set = Car.objects.filter(is_reserved=False, is_published=True)
    qs_values1 = cars_query_set.values_list(value1, flat=True)
    qs_values2 = cars_query_set.values_list(value2, flat=True)

    return list(zip(qs_values1, qs_values2))