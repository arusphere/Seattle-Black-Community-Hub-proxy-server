from app import db 

class Services(db.Model):
    service_id = db.Column(db.Integer, primary_key =True,autoincrement=True)
    service_type = db.Column(db.String)
    name = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip_code = db.Column(db.String)
    county = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    website = db.Column(db.String)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    public_business = db.Column(db.Boolean)
    non_profit = db.Column(db.Boolean)
    description = db.Column(db.String)

    def to_dict(self):
        return {
            "id":self.service_id,
            "service_type":self.service_type,
            "name":self.name,
            "address":self.address,
            "city":self.city,
            "state":self.state,
            "zip_code":self.zip_code,
            "county":self.county,
            "phone":self.phone,
            "email":self.email,
            "website":self.website,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "public_business":self.public_business,
            "non_profit":self.non_profit,
            "description":self.description,

        }