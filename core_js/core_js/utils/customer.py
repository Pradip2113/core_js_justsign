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
    # frappe.msgprint(f"{doc['custom_from_prospect']}")
    if doc['custom_from_prospect']:
        # is_contact_exists = frappe.db.exists("Contact",{"mobile_no":doc.custom_phone_no})
        # if is_contact_exists:
        #     frappe.throw(f"Mobile no already exists in Contact - <b>{is_contact_exists}</b>")
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
@frappe.whitelist()
def add_contact_ref(doc,event):
    if doc.mobile_no:
        contact_doc_id = frappe.get_value("Contact",{"mobile_no":doc.mobile_no},"name")
        doc.customer_primary_contact = contact_doc_id if contact_doc_id else frappe.throw(f"Contact for {doc.mobile_no} does not exist")
    # Change Lead status to Converted
    if doc.custom_from_prospect:
        lead_id = frappe.get_value("Prospect Lead",{"parent":doc.custom_from_prospect},"lead")
        suspect_id = frappe.get_value("Prospect",{"name":doc.custom_from_prospect},"custom_suspect_id")
        if suspect_id:
            doc.custom_from_suspect = suspect_id
        if lead_id:
            doc.lead_name = lead_id
            lead_doc = frappe.get_doc("Lead",lead_id)
            lead_doc.status = "Converted"
            lead_doc.save()
            
            
   
        
#  @frappe.whitelist()
# def beforesaveevent(doc):       
# if isinstance(doc, str):
#     # Fetch the full document using get_doc
#     doc = frappe.get_doc("Customer", doc)

# # Ensure we are working with a dictionary-style doc object
# custom_from_prospect = doc.get("custom_from_prospect")

# if custom_from_prospect:
#     # Fetch the lead using frappe.get_value
#     set_lead_id = frappe.get_value("Prospect Lead", {"parent": custom_from_prospect}, "lead")
    
#     if set_lead_id:
#         # Set the lead_name field directly since get_value returns the value
#         doc.lead_name = set_lead_id
#     else:
#         frappe.throw("Lead not found for the given custom_from_prospect.")
# else:
#     frappe.throw("custom_from_prospect is missing from the document.")

# # Optionally return the modified document
# return doc