
$.validator.addMethod("comienzaPor", function(value, element, parametro){    
    if(value.endsWith(parametro)){
        return true;
    }
    return false;
})

$("#formulario_contacto").validate({
    nombre_cont:{
        required:true,
        minlength:5,
        maxlength:20
    },
    email_cont:{
        required:true,
        email:true
    },
    telefono_cont:{
        required:true,
        number:true,
        min:9,
        max:11
    },
    msg_cont:{
        required:true,
        minlength:10,
        maxlength:200
    }

    })

$("#guardar_cont").click(function(){
    let nombre_cont=$("#nombre_cont").val()
    let email_cont=$("#email_cont").val()
    let telefono_cont=$("telefono_cont").val()
    let msg_cont=$("msg_cont").val()

})
