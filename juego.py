import random
from ejercicios import EJERCICIOS

ACIERTOS_PARA_SUBIR = 2
EJERCICIOS_POR_PARTIDA = 10
INTENTOS_POR_PASO = 2

def nueva_partida(tema):
    """Crea una partida nueva: empieza en nivel 1 con el primer ejercicio."""
    partida = {
        "tema": tema,
        "nivel": 1,
        "nivel_max": max(e["nivel"] for e in EJERCICIOS[tema]),
        "vistos": [],
        "actual": None,
        "paso": 0,
        "opciones": [],
        "intentos": 0,
        "errores_ej": 0,
        "racha": 0,
        "completados": 0,
        "limpios": 0,
        "errores": [],
        "pista": None,
        "paso_ok": False,
        "paso_fallado": False,
        "hechos": [],
        "repaso": [],
        "avisos": None,
        "termino": False,
    }

    pasar_al_siguiente(partida)
    return partida

def elegir_siguiente(partida):
    """Elige un ejercicio que no se haya visto, lo más cercano al nivel actual."""
    pendientes = [e for e in EJERCICIOS[partida["tema"]] if e["id"] not in partida["vistos"]]
    if not pendientes:
        return None
    nivel = partida["nivel"]

    cercano = min(pendientes, key=lambda e: (abs(e["nivel"] - nivel), -e["nivel"]))
    del_mismo_nivel = [e for e in pendientes if e["nivel"] == cercano["nivel"]]
    return random.choice(del_mismo_nivel)

def preparar_paso(partida):
    """Deja listo el paso actual: opciones en orden aleatorio y sin errores."""
    paso = partida["actual"]["pasos"][partida["paso"]]
    partida["opciones"] = random.sample(paso["opciones"], len(paso["opciones"]))
    partida["intentos"] = 0
    partida["paso_ok"] = False
    partida["paso_fallado"] = False
    partida["pista"] = None

def pasar_al_siguiente(partida):
    """Prepara el siguiente ejercicio, o termina la partida si ya no hay."""
    siguiente = None
    if partida["completados"] < EJERCICIOS_POR_PARTIDA:
        siguiente = elegir_siguiente(partida)
    if siguiente is None:
        partida["actual"] = None
        partida["termino"] = True
        return
    
    partida["actual"] = siguiente
    partida["vistos"].append(siguiente["id"])
    partida["paso"] = 0
    partida["errores_ej"] = 0
    partida["hechos"] = []
    preparar_paso(partida)

def comprobar(partida, texto_elegido):
    """Revisa la opción elegida en el paso actual."""
    if partida["paso_ok"]:
        return
    if texto_elegido is None:
        partida["pista"] = "Elige una opción antes de comprobar."
        return
 
    ejercicio = partida["actual"]
    paso = ejercicio["pasos"][partida["paso"]]
    opcion = next(o for o in paso["opciones"] if o["texto"] == texto_elegido)

    if opcion is None:
        preparar_paso(partida)
        partida["pista"] = "Se actualizaron las opciones de este paso. Elige una opción de nuevo."
        return
 
    if opcion["ok"]:
        partida["paso_ok"] = True
        partida["pista"] = None
        return
 
    # respuesta incorrecta
    partida["errores_ej"] += 1
    partida["intentos"] += 1
    partida["errores"].append(opcion["pista"])
 
    if partida["intentos"] >= INTENTOS_POR_PASO:
        # se acabaron los intentos: se muestra la respuesta y se guarda para repasar
        partida["paso_ok"] = True
        partida["paso_fallado"] = True
        partida["pista"] = None
        partida["repaso"].append({
            "enunciado": ejercicio["enunciado"],
            "pregunta": paso["pregunta"],
            "correcta": next(o["texto"] for o in paso["opciones"] if o["ok"]),
            "explicacion": paso["explicacion"],
            "pista": opcion["pista"],
        })
    else:
        partida["pista"] = opcion["pista"]

def continuar(partida):
    """Avanza al siguiente paso; si era el último, cierra el ejercicio y aplica las reglas de nivel."""

    if not partida["paso_ok"]:
        return

    partida["avisos"] = None
    partida["pista"] = None

    paso_actual = partida["actual"]["pasos"][partida["paso"]]
    marca = "❌" if partida["paso_fallado"] else "✅"
    partida["hechos"].append(f"{marca} Paso {partida['paso'] + 1}: {paso_actual['explicacion']}")

    if partida["paso"] + 1 < len(partida["actual"]["pasos"]):
        partida["paso"] += 1
        preparar_paso(partida)
        return
    
    #termino el ejercicio
    partida["completados"] += 1
    if partida["errores_ej"] == 0:
        partida["limpios"] += 1
        partida["racha"] += 1
        if partida["racha"] >= ACIERTOS_PARA_SUBIR and partida["nivel"] < partida["nivel_max"]:
            partida["nivel"] += 1
            partida["racha"] = 0
            partida["avisos"] = f"¡Subiste al nivel {partida['nivel']}!"
    else:
        partida["racha"] = 0
    pasar_al_siguiente(partida)
        
