def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def are():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {are()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
