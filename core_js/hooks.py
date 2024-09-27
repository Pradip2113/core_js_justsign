from . import __version__ as app_version

app_name = "core_js"
app_title = "Core Js"
app_publisher = "Justsigns"
app_description = "Justsigns Customization"
app_email = "dev@justsigns.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/core_js/css/core_js.css"
# app_include_js = "/assets/core_js/js/core_js.js"

# include js, css files in header of web template
# web_include_css = "/assets/core_js/css/core_js.css"
# web_include_js = "/assets/core_js/js/core_js.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "core_js/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Opportunity" : "public/js/opportunity.js",
              "Lead":"public/js/lead.js",
              "Prospect":"public/js/prospect.js",
              "Customer":"public/js/customer.js"}

doctype_list_js = {"Prospect" : "public/js/prospect_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "core_js.utils.jinja_methods",
#	"filters": "core_js.utils.jinja_filters"
# }

jinja = {
    "methods" : [
      "core_js.core_js.utils.sales_order_print.get_invoice_item_and_tax_details",
      "core_js.core_js.utils.sales_invoice_print.get_inv_item_and_tax_details",
      "frappe.utils.data.money_in_words"
    ]
}

# Installation
# ------------

# before_install = "core_js.install.before_install"
# after_install = "core_js.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "core_js.uninstall.before_uninstall"
# after_uninstall = "core_js.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "core_js.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Lead": "core_js.core_js.utils.contact_updation._Lead",
    
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Contact": {
		"validate": "core_js.core_js.utils.contact_updation.validate"
	},
    "Lead":{
        "validate":"core_js.core_js.utils.leads.validate",
        
    },
    "Opportunity":{
        "validate":"core_js.core_js.utils.opportunity.validate"
    },
    "Prospect":{
        "validate":"core_js.core_js.utils.prospect.validate",
        "on_trash": "core_js.core_js.utils.prospect.on_trash",
        "after_insert": "core_js.core_js.utils.prospect.after_insert"
    },
    "Customer":{
        "before_save":"core_js.core_js.utils.customer.add_contact_ref"
    },
    
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron":{
		'00 11 * * *':"core_js.core_js.utils.shift_type.thirvusoft_process_auto_attendance_shift",
	}
#	"all": [
#		"core_js.tasks.all"
#	],
#	"daily": [
#		"core_js.tasks.daily"
#	],
#	"hourly": [
#		"core_js.tasks.hourly"
#	],
#	"weekly": [
#		"core_js.tasks.weekly"
#	],
#	"monthly": [
#		"core_js.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "core_js.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "core_js.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "core_js.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["core_js.utils.before_request"]
# after_request = ["core_js.utils.after_request"]

# Job Events
# ----------
# before_job = ["core_js.utils.before_job"]
# after_job = ["core_js.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"core_js.auth.validate"
# ]
