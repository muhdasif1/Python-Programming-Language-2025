# variables_demo.py

def variables():
    print("=== Python Variables ===\n")

    # 1. Basic assignment
    name = "Alice"
    age = 28
    height = 5.6
    is_student = False

    # 2. Multiple assignment
    x, y, z = 10, 20, 30

    # 3. Same value to many
    a = b = c = 100

    # 4. Swapping
    print(f"Before swap: x={x}, y={y}")
    x, y = y, x
    print(f"After swap:  x={x}, y={y}")

    # 5. Dynamic typing
    counter = 5
    print(f"counter = {counter} ({type(counter)})")
    counter = "five"
    print(f"counter = {counter} ({type(counter)})")

    # 6. Print all
    print("\n--- Variable Summary ---")
    vars_list = [
        ("name", name),
        ("age", age),
        ("height", height),
        ("is_student", is_student),
        ("x, y, z", f"{x}, {y}, {z}"),
        ("a = b = c", a),
    ]

    for label, value in vars_list:
        print(f"{label:15}: {value} → {type(value).__name__}")

    # 7. Delete a variable
    del counter
    # print(counter)  # Would raise NameError

if __name__ == "__main__":
    variables()