from flask import Blueprint, request, jsonify
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        if not pizza or not restaurant:
            return jsonify({"errors": ["Invalid restaurant_id or pizza_id"]}), 400

        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        return jsonify(pizza.to_dict()), 201  # as per spec
    except KeyError as ke:
        return jsonify({"errors": [f"Missing field: {ke.args[0]}"]}), 400
    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Invalid restaurant_id or pizza_id"]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 500
