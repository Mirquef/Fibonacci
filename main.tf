# Configurar el proveedor
provider "null" {}

# Usa el provisioner local-exec para ejecutar fibonacci.py
resource "null_resource" "fibonacci_execution" {
  provisioner "local-exec" {
    # Comando para ejecutar el archivo Python y capturar su salida
    command = "python3 fibonacci.py"
  }
}
