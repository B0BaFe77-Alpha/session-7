class InvalidCustomizationError(Exception):
    """Raised when a drink customization is invalid."""
    pass
    def drinkSizeError(self) :
            """error for the wrong size of drink"""  
            raise ValueError("WE DO NOT HAVE THAT DRINK SIZE")
    def drinkTypeError(self) :
                """error for the wrong type of drink"""  
                raise ValueError("WE DO NOT HAVE THAT DRINK TYPE")
    def drinkMilkError(self) :
                """error for the wrong milk in the drink"""  
                raise ValueError("WE DO NOT HAVE THAT MILK TYPE")

class InsufficientPointsError(Exception):
    """Raised when customer doesn't have enough loyalty points."""
    pass


    def redeem_points(points):
        if points < 100:
            raise InsufficientPointsError(f"Need 100 points, have {points}")
class InvalidCustomerError(Exception):
    """Raised when customer is not valid."""
    pass
class InvalidOrderError(Exception):
    """Raised when order is not valid."""
    pass
class InvalidSalesError(Exception):
    """Raised when sale is not valid."""
    pass

# Backward-compatible alias for older code.
InvalidsSaleError = InvalidSalesError

class InvalidSaveError(Exception):
    """Raised when save is not valid."""
    pass