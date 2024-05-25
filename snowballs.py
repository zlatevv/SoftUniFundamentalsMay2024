snowballs = int(input())
best_snowball = 0
weight_for_print = "" 
time_needed_for_print = ""
quality_for_print = ""
for _ in range(snowballs):
    weight = int(input())  
    time_needed = int(input())
    quality = int(input())
    snowball_value = (weight / time_needed) ** quality
    if snowball_value > best_snowball:
        best_snowball = snowball_value
        weight_for_print = weight  
        time_needed_for_print = time_needed
        quality_for_print = quality
print(f"{weight_for_print} : {time_needed_for_print} = {int(best_snowball)} ({quality_for_print})")