import sqlite3
from contextlib import closing
from datetime import datetime
from pathlib import Path
 
from ejercicios import EJERCICIOS
 
# el archivo queda junto a este programa, en la carpeta del proyecto
RUTA_DB = Path(__file__).parent / "progreso.db"
 
 
def _conectar():
    return sqlite3.connect(RUTA_DB)
 
 
def _ahora():
    return datetime.now().isoformat(timespec="seconds")
 
 
def _ids_validos():
    return {e["id"] for lista in EJERCICIOS.values() for e in lista}
 
 
def normalizar_usuario(texto):
    """Limpia el apodo: sin espacios de más, en minúsculas y de máximo 30 caracteres."""
    return " ".join((texto or "").split()).lower()[:30]
 
 
def iniciar():
    """Crea las tablas si todavía no existen (se puede llamar muchas veces sin problema)."""
    with closing(_conectar()) as db, db:
        # un logro = un ejercicio aprobado sin errores por un usuario.
        # La clave (usuario, ejercicio) impide guardar el mismo logro dos veces.
        db.execute(
            "CREATE TABLE IF NOT EXISTS logros ("
            " usuario TEXT NOT NULL,"
            " ejercicio TEXT NOT NULL,"
            " fecha TEXT NOT NULL,"
            " PRIMARY KEY (usuario, ejercicio))"
        )
        # una fila por partida terminada
        db.execute(
            "CREATE TABLE IF NOT EXISTS partidas ("
            " id INTEGER PRIMARY KEY AUTOINCREMENT,"
            " usuario TEXT NOT NULL,"
            " tema TEXT NOT NULL,"
            " fecha TEXT NOT NULL,"
            " completados INTEGER NOT NULL,"
            " limpios INTEGER NOT NULL,"
            " errores INTEGER NOT NULL,"
            " nivel INTEGER NOT NULL)"
        )
 
 
def registrar_logro(usuario, ejercicio_id):
    """Guarda que el usuario aprobó (sin errores) un ejercicio. Si ya lo tenía, no hace nada."""
    if ejercicio_id not in _ids_validos():
        raise ValueError("Ejercicio desconocido: " + str(ejercicio_id))
    # Los ? son parámetros: así lo que escriba el usuario se guarda como dato y nunca como código SQL.
    with closing(_conectar()) as db, db:
        db.execute(
            "INSERT OR IGNORE INTO logros (usuario, ejercicio, fecha) VALUES (?, ?, ?)",
            (usuario, ejercicio_id, _ahora()),
        )
 
 
def guardar_partida(usuario, partida):
    """Guarda el resumen de una partida terminada."""
    with closing(_conectar()) as db, db:
        db.execute(
            "INSERT INTO partidas (usuario, tema, fecha, completados, limpios, errores, nivel)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (usuario, partida["tema"], _ahora(), partida["completados"],
             partida["limpios"], len(partida["errores"]), partida["nivel"]),
        )
 
 
def logros_de(usuario):
    """Conjunto con los ids de los ejercicios aprobados por el usuario."""
    with closing(_conectar()) as db:
        filas = db.execute("SELECT ejercicio FROM logros WHERE usuario = ?", (usuario,)).fetchall()
    return {fila[0] for fila in filas}
 
 
def partidas_jugadas(usuario):
    with closing(_conectar()) as db:
        return db.execute("SELECT COUNT(*) FROM partidas WHERE usuario = ?", (usuario,)).fetchone()[0]
 
 
def mejor_nivel(usuario, tema):
    """Nivel más alto alcanzado en ese tema (0 si nunca lo jugó)."""
    with closing(_conectar()) as db:
        resultado = db.execute(
            "SELECT MAX(nivel) FROM partidas WHERE usuario = ? AND tema = ?", (usuario, tema)
        ).fetchone()[0]
    return resultado or 0
 
 
def progreso_por_tema(usuario):
    """Devuelve {tema: (aprobados, total)} aplicando la regla de progreso."""
    aprobados = logros_de(usuario)
    resumen = {}
    for tema, lista in EJERCICIOS.items():
        ids_del_tema = {e["id"] for e in lista}
        resumen[tema] = (len(ids_del_tema & aprobados), len(ids_del_tema))
    return resumen