frappe.ui.form.on('Customer', {
    after_save:async function(frm) {
        // frappe.throw("throw")
        await frappe.call({
            method:"core_js.core_js.utils.customer.add_cust_to_contact",
            args: { doc: frm.doc },
        })
    }
    
});

