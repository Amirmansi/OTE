from . import __version__ as app_version

app_name = "dox_theme"
app_title = "Dox Theme"
app_publisher = "Nesscale"
app_description = "Dox Theme"
app_email = "info@nesscale.com"
app_license = "MIT"
app_logo = "/assets/dox_theme/images/dox_logo.png"

# Includes in <head>
# ------------------

# Include CSS and JavaScript files in header of desk.html
app_include_css = ["/assets/dox_theme/css/dox_theme.css", "/assets/dox_theme/css/dox.bundle.css"]
app_include_js = ["/assets/dox_theme/js/dox_theme.js", "/assets/dox_theme/js/dox_theme_desk.bundle.js"]

# Include CSS and JavaScript files in header of web template
# Uncomment if needed for web views
# web_include_css = "/assets/dox_theme/css/dox_theme_web.css"
# web_include_js = "/assets/dox_theme/js/dox_theme.js"

# Include custom SCSS in every website theme (without file extension ".scss")
# website_theme_scss = "dox_theme/public/scss/website"

# Include JavaScript in doctype views if needed
# Uncomment if you have specific files for each doctype view
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Installation Hooks
# ------------------
# Hook functions to run after installation, uninstallation, and migration
# These functions must be compatible with ERPNext v15

after_uninstall = [
    "dox_theme.whitelabel.dox_patch",
    "dox_theme.workspace_icon_set.update_workspace_images",
]

after_migrate = [
    "dox_theme.whitelabel.dox_patch",
    "dox_theme.workspace_icon_set.update_workspace_images",
]

# Method Overrides
# ----------------
# Override ERPNext or Frappe methods if needed

override_whitelisted_methods = {
    "frappe.desk.desktop.get_workspace_sidebar_items": "dox_theme.utils.get_workspace_sidebar_items"
}

# Scheduler Events (Optional)
# ------------------
# Uncomment if you need scheduled tasks
# scheduler_events = {
#     "all": ["dox_theme.tasks.all"],
#     "daily": ["dox_theme.tasks.daily"],
#     "hourly": ["dox_theme.tasks.hourly"],
#     "weekly": ["dox_theme.tasks.weekly"],
#     "monthly": ["dox_theme.tasks.monthly"],
# }

# Authentication and authorization
# --------------------------------
# Uncomment if you have custom auth hooks
# auth_hooks = [
#     "dox_theme.auth.validate"
# ]

# Testing
# -------
# Uncomment if there are tests that need to run before tests
# before_tests = "dox_theme.install.before_tests"
