

def ft_count_harvest_recursive(i=0, day=0):
    if (i == 0):
        day = int(input("Days until harvest: "))
    if (i == day):
        print("Harvest time!")
        return
    print(f"Day {i+1}")
    return (ft_count_harvest_recursive(i+1, day))
