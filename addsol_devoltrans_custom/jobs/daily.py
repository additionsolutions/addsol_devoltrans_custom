import frappe


def cleanup_old_logs():
    frappe.logger().info("Cleaning up old logs...")
    # example maintenance job
    frappe.db.delete("Error Log", {"creation": (
        "<", frappe.utils.add_days(frappe.utils.nowdate(), -30))})


daily = ["addsol_devoltrans_custom.jobs.daily.cleanup_old_logs"]
