ordered_product = """
SELECT 
	order_item.order_id,
	products.product_category_name
FROM olist_products_dataset as products
LEFT JOIN olist_order_items_dataset as order_item
ON products.product_id = order_item.product_id;
"""

product_reviews = """
WITH order_reviews as (
SELECT
	order_items.product_id,
	order_items.order_id,
	reviews.review_id,
	reviews.review_score
FROM olist_order_dataset AS order_data
JOIN olist_order_reviews_dataset AS reviews USING(order_id)
JOIN olist_order_items_dataset AS order_items USING(order_id)
)

SELECT
	order_reviews.order_id,
	products.product_category_name,
	order_reviews.review_score
FROM olist_products_dataset as products
LEFT JOIN order_reviews ON products.product_id = order_reviews.product_id
;
"""

sellers_sold_items = """
SELECT
	order_item.order_id,
	products.product_category_name,
	sellers.seller_id,
	sellers.seller_city,
	sellers.seller_state
FROM olist_order_items_dataset AS order_item
JOIN olist_products_dataset AS products ON order_item.product_id = products.product_id
JOIN olist_sellers_dataset as sellers ON order_item.seller_id = sellers.seller_id; 
"""