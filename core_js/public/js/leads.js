frappe.ui.form.on('Lead', {
    onload: function(frm) {
        // Check status on form load
        if (cur_frm.doc.status === "Converted") {
            frm.set_read_only();
        } else {
            frm.set_read_only(false);
        }
    },
    status: function(frm) {
        // Check status whenever it changes
        if (cur_frm.doc.status === "Converted") {
            frm.set_read_only();
        } else {
            frm.set_read_only(false);
        }
    }
});





