from supabase import create_client, Client
import json
from decimal import Decimal

# Initialize Supabase client
url = "https://cfwxqciwyfpieiltepmq.supabase.co"  # Replace with your Supabase URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNmd3hxY2l3eWZwaWVpbHRlcG1xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzk1MzkzNDIsImV4cCI6MjA1NTExNTM0Mn0.FYzz_RxVfTePjSps29r_lqUlCqOro4Om8kPUsRO8HVI"  # Replace with your Supabase anon key"
supabase: Client = create_client(url, key)

def save_user_signup_details(signup_details):
    try:
        data = {
            "full_name": signup_details['full_name'],
            "email": signup_details['email'],
            "password": signup_details['password']
        }

        if signup_details['role'] == "user":
            supabase.table("user_info").insert(data).execute()
            supabase.table("user_login").insert({"email": data['email'], "password": data['password']}).execute()

        elif signup_details['role'] == "admin":
            supabase.table("admin_info").insert(data).execute()
            supabase.table("admin_login").insert({"email": data['email'], "password": data['password']}).execute()

        return "Success"

    except Exception as e:
        print("Error:", str(e))
        return f"Error: {str(e)}"

def validate_login_details(login_data):
    try:
        table = "user_login" if login_data['role'] == "user" else "admin_login"
        response = supabase.table(table).select("email, password").eq("email", login_data['email']).execute()
        if response.data:
            user = response.data[0]
            return login_data['password'] == user['password']
        return False
    except Exception as e:
        print("Error:", str(e))
        return False

def save_contact_message(contact_data):
    try:
        data = {
            "full_name": contact_data['full_name'],
            "email": contact_data['email'],
            "message": contact_data['message']
        }
        supabase.table("contact_messages").insert(data).execute()
        return "Success"
    except Exception as e:
        print("Error:", str(e))
        return f"Error: {str(e)}"

def upload_image(image_data):
    try:
        data = {
            "plant_name": image_data['plantName'],
            "price": image_data['plantPrice'],
            "description": image_data['plantDescription'],
            "plant_images": image_data['image'],
            "plant_type": image_data['plantType'],
            "plant_product": image_data['productType'],
            "uploader_email": image_data['uploaderEmail']
        }
        supabase.table("plants_images").insert(data).execute()
        return "Success"
    except Exception as e:
        print("Error:", str(e))
        return f"Error: {str(e)}"


def get_plant_image_data(filter_data):
    try:
        query = supabase.table("plants_images").select("*")
        if filter_data.get('selectPlantType'):
            query = query.eq("plant_type", filter_data['selectPlantType'])
        if filter_data.get('selectFertilizerandSeeds'):
            query = query.eq("plant_product", filter_data['selectFertilizerandSeeds'])
        response = query.execute()

        for record in response.data:
            if isinstance(record.get("price"), Decimal):
                record["price"] = float(record["price"])

        return json.dumps(response.data, indent=4)
    except Exception as e:
        print("Error:", str(e))
        return json.dumps({"error": "Error occurred while fetching plant data."})

def save_cart_details(cart_data):
    try:
        data = {
            "email_id": cart_data['email_id'],
            "plant_name": cart_data['name'],
            "price": cart_data['price'],
            "plant_image": cart_data['image']
        }
        supabase.table("cart_details").insert(data).execute()
        return "Success"
    except Exception as e:
        print("Error:", str(e))
        return f"Error: {str(e)}"

def get_cart_details_data(cart_data):
    try:
        response = supabase.table("cart_details").select("*").eq("email_id", cart_data['email_id']).execute()

        for record in response.data:
            if isinstance(record.get("price"), Decimal):
                record["price"] = float(record["price"])
            if isinstance(record.get("total_price"), Decimal):
                record["total_price"] = float(record["total_price"])

        return json.dumps(response.data, indent=4)
    except Exception as e:
        print("Error:", str(e))
        return json.dumps({"error": "Error occurred while fetching cart data."})

def get_remove_cart_item_data(remove_cart_data):
    try:
        supabase.table("cart_details").delete().eq("id", remove_cart_data['itemId']).execute()
        return "Success"
    except Exception as e:
        print("Error:", str(e))
        return f"Error: {str(e)}"

def save_submit_order_details(order_data):
    try:
        print("Inserting order data into Supabase:", order_data)

        response = supabase.table("order_details").insert(order_data).execute()
        
        print("Supabase response:", response)
        
        if response.data:
            return "Success"
        else:
            return f"Error: No data returned from Supabase"

    except Exception as e:
        print("Error inserting into Supabase:", str(e))
        return f"Error: {str(e)}"

