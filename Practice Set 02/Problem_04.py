first_side = int(input("Enter first side: "))
second_side = int(input("Enter second side: "))
third_side = int(input("Enter third side: "))

if first_side <= 0 or second_side <= 0 or third_side <= 0:
    print("Triangle: Invalid")

elif (first_side + second_side <= third_side or
      second_side + third_side <= first_side or
      first_side + third_side <= second_side):

    print("Triangle: Invalid")

else:
    print("Triangle: Valid")

    if first_side == second_side and second_side == third_side:
        print("Type: Equilateral")

    elif first_side == second_side or second_side == third_side or first_side == third_side:
        print("Type: Isosceles")

    else:
        print("Type: Scalene")

    if first_side >= second_side and first_side >= third_side:
        largest_side = first_side
        other_side_one = second_side
        other_side_two = third_side

    elif second_side >= first_side and second_side >= third_side:
        largest_side = second_side
        other_side_one = first_side
        other_side_two = third_side

    else:
        largest_side = third_side
        other_side_one = first_side
        other_side_two = second_side

    if largest_side ** 2 == other_side_one ** 2 + other_side_two ** 2:
        print("Angle Classification: Right-Angled")

    elif largest_side ** 2 < other_side_one ** 2 + other_side_two ** 2:
        print("Angle Classification: Acute-Angled")

    else:
        print("Angle Classification: Obtuse-Angled")
