---
---
(function(){
    var form_register = $("#form_register");
	
    form_register.submit(function(event){
        // Stop form from submitting normally
        event.preventDefault();
		
        var txt_nama = document.getElementById("txt_nama")
        var rb_jenis_kelamin = document.getElementsByName("rb_jenis_kelamin")[0]
        var txt_email = document.getElementById("txt_email")
        var txt_hp = document.getElementById("txt_hp")
        var txt_institusi = document.getElementById("txt_institusi")
        var txt_profesi = document.getElementById("txt_profesi")
        var txt_minat = document.getElementById("txt_minat")

        console.log(txt_nama.value)
        console.log(rb_jenis_kelamin.value)
        console.log(txt_email.value)
        console.log(txt_hp.value)
        console.log(txt_institusi.value)
        console.log(txt_profesi.value)
        console.log(txt_minat.value)

        $.ajax({
            type: "POST",
            dataType: "json",
            url: "{{site.webserver}}/register",
            data: {
                "txt_nama":txt_nama.value,
                "rb_jenis_kelamin":rb_jenis_kelamin.value,
                "txt_email":txt_email.value,
                "txt_hp":txt_hp.value,
                "txt_institusi":txt_institusi.value,
                "txt_profesi":txt_profesi.value,
                "txt_minat":txt_minat.value
            },
            success: function(response){
                window.location.assign("{{site.url}}/register_complete")
            }
        })
    })
})();