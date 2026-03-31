# --- PROGRAMA BASE: ASISTENTE DE MISIÓN ESPACIAL ---

def mostrar_menu():
  print("\n--- 🚀 SISTEMA DE CONTROL LUNAR ---")
  print("1. Verificar niveles de oxígeno")
  print("2. Calcular distancia a la Tierra")
  print("3. Personalizar nombre de la nave")
  print("4. Salir")

def ejecutar_asistente():
  nave = "Apolo 11"
  continuar = True

  while continuar:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
      print("✅ Oxígeno al 98%. Todo normal.")
    elif opcion == "2":
      distancia = 384400
      print(f"📍 La distancia actual es de {distancia}km.")
    elif opcion == "3":
      nuevo_nombre = input("Ingresa el nuevo nombre de tu nave: ")
      nave = nuevo_nombre
      print(f"🚀 Nombre actualizado: {nave}")
    elif opcion == "4":
      print(f"🛰 Cerrando conexión desde la nave{nave}. ¡Adiós!")
      continuar = False
    else:
      print("⚠ Opción no válida. Intenta de nuevo.")

# Iniciar el programa
ejecutar_asistente()
