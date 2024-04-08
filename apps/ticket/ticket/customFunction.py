import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def receive_data_from_other_app():
    try:

        data = frappe.request.data

        data = data.decode('utf-8')

        parsed_data = frappe.parse_json(data)
        print("data comes", data)

        ticketid = parsed_data.get("ticketid")
        topic = parsed_data.get("topic")
        createdby = parsed_data.get("createdby")

        doc = frappe.get_doc({
            "doctype": "CustomerTickets",
            "ticketid": ticketid,
            "topic": topic,
            "createdby": createdby
        })
        doc.insert()
        print("data added")
        return _("Data successfully received and stored.")
    except Exception as e:
        frappe.log_error(f"Error receiving data from other app: {str(e)}", "Custom Function Error")
        return _("Failed to receive and store data. Please check logs for details.")


@frappe.whitelist(allow_guest=True)
def add_comment_with_created_by(doctype, docname, message, user=None):
    doc = frappe.get_doc(doctype, docname)
    comment = "Comment"
    if user:
        created_by = user
    else:
        created_by = "r"

    doc.add_comment(comment_type=comment, comment_by=created_by, text=message, comment_email="new@gmil.com" )

    doc.save()
