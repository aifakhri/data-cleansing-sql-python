ordered_product = """
SELECT 
	order_item.order_id,
	products.product_category_name
FROM olist_products_dataset as products
LEFT JOIN olist_order_items_dataset as order_item
ON products.product_id = order_item.product_id;
"""