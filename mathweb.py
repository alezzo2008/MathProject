import streamlit as st
import base64
from collections import Counter

from ejercicios import EJERCICIOS
import juego
import progreso

def imagen_a_base64(ruta):
    with open(ruta, "rb") as archivo:
        return base64.b64encode(archivo.read()).decode()

fondo = imagen_a_base64("fondo3.png")
caja = imagen_a_base64("textbox.png")
fuente = imagen_a_base64("HigherPixels.ttf")
fuente2 = imagen_a_base64("Pixelazurebonds.otf")

progreso.iniciar()

# 1. Configuración de la página
st.set_page_config(
    page_title="Math II Training",
    page_icon="✏️",
    layout="wide",
)

# 2. Estado
if "tema" not in st.session_state:
    st.session_state.tema = None
if "partida" not in st.session_state:
    st.session_state.partida = None
if "usuario" not in st.session_state:
    st.session_state.usuario = progreso.normalizar_usuario(st.query_params.get("u", ""))

def guardar_apodo():
    st.session_state.usuario = progreso.normalizar_usuario(st.session_state.get("campo_apodo", ""))
    if st.session_state.usuario:
        st.query_params["u"] = st.session_state.usuario
    elif "u" in st.query_params:
        del st.query_params["u"]

def limpiar_respuestas():
    for clave in list(st.session_state.keys()):
        if clave.startswith("resp_"):
            del st.session_state[clave]

def elegir_tema(nombre):
    limpiar_respuestas()
    st.session_state.tema = nombre
    st.session_state.partida = juego.nueva_partida(nombre)
    
def volver_a_inicio():
    limpiar_respuestas()
    st.session_state.tema = None
    st.session_state.partida = None

def comprobar_respuesta(clave):
    juego.comprobar(st.session_state.partida, st.session_state.get(clave))

def seguir():
    partida = st.session_state.partida
    ejercicio_id = partida["actual"]["id"]
    limpios_antes = partida["limpios"]
    juego.continuar(partida)

    usuario = st.session_state.usuario
    if usuario:
        if partida["limpios"] > limpios_antes:
            progreso.registrar_logro(usuario, ejercicio_id)
        if partida["termino"] and not partida.get("guardada"):
            progreso.guardar_partida(usuario, partida)
            partida["guardada"] = True

# 3. Estilo(CSS)

st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'HigherPixels';
        src: url("data:font/ttf;base64,{fuente}") format('truetype');
        font-weight: normal;
        font-style: normal;
    }}

    @font-face {{
        font-family: 'Pixelazurebonds';
        src: url("data:font/ttf;base64,{fuente2}") format('truetype');
        font-weight: normal;
        font-style: normal;
        ascent-override: 75%;
        descent-override: 25%;
        line-gap-override: 0%;
    }}

    .logo, .subtitle {{
        font-family: 'HigherPixels', sans-serif !important;
        word-spacing: 0.3em;
    }}

    .stApp, .stApp h1, .stApp h2, .stApp h3, .stApp h4,
    .etiqueta,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stCaptionContainer"],
    [data-testid="stWidgetLabel"] p,
    [data-testid="stMetric"] *,
    .stApp label, .stApp button, .stApp input {{
        font-family: 'Pixelazurebonds', sans-serif !important;
    }}

    
    /*Fondo de cuaderno*/
    .stApp {{
        background-image: url("data:image/jpeg;base64,{fondo}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        font-family: 'Pixelazurebonds', sans-serif;
        color: #E0562F;
    }}

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    /*Logo*/
    .logo {{
        font-family: 'HigherPixels', cursive;
        font-size: 5rem;
        text-align: center;
        line-height: 1;
        margin-bottom: 1rem;
    }}
    .logo span {{
        background: linear-gradient(transparent 55%, #FFD84D 55%);
        padding: 0 0.3em;
    }}

    .subtitle, .etiqueta, [class*="st-key-tarjeta"] {{
        background: none !important;
        border-style: solid !important;
        border-image-width: 32px;
        border-color: transparent !important;
        border-image-source: url("data:image/png;base64,{caja}") !important;
        border-image-slice: 16 fill !important;
        border-image-width: 32px !important;
        border-image-repeat: stretch !important;
        image-rendering: pixelated;
        border-radius: 0 !important;
        box-shadow: none !important;
        color: #E6951C;
    }}

    .subtitle {{
        text-align: center;
        font-size: 1.1rem;
        margin: 0 auto 2rem auto;
        width: fit-content;
        background-color: rgba(255, 255, 255, 0.92);
        color: #E6951C;
        border: 3px solid #E6951C;
        border-radius: 10px;
        padding: 0.4rem 1rem;
    }}

    .etiqueta {{
        display: inline-block;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.6rem;
        background-color: rgba(255, 255, 255, 0.92);
        color: #05A887;
        border: 3px solid #05A887;
        border-radius: 10px;
        padding: 0.3rem 0.8rem;
    }}

    [class*="st-key-tarjeta"] {{
        background-color: rgba(255, 255, 255, 0.92);
        border: 3px solid #05A887;
        border-radius: 10px;
        padding: 1.5rem;
        overflow-wrap: anywhere;
    }}
    [class*="st-key-tarjeta"] * {{
        color: #05A887;
    }}

    /*Botones de tema*/
    div.stButton > button {{
        width: 100%;
        border: 2px solid #1B2A4A;
        background-color: #DCB0F5;
        color: #1B2A4A;
        font-family: 'Pixelazurebonds', sans-serif;
        font-weight: 600;
    }}

    div.stButton > button:hover {{
        background-color: #FFD84D;
        border-color: #1B2A4A;
        color: #1B2A4A;
    }}

    [data-testid="InputInstructions"] {{
        display: none !important;
    }}

    /* Logros, y más adelante Configuración, etc. */
    [class*="st-key-btn_icono"] button {{
        padding: 0.3rem 0;
        min-height: 2.6rem;
        font-size: 1.3rem;
    }}
 
    /* Ventana de Logros */
    div[data-testid="stDialog"] div[role="dialog"] {{
        background-color: #0B0615;
        border: 3px solid #05A887;
        border-radius: 10px;
        max-height: 80vh;
        overflow-y: auto;      /* solo se desplaza la ventana */
    }}
    div[data-testid="stDialog"] div[role="dialog"] * {{
        font-family: 'Pixelazurebonds', sans-serif !important;
        color: #05A887;
    }}
    div[data-testid="stDialog"] h2 {{
        font-family: 'HigherPixels', sans-serif !important;
    }}
 
    /* Mientras la ventana está abierta, la página de atrás no se desplaza */
    body:has(div[data-testid="stDialog"]) [data-testid="stMain"],
    body:has(div[data-testid="stDialog"]) [data-testid="stAppViewContainer"] {{
        overflow: hidden !important;
    }}

    </style>
    """,


    unsafe_allow_html=True

)

# 4. Datos
TEMAS = {
    "Límites de funciones de dos variables": {
        "desc": "Calcular límites en un punto, probar que no existen con trayectorias y usar polares.",
        "listo": False
    },
    
    "Incremento diferencial total": {
        "desc": "Cambio real frente a aproximación lineal con derivadas parciales.",
        "listo": False
    },
    "Regla de la cadena": {
        "desc": "Derivación de funciones compuestas de varias variables.",
        "listo": False
    },
    "Plano tangente y recta normal": {
        "desc": "Ecuación del plano tangente y la recta normal a una superficie.",
        "listo": False
    },
    "Derivadas direccionales y gradiente": {
        "desc": "Razón de cambio en una dirección y dirección de máximo crecimiento.",
        "listo": False
    },
    "Puntos críticos y criterios de la segunda derivada": {
        "desc": "Hallar puntos críticos y clasificarlos con el determinante Δ.",
        "listo": False
    },
    "Multiplicadores de Lagrange": {
        "desc": "Máximos y mínimos sujetos a una restricción.",
        "listo": False
    },
    "Cambio de variable: polares y Jacobiano": {
        "desc": "Pasar a polares o a nuevas variables (u, v) y ajustar el área con el Jacobiano.",
        "listo": False
    },
    "Masa y centro de masa de láminas": {
        "desc": "Masa, momentos estáticos y centroide de una lámina con densidad variable.",
        "listo": False
    }
}

# 5. Ventana de Logros
@st.dialog("Logros", width="large")
def ventana_logros():
    st.caption("Contenido de prueba")
    for i in range(1, 31):
        st.markdown(f"Logro de prueba número {i}")

# 6. Pantalla de inicio
def pantalla_inicio():
    st.markdown('<div class="logo"><span>Calc-Up</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">¡Bienvenido! Selecciona un tema para comenzar a practicar.</div>', unsafe_allow_html=True)

    izq, centro, der = st.columns([1, 2, 1], gap="large")
    with izq:
        st.markdown('<div class="etiqueta">Tu apodo</div>', unsafe_allow_html=True)
        with st.container(border=True, key="tarjeta_apodo"):
            st.text_input("Escribe un apodo y pulsa Enter para guardar tu progreso",
                          value=st.session_state.usuario, key="campo_apodo",
                          on_change=guardar_apodo, placeholder="Tu apodo")
            usuario = st.session_state.usuario
            if usuario:
                resumen = progreso.progreso_por_tema(usuario)
                aprobados = sum(a for a, t in resumen.values())
                total = sum(t for a, t in resumen.values())
                st.progress(aprobados / total, text=f"{aprobados} de {total} ejercicios dominados")
                st.caption(f"Partidas jugadas: {progreso.partidas_jugadas(usuario)}. "
                           "Un ejercicio cuenta cuando lo resuelves sin ningún error.")
            else:
                st.caption("Sin apodo puedes jugar, pero tu progreso no se guarda.")

        st.markdown('<div class="etiqueta">Tu progreso:</div>', unsafe_allow_html=True)
        with st.container(border=True, key="tarjeta_progreso"):
            st.markdown("1. Elige un tema.")
            st.markdown("2. Empiezas en el nivel 1.")
            st.markdown("3. Al acumular aciertos, los ejercicios sube de nivel.")
            st.markdown("4. Si fallas, recibes una pista sobre tu error.")

        c1, c2, c3, c4 = st.columns(4, gap="small")
        with c1:
            if st.button("🏆", key="btn_icono_logros", help="Logros"):
                ventana_logros()
            
    with centro:
        st.markdown('<div class="etiqueta">¿Qué quieres practicar hoy?</div>', unsafe_allow_html=True)

        usuario = st.session_state.usuario
        resumen_usuario = progreso.progreso_por_tema(usuario) if usuario else {}

        for i, (nombre, datos) in enumerate(TEMAS.items()):
            with st.container(border=True, key=f"tarjeta_tema_{i}"):
                st.subheader(nombre)
                st.caption(datos["desc"])
                if nombre in resumen_usuario:
                    aprobados_tema, total_tema = resumen_usuario[nombre]
                    texto = f"{aprobados_tema} de {total_tema} ejercicios dominados"
                    mejor = progreso.mejor_nivel(usuario, nombre)
                    if mejor:
                        texto += f"  ·  mejor nivel: {mejor}"
                    st.progress(aprobados_tema / total_tema, text=texto)
                if nombre in EJERCICIOS:
                    st.button(
                        "Practicar",
                        key=nombre,
                        on_click=elegir_tema,
                        args=(nombre,)
                    )
                else:
                    st.button(
                        "Próximamente",
                        key=nombre,
                        disabled=True
                    )
                

    with der:
        st.markdown('<div class="etiqueta">Así se ve un problema</div>', unsafe_allow_html=True)
        with st.container(border=True, key="tarjeta_ejemplo"):
            st.markdown(r"**Dada** $f(x,y)=x^2y+3y^2$, **calcula** $\nabla f(2,1)$")
            st.markdown(r"1. Deriva: $f_x=2xy$ y $f_y=x^2+6y$")
            st.markdown(r"2. Evalúa en $(2,1)$: $\nabla f(2,1)=(4,10)$")
            st.caption("Primero la expresión, luego el valor en el punto. Respondes cada paso.")

# 7. Pantalla de tema
def pantalla_tema(nombre):
    partida = st.session_state.partida
    with st.container(border=True, key="tarjeta_partida"):
        st.button("Salir al inicio", on_click=volver_a_inicio)
        if partida["termino"]:
            pantalla_resultados(partida)
        else:
            pantalla_ejercicio(partida)

def pantalla_ejercicio(partida):
    ejercicio = partida["actual"]
    paso = ejercicio["pasos"][partida["paso"]]

    st.caption(f"{partida['tema']}  ·  Nivel {partida['nivel']}  ·  Ejercicio {partida['completados'] + 1}")
    if partida["avisos"]:
        st.success(partida["avisos"])

    st.markdown(ejercicio["enunciado"])

    for hecho in partida["hechos"]:
        st.markdown(hecho)

    st.markdown(paso["pregunta"])

    # la clave cambia en cada ejercicio y paso, así cada pregunta empieza sin nada marcado
    clave = f"resp_{ejercicio['id']}_{partida['paso']}"

    if sorted(o["texto"] for o in partida["opciones"]) != sorted(o["texto"] for o in paso["opciones"]):
        juego.preparar_paso(partida)
        st.session_state.pop(clave, None)
        
    textos = [o["texto"] for o in partida["opciones"]]
    st.radio("Elige una opción", textos, index=None, key=clave,
             label_visibility="collapsed", disabled=partida["paso_ok"])

    if partida["paso_ok"]:
        if partida["paso_fallado"]:
            correcta = next(o["texto"] for o in paso["opciones"] if o["ok"])
            st.warning("Se acabaron los intentos. La respuesta correcta era " + correcta + ". " + paso["explicacion"])
        else:
            st.success("¡Correcto! " + paso["explicacion"])
        st.button("Continuar", on_click=seguir)
    else:
        st.button("Comprobar", on_click=comprobar_respuesta, args=(clave,))
        st.caption(f"Intentos restantes en este paso: {juego.INTENTOS_POR_PASO - partida['intentos']}")
        if partida["pista"]:
            st.error(partida["pista"])

def pantalla_resultados(partida):
    st.subheader("Resultados de la partida")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Ejercicios", partida["completados"])
    c2.metric("Sin errores", f"{partida['limpios']} de {partida['completados']}")
    c3.metric("Errores cometidos", len(partida["errores"]))
    c4.metric("Nivel alcanzado", f"{partida['nivel']} de {partida['nivel_max']}")
    st.caption(f"'Sin errores' cuenta los ejercicios que resolviste sin fallar ningún paso. "
               f"Para subir de nivel hacen falta {juego.ACIERTOS_PARA_SUBIR} seguidos.")

    if partida["errores"]:
        st.markdown("**Errores más frecuentes:**")
        for pista, veces in Counter(partida["errores"]).most_common(3):
            st.markdown(f"- ({veces}x) {pista}")
    else:
        st.success("¡Partida perfecta! No cometiste ningún error.")

    if partida["repaso"]:
        st.markdown("**Para repasar** (pasos en los que se acabaron los intentos):")
        for r in partida["repaso"]:
            with st.container(border=True):
                st.markdown(r["enunciado"])
                st.markdown(r["pregunta"])
                st.markdown("Respuesta correcta: " + r["correcta"] + ". " + r["explicacion"])

    if st.session_state.usuario:
        st.caption(f"Progreso guardado para «{st.session_state.usuario}».")
    else:
        st.caption("Escribe un apodo en la pantalla de inicio para que tu progreso se guarde.")

    st.button("Jugar otra vez", on_click=elegir_tema, args=(partida["tema"],))

# 8. Decidir que pantalla mostrar
if st.session_state.tema is None:
    pantalla_inicio()
else:
    pantalla_tema(st.session_state.tema)