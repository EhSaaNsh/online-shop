from home.models import Product
CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session ## ijad session karbar
        cart = self.session.get(CART_SESSION_ID) ## gerfetan etalate session be esme cart
        if not cart:
            cart = self.session[CART_SESSION_ID] = {} ## age karbar bar avale ke kharid mikone va sabad nadashte khali bezar
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys() ## gereftane kelidhaye session cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy() ## ijad copy az session cart (sabade kharid )
        for product in products:
            cart[str(product.id)]['product'] = product ## ijad name mahsol (product khali method str dar model ro sedamizane)

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['quantity'] ## mohasebe gheymat kol baraye har mahsol
            yield item

    ##tedad har item ro migire va jameshon ro barmigardone
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart: ### age mahsol dar sabad nist
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity  ## age dar sabad vojod dasht be tedad entekhab shode ezafe kon
        self.save()

    def save(self):
        self.session.modified = True  ## zakhire kardane session

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart: ## age mahsol dar sabad bod
            del self.cart[product_id] ## hazfe mahsol
            self.save()

    def get_total_price(self):
        return sum(int(item['price'])*item['quantity'] for item in self.cart.values())

    ##khali kardane sabad kharid
    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

