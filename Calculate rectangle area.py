def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_rectangle_area(length, width)

# Display the result
print(f"The area of the rectangle with length {length} and width {width} is: {area}")
