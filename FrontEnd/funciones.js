$(document).ready(function() {
    let arr = [];  // Inicializa el array vacío
  
    // Maneja los clics en los botones de números y operadores
    $('.numeros, .operadores').on('click', function() {
        let valor = $(this).val();  // Obtiene el valor del botón presionado

        // Convierte los números a tipo Number y asegura que solo haya dos números y un operador
        if (arr.length < 3) {
            if (!isNaN(valor)) {
                valor = Number(valor);
            }
            arr.push(valor);
        }

        // Muestra la expresión en el display
        let arrayString = arr.join(' ');
        $("#display").html(`<h1>${arrayString}</h1>`);
    });
  
    // Maneja el botón de reset
    $('.reset').on('click', function() {
        arr = [];  // Resetea el array
        $("#display").html('<h1>0</h1>');
    });
  
    // Maneja la petición AJAX cuando se presiona el botón "igual"
    $('#peticion').on('click', function() {
        // Filtra valores no válidos
        let filteredArr = arr.filter(value => value !== undefined && value !== null && value !== '');

        // Verifica si hay exactamente dos números y un operador
        if (filteredArr.length === 3 && !isNaN(filteredArr[0]) && !isNaN(filteredArr[2]) && ["+", "-", "*", "/", "^", "√"].includes(filteredArr[1])) {
            var jsonString = JSON.stringify({ ListaExpresion: filteredArr });  // Convertir el array a JSON con la estructura correcta
            
            console.log('Enviando JSON:', jsonString);  // Muestra el JSON que se enviará

            $.ajax({
                url: 'http://127.0.0.1:8000/calculadora/',  // URL del servidor Django
                type: 'POST',
                contentType: 'application/json',  // Tipo de contenido que se envía
                data: jsonString,  // Datos que se envían
                dataType: 'json',  // Formato de respuesta esperado
                success: function(response) {
                    console.log('Respuesta del servidor:', response);
                    $("#display").html(`<h1>${response.resultado}</h1>`);  // Muestra el resultado en el display
                },
                error: function(xhr, status, error) {
                    console.error('Error en la solicitud AJAX:', status, error);
                }
            });
        } else {
            console.error('Expresión inválida: debe contener exactamente dos números y un operador.');
        }
    });
});
