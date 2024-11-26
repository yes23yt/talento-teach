function validarFormulario(){
    let nombre = document.getElementById("nombre").value; // Obtiene el valor del campo con id="nombre".
    let email = document.getElementById("email").value;   // Obtiene el valor del campo con id="email".
    let imagen = document.getElementById("imagen").value; // Obtiene el valor del campo con id="imagen".
    // Comprueba si alguno de los campos está vacío.
    if(nombre == "" || email == "" || imagen == ""){
        alert("Todos los campos son obligatorios..."); // Muestra un mensaje de alerta.
        return false; // Evita que el formulario se envíe.
    }
    return true; // Si todos los campos están completos, permite el envío del formulario.
}
 
function mostrarImagen(event){
    let imagen = document.getElementById('ver-imagen'); // Obtiene el elemento de imagen (img) donde se mostrará la vista previa.
    // Asigna la URL del archivo seleccionado al atributo `src` de la imagen.
    imagen.src = URL.createObjectURL(event.target.files[0]);
}