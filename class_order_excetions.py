class InvalidCustomizationError(Exception):
    """Raised when a drink customization is invalid."""
    pass
   

class InsufficientPointsError(Exception):
    """Raised when customer doesn't have enough loyalty points."""
    pass


       
class InvalidCustomerError(Exception):
    """Raised when customer is not valid."""
    pass
class InvalidOrderError(Exception):
    """Raised when order is not valid."""
    pass
class InvalidSalesError(Exception):
    """Raised when sales data is not valid."""
    pass
class InvalidSaveError(Exception):
    """Raised when save operation is not valid."""
    pass