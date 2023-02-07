from app import db

class Restaurants(db.Model):
    restaurant_id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    cuisine_shop_type = db.Column(db.String)
    name = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    county = db.Column(db.String)
    phone_number = db.Column(db.String)
    email = db.Column(db.String)
    website = db.Column(db.String)
    description = db.Column(db.String)
    latitude = db.Column(db.String)
    longitude = db.Column(db.String)

    def to_dict(self):
        return {
            "id":self.restaurant_id,
            "cuisine_shop_type":self.cuisine_shop_type,
            "name":self.name,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "zip_code":self.zip_code,
            "county":self.county,
            "phone_number":self.phone_number,
            "email":self.email,
            "website":self.website,
            "description":self.description,
            "latitude":self.latitude,
            "longitude":self.longitude
        }