

$("#mensajeError1").hide();


function IsEmail(email) {
    var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (!regex.test(email)) {
        return false;
    } else {
        return true;
    }
}


$("#mensajeError").hide();
$("#mensajeErrorPass").hide();
$("#loginBTN").click(function() {
    var correo = $("#correo").val();
    if (IsEmail(correo) && correo != "") {
        if ($("#pass").val() != "") {
            $("#mensajeError").hide();
            $(location).prop('href', 'http://127.0.0.1:8000/Platos/')
        } else {
            $("#mensajeError").show();
        }
    } else {
        $("#mensajeError").show();
    }
});



$("#crearusuarioN").click(function() {
    var correo = $("#newcorreo").val();

    if (IsEmail(correo) && correo != "") {
        $("mensajeError1").hide();
        if (($("#clave1").val() != "")) {
            if (($("#clave2").val()) == ($("#clave1").val())) {
                $("#mensajeError1").hide();
                $("#mensajeErrorPass").hide();
                alert("Nuevo usuario creado");
                $(location).prop('href', 'http://127.0.0.1:8000/Registrar/')
            } else {
                $("#mensajeErrorPass").show();
            }
        }
    } else {
        $("mensajeError1").show();
    }
})


$("#mensajeErrorMail").hide()
$("#recuperar").click(function() {
    if (IsEmail($("#recupEmail").val())) {
        $("#mensajeErrorMail").hide();
    } else {
        $("#mensajeErrorMail").show();
    }
})
