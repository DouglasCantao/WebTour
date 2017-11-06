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

	$('#seleciona_onibus').bind("click",function(e){
        e.preventDefault;
        var placa = $('#seleciona_onibus').text();
        console.log(placa);
        $('#inputPlaca').val(placa);
    });


});