from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_all_pizzas():
    try:
        pizzas = Pizza.query.all()
        return jsonify([p.to_dict() for p in pizzas]), 200
    except Exception as e:
            return jsonify({"error": str(e)}), 500