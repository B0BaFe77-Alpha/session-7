import unittest
from coffee_shop_exceptions import InsufficientPointsError, InvalidCustomerError, InvalidOrderError, InvalidSaveError,  InvalidSalesError
from coffee_shop_refactored import Menu, Order, MenuItem, Customer, LoyaltyProgram

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.latte = MenuItem("Latte", 4.50)
        self.customer = Customer("Alice", member=True, staff=False)
        self.loyalty = LoyaltyProgram(0, False)

    def test_menu_item_pricing_small(self):
        """Test Menu calculates small drink price correctly."""

        menu = Menu()
        price = menu.calculate_price('latte', 'small', 'oat')

        self.assertEqual(price, 5.50)

  

    def test_order_total_with_multiple_items(self):
        """Test Order calculates total correctly."""
        customer_order = [
        ('latte', 'small', 'cow'),
        ('cappuccino', 'medium', 'oat')
        ]

        order = Order(customer_order, "Alice", True, False, 0, False)
     
        self.assertAlmostEqual(order.order_total(), 9.9225)

    def test_member_discount_applied(self):
        """Test member discount is 10%."""
        customer_order = [
                ('latte', 'small', 'cow')
        ]

        order = Order(customer_order, "Alice", True, False, 0, False)

        self.assertAlmostEqual(order.order_total(), 4.05)  # 4.50 * 0.9

    def test_loyalty_points_earned(self):
        """Test loyalty points: $1 = 1 point."""
         
        customer_order = [
        ('latte', 'small', 'cow'),
        ('cappuccino', 'medium', 'goat')
        ]
    
        order = Order(customer_order, "Alice", member=True, staff=False, points=0, wants_free_drink=False)

        price = order.order_total()
        points = order.loyalty.earn_points(price)
        self.assertEqual(points, 10)

        # Add implementation
    def test_spend_points(self):
        """Test redeeming points reduces total correctly."""
        customer_order = [
            ('latte', 'small', 'cow')
        ]

        order = Order(customer_order, "Alice", member=True, staff=False, points=100, wants_free_drink=True)

        total_after_redeem = order.order_total()
        self.assertAlmostEqual(total_after_redeem, 0.0)  # Assuming 10 points = $1 discount
    def test_customer_is_staff_logged(self):
        """Test that staff orders are counted correctly."""
        customer_order = [
            ('latte', 'small', 'cow')
        ]

        order = Order(customer_order, "Bob", member=True, staff=True, points=0, wants_free_drink=False)
        order.number_of_orders_in_a_day()
        self.assertEqual(Order.staff_order_count, 1)
    def test_customer_is_not_staff_logged(self):
        """Test that non-staff orders are counted correctly."""
        customer_order = [
            ('latte', 'small', 'cow')
        ]

        order = Order(customer_order, "Alice", member=True, staff=False, points=0, wants_free_drink=False)
        order.number_of_orders_in_a_day()
        self.assertEqual(Order.order_count, 1)
    def test_customer_is_staff(self):
        """Test that staff orders are counted correctly."""
        customer_order = [
            ('latte', 'small', 'cow')
        ]

        order = Order(customer_order, "Bob", member=True, staff=True, points=0, wants_free_drink=False)
        price = order.order_total()
        self.assertEqual(price, 0)
    def test_more_then_one_order_in_a_day(self):
        """Test that multiple orders in a day are counted correctly."""
        customer_order1 = [
            ('latte', 'small', 'cow')
        ]
        customer_order2 = [
            ('cappuccino', 'medium', 'oat')
        ]

        order1 = Order(customer_order1, "Alice", member=True, staff=False, points=0, wants_free_drink=False)
        order1.number_of_orders_in_a_day()
        order1.order_total()
        order2 = Order(customer_order2, "Bob", member=True, staff=True, points=0, wants_free_drink=False)
        order2.order_total()
        order2.number_of_orders_in_a_day()
        

        self.assertEqual(Order.order_count, 3)
      
        self.assertEqual(Order.staff_order_count, 2) 
        #it doesnt reset between orders so it counts all orders in the day, not just the current order.
    def test_saving(self):
        customer_order1 = [
                    ('latte', 'small', 'cow')
                ]
        customer_order2 = [
                    ('cappuccino', 'medium', 'oat'),
                    ('cappuccino', 'medium', 'oat')
                ]
        
        order1 = Order(customer_order1, "Alice", member=True, staff=False, points=0, wants_free_drink=False)
        order1.number_of_orders_in_a_day()
        
        
        order2 = Order(customer_order2, "Bob", member=True, staff=True, points=0, wants_free_drink=False)
        order2.number_of_orders_in_a_day()
                
        Order.daily_report()
    def test_insufficient_points(self):
        loyalty = LoyaltyProgram(50, False)

        with self.assertRaises(InsufficientPointsError):
            loyalty.spend_points()
    def test_invalid_customer(self):
        with self.assertRaises(InvalidCustomerError):
            customer = Customer("", member=True, staff=False)
            customer.get_name()
    def test_invalid_order(self):
        with self.assertRaises(InvalidOrderError):
            order = Order([], "Alice", member=True, staff=False, points=0, wants_free_drink=False)  

    def test_invalid_sale(self):
        with self.assertRaises(InvalidSalesError):
            Order.daily_sales = -10.0   
            Order.order_count = 1
            Order.daily_report()
    
    
    
        

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()