# Represents a company that uses the software
class Organization(models.Model):
    name = models.CharField(max_length=120, db_index=True)


# Represents an Order that a custom places on a storefront like Shopify or eBay
class Order(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='orders')
	address = CharField(max_length=1000)
	status = models.CharField(choices=STATUS_CHOICES, default=SYNCED, max_length=25)


# Represents a unique product and total stock of that product
class Product(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=1000)
    color = models.CharField(max_length=20, blank=True)
    stock_quantity = models.IntegerField()


# Represents a line item in an Order e.g. 2x Red Hat or 1x Blue Shirt
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
    quantity = models.IntegerField()


# 1. Return an iterable of unique orders that have a given product in them
def get_orders_for_product(product: Product):
    return Order.objects.filter(items__product=product).all().distinct() # -> [order1, order1, order2, order3]


# 2. Return an iterable of Products where the color value contains "red" or name contains "red"
def get_products_for_color(color: str) -> Iterable[Product]:
	return Product.objects.filter(Q(color__contains=color) | Q(name__contains=color)).all()


# 3. Return an iterable of unique products that have been ordered for a given organization
def get_products_in_orders_items(organization: Organization) -> Iterable[Product]:
	return Product.objects.filter().annotate(cnt=Count(order_items)).filter(cnt__gt=0).all()

# OrderItem(order=order1, quantity=5, product=product_1), OrderItem(order=order2, quantity=1, product=product_1)
# 4. Return an iterable of dictionary objects ordered (descending) by the total quantity ordered of that Product
# For example [{product_1: 10}, {product_3: 8}, {product_2: 1}]
def get_products_in_orders_items(organization: Organization) -> Iterable[Dict[Product, int]]:
    #products = Product.objects.filter().annotate(cnt=Count(order_items)) # [Product -> product.cnt = 5]
	return ({product: product.cnt} 
	    for product in Product.objects.annotate(cnt=Sum(order_items__quantity)) \
	        .filter(organization=organization) \
	        .order('cnt').desc().all()
	)
