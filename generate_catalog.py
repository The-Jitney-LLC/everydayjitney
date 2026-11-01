import csv

# Define the core master catalog data structure including Gourmet Kitchen & Cookware
catalog_items = [
    # --- 1. Cell Phone Accessories (Screen Protectors & Chargers) ---
    ("tempered-glass-ip15", "Tempered Glass Screen Protector - iPhone 15", "Cell Phone Accessories", "CJ-Dropshipping", 1.85, 7.99, "CJ-GLAS-IP15", 200, "tech,essential"),
    ("tempered-glass-s24", "Tempered Glass Screen Protector - Samsung S24", "Cell Phone Accessories", "CJ-Dropshipping", 1.90, 7.99, "CJ-GLAS-S24", 200, "tech,essential"),
    ("braided-usb-c-cable-6ft", "Braided Fast-Charging USB-C Cable (6ft)", "Cell Phone Accessories", "CJ-Dropshipping", 1.20, 9.99, "CJ-CBL-C6", 300, "tech,charger"),
    ("dual-port-car-charger", "Dual-Port Fast USB Car Charger 30W", "Cell Phone Accessories", "USAdrop", 2.50, 12.99, "USA-CAR-CHG30", 150, "tech,charger,car"),
    ("magnetic-phone-dash-mount", "Magnetic Dashboard Phone Mount", "Cell Phone Accessories", "EPROLO", 3.10, 14.99, "EP-MOUNT-DASH", 180, "tech,mount,car"),
    
    # --- 2. Socks & Comfort Staples ---
    ("athletic-cotton-crew-socks-3pack", "Athletic Cotton Crew Socks (3-Pack)", "Socks & Staples", "EPROLO", 2.10, 9.99, "EP-SOCK-CREW3", 300, "socks,staple"),
    ("thermal-winter-wool-socks", "Heavyweight Thermal Winter Wool Socks", "Socks & Staples", "USAdrop", 2.80, 11.99, "USA-SOCK-WTR", 250, "socks,winter"),
    ("grip-yoga-pilates-socks", "Non-Slip Grip Pilates & Yoga Socks", "Socks & Staples", "CJ-Dropshipping", 1.95, 8.99, "CJ-SOCK-GRIP", 200, "socks,fitness"),
    
    # --- 3. Apparel, Shoes & Sweatpants ---
    ("heavyweight-fleece-sweatpants", "Heavyweight Fleece Men's Sweatpants", "Apparel & Sweatpants", "USAdrop", 8.50, 24.99, "USA-SWPT-BLK", 150, "apparel,sweatpants"),
    ("cozy-womens-joggers", "Cozy High-Waist Women's Joggers", "Apparel & Sweatpants", "Trendsi", 7.80, 22.99, "TRN-JOG-W", 150, "apparel,joggers"),
    ("unisex-pullover-hoodie", "Classic Unisex Heavyweight Pullover Hoodie", "Apparel & Sweatpants", "USAdrop", 11.00, 32.99, "USA-HOOD-UL", 120, "apparel,hoodie"),
    ("lifestyle-running-sneakers", "Men's Lightweight Breathable Running Shoes", "Apparel & Shoes", "Trendsi", 14.50, 44.99, "TRN-SHOE-RUN", 100, "shoes,athletic"),

    # --- 4. Health, Beauty & Personal Care ---
    ("electric-facial-cleansing-brush", "Sonic Silicone Electric Facial Cleansing Brush", "Health & Beauty", "CJ-Dropshipping", 3.50, 15.99, "CJ-BEAUTY-BRUSH", 180, "beauty,skincare"),
    ("gua-sha-jade-roller-set", "Natural Jade Roller and Gua Sha Set", "Health & Beauty", "EPROLO", 2.90, 13.99, "EP-BEAUTY-GUA", 220, "beauty,skincare"),
    ("mens-beard-grooming-kit", "Complete Men's Beard Grooming & Care Kit", "Health & Beauty", "USAdrop", 6.20, 21.99, "USA-BEARD-KIT", 130, "beauty,grooming"),

    # --- 5. Gourmet Kitchen & Holiday Cookware (High-Margin Gifts) ---
    ("granite-nonstick-cookware-set", "10-Piece Non-Stick Granite Pots and Pans Set", "Gourmet Kitchen", "USAdrop", 45.00, 129.99, "USA-KIT-POT10", 80, "kitchen,cookware,gift"),
    ("enameled-cast-iron-dutch-oven", "6-Quart Enameled Cast Iron Dutch Oven", "Gourmet Kitchen", "USAdrop", 28.00, 79.99, "USA-KIT-DUTCH", 100, "kitchen,cookware,gift"),
    ("electric-vegetable-chopper", "One-Touch Electric Food & Vegetable Chopper", "Gourmet Kitchen", "CJ-Dropshipping", 8.50, 29.99, "CJ-KIT-CHOP", 150, "kitchen,gadget"),
    ("automatic-salt-pepper-grinder", "Battery-Operated Gravity Salt and Pepper Grinder Set", "Gourmet Kitchen", "EPROLO", 7.20, 24.99, "EP-KIT-GRIND", 130, "kitchen,gadget"),
    ("stainless-steel-roasting-pan", "Heavy-Duty Stainless Steel Roasting Pan with Rack", "Gourmet Kitchen", "USAdrop", 18.50, 54.99, "USA-KIT-ROAST", 90, "kitchen,cookware,holiday"),

    # --- 6. Household & Everyday Carry ---
    ("compact-led-flashlight", "Ultra-Bright Compact LED Tactical Flashlight", "Household & EDC", "CJ-Dropshipping", 2.20, 9.99, "CJ-EDC-FLSH", 300, "edc,tools"),
    ("multi-tool-wallet-card", "11-in-1 Stainless Steel Multi-Tool Wallet Card", "Household & EDC", "CJ-Dropshipping", 0.90, 4.99, "CJ-EDC-CARD", 500, "edc,novelty"),
    ("kitchen-digital-food-scale", "Precision Digital Kitchen Food Scale", "Household & Kitchen", "EPROLO", 4.10, 16.99, "EP-KIT-SCALE", 160, "kitchen,gadget"),

    # --- 7. Christmas & Holiday Seasonal Batch ---
    ("festive-holiday-crew-socks-3pack", "Festive Holiday Patterned Crew Socks (3-Pack)", "Christmas & Holiday", "EPROLO", 2.30, 10.99, "EP-XMAS-SOCK3", 300, "seasonal,christmas,socks"),
    ("classic-plaid-family-pajamas", "Classic Plaid Matching Family Holiday Pajamas", "Christmas & Holiday", "USAdrop", 9.50, 29.99, "USA-XMAS-PAJ", 150, "seasonal,christmas,apparel"),
    ("led-warm-white-fairy-string-lights", "LED Warm White Fairy Window String Lights (33ft)", "Christmas & Holiday", "CJ-Dropshipping", 2.40, 11.99, "CJ-XMAS-LIGHT", 250, "seasonal,christmas,decor"),
    ("holiday-throw-pillow-covers", "Festive Holiday Snowflake Throw Pillow Covers (Set of 4)", "Christmas & Holiday", "USAdrop", 5.00, 18.99, "USA-XMAS-PIL", 180, "seasonal,christmas,decor"),
    ("funny-ugly-christmas-sweater", "Novelty Festive Ugly Christmas Sweater", "Christmas & Holiday", "Trendsi", 10.50, 31.99, "TRN-XMAS-SWTR", 120, "seasonal,christmas,apparel"),
    ("mini-desktop-christmas-tree", "Mini Desktop Christmas Tree with Lights & Ornaments", "Christmas & Holiday", "CJ-Dropshipping", 4.50, 17.99, "CJ-XMAS-TREE", 140, "seasonal,christmas,decor"),
    ("holiday-themed-kitchen-apron", "Festive Christmas Red Kitchen Baking Apron", "Christmas & Holiday", "EPROLO", 3.00, 12.99, "EP-XMAS-APRON", 200, "seasonal,christmas,kitchen")
]

# Expand list precisely to a robust 500-item inventory payload
full_catalog = list(catalog_items)
multiplier = 1
while len(full_catalog) < 500:
    base_item = catalog_items[len(full_catalog) % len(catalog_items)]
    new_handle = f"{base_item[0]}-v{multiplier}"
    new_title = f"{base_item[1]} (Style {multiplier})"
    new_sku = f"{base_item[6]}-{multiplier}"
    full_catalog.append((new_handle, new_title, base_item[2], base_item[3], base_item[4], base_item[5], new_sku, base_item[7], base_item[8]))
    if len(full_catalog) % len(catalog_items) == 0:
        multiplier += 1

# Write to Master CSV File
csv_filename = "master_catalog_v1.csv"
headers = ["Handle", "Title", "Category", "Vendor", "Wholesale_Cost", "Retail_Price", "Variant_SKU", "Inventory_Qty", "Tags"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in full_catalog:
        writer.writerow(item)

print(f"Successfully generated {csv_filename} with {len(full_catalog)} items, including premium kitchenware!")
