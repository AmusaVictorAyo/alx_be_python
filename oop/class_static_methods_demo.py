class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method does not access class or instance state
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method accesses class-level data
        print(f"Calculation type: {cls.calculation_type}")
        return a * b