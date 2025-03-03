"""
Python Match Case Statement Tutorial
-----------------------------------
The match case statement (introduced in Python 3.10) is a structural pattern matching
feature that provides a more elegant way to handle multiple conditions compared to
if-elif-else chains.
"""

# Basic Match Case Example
def check_number(number):
    match number:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:  # Default case (like else)
            return "Something else"

# Example with multiple values in one case
def check_grade(grade):
    match grade.upper():
        case "A" | "A+" | "A-":
            return "Excellent"
        case "B" | "B+" | "B-":
            return "Good"
        case "C" | "C+" | "C-":
            return "Fair"
        case "D" | "D+" | "D-":
            return "Poor"
        case "F":
            return "Failed"
        case _:
            return "Invalid grade"

# Pattern matching with sequences (lists/tuples)
def analyze_coordinates(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y-axis at y={y}"
        case (x, 0):
            return f"X-axis at x={x}"
        case (x, y):
            return f"Point at x={x}, y={y}"
        case _:
            return "Not a point"

# Pattern matching with mapping (dictionaries)
def process_user_data(data):
    match data:
        case {"name": str(name), "age": int(age)} if age >= 18:
            return f"{name} is an adult"
        case {"name": str(name), "age": int(age)}:
            return f"{name} is a minor"
        case {"name": str(name)}:
            return f"{name}'s age is unknown"
        case _:
            return "Invalid user data"

# Complex pattern matching with classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def analyze_point(point):
    match point:
        case Point(x=0, y=0):
            return "Point is at origin"
        case Point(x=x, y=y) if x == y:
            return f"Point is on line x=y at {x}"
        case Point(x=x, y=y):
            return f"Point is at x={x}, y={y}"
        case _:
            return "Not a valid point"

# Example usage
if __name__ == "__main__":
    # Testing number matching
    print("\nNumber matching:")
    print(check_number(1))  # Output: One
    print(check_number(5))  # Output: Something else

    # Testing grade matching
    print("\nGrade matching:")
    print(check_grade("A+"))  # Output: Excellent
    print(check_grade("C"))   # Output: Fair

    # Testing coordinate matching
    print("\nCoordinate matching:")
    print(analyze_coordinates((0, 0)))  # Output: Origin
    print(analyze_coordinates((5, 0)))  # Output: X-axis at x=5

    # Testing dictionary matching
    print("\nDictionary matching:")
    user1 = {"name": "Alice", "age": 20}
    user2 = {"name": "Bob", "age": 15}
    print(process_user_data(user1))  # Output: Alice is an adult
    print(process_user_data(user2))  # Output: Bob is a minor

    # Testing class matching
    print("\nClass matching:")
    p1 = Point(0, 0)
    p2 = Point(3, 3)
    print(analyze_point(p1))  # Output: Point is at origin
    print(analyze_point(p2))  # Output: Point is on line x=y at 3
