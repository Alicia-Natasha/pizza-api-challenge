from server.models import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Pizza name must be at least 2 characters.")
        return value

    @validates('ingredients')
    def validate_ingredients(self, key, value):
        if not value or ',' not in value:
            raise ValueError("Ingredients should be a comma-separated list.")
        return value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

    
