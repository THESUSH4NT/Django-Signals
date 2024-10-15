# Topic: Custom Classes in Python


# Initializing
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

# Iterating over an instance
    def __iter__(self):     
        yield {'length': self.length}
        yield {'width': self.width}

# Example:
if __name__ == "__main__":
    my_rectangle = Rectangle(40, 20)

    # Iterating over the rectangle instance
    for dimension in my_rectangle:
        print(dimension)
