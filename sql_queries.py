main_query = """
WITH order_information AS (
SELECT
	order_items.product_id,
	order_data.order_id,
	reviews.review_id,
    order_items.seller_id,
	order_items.order_item_id,
	order_items.price,
	reviews.review_score
FROM olist_order_dataset AS order_data
LEFT JOIN olist_order_reviews_dataset AS reviews
	ON order_data.order_id = reviews.order_id
LEFT JOIN olist_order_items_dataset AS order_items
	ON order_data.order_id = order_items.order_id
)

SELECT
	order_information.order_id,
	order_information.order_item_id,
	sellers.seller_id,
	products.product_category_name AS product_name,
	order_information.price,
	order_information.review_score
FROM order_information
LEFT JOIN olist_products_dataset AS products 
	ON order_information.product_id = products.product_id
LEFT JOIN olist_sellers_dataset AS sellers
	ON order_information.seller_id = sellers.seller_id
;
"""
