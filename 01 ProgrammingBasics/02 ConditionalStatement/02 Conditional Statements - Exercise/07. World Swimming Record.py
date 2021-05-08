from math import fabs
from math import floor

world_record_sec = float(input())
length_m = float(input())
seconds_for_1metr_swimming = float(input())

trqbva_da_prepluva = length_m * seconds_for_1metr_swimming
na_vseki15 = floor(length_m / 15) * 12.5

obshtoto_vr = trqbva_da_prepluva + na_vseki15
if world_record_sec <= obshtoto_vr:
    print(f"No, he failed! He was {fabs(world_record_sec - obshtoto_vr):.2f} seconds slower.")
if world_record_sec > obshtoto_vr:
    print(f"Yes, he succeeded! The new world record is {fabs(obshtoto_vr):.2f} seconds.")
