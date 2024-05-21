
def generate_circle_points(dice_value, dice_number):
    points = []
    for _ in range(dice_number):
        dice_value += 50
        points.append(dice_value)
    return points 

