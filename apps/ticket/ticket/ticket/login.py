import frappe
from frappe.auth import LoginManager

@frappe.whitelist(allow_guest = True)

def get_user_details(user):
	user_details = frappe.get_all("User",filters={"name":user},fields=["name","first_name","last_name","email","role_profile_name"])
	print(user_details)
	if user_details:
		return user_details
