import frappe
import json
def on_trash(doc,event):
    if doc.custom_from_prospect:
        frappe.set_value("Prospect", doc.custom_from_prospect, "status", "New")
        frappe.set_value("Prospect", doc.custom_from_prospect, "custom_make_read_only", 0)
        
@frappe.whitelist()
def add_cust_to_contact(doc):
    doc = json.loads(doc)
    # frappe.throw(f"{doc['custom_from_prospect']}")
    frappe.msgprint(f"{doc['custom_from_prospect']}")
    if doc['custom_from_prospect']:
        mob_no = frappe.get_value("Prospect Lead",{"parent":doc['custom_from_prospect']},"mobile_no")
        contact_doc = frappe.get_doc("Contact",{"mobile_no":mob_no})
        contact_doc.append("links",{
            "link_doctype":"Customer",
            "link_name":doc['name']
            
        })
        contact_doc.save()
    else:
        is_contact_exists = frappe.db.exists("Contact",{"mobile_no":doc.custom_phone_no})
        if is_contact_exists and not doc.custom_override_contact:
            frappe.throw(f"Mobile no already exists in Contact - <b>{is_contact_exists}</b>")
            # contact_doc = frappe.get_doc("Contact",is_contact_exists)
            # if not doc.custom_override_contact:
                
            #     override_field = contact_doc.get("links")
            #     override_field[0].link_name = doc.name
            #     contact_doc.insert()
            #     # frappe.throw(str(override_field[0]))
            # else:  
            #     frappe.throw(str(is_contact_exists))