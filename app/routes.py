from flask import Blueprint, request, jsonify, make_response,abort 
from app import db
import os,requests
from dotenv import load_dotenv

from app.models.restaurants import Restaurants
from app.models.historical_sites import Sites
from app.models.stores import Stores
from app.models.services import Services 
# example_bp = Blueprint('example_bp', __name__)

#RESTAURANTS
restaurants_bp = Blueprint("restaurants_bp", __name__, url_prefix="/restaurants")

@restaurants_bp.route('', methods = ['GET'])
def get_all_restaurants():
    restaurants = Restaurants.query.all()

    result = []
    for item in restaurants:
        result.append(item.to_dict())

    return jsonify(result), 200 

@restaurants_bp.route('/<restaurant_id>', methods=['GET'])
def get_one_restaurant(restaurant_id):
    chosen_restaurant = get_model_from_id(Restaurants, restaurant_id) 
    return jsonify({"restaurant": chosen_restaurant.to_dict()}), 200

@restaurants_bp.route('', methods=['POST'])
def create_one_restaurant():
    request_body = request.get_json()

    try:
        new_restaurant = Restaurants(type = request_body["type"], address = request_body["address"], city = request_body['city'],
        state = request_body['state'],zip_code = request_body['zipcode'], county = request_body['county'], phone_number = request_body['number'], email = request_body['email'],website = request_body['website'],
        description = request_body['description'], latitude = request_body['latitude'], longitude = request_body['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({"restaurant": new_restaurant.to_dict()}), 201

@restaurants_bp.route('/<restaurant_id>', methods=['PUT'])
def update_one_restaurant(restaurant_id):
    update_restaurant = get_model_from_id(Restaurants, restaurant_id)

    request_body = request.get_json()

    try:
        update_restaurant.cuisine_shop_type = request_body['cuisine_shop_type']
        update_restaurant.name = request_body['name']
        update_restaurant.address = request_body["address"]
        update_restaurant.city = request_body['city']
        update_restaurant.state = request_body['state']
        update_restaurant.zip_code = request_body['zip_code']
        update_restaurant.county = request_body['county']
        update_restaurant.phone_number = request_body['phone_number']
        update_restaurant.email = request_body['email']
        update_restaurant.website = request_body['website']
        update_restaurant.description = request_body['description']
        update_restaurant.latitude = request_body['latitude']
        update_restaurant.longitude = request_body['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"restaurant": update_restaurant.to_dict()}), 200

@restaurants_bp.route('/<restaurant_id>', methods=['DELETE'])
def delete_one_restaurant(restaurant_id):
    restaurant_to_delete = get_model_from_id(Restaurants, restaurant_id)

    db.session.delete(restaurant_to_delete)
    db.session.commit()

    return jsonify({"details": f'Restaurant {restaurant_to_delete.restaurant_id} {restaurant_to_delete.title} successfully deleted'}), 200 



# HISTORICAL SITES
historicalsites_bp = Blueprint("historicalsites_bp", __name__, url_prefix="/historicalsites")

@historicalsites_bp.route('', methods = ['GET'])
def get_all_historicalsites():
    historicalsites= Sites.query.all()

    result = []
    for item in historicalsites:
        result.append(item.to_dict())

    return jsonify(result), 200 

@historicalsites_bp.route('/<sites_id>', methods=['GET'])
def get_one_historicalsites(sites_id):
    chosen_historicalsites = get_model_from_id(Sites, sites_id) 
    return jsonify({"restaurant": chosen_historicalsites.to_dict()}), 200

@historicalsites_bp.route('', methods=['POST'])
def create_one_historicalsites():
    request_body = request.get_json()

    try:
        new_historicalsites = Sites(type = request_body["type"], address = request_body["address"], city = request_body['city'],
        state = request_body['state'],zip_code = request_body['zip_code'], county = request_body['county'],website = request_body['website'],
        description = request_body['description'], latitude = request_body['latitude'], longitude = request_body['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_historicalsites)
    db.session.commit()

    return jsonify({"board": new_historicalsites.to_dict()}), 201

@historicalsites_bp.route('/<sites_id>', methods=['PUT'])
def update_one_historicalsites(sites_id):
    update_historicalsites = get_model_from_id(Sites, sites_id)

    request_body = request.get_json()

    try:
        update_historicalsites.name = request_body["name"]
        update_historicalsites.address = request_body["address"]
        update_historicalsites.city = request_body['city']
        update_historicalsites.state = request_body['state']
        update_historicalsites.zip_code = request_body['zip_code']
        update_historicalsites.county = request_body['county']
        update_historicalsites.website = request_body['website']
        update_historicalsites.description = request_body['description']
        update_historicalsites.latitude = request_body['latitude']
        update_historicalsites.longitude = request_body['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"historical sites": update_historicalsites.to_dict()}), 200

@historicalsites_bp.route('/<sites_id>', methods=['DELETE'])
def delete_one_historicalsites(sites_id):
    historicalsites_to_delete = get_model_from_id(Sites, sites_id)

    db.session.delete(historicalsites_to_delete)
    db.session.commit()

    return jsonify({"details": f'Historical site {historicalsites_to_delete.historicalsites_id} {historicalsites_to_delete.title} successfully deleted'}), 200 

#SERVICES

services_bp = Blueprint("services_bp", __name__, url_prefix="/blackownedservices")

@services_bp.route('', methods = ['GET'])
def get_all_services():
    services = Services.query.all()

    result = []
    for item in services:
        result.append(item.to_dict())

    return jsonify(result), 200 

@services_bp.route('/<service_id>', methods=['GET'])
def get_one_service(service_id):
    chosen_service = get_model_from_id(Services, service_id) 
    return jsonify({"restaurant": chosen_service.to_dict()}), 200

@services_bp.route('', methods=['POST'])
def create_one_service():
    request_body = request.get_json()

    try:
        new_restaurant = Services(service_type = request_body["service_type"],name = request_body["name"], address = request_body["address"], city = request_body['city'],
        state = request_body['state'],zip_code = request_body['zip_code'], county = request_body['county'],
        phone = request_body['phone'], email = request_body['email'],website = request_body['website'],latitude = request_body['latitude'], longitude = request_body['longitude'],
        public_business = request_body["public_business"],non_profit = request_body["non_profit"],description = request_body['description'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({"restaurant": new_restaurant.to_dict()}), 201

@services_bp.route('/<service_id>', methods=['PUT'])
def update_one_service(service_id):
    update_service = get_model_from_id(Services, service_id)

    request_body = request.get_json()

    try:
        update_service.servicetype = request_body['service_type']
        update_service.name = request_body['name']
        update_service.address = request_body["address"]
        update_service.city = request_body['city']
        update_service.state = request_body['state']
        update_service.zip_code = request_body['zip_code']
        update_service.county = request_body['county']
        update_service.phone= request_body['phone']
        update_service.email = request_body['email']
        update_service.website = request_body['website']
        update_service.latitude = request_body['latitude']
        update_service.longitude = request_body['longitude']
        update_service.public_business = request_body['public_business']
        update_service.non_profit = request_body['non_profit']
        update_service.description = request_body['description']
        

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"Service": update_service.to_dict()}), 200

@services_bp.route('/<service_id>', methods=['DELETE'])
def delete_one_service(service_id):
    service_to_delete = get_model_from_id(Services, service_id)

    db.session.delete(service_to_delete)
    db.session.commit()

    return jsonify({"details": f'Restaurant {service_to_delete.restaurant_id} {service_to_delete.title} successfully deleted'}), 200 









#STORES

stores_bp = Blueprint("stores_bp", __name__, url_prefix="/blackownedstores")
@stores_bp.route('', methods = ['GET'])
def get_all_stores():
    black_owned_stores= Stores.query.all()

    result = []
    for item in black_owned_stores:
        result.append(item.to_dict())

    return jsonify(result), 200 

@stores_bp .route('/<store_id>', methods=['GET'])
def get_one_store(store_id):
    chosen_store = get_model_from_id(Stores, store_id) 
    return jsonify({"Store": chosen_store.to_dict()}), 200

@stores_bp .route('', methods=['POST'])
def create_one_store():
    request_body = request.get_json()

    try:
        new_store = Stores(store_type = request_body["store_type"], address = request_body["address"], city = request_body['city'],
        state = request_body['state'],zip_code = request_body['zip_code'], county = request_body['county'],phone = request_body['phone'],email = request_body['email'], website = request_body['website'],
        description = request_body['description'], latitude = request_body['latitude'], longitude = request_body['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_store)
    db.session.commit()

    return jsonify({"board": new_store.to_dict()}), 201


@stores_bp.route('/<store_id>', methods=['PUT'])
def update_one_stores(store_id):
    update_stores = get_model_from_id(Stores, store_id)

    request_body = request.get_json()

    try:
        update_stores.store_type = request_body['store_type']
        update_stores.name = request_body['name']
        update_stores.address = request_body["address"]
        update_stores.city = request_body['city']
        update_stores.state = request_body['state']
        update_stores.zip_code = request_body['zip_code']
        update_stores.county = request_body['county']
        update_stores.phone = request_body['phone']
        update_stores.email = request_body['email']
        update_stores.website = request_body['website']
        update_stores.description = request_body['description']
        update_stores.latitude = request_body['latitude']
        update_stores.longitude = request_body['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"Store": update_stores.to_dict()}), 200

@stores_bp.route('/<store_id>', methods=['DELETE'])
def delete_one_restaurant(store_id):
    store_to_delete = get_model_from_id(Stores, store_id)

    db.session.delete(store_to_delete)
    db.session.commit()

    return jsonify({"details": f'Store {store_to_delete.store_id} {store_to_delete.title} successfully deleted'}), 200 



# helper function
def get_model_from_id(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        return abort(make_response({"msg": f"invalid data: {model_id}"}, 400))

    chosen_model = cls.query.get(model_id)

    if chosen_model is None:
        return abort(make_response({"msg": f"Could not find item with id: {model_id}"}, 404))
    
    return chosen_model