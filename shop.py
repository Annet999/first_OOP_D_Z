class Product: 
    def __init__(self, name, price):
        # Инициализация атрибутов
        self.name = name 
        self.price = price
        
        
    def __str__(self):
        # Возвращает строковое представление продукта
        return f"Product(name: {self.name}, price:{self.price})"
    
    
    def __eq__(self, other):
        # Сравнение продуктов по цене
        if isinstance(other, Product):
            return self.price == other.price
        return False
    
    
    def __lt__(self, other):
        # Сравнение продуктов по цене для сортировки
        if isinstance(other, Product):
            return self.price < other.price
        return False
    
# Новый тип продукта - HouseholdItem
class HouseholdItem(Product):
    def __init__(self, name, price, brend):
        super().__init__(name, price)
        self.brend = brend

    def __str__(self): 
        return f"HouseholdItem(name:{self.name}, price: {self.price}, brend: {self.brend})"
           
    
class Customer:
    def __init__(self, name):
        # Инициализация атрибутов name и списка заказов orders
        self.name = name
        self.orders = []
                
                
    def add_order(self, order):
        self.orders.append(order)   
                
                
    def __str__(self):
        # Возвращает строковое представление клиента и его заказов
        orders_str = ', '.join(str(order) for order in self.orders)
        return f"Customer(name: {self.name}, orders: [{orders_str}])"
            
             
class Order: 
    # Статические переменные для подсчёта общего колличества заказов и общей суммы заказов
    order_count = 0    
    total_revenue = 0
                
                
    def __init__(self, products):
        # Инициализация атрибута products и обновление статических переменных
        self.products = products
        Order.order_count += 1
        Order.total_revenue += self.calculate_total()
        
        
    def calculate_total(self):  
        # Рассчитываем общую стоимость товаров в заказе
        return sum(product.price for product in self.products)  
     
    
    @classmethod        
    def get_total_orders(cls):
        # Возвращает общее количество заказов
        return cls.order_count
 
                
    @classmethod 
    def get_total_revenue(cls):
        # Возвращает общую сумму заказов
        return cls.total_revenue
    
    def apply_discount(self, discount):
        # Применение скидки к заказу и обновление общей суммы заказов
        total = self.calculate_total()
        discounted_total = total - (total * discount.discount_percent / 100)
        Order.total_revenue -= (total - discounted_total)
        return discounted_total
    
    
    def __str__(self):
        # Возвращает строковое представление заказа и его товаров
        products_str = ', '.join(str(product) for product in self.products)
        return f"Order(products: [{products_str}])"
    
    
class Discount:
    def __init__(self, description, discount_percent):
        # Инициализация атрибутов description и discount_percent
        self.description = description
        self.discount_percent = discount_percent
        
        
    @staticmethod
    def apply_discount(total, discount_percent):
        # Статический метод для расчёта цены со скидкой
        return total - (total * discount_percent / 100)
    
    
    def __str__(self):
        # Возвращает строковое представление скидки
        return f"Discount(description: {self.description}, discount_percent: {self.discount_percent})"


# Класс ShoppingCart
class ShoppingCart:
    admin_user = "admin"

    def __init__(self,customer):
        self.customer = customer
        self.orders = []


    def add_order(self,order):
        self.orders.append(order)  


    def get_details(self):
        orders_str =', '.join(str(order) for order in self.orders)
        total = sum(order.calculate_total() for order in self.orders)
        return (f"Покупатель {self.customer.name} приобрёл: {orders_str}."
                f"Общая сумма: {total}. Зарегестрировал покупки пользователь: {ShoppingCart.admin_user}")
    

    def __str__(self):
        return self.get_details()



# Создание продуктов
product1 = Product("Laptop",1000)
product2 = Product("Smartphone",500)
product3 = Product("Column",100)
household_item1 = HouseholdItem("Washing Powder", 20, "Brend")



# Создание клиентов
customer1 = Customer("Алёна")
customer2 = Customer("Борис")

# Создание заказов
order1 = Order([product1, product2])
order2 = Order([product2, product3]) 
order3 = Order([product1, product3, household_item1])  


# Создание корзин
cart1 = ShoppingCart(customer1)
cart2 = ShoppingCart(customer2)


# Добавление заказов к клиентам и корзинам
customer1.add_order(order1)
customer1.add_order(order2)
cart1.add_order(order1)
cart1.add_order(order2)


customer2.add_order(order3)
cart2.add_order(order3)


# Создание скидок
discount1 = Discount("Summer Sale", 10)
discount2 = Discount("Promo code", 20)


# Применение скидок к заказам
order1_discounted_total = order1.apply_discount(discount1)
order2_discounted_total = order2.apply_discount(discount2)


#  Подсчёт общего количества заказов и общей суммы всех заказов для всех клиентов
total_orders = Order.get_total_orders()
total_revenue = Order.get_total_revenue()


# Вывод информации
print(customer1)
print(customer2)
print(cart1)
print(cart2)
print(f"Total orders: {total_orders}")
print(f"Total revenue: {total_revenue}")
print(f"Order 1 discountedtotal: {order1_discounted_total}")
print(f"Order 2 discountedtotal: {order2_discounted_total}")


        
    
    
                
                    
                     