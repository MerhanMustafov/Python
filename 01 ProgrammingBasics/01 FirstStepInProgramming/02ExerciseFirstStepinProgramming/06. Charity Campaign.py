days_campaign = int(input())
confectioner = int(input())

cakes = int(input())
waffles = int(input())
pancake = int(input())

cake_price = cakes * 45
waffles_price = waffles * 5.80
pancake_price = pancake * 3.20

total_sum_for_day = (cake_price + waffles_price + pancake_price) * confectioner

total_sum_whole_campaign = total_sum_for_day * days_campaign

total_sum_after_expense = total_sum_whole_campaign - (total_sum_whole_campaign/8)
print(total_sum_after_expense)