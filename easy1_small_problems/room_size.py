# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet

# using float prevents error if input length or width are not integers
length_meters = float(input("Enter length of room in meters: "))
width_meters = float(input("Enter width of room in meters: "))


length_sq_ft = length_meters * 10.7639
width_sq_ft = width_meters * 10.7639


area_sq_meters = length_meters * width_meters
area_sq_ft = length_sq_ft * width_sq_ft

# The format specification {:.2f} ensures that the output is formatted to two decimal places.
print(f'Room area in sq meters: {area_sq_meters:.2f}!')
print(f'Room area in sq feet: {area_sq_ft:.2f}!')

# LS solution just multiplied area_square_meters with 10.7639 
# rather than storing L and W as feet and then doing are; more concise 
# + used {:.2f} format to print area

# Further Exploration:
# Modify the program to let the user specify the measurement type (meters or feet).
# Compute the area accordingly and print it and its conversion in parentheses.

# use .lower() to convert answer to all lower so case doesnt matter
ft_or_meters = input('Will you be inputting your measurements as feet or meters? Please enter feet OR meters: ').lower()

# based on user input (ft_or_meters) action is done
match ft_or_meters:
    case "feet":  
        length = float(input("Enter length of room: "))
        width = float(input("Enter width of room: "))
        if length and width > 0: # check length/width is >0
            area = length * width
            convert_meters = area / 10.7639
            print(f"The area of the room is: {area:.2f} square feet (and {convert_meters:.2f} square meters)!")
        else: # if length/width not greater than 0 raise error
            print(f'Try again! Length and width must be greater than 0.')
    case "meters":
        length = float(input("Enter length of room: "))
        width = float(input("Enter width of room: "))
        if length and width > 0:
            area = length * width
            convert_ft = area * 10.7639
            print(f"The area of the room is: {area:.2f} square meters (and {convert_ft:.2f} square ft)!")
        else:
            print(f'Try again! Length and width must be greater than 0.')
    case _: # error: incorrect input
        print("Try again! Please enter 1 of the two options, feet OR meters.")
