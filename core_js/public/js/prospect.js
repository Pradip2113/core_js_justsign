// frappe.ui.form.on('Prospect', {
// refresh(frm) {
//         if(cur_frm.doc.__islocal==1 && cur_frm.doc.custom_make_read_only==1){
//                 cur_frm.set_value("custom_make_read_only",0)
//             }
//         if(frm.doc.custom_make_read_only){
//                 setTimeout(()=>{
//                 frm.remove_custom_button("Customer","Create");
//                 frm.remove_custom_button("Opportunity","Create");
//                 frm.remove_custom_button("Call");
//                 frm.remove_custom_button("Next Follow-up");
//                 frm.disable_form();
//         },100)
//         }},
//     set_status_: function(frm){
    
//         if(cur_frm.doc.custom_status=="Converted")
//         {
//                 frm.remove_custom_button("Customer","Create");
//                 frm.remove_custom_button("Opportunity","Create");
//                 frm.remove_custom_button("Call");
//                 frm.remove_custom_button("Next Follow-up");
//         }
	
// },


// })
frappe.ui.form.on('Prospect', {
    after_save:async function(frm){
        if(frm.doc.leads){
            await frappe.db.set_value("Prospect",frm.doc.name,"mobile_no",(frm.doc.leads)[0].mobile_no)
            frm.doc.mobile_no = (frm.doc.leads)[0].mobile_no
            await frm.refresh_field("mobile_no")
            console.log("hello" + frm.doc.mobile_no)
        }
       await frm.save()
       frm.reload_doc()
    }
})