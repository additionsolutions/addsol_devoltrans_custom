import frappe


def validate(doc, method):
    frappe.logger().info(f"Validating Project {doc.name}")


doc_events = {
    "Project": {
        "validate": validate
    }
}
