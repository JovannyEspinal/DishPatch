from dataclasses import dataclass

@dataclass
class Order:
    order_id: str
    item_id: str
    item_name: str
    customer_name: str
    customer_email: str
    status: str
    price: int
    order_date: str
    estimated_delivery: str
    tracking_id: str

ORDERS: dict[str, Order] = {
    "ORD-201": Order(
        order_id="ORD-201",
        item_id="m3",
        item_name="Butter Chicken",
        customer_name="Priya Nair",
        customer_email="priya@example.com",
        status="Out for Delivery",
        price=379,
        order_date="2024-01-15",
        estimated_delivery="2024-01-15",
        tracking_id="SS201TRK",
    ),
    "ORD-202": Order(
        order_id="ORD-202",
        item_id="m1",
        item_name="Margherita Pizza",
        customer_name="Arjun Mehta",
        customer_email="arjun@example.com",
        status="Placed",
        price=299,
        order_date="2024-01-15",
        estimated_delivery="2024-01-15",
        tracking_id="SS202TRK",
    ),
    "ORD-203": Order(
        order_id="ORD-203",
        item_id="m5",
        item_name="Classic Cheeseburger",
        customer_name="Sneha Roy",
        customer_email="sneha@example.com",
        status="Preparing",
        price=259,
        order_date="2024-01-15",
        estimated_delivery="2024-01-15",
        tracking_id="SS203TRK",
    ),
    "ORD-204": Order(
        order_id="ORD-204",
        item_id="m4",
        item_name="Vegan Buddha Bowl",
        customer_name="Rahul Das",
        customer_email="rahul@example.com",
        status="Delivered",
        price=319,
        order_date="2024-01-14",
        estimated_delivery="2024-01-14",
        tracking_id="SS204TRK",
    ),
    "ORD-205": Order(
        order_id="ORD-205",
        item_id="m6",
        item_name="Paneer Tikka",
        customer_name="Kavya Sharma",
        customer_email="kavya@example.com",
        status="Placed",
        price=199,
        order_date="2024-01-15",
        estimated_delivery="2024-01-15",
        tracking_id="SS205TRK",
    ),
}
