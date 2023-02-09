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
    request_data = request.get_json()

    try:
        new_restaurant = Restaurants(
            cuisine_shop_type = request_data["cuisine_shop_type"], 
            name = request_data['name'],
            address = request_data["address"], 
            city = request_data['city'],
            state = request_data['state'],
            zip_code = request_data['zip_code'], 
            county = request_data['county'], 
            phone_number = request_data['phone_number'], 
            email = request_data['email'],
            website = request_data['website'],
            description = request_data['description'], 
            latitude = request_data['latitude'], 
            longitude = request_data['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({"restaurant": new_restaurant.to_dict()}), 201

@restaurants_bp.route('/<restaurant_id>', methods=['PUT'])
def update_one_restaurant(restaurant_id):
    update_restaurant = get_model_from_id(Restaurants, restaurant_id)

    request_data = request.get_json()

    try:
        update_restaurant.cuisine_shop_type = request_data['cuisine_shop_type']
        update_restaurant.name = request_data['name']
        update_restaurant.address = request_data["address"]
        update_restaurant.city = request_data['city']
        update_restaurant.state = request_data['state']
        update_restaurant.zip_code = request_data['zip_code']
        update_restaurant.county = request_data['county']
        update_restaurant.phone_number = request_data['phone_number']
        update_restaurant.email = request_data['email']
        update_restaurant.website = request_data['website']
        update_restaurant.description = request_data['description']
        update_restaurant.latitude = request_data['latitude']
        update_restaurant.longitude = request_data['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"restaurant": update_restaurant.to_dict()}), 200

@restaurants_bp.route('/<restaurant_id>', methods=['DELETE'])
def delete_one_restaurant(restaurant_id):
    restaurant_to_delete = get_model_from_id(Restaurants, restaurant_id)

    db.session.delete(restaurant_to_delete)
    db.session.commit()

    return jsonify({"details": f'Restaurant {restaurant_to_delete.restaurant_id} {restaurant_to_delete.name} successfully deleted'}), 200 



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
    request_data = request.get_json()

    try:
        new_historicalsites = Sites(
        name = request_data['name'], 
        address = request_data['address'], 
        city = request_data['city'],
        state = request_data['state'],
        zip_code = request_data['zip_code'], 
        county = request_data['county'],
        website = request_data['website'],
        description = request_data['description'], 
        latitude = request_data['latitude'], 
        longitude = request_data['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_historicalsites)
    db.session.commit()

    return jsonify(new_historicalsites.to_dict()), 201


@historicalsites_bp.route('/<sites_id>', methods=['PUT'])
def update_one_historicalsites(sites_id):
    update_historicalsites = get_model_from_id(Sites, sites_id)

    request_data = request.get_json()

    try:
        update_historicalsites.name = request_data["name"]
        update_historicalsites.address = request_data["address"]
        update_historicalsites.city = request_data['city']
        update_historicalsites.state = request_data['state']
        update_historicalsites.zip_code = request_data['zip_code']
        update_historicalsites.county = request_data['county']
        update_historicalsites.website = request_data['website']
        update_historicalsites.description = request_data['description']
        update_historicalsites.latitude = request_data['latitude']
        update_historicalsites.longitude = request_data['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"historical sites": update_historicalsites.to_dict()}), 200

@historicalsites_bp.route('/<sites_id>', methods=['DELETE'])
def delete_one_historicalsites(sites_id):
    historicalsites_to_delete = get_model_from_id(Sites, sites_id)

    db.session.delete(historicalsites_to_delete)
    db.session.commit()

    return jsonify({"details": f'Historical site {historicalsites_to_delete.sites_id} {historicalsites_to_delete.name} successfully deleted'}), 200 

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
    request_data = request.get_json()

    try:
        new_restaurant = Services(
            service_type = request_data["service_type"],
            name = request_data["name"], 
            address = request_data["address"], 
            city = request_data['city'],
            state = request_data['state'],
            zip_code = request_data['zip_code'], 
            county = request_data['county'],
            phone = request_data['phone'], 
            email = request_data['email'],
            website = request_data['website'],
            latitude = request_data['latitude'], 
            longitude = request_data['longitude'],
            public_business = request_data["public_business"],
            non_profit = request_data["non_profit"],
            description = request_data['description'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({"restaurant": new_restaurant.to_dict()}), 201

@services_bp.route('/<service_id>', methods=['PUT'])
def update_one_service(service_id):
    update_service = get_model_from_id(Services, service_id)

    request_data = request.get_json()

    try:
        update_service.servicetype = request_data['service_type']
        update_service.name = request_data['name']
        update_service.address = request_data["address"]
        update_service.city = request_data['city']
        update_service.state = request_data['state']
        update_service.zip_code = request_data['zip_code']
        update_service.county = request_data['county']
        update_service.phone= request_data['phone']
        update_service.email = request_data['email']
        update_service.website = request_data['website']
        update_service.latitude = request_data['latitude']
        update_service.longitude = request_data['longitude']
        update_service.public_business = request_data['public_business']
        update_service.non_profit = request_data['non_profit']
        update_service.description = request_data['description']
        

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"Service": update_service.to_dict()}), 200

@services_bp.route('/<service_id>', methods=['DELETE'])
def delete_one_service(service_id):
    service_to_delete = get_model_from_id(Services, service_id)

    db.session.delete(service_to_delete)
    db.session.commit()

    return jsonify({"details": f'Black owned Service {service_to_delete.service_id} {service_to_delete.name} successfully deleted'}), 200 


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
    request_data = request.get_json()

    try:
        new_store = Stores(
            store_type = request_data['store_type'],
            name = request_data['name'],
            address = request_data['address'], 
            city = request_data['city'],
            state = request_data['state'],
            zip_code = request_data['zip_code'], 
            county = request_data['county'],
            phone = request_data['phone'],
            email = request_data['email'], 
            website = request_data['website'],
            description = request_data['description'], 
            latitude = request_data['latitude'], 
            longitude = request_data['longitude'])
    except KeyError:
        return jsonify({"details": "Invalid data"}), 400

    db.session.add(new_store)
    db.session.commit()

    return jsonify({"stores": new_store.to_dict()}), 201


@stores_bp.route('/<store_id>', methods=['PUT'])
def update_one_stores(store_id):
    update_stores = get_model_from_id(Stores, store_id)

    request_data = request.get_json()

    try:
        update_stores.store_type = request_data['store_type']
        update_stores.name = request_data['name']
        update_stores.address = request_data["address"]
        update_stores.city = request_data['city']
        update_stores.state = request_data['state']
        update_stores.zip_code = request_data['zip_code']
        update_stores.county = request_data['county']
        update_stores.phone = request_data['phone']
        update_stores.email = request_data['email']
        update_stores.website = request_data['website']
        update_stores.description = request_data['description']
        update_stores.latitude = request_data['latitude']
        update_stores.longitude = request_data['longitude']

    except KeyError:
        return jsonify({"msg": "Missing needed data"}), 400

    db.session.commit()
    return jsonify({"Store": update_stores.to_dict()}), 200

@stores_bp.route('/<store_id>', methods=['DELETE'])
def delete_one_restaurant(store_id):
    store_to_delete = get_model_from_id(Stores, store_id)

    db.session.delete(store_to_delete)
    db.session.commit()

    return jsonify({"details": f'Store {store_to_delete.store_id} {store_to_delete.name} successfully deleted'}), 200 



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

    #LOCATION API route 
load_dotenv()

proxy_bp = Blueprint("proxy_bp", __name__)

location_key = os.environ.get("LOCATION_KEY")

@proxy_bp.route("/location", methods=["GET"])
def get_lat_lon():
    loc_query = request.args.get("q")
    if not loc_query:
        return {"message": "must provide q parameter (location)"}

    response = requests.get(
        "https://us1.locationiq.com/v1/search.php",
        params={"q": loc_query, "key": location_key, "format": "json"}
    )

    return jsonify(response.json())