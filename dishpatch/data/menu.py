from dataclasses import dataclass

@dataclass
class MenuItem:
    id: str
    name: str
    category: str
    cuisine: str
    price: int
    rating: float
    dietary_tags: list[str]
    description: str
    available: bool

MENU: list[MenuItem] = [
    MenuItem(
      id="m1",
      name="Margherita Pizza",
      category="Main",
      cuisine="Italian",
      price=299,
      rating=4.7,
      dietary_tags=["Veg"],
      description="Classic thin crust with tomato, mozzarella, basil",
      available=True
    ),
    MenuItem(
        id="m2",
        name="Vegan Pasta Primavera",
        category="Main",
        cuisine="Italian",
        price=349,
        rating=4.5,
        dietary_tags=["Vegan"],
        description="Penne with seasonal vegetables, olive oil, garlic",
        available=True
    ),
    MenuItem(
        id="m3",
        name="Butter Chicken",
        category="Main",
        cuisine="Indian",
        price=379,
        rating=4.9,
        dietary_tags=["GF"],
        description="Creamy tomato curry with tender chicken and naan",
        available=True
    ),
    MenuItem(
        id="m4",
        name="Vegan Buddha Bowl",
        category="Main",
        cuisine="Fusion",
        price=319,
        rating=4.6,
        dietary_tags=["Vegan", "GF"],
        description="Quinoa, chickpeas, avocado, greens, tahini",
        available=True
    ),
    MenuItem(
        id="m5",
        name="Classic Cheeseburger",
        category="Main",
        cuisine="American",
        price=259,
        rating=4.4,
        dietary_tags=[],
        description="Beef patty, cheddar, lettuce, tomato, brioche bun",
        available=True
    ),
    MenuItem(
        id="m6",
        name="Paneer Tikka",
        category="Main",
        cuisine="Indian",
        price=199,
        rating=4.8,
        dietary_tags=["Veg", "GF"],
        description="Tandoor-grilled cottage cheese with peppers",
        available=True
    ),
    MenuItem(
        id="m7",
        name="Aglio e Olio",
        category="Main",
        cuisine="Italian",
        price=279,
        rating=4.5,
        dietary_tags=["Vegan"],
        description="Spaghetti with garlic, chilli, olive oil, parsley",
        available=True
    ),
    MenuItem(
        id="m8",
        name="Mango Lassi",
        category="Drink",
        cuisine="Indian",
        price=99, rating=4.7,
        dietary_tags=["Veg", "GF"],
        description="Blended yogurt with Alphonso mango, cardamom",
        available=True
    ),
  ]