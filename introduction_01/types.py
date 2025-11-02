print(type("Hello"))       # str (string)
print(type(123))           # int (integer)
print(type(3.14))          # float (decimal number)
print(type(True))          # bool (boolean)
print(type([1, 2, 3]))     # list
print(type((1, 2, 3)))     # tuple
print(type({1, 2, 3}))     # set
print(type({"name": "Asif", "age": 20}))  # dict (dictionary)
print(type(None))          # NoneType (represents absence of value)
print()

print("***********************************************************************")

# data_types_demo.py
def demo_data_types():
    # ---------- Numeric ----------
    age = 30                # int
    price = 19.99           # float
    imaginary = 1 + 2j      # complex

    # ---------- Sequence ----------
    name = "Alice"          # str
    scores = [85, 92, 78]   # list (mutable)
    point = (10, 20)        # tuple (immutable)

    # ---------- Mapping ----------
    person = {"name": "Bob", "age": 25}  # dict

    # ---------- Set ----------
    unique_ids = {101, 102, 103}          # set (mutable)
    frozen_ids = frozenset([201, 202])    # frozenset (immutable)

    # ---------- Boolean ----------
    is_active = True

    # ---------- None ----------
    middle_name = None

    # ---- Print everything with its type ----
    variables = [
        ("age", age),
        ("price", price),
        ("imaginary", imaginary),
        ("name", name),
        ("scores", scores),
        ("point", point),
        ("person", person),
        ("unique_ids", unique_ids),
        ("frozen_ids", frozen_ids),
        ("is_active", is_active),
        ("middle_name", middle_name),
    ]

    print("=== Python Data Types Demo ===\n")
    for label, value in variables:
        print(f"{label:12} = {value!r:20}  →  type: {type(value).__name__}")

if __name__ == "__main__":
    demo_data_types()