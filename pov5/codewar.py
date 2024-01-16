def sea_sick(sea):
    sea_list = list(sea)
    counter = 0
    for i in range(len(sea_list)-1):
        if sea_list[i] != sea_list[i + 1]:
            counter += 1
    percentage = counter / len(sea_list) * 100
    return "Throw Up" if percentage > 20 else "No Problem"

