import utils
import converters
from utils import find_max_number
from converters import kg_to_lbs,lbs_to_kg

max_number = find_max_number([5, 8, 3, 4, 13, 6, 32, 7, 2, 4])
lbs = kg_to_lbs(70)
kg = lbs_to_kg(70)
print(max_number, lbs, kg)
