import pandas as pd
from app import db, create_app
from dotenv import load_dotenv
from app.models.restaurants import Restaurants
from app.models.services import Services
from app.models.stores import Stores

# Load environment variables from .env file
load_dotenv()


def import_csv_to_db(filename, model, column_mappings, dtype_dict):
    app = create_app()
    with app.app_context():
        db.session.query(model).delete()

        # Read CSV data with specified data types
        data = pd.read_csv(filename, dtype=dtype_dict)

        # Rename columns to match model attributes
        data.rename(columns=column_mappings, inplace=True)

        # Insert data into database
        for _, row in data.iterrows():
            row_dict = row.to_dict()

            # Remove unwanted keys from row_dict if it exists
            row_dict.pop("Latitude", None)
            row_dict.pop("Longitude", None)
            row_dict.pop("First Name ", None)
            row_dict.pop("Last Name ", None)

            # Handle public business column
            if "public_business" in row_dict:
                if pd.isna(row_dict["public_business"]):
                    row_dict["public_business"] = None  # Keep it empty if NaN
                else:
                    row_dict["public_business"] = bool(row_dict["public_business"])

            # Handle non profit column
            if "non_profit" in row_dict:
                if pd.isna(row_dict["non_profit"]):
                    row_dict["non_profit"] = None  # Keep it empty if NaN
                else:
                    row_dict["non_profit"] = bool(row_dict["non_profit"])
            record = model(**row_dict)
            db.session.add(record)
        db.session.commit()


if __name__ == "__main__":
    # Column mappings for entities
    restaurants_column_mappings = {
        "Cuisine/Shop type": "cuisine_shop_type",
        "Buisness Name": "name",
        "Address": "address",
        "City": "city",
        "State ": "state",
        "Zip Code ": "zip_code",
        "County ": "county",
        "Phone": "phone_number",
        "Email": "email",
        "Website": "website",
        "Description": "description",
    }
    stores_column_mappings = {
        "Store type": "store_type",
        "Store Name": "name",
        "Address": "address",
        "City": "city",
        "State ": "state",
        "Zip Code ": "zip_code",
        "County ": "county",
        "Phone": "phone",
        "Email": "email",
        "Website": "website",
        "Description": "description",
    }

    services_column_mappings = {
        "Category": "service_type",
        "Company Name": "name",
        "Address": "address",
        "City": "city",
        "State ": "state",
        "Zip Code ": "zip_code",
        "County ": "county",
        "Phone": "phone",
        "Email": "email",
        "Website": "website",
        "Public Business Entity Y/N": "public_business",
        "Non Profit  Y/N": "non_profit",
        "Profile of Service  Description": "description",
    }

    # sites_column_mappings = {
    #     "Name ":"name",
    #     "Adress":"address",
    #     "City":"city",
    #     "State":"state ",
    #     "Zip code":"zip_code",
    #     "County":"county",
    #     "Website":"description",
    # }
    restaurants_dtype_dict = {"Zip Code ": str, "Description": str}

    import_csv_to_db(
        "data/Black_owned_restaurants.csv",
        Restaurants,
        restaurants_column_mappings,
        restaurants_dtype_dict,
    )
    import_csv_to_db("data/Black owned stores.csv", Stores, stores_column_mappings, {})
    import_csv_to_db(
        "data/Black owned services .csv", Services, services_column_mappings, {}
    )

    print("Data import completed successfully.")
