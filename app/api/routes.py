"""
Verka Dairy IIT Ropar — API Routes
Endpoints: /api/products, /health
"""

from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel

router = APIRouter()


# ── Data Models ────────────────────────────────────────────────────────────────

class Product(BaseModel):
    id: int
    name: str
    description: str
    category: str
    emoji: str
    price_small: Optional[str] = None   # Small size price (None if not available)
    price_big: Optional[str] = None     # Big / standard size price (None if not available)


# ── Full Menu Catalogue ────────────────────────────────────────────────────────

PRODUCTS: List[dict] = [

    # ── Prantha ───────────────────────────────────────────────────────────────
    {
        "id": 1,
        "name": "Mix Prantha",
        "description": "Mixed stuffed paratha — a hearty Punjabi classic.",
        "category": "Prantha",
        "emoji": "🥙",
        "price_small": None,
        "price_big": "₹40",
    },
    {
        "id": 2,
        "name": "Aloo Prantha",
        "description": "Spiced potato stuffed paratha, a campus favourite.",
        "category": "Prantha",
        "emoji": "🥙",
        "price_small": None,
        "price_big": "₹25",
    },
    {
        "id": 3,
        "name": "Paneer Prantha",
        "description": "Soft paneer stuffed paratha — rich and filling.",
        "category": "Prantha",
        "emoji": "🥙",
        "price_small": None,
        "price_big": "₹60",
    },
    {
        "id": 4,
        "name": "Gobi Prantha",
        "description": "Cauliflower stuffed paratha with a hint of spice.",
        "category": "Prantha",
        "emoji": "🥙",
        "price_small": None,
        "price_big": "₹30",
    },
    {
        "id": 5,
        "name": "Simple Prantha",
        "description": "Plain layered paratha — best with dahi or lassi.",
        "category": "Prantha",
        "emoji": "🫓",
        "price_small": None,
        "price_big": "₹20",
    },

    # ── Tea & Beverages ───────────────────────────────────────────────────────
    {
        "id": 6,
        "name": "Dudh Patti",
        "description": "Strong milk tea brewed the Punjabi way.",
        "category": "Tea & Beverages",
        "emoji": "☕",
        "price_small": "₹25",
        "price_big": "₹30",
    },
    {
        "id": 7,
        "name": "Gurh Chai",
        "description": "Jaggery tea — naturally sweetened, warming and comforting.",
        "category": "Tea & Beverages",
        "emoji": "☕",
        "price_small": "₹30",
        "price_big": "₹35",
    },
    {
        "id": 8,
        "name": "Adrak Chai",
        "description": "Ginger tea — great for early mornings and study sessions.",
        "category": "Tea & Beverages",
        "emoji": "🫖",
        "price_small": None,
        "price_big": "₹30",
    },
    {
        "id": 9,
        "name": "Bornvita Dudh",
        "description": "Hot Bournvita milk — energy boost in a cup. (Medium)",
        "category": "Tea & Beverages",
        "emoji": "🍫",
        "price_small": None,
        "price_big": "₹35",
    },

    # ── Dairy Products ────────────────────────────────────────────────────────
    {
        "id": 10,
        "name": "Flavour Yogurt",
        "description": "Chilled flavoured yogurt — smooth and creamy.",
        "category": "Dairy Products",
        "emoji": "🍨",
        "price_small": None,
        "price_big": "₹40",
    },
    {
        "id": 11,
        "name": "Dahi",
        "description": "Fresh set curd made daily from pure Verka milk.",
        "category": "Dairy Products",
        "emoji": "🥣",
        "price_small": "₹20",
        "price_big": "₹35",
    },
    {
        "id": 12,
        "name": "Kheer",
        "description": "Traditional rice kheer — sweet, creamy, and homemade.",
        "category": "Dairy Products",
        "emoji": "🍚",
        "price_small": None,
        "price_big": "₹25",
    },
    {
        "id": 13,
        "name": "Rabri",
        "description": "Thick condensed milk dessert with a hint of cardamom.",
        "category": "Dairy Products",
        "emoji": "🍮",
        "price_small": None,
        "price_big": "₹25",
    },
    {
        "id": 14,
        "name": "Flavour Milk",
        "description": "Mango, Rose, Strawberry & Kesar — chilled and energising.",
        "category": "Dairy Products",
        "emoji": "🧋",
        "price_small": None,
        "price_big": "₹25",
    },
    {
        "id": 15,
        "name": "Paneer",
        "description": "Soft daily-fresh paneer from pure buffalo milk.",
        "category": "Dairy Products",
        "emoji": "🧀",
        "price_small": None,
        "price_big": "₹85",
    },
    {
        "id": 16,
        "name": "Full Cream Milk",
        "description": "Farm-fresh whole milk — rich in calcium and protein.",
        "category": "Dairy Products",
        "emoji": "🥛",
        "price_small": None,
        "price_big": "₹35",
    },
    {
        "id": 17,
        "name": "Milk (Green Packet)",
        "description": "Toned milk — light, healthy, and great for daily use.",
        "category": "Dairy Products",
        "emoji": "🍼",
        "price_small": None,
        "price_big": "₹32",
    },
    {
        "id": 18,
        "name": "Desi Ghee",
        "description": "Pure cow ghee — rich aroma, golden colour, traditionally churned.",
        "category": "Dairy Products",
        "emoji": "🫕",
        "price_small": None,
        "price_big": "₹665",
    },
    {
        "id": 19,
        "name": "Sweet Lassi",
        "description": "Thick Punjabi sweet lassi in a convenient T-pack.",
        "category": "Dairy Products",
        "emoji": "🥤",
        "price_small": None,
        "price_big": "₹25",
    },
    {
        "id": 20,
        "name": "Plain Lassi",
        "description": "Simple, pure lassi — cool and refreshing.",
        "category": "Dairy Products",
        "emoji": "🫙",
        "price_small": None,
        "price_big": "₹35",
    },
    {
        "id": 21,
        "name": "Ice Cream",
        "description": "Verka ice cream — ask at the counter for today's flavours.",
        "category": "Dairy Products",
        "emoji": "🍦",
        "price_small": None,
        "price_big": None,   # price not specified — ask at counter
    },
]


# ── Endpoints ──────────────────────────────────────────────────────────────────

@router.get("/health", tags=["Utility"])
async def health_check():
    """Health check endpoint for monitoring and Docker health probes."""
    return {"status": "ok", "service": "verka-landing", "campus": "IIT Ropar"}


@router.get("/api/products", response_model=List[Product], tags=["Products"])
async def get_products():
    """Returns the full Verka Dairy + Prantha menu for IIT Ropar."""
    return PRODUCTS
