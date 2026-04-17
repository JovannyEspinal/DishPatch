from langchain_core.tools import tool
from dishpatch.data.orders import ORDERS, Order


def find_order(key: str) -> tuple[str | None, Order | None]:
    key = key.strip()
    upper_key = key.upper()

    if upper_key in ORDERS:
        return upper_key, ORDERS[upper_key]

    for order_id, order in ORDERS.items():
        if order.tracking_id.upper() == upper_key:
            return order_id, order
        if order.customer_email.lower() == key.lower():
            return order_id, order

    return None, None


def format_order(order_id: str, order: Order) -> str:
    return (
        f"Order {order_id} Details:\n"
        f"  Item         : {order.item_name}\n"
        f"  Customer     : {order.customer_name}\n"
        f"  Email        : {order.customer_email}\n"
        f"  Status       : {order.status}\n"
        f"  Price        : ${order.price}\n"
        f"  Ordered on   : {order.order_date}\n"
        f"  Est. delivery: {order.estimated_delivery}\n"
        f"  Tracking ID  : {order.tracking_id}"
    )


@tool
def get_order_status(lookup_key: str) -> str:
    """Look up the current status of a customer's order.

    Args:
        lookup_key: An order ID (e.g. 'ORD-201'), tracking ID (e.g. 'SS201TRK'),
                    or customer email (e.g. 'priya@example.com').

    Returns:
        Formatted order details including status and estimated delivery,
        or an error message if no matching order was found.
    """
    order_id, order = find_order(lookup_key)

    if not order:
        return (
            f"No order found for '{lookup_key}'. "
            "Please double-check and provide a valid Order ID (e.g. ORD-201), "
            "Tracking ID (e.g. SS201TRK), or email address."
        )

    return format_order(order_id, order)


order_tools_list = [get_order_status]
