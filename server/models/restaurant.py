from sqlalchemy.orm import validates
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete'
    )

    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value.strip()) < 3:
            raise ValueError("Restaurant name must be at least 3 characters long.")
        return value

    @validates('address')
    def validate_address(self, key, value):
        if not value or len(value.strip()) < 5:
            raise ValueError("Restaurant address must be provided.")
        return value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [rp.pizza.to_dict() for rp in self.restaurant_pizzas if rp.pizza]
        }

    