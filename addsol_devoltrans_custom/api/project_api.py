import frappe
from frappe import _


@frappe.whitelist()
def get_project_summary(project_name):
    project = frappe.get_doc("Project", project_name)
    return {
        "name": project.name,
        "status": project.status,
        "customer": project.customer,
        "tasks": len(project.tasks or []),
    }


whitelisted_methods = {
    "addsol_devoltrans_custom.api.project_api.get_project_summary": "addsol_devoltrans_custom.api.project_api.get_project_summary"
}
