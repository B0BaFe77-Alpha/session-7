#!/usr/bin/env python3
from coffee_shop_exceptions import (
    InvalidCustomizationError,
    InsufficientPointsError,
    InvalidCustomerError,
    InvalidOrderError,
    InvalidSalesError,
    InvalidSaveError
)
"""
Coffee Shop Ordering System
Version 7.4 - "It works, don't touch it"

Started as a simple order system. Got... complicated.
Good luck!
"""
class Customer:
        """creates a customer for the coffee shop
        Args:
            name (str): The name of the customer.
            member (bool): Whether the customer is a member.
            staff (bool): Whether the customer is staff.
        """
        def __init__(self, name, member, staff):
                self.name = name 
                self.member = member
                self.staff = staff
                
        def get_name(self):
              """gets the name of the customer and checks if its empt
              Args:
                  name (str): The name of the customer."""
              if self.name == "":
                  raise InvalidCustomerError("Customer name cannot be empty")
              return self.name
        def is_staff(self):
              """checks if the customer is staff
              args:
                  staff (bool): Whether the customer is staff."""
              return self.staff
        def is_member(self):
              """checks if the customer is a member
              Args:
                  member (bool): Whether the customer is a member."""
              return self.member
              
              
class LoyaltyProgram:
        def __init__(self, points, wants_free_drink):
            """Initializes the loyalty rewards program.
            Args:
                points (int): The number of loyalty points the customer has.
                wants_free_drink (bool): Whether the customer wants a free drink.
            """
            self.points = points
            self.wants_free_drink = wants_free_drink
        def earn_points(self, price):
            """Earns loyalty points based on the price of the order.
            Args:
                price (float): The price of the order.
            Returns:
                int: The number of loyalty points earned.
            """
            group = price // 10
            
            self.points += (group * 10)

            return self.points 
        def spend_points(self):
                """spends the points for a free drink 
                Raises:
                    InsufficientPointsError: If the customer doesn't have enough points for a free drink."""
                if self.points < 100:
                    raise InsufficientPointsError("Not enough points for a free drink")
                else:
                    self.points -= 100
                return self.points

class MenuItem:
    """Base class for menu items.
    Args:
        name (str): The name of the menu item.
        base_price (float): The base price of the menu item.
    """
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
class Drink(MenuItem):
    """Represents a drink item in the menu.
    Args:
        name (str): The name of the drink.
        base_price (float): The base price of the drink.
    """
    def __init__(self, name, base_price):
        super().__init__(name, base_price)




class Menu:
    """whats in the menu for the coffe shop 
    Args:
        drinks (list): A list of Drink objects available in the menu.
        size_multipliers (dict): A dictionary mapping drink sizes to their price multipliers.
        milk_type (dict): A dictionary mapping milk types to their additional costs.
        
    """

    def __init__(self 
                 ):
      
       
        self.drinks = [
            Drink('latte', 4.50),
            Drink('cappuccino', 4.25),
            Drink('espresso', 3.50),
            Drink('americano', 3.75),
            Drink('mocha', 5.00)
        ]
        

        self.SIZE_MUL = {
            'small': 1.0,
            'medium': 1.3,
            'large': 1.6
        }

        self.milk_type = {
            "coconut": 2.5,
            "soy": 1.0,
            "cow": 0.0,
            "goat": 3.0,
            "almond": 1.5,
            "oat": 1.0
        }
     
    def add_drink(self, drink):
        """adds a drink to the menu
        Args:
            drink (Drink): The drink to add to the menu.
        """
        self.drinks.append(drink)
    def drinkSizeError(self) :
                """error for the wrong size of drink
                Raises:
                    InvalidCustomizationError: If the drink size is invalid."""  
                raise InvalidCustomizationError("WE DO NOT HAVE THAT DRINK SIZE")
    def drinkTypeError(self) :
                    """error for the wrong type of drink
                    Raises:
                        InvalidCustomizationError: If the drink type is invalid."""  
                    raise InvalidCustomizationError("WE DO NOT HAVE THAT DRINK TYPE")
    def drinkMilkError(self) :
                    """error for the wrong milk in the drink
                    Raises:
                        InvalidCustomizationError: If the milk type is invalid."""  
                    raise InvalidCustomizationError("WE DO NOT HAVE THAT MILK TYPE")
    def calculate_price(self, drink, size, milk):
        """calculates the cost of the items
         Args:
            drink (str): The name of the drink.
            size (str): The size of the drink.
            milk (str): The type of milk to use.
         Returns:
            float: The total price of the drink.
         Raises:
            InvalidCustomizationError: If the drink, size, or milk type is invalid."""
        selected_drink = None
        for item in self.drinks:
            if item.name == drink:
                selected_drink = item
                break

        if selected_drink is None:
            self.drinkTypeError()
        elif milk not in self.milk_type:
            self.drinkMilkError()
        elif size not in  self.SIZE_MUL:
            self.drinkSizeError()
        else:
             price =  selected_drink.base_price * self.SIZE_MUL[size] + self.milk_type[milk]
             return price

    
            
class Order:
        """handles the order for the coffee shop
        Args:
            customerOrder (list): A list of tuples representing the customer's order.
            name (str): The name of the customer.
            member (bool): Whether the customer is a member.
            staff (bool): Whether the customer is staff.
            points (int): The number of loyalty points the customer has."""
        order_count = 0
        staff_order_count = 0
        daily_sales = 0
        # def __init__(self,  customerOrder , name, member, staff, points, wants_free_drink): 
                        
        #     """the intioniser for the order """
        #     if not customerOrder:
        #         raise InvalidOrderError("Order cannot be empty")
        #     self.customerOrder = customerOrder
        #     self.MenuItem = Menu()
            
        #     self.customer = Customer(name, member, staff)
        #     self.loyalty = LoyaltyProgram(points, wants_free_drink)
        def __init__(
    self,
    customerOrder,
    customer: Customer,
    loyalty: LoyaltyProgram,
    menu: Menu
):
            if not customerOrder:
                raise InvalidOrderError("Order cannot be empty")

            self.customerOrder = customerOrder
            self.customer = customer
            self.loyalty = loyalty
            self.menu = menu
            self.sales_recorded = False
            





        def order_total (self):
            """ gets a normal oder and gets the price as well
            ARGS:
                drink
                SIZE_MUL
                milk_type
            Raises:
                InvalidCustomizationError: If the drink, size, or milk type is invalid.
            Returns:
                float: The total price of the order.
            """
            price = 0
            for drink, size, milk in self.customerOrder:
                if self.loyalty.points >= 100 and size == "small" and self.loyalty.wants_free_drink:
                    self.loyalty.spend_points()
                else:
                    #price += self.MenuItem.calculate_price(drink, size, milk)
                    price += self.menu.calculate_price(drink, size, milk)
            
            if self.customer.is_staff():
                price = 0
            elif self.customer.is_member():
                price -= price / 10
               
                  
            return price
        def drink_logging (self):
                    """logs the number of drinks ordered
                    Returns:
                        int: The total number of drinks ordered."""

                    return len(self.customerOrder)
        
        def number_of_orders_in_a_day(self):
            """logs the number of orders in a day
            Args:
                order_count (int): The total number of orders in a day.
                Returns:
                    tuple: A tuple containing the total order count and staff order count."""
            Order.order_count += 1
            if self.customer.is_staff():
                Order.staff_order_count += 1
            return Order.order_count, Order.staff_order_count

        
        def reciept(self):
            """prints the reciept for the order
            Args:
                customer (Customer): The customer placing the order.
                customerOrder (list): A list of tuples representing the customer's order.
                order_total (float): The total price of the order.
                drink_logging (int): The total number of drinks ordered.
            """
            total = self.order_total()
            
            if not self.sales_recorded:
                self.number_of_orders_in_a_day()
                Order.daily_sales += total
                self.sales_recorded = True
            print("\n--- Receipt ---")
            print(f"Customer: {self.customer.name.title()}")
            for drink, size, milk in self.customerOrder:
                print(f"Drink: {drink.title()} ({size})")
                
            if self.customer.is_member():
                print("Member discount applied")
            elif self.customer.is_staff():
                print("Staff order - free")
            
            print(f"Total: ${total:.2f}")
            print(f"Drinks ordered: {self.drink_logging()}")
            print("Thank you!")
            print("---------------\n")
        def daily_report():
            """Print and save daily sales report.
            Raises:
                InvalidSalesError: If the daily sales are negative."""
            
            
            print("\n=== Daily Sales Report ===")
            print(f"Total orders: {Order.order_count}")
            print(f"Total sales: ${Order.daily_sales:.2f}")
            if Order.daily_sales < 0:
                raise InvalidSalesError("Daily sales cannot be negative")
            if Order.order_count > 0:
                avg_order = Order.daily_sales / Order.order_count
                print(f"Average order: ${avg_order:.2f}")
        
            # Save to file
             
            try:
                with open('daily_sales.txt', 'a') as file:
                    file.write(
                        f"Orders: {Order.order_count}, "
                        f"Sales: ${Order.daily_sales:.2f}\n"
                    )
            except:
                raise InvalidSaveError("Could not save daily sales report")
                





menu = Menu()
menu.add_drink(Drink('flat white', 4.00))
# customer = Customer("Asher", True, False)
# loyalty = LoyaltyProgram(50, False)

# customerOrder = [("latte", "small", "cow")]

# order = Order(customerOrder, customer, loyalty, menu)
# order.reciept()
# Order.daily_report()







              

            
          
                 
    # Global variables (added over time)


# loyalty_accounts = {}  # {customer_name: points}
# member_list = ['alice', 'bob', 'charlie']  # Members get discount
# daily_sales = 0.0
# order_count = 0
# member_discount = 0.10
# points_per_dollar = 1
# free_drink_points = 100

# def take_order():
#     """Main order function - handles everything."""
#     global daily_sales, order_count
    
#     print("\n=== New Order ===")
#     customer_name = input("Customer name: ").strip().lower()
    
#     # Check if member
#     is_member = customer_name in member_list
#     if is_member:
#         print(f"Welcome back, {customer_name.title()}! (Member discount applies)")
    
#     # Get drink
#     print("\nAvailable drinks:")
#     for drink in menu:
#         print(f"  - {drink.title()}")
    
#     drink_name = input("Drink: ").strip().lower()
    
#     # Validate drink
#     if drink_name not in menu:
#         print("Error: Drink not on menu")
#         return
    
#     base_price = menu[drink_name]
    
#     # Get size
#     size = input("Size (small/medium/large): ").strip().lower()
    
#     # Calculate size price
#     if size == 'small':
#         price = base_price * 1.0
#     elif size == 'medium':
#         price = base_price * 1.3
#     elif size == 'large':
#         price = base_price * 1.6
#     else:
#         print("Error: Invalid size")
#         return
    
#     # Milk options
#     milk_type = input("Milk (whole/skim/oat/almond/none): ").strip().lower()
    
#     # Milk surcharge
#     if milk_type == 'oat':
#         price += 0.50
#     elif milk_type == 'almond':
#         price += 0.50
#     elif milk_type == 'whole' or milk_type == 'skim' or milk_type == 'none':
#         pass  # No extra charge
#     else:
#         print("Error: Invalid milk type")
#         return
    
#     # Extras
#     extra_shot = input("Extra shot? (y/n): ").strip().lower()
#     if extra_shot == 'y':
#         price += 1.00
    
#     whipped_cream = input("Whipped cream? (y/n): ").strip().lower()
#     if whipped_cream == 'y':
#         price += 0.75
    
#     # Apply member discount
#     if is_member:
#         discount_amount = price * member_discount
#         price = price - discount_amount
#         print(f"Member discount applied: -${discount_amount:.2f}")
    
#     # Total before loyalty
#     print(f"\nTotal: ${price:.2f}")
    
#     # Ask about loyalty points
#     use_points = input("Redeem loyalty points for free drink? (y/n): ").strip().lower()
    
#     if use_points == 'y':
#         if customer_name not in loyalty_accounts:
#             print("No loyalty account found.")
#             loyalty_accounts[customer_name] = 0
        
#         current_points = loyalty_accounts[customer_name]
#         print(f"Current points: {current_points}")
        
#         if current_points >= free_drink_points:
#             # Free drink must be small
#             if size != 'small':
#                 print("Error: Free drinks must be small size")
#                 return
            
#             # Deduct points
#             loyalty_accounts[customer_name] -= free_drink_points
#             price = 0.0
#             print(f"Free drink! Points remaining: {loyalty_accounts[customer_name]}")
#         else:
#             print(f"Not enough points. Need {free_drink_points}, have {current_points}")
    
#     # Final payment
#     if price > 0:
#         payment = float(input(f"Payment (total ${price:.2f}): $"))
        
#         if payment < price:
#             print("Error: Insufficient payment")
#             return
        
#         change = payment - price
#         if change > 0:
#             print(f"Change: ${change:.2f}")
        
#         # Add loyalty points (if not free drink)
#         if use_points != 'y' or loyalty_accounts.get(customer_name, 0) < free_drink_points:
#             points_earned = int(price * points_per_dollar)
#             if customer_name not in loyalty_accounts:
#                 loyalty_accounts[customer_name] = 0
#             loyalty_accounts[customer_name] += points_earned
#             print(f"Loyalty points earned: {points_earned}")
#             print(f"Total loyalty points: {loyalty_accounts[customer_name]}")
    
#     # Update daily totals
#     daily_sales += price
#     order_count += 1
    
#     # Receipt
#     print("\n--- Receipt ---")
#     print(f"Customer: {customer_name.title()}")
#     print(f"Drink: {drink_name.title()} ({size})")
#     if milk_type != 'none':
#         print(f"Milk: {milk_type.title()}")
#     if extra_shot == 'y':
#         print("Extra shot")
#     if whipped_cream == 'y':
#         print("Whipped cream")
#     if is_member:
#         print("Member discount applied")
#     print(f"Total: ${price:.2f}")
#     print("Thank you!")
#     print("---------------\n")


# def staff_order():
#     """Handle staff drinks - free but track for inventory."""
#     global order_count
    
#     print("\n=== Staff Order ===")
    
#     # Get drink
#     print("Available drinks:")
#     for drink in menu:
#         print(f"  - {drink.title()}")
    
#     drink_name = input("Drink: ").strip().lower()
    
#     if drink_name not in menu:
#         print("Error: Drink not on menu")
#         return
    
#     # Get size  
#     size = input("Size (small/medium/large): ").strip().lower()
#     if size not in ['small', 'medium', 'large']:
#         print("Error: Invalid size")
#         return
    
#     # Staff drinks always free
#     price = 0.0
#     order_count += 1
    
#     print(f"\nStaff drink: {drink_name.title()} ({size})")
#     print("Total: $0.00 (Staff)")
#     print("Recorded for inventory.\n")


# def daily_report():
#     """Print and save daily sales report."""
#     global daily_sales, order_count
    
#     print("\n=== Daily Sales Report ===")
#     print(f"Total orders: {order_count}")
#     print(f"Total sales: ${daily_sales:.2f}")
    
#     if order_count > 0:
#         avg_order = daily_sales / order_count
#         print(f"Average order: ${avg_order:.2f}")
    
#     # Save to file
#     try:
#         with open('daily_sales.txt', 'a') as f:
#             f.write(f"Orders: {order_count}, Sales: ${daily_sales:.2f}\n")
#         print("Report saved to daily_sales.txt")
#     except:
#         print("Error: Could not save report")
    
#     print("=========================\n")


# def reset_day():
#     """Reset daily counters."""
#     global daily_sales, order_count
#     daily_sales = 0.0
#     order_count = 0
#     print("Daily counters reset.\n")


# def view_loyalty():
#     """Show all loyalty accounts."""
#     print("\n=== Loyalty Accounts ===")
#     if not loyalty_accounts:
#         print("No accounts yet.")
#     else:
#         for name, points in loyalty_accounts.items():
#             print(f"{name.title()}: {points} points")
#     print("========================\n")


# def main_menu():
#     """Main program loop."""
#     while True:
#         print("\n======= Coffee Shop POS =======")
#         print("1. Take Order")
#         print("2. Staff Order (Free)")
#         print("3. Daily Report")
#         print("4. View Loyalty Accounts")
#         print("5. Reset Daily Counters")
#         print("6. Exit")
#         print("===============================")
        
#         choice = input("Choice: ").strip()
        
#         if choice == '1':
#             take_order()
#         elif choice == '2':
#             staff_order()
#         elif choice == '3':
#             daily_report()
#         elif choice == '4':
#             view_loyalty()
#         elif choice == '5':
#             reset_day()
#         elif choice == '6':
#             print("Goodbye!")
#             break
#         else:
#             print("Error: Invalid choice")


# if __name__ == '__main__':
#     main_menu()
    