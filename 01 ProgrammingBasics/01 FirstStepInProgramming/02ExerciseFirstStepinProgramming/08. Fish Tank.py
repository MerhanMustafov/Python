length_sm = int(input())
width_sm = int(input())
height_sm = int(input())
persentage_fulled_volume = float(input())

volume_aquarium = length_sm * width_sm * height_sm
totall_litter_capacity = volume_aquarium * 0.001
percentage = persentage_fulled_volume * 0.01
required_litters = totall_litter_capacity * (1-percentage)

print(required_litters)
