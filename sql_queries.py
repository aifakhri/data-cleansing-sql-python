ordered_product = """
SELECT 
	order_items.order_id,
	products.product_category_name AS product_name
FROM olist_order_items_dataset AS order_items
LEFT JOIN olist_products_dataset AS products
	ON order_items.product_id = products.product_id
"""

product_reviews = """
WITH order_reviews as (
SELECT
	order_items.product_id,
	order_data.order_id,
	reviews.review_id,
	reviews.review_score,
	order_data.order_status
FROM olist_order_dataset AS order_data
LEFT JOIN olist_order_reviews_dataset AS reviews 
	ON order_data.order_id = reviews.order_id
LEFT JOIN olist_order_items_dataset AS order_items 
	ON order_data.order_id = order_items.order_id
)

SELECT
	order_reviews.order_id,
	products.product_category_name AS product_name,
	order_reviews.review_score
FROM olist_products_dataset AS products
LEFT JOIN order_reviews 
	ON products.product_id = order_reviews.product_id;
"""

sellers_sold_items = """
SELECT
	order_item.order_id,
	products.product_category_name AS product_name,
	sellers.seller_id
FROM olist_order_items_dataset AS order_item
LEFT JOIN olist_products_dataset AS products 
	ON order_item.product_id = products.product_id
LEFT JOIN olist_sellers_dataset AS sellers 
	ON order_item.seller_id = sellers.seller_id; 
"""

translation_table = """
SELECT
	*
FROM product_category_name_translation
"""