import frappe


def before_save(doc, method):
    frappe.logger().info(f"BOM {doc.name} before save triggered")


doc_events = {
    "BOM": {
        "before_save": before_save
    }
}
