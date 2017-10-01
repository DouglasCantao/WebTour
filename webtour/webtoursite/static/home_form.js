$(document).ready(function() {
    var cidades = ['Belo Horizonte', 'São Paulo', 'Belém', 'Curitiba'];
    
    $('#inputOrigem').autocomplete({
        source: cidades
    });
    
    $('#inputDestino').autocomplete({
        source: cidades
    });
});
