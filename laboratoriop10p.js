let esMayorDeEdad = true;
let tieneLicencia = true;
 
let puedeConducir = esMayorDeEdad && tieneLicencia;
let cumpleAlgunaCondicion = esMayorDeEdad || tieneLicencia;
 
 
let mensajeConcatenado = "Bienvenido. " + "¿puedes conducir ?: " + puedeConducir;
 
console.log("¿Puede conducir: ?  (Mayor de edad y tener licencia)", puedeConducir);
console.log("Cumple alguna condicion para conducir? (mayor o licencia", cumpleAlgunaCondicion);
 
