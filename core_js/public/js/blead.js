frappe.ui.form.on('Lead', {
    refresh(frm) {
        if (cur_frm.doc.__islocal == 1 && cur_frm.doc.custom_make_read_only == 1) {
            cur_frm.set_value("custom_make_read_only", 0);
        }

        if (cur_frm.doc.custom_make_read_only) {
            setTimeout(() => {
                frm.remove_custom_button("Customer", "Create");
                frm.remove_custom_button("Opportunity", "Create");
                frm.remove_custom_button("Quotation", "Create");
                frm.remove_custom_button("Call");
                frm.remove_custom_button("Next Follow-up");
            }, 100);
            frm.disable_form();
        } else {
            frm.enable_form();
        }
    },

    status: function(frm) {
        if (cur_frm.doc.status == "Converted") {
            frm.remove_custom_button("Customer", "Create");
            frm.remove_custom_button("Opportunity", "Create");
            frm.remove_custom_button("Quotation", "Create");
            frm.remove_custom_button("Call");
            frm.remove_custom_button("Next Follow-up");
            frm.set_read_only();
        } else {
            frm.set_read_only(false);
        }
    }
});
