document.getElementById("registroForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario
    // ... (código de validación, tal como lo tienes en el ejemplo original) ...
  });
  
  // Funciones de validación en tiempo real con el evento "oninput"
  document.getElementById("num_identificacion").addEventListener("input", function() {
    const numIdentificacion = this.value;
    const tipoIdentificacion = document.getElementById("tipo_identificacion").value;
    const cedulaRegex = /^[0-9]{10}$/;
    const pasaporteRegex = /^[A-Z]{1}[0-9]{6}$/;
    let errorMessage = "";
  
    if (tipoIdentificacion === "Cédula") {
      if (!cedulaRegex.test(numIdentificacion)) {
        errorMessage = "El número de identificación no cumple con el formato requerido.";
      }
    } else if (tipoIdentificacion === "Pasaporte") {
      if (!pasaporteRegex.test(numIdentificacion)) {
        errorMessage = "El número de pasaporte no cumple con el formato requerido.";
      }
    }
  
    document.getElementById("errorNumIdentificacion").textContent = errorMessage;
  });
  
  document.getElementById("nombres").addEventListener("input", function() {
    const nombres = this.value;
    const nombresRegex = /^[A-Za-z\s]+$/;
    const errorMessage = !nombresRegex.test(nombres) ? "Los nombres no deben contener caracteres especiales." : "";
    document.getElementById("errorNombres").textContent = errorMessage;
  });
  
  document.getElementById("apellido_paterno").addEventListener("input", function() {
    const apellidoPaterno = this.value;
    const nombresRegex = /^[A-Za-z\s]+$/;
    const errorMessage = !nombresRegex.test(apellidoPaterno) ? "El apellido paterno no debe contener caracteres especiales." : "";
    document.getElementById("errorApellidoPaterno").textContent = errorMessage;
  });
  
  document.getElementById("apellido_materno").addEventListener("input", function() {
    const apellidoMaterno = this.value;
    const nombresRegex = /^[A-Za-z\s]+$/;
    const errorMessage = !nombresRegex.test(apellidoMaterno) ? "El apellido materno no debe contener caracteres especiales." : "";
    document.getElementById("errorApellidoMaterno").textContent = errorMessage;
  });
  
  document.getElementById("email").addEventListener("input", function() {
    const email = this.value;
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const errorMessage = !emailRegex.test(email) ? "El email no cumple con el formato requerido." : "";
    document.getElementById("errorEmail").textContent = errorMessage;
  });

  
  document.getElementById("confirmar_contrasena").addEventListener("input", function() {
    const confirmarContrasena = this.value;
    const contrasena = document.getElementById("contrasena").value;
    const errorMessage = contrasena !== confirmarContrasena ? "La confirmación de contraseña no coincide." : "";
    document.getElementById("errorConfirmarContrasena").textContent = errorMessage;
  });
  