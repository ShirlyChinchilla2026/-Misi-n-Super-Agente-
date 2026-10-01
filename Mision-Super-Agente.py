# ==========================================
# VIDEOJUEGO: MISION SUPER AGENTE
# ==========================================

# ========= CLASE PADRE =========

class Herramienta:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self):
        pass


# ========= CLASES HIJAS =========

class Linterna(Herramienta):
    def __init__(self):
        super().__init__("Linterna")

    def usar(self):
        print("🔦 LINTERNA ACTIVADA")
        print("Pista extra: La respuesta está más cerca de lo que imaginas.")


class Lupa(Herramienta):
    def __init__(self):
        super().__init__("Lupa")

    def usar(self):
        print("🔍 LUPA ACTIVADA")
        print("Observa cuidadosamente las opciones.")


class Radio(Herramienta):
    def __init__(self):
        super().__init__("Radio")

    def usar(self):
        print("📻 RADIO ACTIVADA")
        print("Comandante: Confía en tus habilidades de detective.")


# ========= AGENTE =========

class Agente:
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.herramienta = herramienta
        self.vidas = 3
        self.puntos = 0


# ========= PORTADA =========

def portada():
    print("""
--------------------------------------------------
    MISIÓN: SUPER_AGENTE
--------------------------------------------------
""")

    print("🕵️‍♂️ Bienvenido Agente.")
    print("Una organización secreta necesita tu ayuda.")
    print("Debes resolver 3 misiones para salvar la ciudad.")


# ========= INSTRUCCIONES =========

def instrucciones():

    print("""
-.-.-.-.-.-.-.- INSTRUCCIONES -.-.-.-.-.-.-.-

1. Elige tu herramienta.
2. Resuelve los acertijos.
3. Puedes escribir PISTA.
4. Ganas 10 puntos por respuesta correcta.
5. Pierdes 1 vida por respuesta incorrecta.
6. Si te quedas sin vidas la misión termina.

-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-
""")


# ========= HERRAMIENTAS =========

def seleccionar_herramienta():

    while True:

        print("\nSelecciona tu herramienta")

        print("1. 🔦 Linterna")
        print("2. 🔍 Lupa")
        print("3. 📻 Radio")

        op = input("Opción: ")

        if op == "1":
            return Linterna()

        elif op == "2":
            return Lupa()

        elif op == "3":
            return Radio()

        else:
            print("⚠ Opción inválida")


# ========= ACERTIJOS =========

def acertijo(agente, pregunta, respuesta, pista):

    print("\n" + pregunta)

    opcion = input(
        "Respuesta (o escribe PISTA): "
    )

    if opcion.lower() == "pista":

        agente.herramienta.usar()
        print("💡", pista)

        opcion = input("Tu respuesta: ")

    if opcion.lower() == respuesta.lower():

        print("✅ Correcto")
        agente.puntos += 10

    else:

        print("❌ Incorrecto")
        agente.vidas -= 1

    print("⭐ Puntos:", agente.puntos)
    print("❤️ Vidas:", agente.vidas)

import random

def acertijo(agente, pregunta, respuesta, pista):

    print("\n" + "=" * 60)
    print(pregunta)
    print("=" * 60)

    opcion = input(
        "Respuesta (o escribe PISTA): "
    )

    if opcion.lower() == "pista":

        print("\n🔧 HERRAMIENTA ACTIVADA")
        agente.herramienta.usar()

        print("\n💡 PISTA:")
        print(pista)

        opcion = input(
            "\nIngresa tu respuesta: "
        )

    if opcion.lower() == respuesta.lower():

        print("\n✅ ¡CORRECTO AGENTE!")
        print("⭐ Has ganado 10 puntos.")

        agente.puntos += 10

    else:

        print("\n❌ RESPUESTA INCORRECTA")
        print(f"✅ La respuesta correcta era: {respuesta}")
        print("❤️ Has perdido una vida.")

        agente.vidas -= 1

        mensajes = [
            "No te rindas Agente.",
            "Todo detective aprende de sus errores.",
            "La siguiente misión será más fácil.",
            "Sigue investigando.",
            "Todavía puedes completar tu misión.",
        ]

        print("\n📢", random.choice(mensajes))

    print("\n⭐ Puntos acumulados:", agente.puntos)
    print("❤️ Vidas restantes:", "❤️" * agente.vidas)

    input("\nPresiona ENTER para continuar...")
# ========= NIVEL 1 =========

def nivel_1(agente):

    
    print(" -.-.-.-.-.-.-.- NIVEL 1: ENTRADA SECRETA -.-.-.-.-.-.-.- ")
   

    acertijo(
        agente,
        "¿Qué tiene llaves pero no abre puertas?",
        "piano",
        "Es un instrumento musical."
    )

    if agente.vidas <= 0:
        return

    acertijo(
        agente,
        "¿Cuántos lados tiene un triángulo?",
        "3",
        "Es menos de 4."
    )

    if agente.vidas <= 0:
        print("\n🏁 NIVEL 1 COMPLETADO")
        print("Has superado la Entrada Secreta.")
        input("Presiona ENTER para continuar...")
        
        return

    acertijo(
        agente,
        "¿Qué sube y baja pero permanece en el mismo lugar?",
        "escalera",
        "La encuentras en edificios."
    )
    

# ========= NIVEL 2 =========

def nivel_2(agente):

    print(" -.-.-.-.-.-.-.- NIVEL 2: CRUCE DE CAMINOS -.-.-.-.-.-.-.- ")

    acertijo(
        agente,
        "Si tienes 5 manzanas y te comes 2 ¿cuántas tienes?",
        "5",
        "Las que te comiste siguen siendo tuyas."
    )

    if agente.vidas <= 0:
        return

    acertijo(
        agente,
        "¿Qué mes tiene 28 días?",
        "todos",
        "No es solo febrero."
    )

    if agente.vidas <= 0:
         print("\n🏁 NIVEL 2 COMPLETADO")
         print("Te acercas a resolver el misterio.")
         input("Presiona ENTER para continuar...")
         return

    acertijo(
        agente,
        "¿Qué pesa más: 1kg de algodón o 1kg de hierro?",
        "ninguno",
        "Los dos pesan igual."
    )

# ========= NIVEL 3 =========

def nivel_3(agente):

    print(" -.-.-.-.-.-.-.- NIVEL 3: MISION FINAL -.-.-.-.-.-.-.- ")

    acertijo(
        agente,
        "Soy alto cuando soy joven y bajo cuando soy viejo.",
        "vela",
        "Produce luz."
    )

    if agente.vidas <= 0:
        return

    acertijo(
        agente,
        "Capital de Guatemala:",
        "ciudad de guatemala",
        "Es la ciudad principal del país."
    )

    if agente.vidas <= 0:
         print("\n🏆 ¡FELICIDADES AGENTE!")
         print("Has completado todas las misiones.")
         input("Presiona ENTER para ver tu reporte final...")
         return

    acertijo(
        agente,
        "¿Qué se rompe al decir su nombre?",
        "silencio",
        "Cuando hablas desaparece."
    )

# ========= REPORTE =========

def reporte(agente):

    print(" -.-.-.-.-.-.-.- REPORTE FINAL DE MISION -.-.-.-.-.-.-.- ")

    print("Agente:", agente.nombre)
    print("Puntos:", agente.puntos)
    print("Vidas:", agente.vidas)

    if agente.puntos <= 30:
        rango = "🥉 AGENTE NOVATO"

    elif agente.puntos <= 70:
        rango = "🥈 AGENTE ELITE"

    else:
        rango = "🥇 LEYENDA DEL ESPIONAJE"

    print("\nRANGO OBTENIDO")
    print(rango)

    print("\n🎉 MISION FINALIZADA")


# ========= JUGAR =========

def jugar():

    nombre = input("\nNombre del agente: ")

    herramienta = seleccionar_herramienta()

    agente = Agente(nombre, herramienta)

    print("\nMisión iniciada...")
    print("❤️❤️❤️ Vidas: 3")
    print("⭐ Puntos: 0")

    nivel_1(agente)

    if agente.vidas > 0:
        nivel_2(agente)

    if agente.vidas > 0:
        nivel_3(agente)

    reporte(agente)


# ========= MENU =========

portada()

print("""
 -.-.-.-.-.-.-.- MENU PRINCIPAL -.-.-.-.-.-.-.-
1. ▶ JUGAR
2. 📖 INSTRUCCIONES
3. 🏆 VER RANGOS
4. ❌ SALIR
................................................
""")

opcion = input("Seleccione una opción: ")

if opcion == "1":
        jugar()

elif opcion == "2":
        instrucciones()

elif opcion == "3":

        print("""
🥉 AGENTE NOVATO = 0 a 30 pts

🥈 AGENTE ELITE = 31 a 70 pts

🥇 LEYENDA DEL ESPIONAJE = 71 a 90 pts
""")

elif opcion == "4":

        print("Gracias por jugar.")
      
else:

    print("⚠ Agente, esa opción no existe.")
