$(document).ready(function() {

	var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});


	$('.remove_onibus').click(function(e){
    	$.post('remove_onibus', {'id_onibus': $(this).attr('id')}, function(data, status){
        	alert("Data: " + data + "\nStatus: " + status);
    	});
        
        // Remove a linha da tabela correspondente ao ônibus excluído.
        $(this).parent().remove();
	});


	$('.remove_passageiro').click(function(e){
    	$.post('remove_passageiro', {'id_passageiro': $(this).attr('id')}, function(data, status){
        	alert("Data: " + data + "\nStatus: " + status);
    	});
        
        // Remove a linha da tabela correspondente ao ônibus excluído.
        $(this).parent().remove();
	});

    // ----------------------Tratamento da modal----------------------------
	$('#seleciona_onibus').click(function(e){                                   
        var placa = $(this).text();                                             
                                                                                                                                    
                                                                                
        $('#inputPlaca').val(placa);
        $('#myModal').modal('hide');                                        
    });
    // --------------------- Tela de Cadastro de Viagem----------------------
    $('.remove_viagem').click(function(e){
    	$.post('remove_viagem', {'id_viagem': $(this).attr('id')}, function(data, status){
        	alert("Data: " + data + "\nStatus: " + status);
    	});
        
        // Remove a linha da tabela correspondente ao ônibus excluído.
        $(this).parent().remove();
	});

    $('.remove_motorista').click(function(e){
        $.post('remove_motorista', {'id_motorista': $(this).attr('id')}, function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
        
        // Remove a linha da tabela correspondente ao ônibus excluído.
        $(this).parent().remove();
    });

// -------------------- Tela de Perfil --------------------------------
    $('#editar').click(function(e){
        event.preventDefault();                                                                               

        $(".input-form").prop("disabled", false);                                                    
                                            
    });

    $('#salvar').click(function(e){
                                                                                      

        $(".input-form").prop("disabled", true);                                                
                                            
    });

});