# ejercicios.py
# Aquí viven SOLO los datos: los ejercicios. No hay lógica de la partida ni de la interfaz.
#
# Cada ejercicio tiene:
#   id         -> nombre único (no se repite nunca)
#   nivel      -> 1, 2 o 3 (dificultad)
#   enunciado  -> lo que se pregunta (se puede usar LaTeX entre $ $)
#   pasos      -> lista de pasos; cada paso es una pregunta de opción múltiple
#
# Cada paso tiene:
#   pregunta, opciones, explicacion (se muestra al acertar)
#
# Las opciones se escriben con dos ayudantes:
#   ok("texto")                 -> la opción correcta (solo una por paso)
#   mal("texto", "pista")       -> una opción incorrecta con SU pista (la que explica ese error)
#
# IMPORTANTE: cada ejercicio hay que resolverlo a mano ANTES de escribirlo.
# La computadora no inventa los pasos ni los errores típicos: los defines tú.

def ok(texto):
    return {"texto": texto, "ok": True}

def mal(texto, pista):
    return {"texto": texto, "ok": False, "pista": pista}

# La clave debe ser EXACTAMENTE igual al nombre del tema en TEMAS (mathweb.py).
EJERCICIOS = {
    "Límites de funciones de dos variables": [
        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "lim_1a",
            "nivel": 1,
            "enunciado": r"Calcula $\displaystyle\lim_{(x,y)\to(1,2)}\frac{x^2+3xy}{x+y}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué pasa al evaluar el denominador en $(1,2)$?",
                    "opciones": [
                        ok(r"Vale $3\neq0$: la función es continua en $(1,2)$ y basta sustituir"),
                        mal(r"Vale $0$: es una indeterminación y hay que factorizar",
                            r"$x+y=1+2=3$, no $0$. No hay indeterminación."),
                        mal(r"Hay que probar con trayectorias porque aparece una fracción",
                            r"Las trayectorias se usan cuando sustituir da $\tfrac00$ y sospechas que el límite no existe. Aquí no hace falta."),
                        mal(r"El límite no existe porque el denominador depende de $x$ y de $y$",
                            r"Un denominador solo da problemas si se anula en el punto. En $(1,2)$ vale $3$."),
                    ],
                    "explicacion": r"El denominador $x+y$ vale $3\neq0$ en $(1,2)$: la función es continua ahí y el límite es el valor de la función.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula el límite.",
                    "opciones": [
                        ok(r"$\tfrac73$"),
                        mal(r"$7$",
                            r"Sustituiste solo en el numerador: $1^2+3\cdot1\cdot2=7$. Falta dividir entre el denominador $3$."),
                        mal(r"$\tfrac37$",
                            r"Dejaste el cociente al revés: es $\tfrac{\text{numerador}}{\text{denominador}}=\tfrac73$."),
                        mal(r"$3$",
                            r"Ese es solo el denominador $x+y$. Falta el numerador: $\tfrac73$."),
                    ],
                    "explicacion": r"$\dfrac{1^2+3(1)(2)}{1+2}=\dfrac73$.",
                },
            ],
        },
        {
            "id": "lim_1b",
            "nivel": 1,
            "enunciado": r"Calcula $\displaystyle\lim_{(x,y)\to(1,1)}\frac{x^2-y^2}{x-y}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué obtienes al sustituir $(1,1)$ directamente?",
                    "opciones": [
                        ok(r"$\tfrac00$: indeterminación, hay que simplificar"),
                        mal(r"$0$: el límite vale $0$",
                            r"El denominador también se anula: queda $\tfrac00$, que no es $0$ sino una indeterminación."),
                        mal(r"$\tfrac20$: el límite no existe",
                            r"El numerador $1^2-1^2$ también vale $0$, así que es $\tfrac00$ y todavía se puede simplificar."),
                        mal(r"$1$: el límite vale $1$",
                            r"Sustituir da $\tfrac00$; no hay un valor que se pueda leer directamente."),
                    ],
                    "explicacion": r"$\tfrac{1-1}{1-1}=\tfrac00$: hay que simplificar antes de evaluar.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cómo queda la expresión al factorizar el numerador (con $x\neq y$)?",
                    "opciones": [
                        ok(r"$x+y$"),
                        mal(r"$x-y$",
                            r"$x^2-y^2=(x-y)(x+y)$: al cancelar $x-y$ queda $x+y$."),
                        mal(r"$(x-y)^2$",
                            r"$x^2-y^2$ es una diferencia de cuadrados, no el cuadrado de una diferencia: $(x-y)(x+y)$."),
                        mal(r"$x^2+y^2$",
                            r"Esa expresión no sale al factorizar. $x^2-y^2=(x-y)(x+y)$."),
                    ],
                    "explicacion": r"$\dfrac{x^2-y^2}{x-y}=\dfrac{(x-y)(x+y)}{x-y}=x+y$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula el límite.",
                    "opciones": [
                        ok(r"$2$"),
                        mal(r"$0$",
                            r"Sigues con el $\tfrac00$ original. Después de simplificar queda $x+y$, que en $(1,1)$ vale $2$."),
                        mal(r"$1$",
                            r"$x+y=1+1=2$, no $1$."),
                        mal(r"No existe",
                            r"Tras simplificar queda $x+y$, que es continua: el límite existe."),
                    ],
                    "explicacion": r"$\lim_{(x,y)\to(1,1)}(x+y)=2$.",
                },
            ],
        },
 
        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "lim_2a",
            "nivel": 2,
            "enunciado": r"Calcula $\displaystyle\lim_{(x,y)\to(0,0)}\frac{\sqrt{x^2+y^2+1}-1}{x^2+y^2}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué obtienes al sustituir $(0,0)$ directamente?",
                    "opciones": [
                        ok(r"$\tfrac00$: indeterminación, conviene multiplicar por el conjugado"),
                        mal(r"$0$: el límite vale $0$",
                            r"El denominador $x^2+y^2$ también se anula en $(0,0)$: es $\tfrac00$."),
                        mal(r"$\tfrac10$: el límite no existe",
                            r"El numerador $\sqrt{0+0+1}-1$ vale $0$, no $1$: es $\tfrac00$."),
                        mal(r"$1$: el límite vale $1$",
                            r"El numerador $\sqrt1-1$ vale $0$ (no $1$), y el denominador también: queda $\tfrac00$."),
                    ],
                    "explicacion": r"Numerador $\sqrt1-1=0$ y denominador $0$: es $\tfrac00$. Como hay una raíz, se multiplica por el conjugado.",
                },
                {
                    "pregunta": r"**Paso 2.** Multiplica arriba y abajo por el conjugado $\sqrt{x^2+y^2+1}+1$ y simplifica: ¿qué queda?",
                    "opciones": [
                        ok(r"$\dfrac{1}{\sqrt{x^2+y^2+1}+1}$"),
                        mal(r"$\dfrac{1}{\sqrt{x^2+y^2+1}-1}$",
                            r"Lo que queda abajo es el conjugado $\sqrt{x^2+y^2+1}+1$, con signo $+$."),
                        mal(r"$\dfrac{x^2+y^2}{\sqrt{x^2+y^2+1}+1}$",
                            r"El numerador $\left(\sqrt{A}-1\right)\left(\sqrt{A}+1\right)=A-1=x^2+y^2$ se cancela con el denominador $x^2+y^2$."),
                        mal(r"$\sqrt{x^2+y^2+1}+1$",
                            r"El factor $\sqrt{x^2+y^2+1}+1$ queda en el denominador, no en el numerador."),
                    ],
                    "explicacion": r"Con $A=x^2+y^2+1$: $\dfrac{\left(\sqrt{A}-1\right)\left(\sqrt{A}+1\right)}{(x^2+y^2)\left(\sqrt{A}+1\right)}=\dfrac{A-1}{(x^2+y^2)\left(\sqrt{A}+1\right)}=\dfrac{1}{\sqrt{A}+1}$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula el límite.",
                    "opciones": [
                        ok(r"$\tfrac12$"),
                        mal(r"$1$",
                            r"En $(0,0)$ el denominador $\sqrt1+1$ vale $2$, no $1$."),
                        mal(r"$0$",
                            r"No es $0$: $\dfrac{1}{\sqrt1+1}=\dfrac12$."),
                        mal(r"$2$",
                            r"Es el inverso: $\dfrac{1}{\sqrt1+1}=\dfrac12$."),
                    ],
                    "explicacion": r"$\dfrac{1}{\sqrt{0+0+1}+1}=\dfrac12$.",
                },
            ],
        },
        {
            "id": "lim_2b",
            "nivel": 2,
            "enunciado": r"Estudia $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2-y^2}{x^2+y^2}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Acércate por el eje $x$ (es decir, $y=0$). ¿Qué valor obtienes?",
                    "opciones": [
                        ok(r"$1$"),
                        mal(r"$0$",
                            r"Con $y=0$: $\tfrac{x^2-0}{x^2+0}=\tfrac{x^2}{x^2}=1$."),
                        mal(r"$-1$",
                            r"El valor $-1$ aparece por el eje $y$ ($x=0$). Por el eje $x$ el numerador es $+x^2$."),
                        mal(r"No está definido",
                            r"Para $x\neq0$ la fracción vale $\tfrac{x^2}{x^2}=1$. Lo que importa es el valor al acercarse, no el punto $(0,0)$ mismo."),
                    ],
                    "explicacion": r"Con $y=0$: $\tfrac{x^2}{x^2}=1$ para todo $x\neq0$, así que por ese camino el límite es $1$.",
                },
                {
                    "pregunta": r"**Paso 2.** Ahora acércate por el eje $y$ ($x=0$). ¿Qué valor obtienes?",
                    "opciones": [
                        ok(r"$-1$"),
                        mal(r"$1$",
                            r"Con $x=0$: $\tfrac{-y^2}{y^2}=-1$. El signo del numerador cambia."),
                        mal(r"$0$",
                            r"Con $x=0$ la fracción es $\tfrac{-y^2}{y^2}=-1$, no $0$."),
                        mal(r"Por ese camino no existe",
                            r"Por ese camino sí existe y vale $-1$. Que el límite global no exista se decide al comparar caminos."),
                    ],
                    "explicacion": r"Con $x=0$: $\tfrac{-y^2}{y^2}=-1$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué concluyes?",
                    "opciones": [
                        ok(r"El límite no existe, porque dos caminos dan valores distintos ($1$ y $-1$)"),
                        mal(r"El límite vale $1$",
                            r"Un solo camino no demuestra nada. Si otro camino da un valor distinto, el límite no existe."),
                        mal(r"El límite vale $0$, el promedio de $1$ y $-1$",
                            r"El límite no se obtiene promediando caminos: si dos caminos dan valores distintos, el límite no existe."),
                        mal(r"El límite vale $-1$",
                            r"Te quedaste con el último camino. Como los dos caminos dan valores distintos, el límite no existe."),
                    ],
                    "explicacion": r"Si por dos caminos el valor es distinto, el límite no existe.",
                },
            ],
        },
 
        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "lim_3a",
            "nivel": 3,
            "enunciado": r"Estudia $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^4+y^2}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Acércate por rectas $y=mx$. ¿Qué valor obtienes?",
                    "opciones": [
                        ok(r"$0$, para cualquier $m$"),
                        mal(r"$\dfrac{m}{1+m^2}$",
                            r"Ese es el resultado para $\dfrac{xy}{x^2+y^2}$. Aquí, con $y=mx$, queda $\dfrac{mx}{x^2+m^2}$, que tiende a $0$."),
                        mal(r"$\tfrac12$",
                            r"Con $y=mx$ queda $\dfrac{mx}{x^2+m^2}\to0$. El valor $\tfrac12$ aparece con otro camino."),
                        mal(r"Depende de $m$",
                            r"Con $y=mx$: $\dfrac{x^2\cdot mx}{x^4+m^2x^2}=\dfrac{mx}{x^2+m^2}\to0$ sin importar $m$."),
                    ],
                    "explicacion": r"$\dfrac{x^2\cdot mx}{x^4+m^2x^2}=\dfrac{mx}{x^2+m^2}\to0$ cuando $x\to0$ (con $m=0$ vale $0$ directamente).",
                },
                {
                    "pregunta": r"**Paso 2.** Prueba ahora con la parábola $y=x^2$. ¿Qué valor obtienes?",
                    "opciones": [
                        ok(r"$\tfrac12$"),
                        mal(r"$0$",
                            r"Con $y=x^2$: $\dfrac{x^2\cdot x^2}{x^4+x^4}=\dfrac{x^4}{2x^4}=\dfrac12$."),
                        mal(r"$1$",
                            r"En el denominador hay dos términos iguales: $x^4+x^4=2x^4$, así que da $\tfrac12$."),
                        mal(r"$\infty$",
                            r"No diverge: numerador y denominador son del mismo orden ($x^4$), y el cociente es $\tfrac12$."),
                    ],
                    "explicacion": r"$\dfrac{x^2\cdot x^2}{x^4+(x^2)^2}=\dfrac{x^4}{2x^4}=\dfrac12$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué concluyes?",
                    "opciones": [
                        ok(r"El límite no existe: las rectas dan $0$ pero la parábola da $\tfrac12$"),
                        mal(r"El límite vale $0$, porque por todas las rectas da $0$",
                            r"Las rectas no son todos los caminos. Basta una curva distinta (la parábola) con otro valor para que no exista."),
                        mal(r"El límite vale $\tfrac12$",
                            r"Un camino no determina el límite: las rectas dan $0$ y la parábola da $\tfrac12$; como son distintos, no existe."),
                        mal(r"El límite vale $\tfrac14$, el promedio de $0$ y $\tfrac12$",
                            r"El límite no se obtiene promediando caminos: valores distintos implican que no existe."),
                    ],
                    "explicacion": r"Dos caminos con valores distintos ($0$ y $\tfrac12$) implican que el límite no existe, aunque todas las rectas den $0$.",
                },
            ],
        },
        {
            "id": "lim_3b",
            "nivel": 3,
            "enunciado": r"Calcula $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2y}{x^2+y^2}$ usando polares.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Sustituye $x=r\cos\theta$, $y=r\sin\theta$ y simplifica: ¿qué queda?",
                    "opciones": [
                        ok(r"$r\cos^2\theta\sin\theta$"),
                        mal(r"$r^3\cos^2\theta\sin\theta$",
                            r"Falta dividir entre $x^2+y^2=r^2$: $\dfrac{r^3\cos^2\theta\sin\theta}{r^2}$."),
                        mal(r"$r\cos\theta\sin^2\theta$",
                            r"Los exponentes están al revés: $x^2$ lleva $\cos^2\theta$ y $y$ lleva $\sin\theta$."),
                        mal(r"$\cos^2\theta\sin\theta$",
                            r"Del numerador $r^3$ se cancelan dos $r$ con el $r^2$ del denominador, pero queda uno: $r\cos^2\theta\sin\theta$."),
                    ],
                    "explicacion": r"$\dfrac{(r\cos\theta)^2(r\sin\theta)}{r^2}=r\cos^2\theta\sin\theta$.",
                },
                {
                    "pregunta": r"**Paso 2.** Cuando $(x,y)\to(0,0)$ se tiene $r\to0$ (sin importar $\theta$). ¿Qué concluyes de $r\cos^2\theta\sin\theta$?",
                    "opciones": [
                        ok(r"Como $|\cos^2\theta\sin\theta|\leq1$, la expresión está acotada por $r$ y tiende a $0$"),
                        mal(r"Depende de $\theta$, así que el límite no existe",
                            r"Depende de $\theta$, pero está multiplicada por $r\to0$ y $\cos^2\theta\sin\theta$ está acotado: el producto tiende a $0$ para cualquier ángulo."),
                        mal(r"Como $\cos^2\theta\sin\theta\to1$, el límite es $1$",
                            r"$\theta$ no tiende a ningún valor: es un ángulo cualquiera. Lo que tiende a $0$ es $r$."),
                        mal(r"El factor $r$ desaparece y queda $\cos^2\theta\sin\theta$",
                            r"$r$ no desaparece: tiende a $0$ y arrastra a todo el producto, porque lo demás está acotado."),
                    ],
                    "explicacion": r"$\left|r\cos^2\theta\sin\theta\right|\leq r\to0$, y esto vale para todo $\theta$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula el límite.",
                    "opciones": [
                        ok(r"$0$"),
                        mal(r"$1$",
                            r"$|r\cos^2\theta\sin\theta|\leq r$, que tiende a $0$, no a $1$."),
                        mal(r"$\tfrac12$",
                            r"Ese valor no aparece: la expresión está acotada por $r$, que tiende a $0$."),
                        mal(r"No existe",
                            r"Por acotación se probó que tiende a $0$ para todo $\theta$: el límite existe."),
                    ],
                    "explicacion": r"Por acotación, $\lim_{(x,y)\to(0,0)}\dfrac{x^2y}{x^2+y^2}=0$.",
                },
            ],
        },
    ],

    "Derivadas direccionales y gradiente": [
        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "grad_1a",
            "nivel": 1,
            "enunciado": r"Dada $f(x,y)=x^2y+3y^2$, calcula $\nabla f(2,1)$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el gradiente $\nabla f(x,y)$?",
                    "opciones": [
                        ok(r"$\langle 2xy,\ x^2+6y\rangle$"),
                        mal(r"$\langle x^2+6y,\ 2xy\rangle$",
                            r"Cambiaste el orden. La primera componente es $f_x$ y la segunda es $f_y$."),
                        mal(r"$\langle 2x,\ x^2+6y\rangle$",
                            r"Al derivar respecto a $x$, la $y$ se trata como constante, pero sigue multiplicando: la derivada de $x^2y$ es $2xy$, no $2x$."),
                        mal(r"$\langle 2xy,\ x^2+3y\rangle$",
                            r"Revisa $f_y$: la derivada de $3y^2$ es $6y$. El exponente baja y multiplica al coeficiente."),
                    ],
                    "explicacion": r"$f_x=2xy$ (con $y$ constante) y $f_y=x^2+6y$ (con $x$ constante).",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $(2,1)$: ¿cuánto vale $\nabla f(2,1)$?",
                    "opciones": [
                        ok(r"$\langle 4,\ 10\rangle$"),
                        mal(r"$\langle 10,\ 4\rangle$",
                            r"El orden importa: la primera componente es $f_x(2,1)$."),
                        mal(r"$\langle 4,\ 13\rangle$",
                            r"Parece que sustituiste $x=1$ y $y=2$. El punto es $(2,1)$: $x=2$ y $y=1$."),
                        mal(r"$\langle 4,\ 7\rangle$",
                            r"Revisa $f_y$ en $(2,1)$. ¿Usaste $3y$ en lugar de $6y$?"),
                    ],
                    "explicacion": r"$f_x(2,1)=2\cdot2\cdot1=4$ y $f_y(2,1)=2^2+6\cdot1=10$.",
                },
            ],
        },
        {
            "id": "grad-1b",
            "nivel": 1,
            "enunciado": r"Dada $f(x,y)=x^3+2xy$, calcula $\nabla f(1,3)$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el gradiente $\nabla f(x,y)$?",
                    "opciones": [
                        ok(r"$\langle 3x^2+2y,\ 2x\rangle$"),
                        mal(r"$\langle 2x,\ 3x^2+2y\rangle$",
                            r"Cambiaste el orden. La primera componente es $f_x$ y la segunda es $f_y$."),
                        mal(r"$\langle 3x,\ 2x\rangle$",
                            r"La derivada de $x^3$ es $3x^2$: el exponente baja en uno, no desaparece."),
                        mal(r"$\langle 3x^2,\ 2x\rangle$",
                            r"Olvidaste que $2xy$ también depende de $x$: $f_x$ incluye el término $2y$."),
                    ],
                    "explicacion": r"$f_x=3x^2+2y$ y $f_y=2x$.",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $(1,3)$: ¿cuánto vale $\nabla f(1,3)$?",
                    "opciones": [
                        ok(r"$\langle 9,\ 2\rangle$"),
                        mal(r"$\langle 2,\ 9\rangle$",
                            r"El orden importa: la primera componente es $f_x(1,3)$."),
                        mal(r"$\langle 3,\ 2\rangle$",
                            r"No olvides sumar el término $2y$ en $f_x$ al evaluar."),
                        mal(r"$\langle 29,\ 6\rangle$",
                            r"Parece que sustituiste $x=3$ y $y=1$. El punto es $(1,3)$."),
                    ],
                    "explicacion": r"$f_x(1,3)=3\cdot1^2+2\cdot3=9$ y $f_y(1,3)=2\cdot1=2$.",
                },
            ],
        },
 
        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "grad-2a",
            "nivel": 2,
            "enunciado": (r"Dada $f(x,y)=x^2y$, calcula la derivada direccional en $P(1,2)$ "
                          r"en la dirección de $\mathbf{v}=\langle 3,4\rangle$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale $\nabla f(1,2)$?",
                    "opciones": [
                        ok(r"$\langle 4,\ 1\rangle$"),
                        mal(r"$\langle 1,\ 4\rangle$",
                            r"El orden importa: primero $f_x$, luego $f_y$."),
                        mal(r"$\langle 2,\ 1\rangle$",
                            r"Revisa $f_x=2xy$: te falta el factor $y$ al evaluar."),
                        mal(r"$\langle 4,\ 2\rangle$",
                            r"$f_y$ es la derivada respecto a $y$ con $x$ constante: queda $x^2$, no $2x$."),
                    ],
                    "explicacion": r"$f_x=2xy\Rightarrow 4$ y $f_y=x^2\Rightarrow 1$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es el vector unitario $\mathbf{u}$ en la dirección de $\mathbf{v}$?",
                    "opciones": [
                        ok(r"$\langle \tfrac35,\ \tfrac45\rangle$"),
                        mal(r"$\langle 3,\ 4\rangle$",
                            r"Ese es $\mathbf{v}$, pero $\mathbf{u}$ debe medir 1. Divide entre la norma $\|\mathbf{v}\|=\sqrt{3^2+4^2}$."),
                        mal(r"$\langle \tfrac37,\ \tfrac47\rangle$",
                            r"Dividiste entre $3+4$. La norma es $\sqrt{3^2+4^2}$, no la suma."),
                        mal(r"$\langle \tfrac45,\ \tfrac35\rangle$",
                            r"Intercambiaste las componentes: $\mathbf{u}$ conserva el orden de $\mathbf{v}$."),
                    ],
                    "explicacion": r"$\|\mathbf{v}\|=5$, así que $\mathbf{u}=\mathbf{v}/5$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $D_{\mathbf{u}}f(1,2)=\nabla f(1,2)\cdot\mathbf{u}$.",
                    "opciones": [
                        ok(r"$\tfrac{16}{5}$"),
                        mal(r"$16$",
                            r"Usaste $\mathbf{v}$ en lugar de $\mathbf{u}$. La derivada direccional exige el vector unitario."),
                        mal(r"$\tfrac{12}{5}$",
                            r"Te faltó sumar el segundo producto del producto punto."),
                        mal(r"$\tfrac{4}{5}$",
                            r"Te faltó sumar el primer producto del producto punto."),
                    ],
                    "explicacion": r"$4\cdot\tfrac35+1\cdot\tfrac45=\tfrac{16}{5}$.",
                },
            ],
        },
        {
            "id": "grad-2b",
            "nivel": 2,
            "enunciado": (r"Dada $f(x,y)=xy+y^2$, calcula la derivada direccional en $P(2,1)$ "
                          r"en la dirección de $\mathbf{v}=\langle -3,4\rangle$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale $\nabla f(2,1)$?",
                    "opciones": [
                        ok(r"$\langle 1,\ 4\rangle$"),
                        mal(r"$\langle 4,\ 1\rangle$",
                            r"El orden importa: primero $f_x$, luego $f_y$."),
                        mal(r"$\langle 1,\ 3\rangle$",
                            r"La derivada de $y^2$ respecto a $y$ es $2y$, no $y$."),
                        mal(r"$\langle 1,\ 2\rangle$",
                            r"$f_y$ también incluye la derivada del término $y^2$."),
                    ],
                    "explicacion": r"$f_x=y\Rightarrow 1$ y $f_y=x+2y\Rightarrow 4$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es el vector unitario $\mathbf{u}$ en la dirección de $\mathbf{v}$?",
                    "opciones": [
                        ok(r"$\langle -\tfrac35,\ \tfrac45\rangle$"),
                        mal(r"$\langle -3,\ 4\rangle$",
                            r"Ese es $\mathbf{v}$, pero $\mathbf{u}$ debe medir 1. Divide entre su norma."),
                        mal(r"$\langle \tfrac35,\ \tfrac45\rangle$",
                            r"Perdiste el signo de la primera componente."),
                        mal(r"$\langle -\tfrac{3}{25},\ \tfrac{4}{25}\rangle$",
                            r"Dividiste entre $\|\mathbf{v}\|^2$. Hay que dividir entre la norma $\|\mathbf{v}\|$, que lleva raíz."),
                    ],
                    "explicacion": r"$\|\mathbf{v}\|=\sqrt{9+16}=5$, así que $\mathbf{u}=\mathbf{v}/5$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $D_{\mathbf{u}}f(2,1)=\nabla f(2,1)\cdot\mathbf{u}$.",
                    "opciones": [
                        ok(r"$\tfrac{13}{5}$"),
                        mal(r"$\tfrac{19}{5}$",
                            r"Revisa el signo: la primera componente de $\mathbf{u}$ es negativa."),
                        mal(r"$13$",
                            r"Usaste $\mathbf{v}$ sin normalizar. Debes usar el vector unitario $\mathbf{u}$."),
                        mal(r"$-\tfrac{13}{5}$",
                            r"Revisa el signo del resultado: calcula el producto punto término por término."),
                    ],
                    "explicacion": r"$1\cdot(-\tfrac35)+4\cdot\tfrac45=\tfrac{13}{5}$.",
                },
            ],
        },
 
        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "grad-3a",
            "nivel": 3,
            "enunciado": (r"Sea $f(x,y)=x^2y$ y $P(3,2)$. Halla la dirección de máximo crecimiento "
                          r"y la máxima razón de cambio de $f$ en $P$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale $\nabla f(3,2)$?",
                    "opciones": [
                        ok(r"$\langle 12,\ 9\rangle$"),
                        mal(r"$\langle 9,\ 12\rangle$",
                            r"El orden importa: primero $f_x$, luego $f_y$."),
                        mal(r"$\langle 6,\ 9\rangle$",
                            r"Revisa $f_x=2xy$: te falta el factor $y$."),
                        mal(r"$\langle 12,\ 6\rangle$",
                            r"La derivada de $x^2y$ respecto a $y$ es $x^2$ (con $x$ constante), no $2x$."),
                    ],
                    "explicacion": r"$f_x=2xy\Rightarrow12$ y $f_y=x^2\Rightarrow9$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es el vector unitario en la dirección de máximo crecimiento?",
                    "opciones": [
                        ok(r"$\langle \tfrac45,\ \tfrac35\rangle$"),
                        mal(r"$\langle 12,\ 9\rangle$",
                            r"La dirección es correcta, pero el vector debe medir 1: divídelo entre $\|\nabla f\|$."),
                        mal(r"$\langle \tfrac35,\ \tfrac45\rangle$",
                            r"Intercambiaste las componentes: $\mathbf{u}=\nabla f/\|\nabla f\|$ conserva el orden."),
                        mal(r"$\langle -\tfrac45,\ -\tfrac35\rangle$",
                            r"Esa es la dirección de máximo decrecimiento. El máximo crecimiento va en el sentido del gradiente."),
                    ],
                    "explicacion": r"$\|\nabla f\|=\sqrt{12^2+9^2}$ y $\mathbf{u}=\nabla f/\|\nabla f\|$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la máxima razón de cambio de $f$ en $P$?",
                    "opciones": [
                        ok(r"$15$"),
                        mal(r"$225$",
                            r"Olvidaste la raíz: $\|\nabla f\|=\sqrt{12^2+9^2}$."),
                        mal(r"$21$",
                            r"La norma no es la suma de las componentes: es $\sqrt{12^2+9^2}$."),
                        mal(r"$1$",
                            r"Eso es la longitud de $\mathbf{u}$. La razón máxima es $\|\nabla f\|$, no $\|\mathbf{u}\|$."),
                    ],
                    "explicacion": r"$\|\nabla f(3,2)\|=\sqrt{144+81}=15$.",
                },
            ],
        },
        {
            "id": "grad-3b",
            "nivel": 3,
            "enunciado": (r"Sea $f(x,y)=x^2+y^2$ y $P(3,4)$. Analiza la curva de nivel de $f$ "
                          r"que pasa por $P$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale $\nabla f(3,4)$?",
                    "opciones": [
                        ok(r"$\langle 6,\ 8\rangle$"),
                        mal(r"$\langle 8,\ 6\rangle$",
                            r"El orden importa: primero $f_x$, luego $f_y$."),
                        mal(r"$\langle 3,\ 4\rangle$",
                            r"Esas son las coordenadas del punto, no las derivadas: $f_x=2x$ y $f_y=2y$."),
                        mal(r"$\langle 2x,\ 2y\rangle$",
                            r"Esa es la expresión general. Falta sustituir $x=3$ y $y=4$."),
                    ],
                    "explicacion": r"$f_x=2x\Rightarrow6$ y $f_y=2y\Rightarrow8$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál de estos vectores es **normal** a la curva de nivel en $P$?",
                    "opciones": [
                        ok(r"$\langle 6,\ 8\rangle$"),
                        mal(r"$\langle 8,\ -6\rangle$",
                            r"Ese vector es perpendicular al gradiente, es decir, **tangente** a la curva de nivel."),
                        mal(r"$\langle -8,\ 6\rangle$",
                            r"Ese vector es perpendicular al gradiente, es decir, **tangente** a la curva de nivel."),
                    ],
                    "explicacion": r"El gradiente es siempre normal a la curva de nivel.",
                },
                {
                    "pregunta": (r"**Paso 3.** ¿Cuánto vale la derivada direccional de $f$ en $P$ en la "
                                 r"dirección del vector unitario tangente $\mathbf{u}=\langle \tfrac45,\ -\tfrac35\rangle$?"),
                    "opciones": [
                        ok(r"$0$"),
                        mal(r"$10$",
                            r"Ese valor es $\|\nabla f\|$, el máximo, que ocurre en la dirección del gradiente. A lo largo de la curva de nivel $f$ no cambia."),
                        mal(r"$\tfrac{48}{5}$",
                            r"Revisa el signo del segundo término del producto punto."),
                        mal(r"$\tfrac{24}{5}$",
                            r"Te faltó el segundo producto del producto punto."),
                    ],
                    "explicacion": r"$6\cdot\tfrac45+8\cdot(-\tfrac35)=0$: sobre la curva de nivel, $f$ no cambia.",
                },
            ],
        },
    ],

    # ==================================================================
    #  TEMA: Plano tangente y recta normal
    # ==================================================================
    "Plano tangente y recta normal": [

        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "plano_1a",
            "nivel": 1,
            "enunciado": r"Halla la ecuación del plano tangente a $z=x^2+y^2$ en el punto $P(1,2,5)$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto valen $f_x(1,2)$ y $f_y(1,2)$?",
                    "opciones": [
                        ok(r"$f_x=2,\ f_y=4$"),
                        mal(r"$f_x=4,\ f_y=2$",
                            r"Cambiaste el orden: $f_x=2x$ se evalúa con $x=1$ y $f_y=2y$ con $y=2$."),
                        mal(r"$f_x=1,\ f_y=2$",
                            r"Esas son las coordenadas del punto, no las derivadas: $f_x=2x$ y $f_y=2y$."),
                        mal(r"$f_x=2x,\ f_y=2y$",
                            r"Esas son las derivadas en general. Falta evaluarlas en $(1,2)$."),
                    ],
                    "explicacion": r"$f_x=2x\Rightarrow 2$ y $f_y=2y\Rightarrow 4$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es el vector normal al plano en $P$?",
                    "opciones": [
                        ok(r"$\langle 2,\ 4,\ -1\rangle$"),
                        mal(r"$\langle 2,\ 4,\ 1\rangle$",
                            r"Para $z=f(x,y)$ el vector normal es $\langle f_x,\ f_y,\ -1\rangle$: la tercera componente es $-1$."),
                        mal(r"$\langle 2,\ 4,\ 0\rangle$",
                            r"La tercera componente no es $0$: viene de escribir la superficie como $f(x,y)-z=0$, y su derivada en $z$ es $-1$."),
                        mal(r"$\langle 4,\ 2,\ -1\rangle$",
                            r"Cambiaste el orden de $f_x$ y $f_y$."),
                    ],
                    "explicacion": r"$\mathbf{N}=\langle f_x,\ f_y,\ -1\rangle=\langle 2,\ 4,\ -1\rangle$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la ecuación del plano tangente?",
                    "opciones": [
                        ok(r"$2x+4y-z=5$"),
                        mal(r"$2x+4y+z=15$",
                            r"El coeficiente de $z$ debe ser $-1$, la tercera componente de la normal."),
                        mal(r"$2x+4y-z=10$",
                            r"Falta el término $z_0$: la ecuación es $2(x-1)+4(y-2)-(z-z_0)=0$."),
                        mal(r"$2x+4y-z=0$",
                            r"Al expandir $2(x-1)+4(y-2)-(z-5)$ queda un término constante: no se anula."),
                    ],
                    "explicacion": r"$2(x-1)+4(y-2)-(z-5)=0\Rightarrow 2x+4y-z=5$.",
                },
            ],
        },
        {
            "id": "plano_1b",
            "nivel": 1,
            "enunciado": r"Halla la ecuación del plano tangente a $z=x^2y$ en el punto $P(1,3,3)$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto valen $f_x(1,3)$ y $f_y(1,3)$?",
                    "opciones": [
                        ok(r"$f_x=6,\ f_y=1$"),
                        mal(r"$f_x=2,\ f_y=1$",
                            r"Revisa $f_x=2xy$: te falta el factor $y$."),
                        mal(r"$f_x=1,\ f_y=6$",
                            r"Cambiaste el orden de $f_x$ y $f_y$."),
                        mal(r"$f_x=6,\ f_y=2$",
                            r"$f_y$ es la derivada de $x^2y$ respecto a $y$ con $x$ constante: queda $x^2$, no $2x$."),
                    ],
                    "explicacion": r"$f_x=2xy\Rightarrow 6$ y $f_y=x^2\Rightarrow 1$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es el vector normal al plano en $P$?",
                    "opciones": [
                        ok(r"$\langle 6,\ 1,\ -1\rangle$"),
                        mal(r"$\langle 6,\ 1,\ 1\rangle$",
                            r"La tercera componente de la normal es $-1$."),
                        mal(r"$\langle 1,\ 6,\ -1\rangle$",
                            r"Cambiaste el orden de $f_x$ y $f_y$."),
                        mal(r"$\langle 6,\ 1,\ 0\rangle$",
                            r"La tercera componente no es $0$: es $-1$."),
                    ],
                    "explicacion": r"$\mathbf{N}=\langle f_x,\ f_y,\ -1\rangle=\langle 6,\ 1,\ -1\rangle$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la ecuación del plano tangente?",
                    "opciones": [
                        ok(r"$6x+y-z=6$"),
                        mal(r"$6x+y+z=12$",
                            r"El coeficiente de $z$ debe ser $-1$."),
                        mal(r"$6x+y-z=9$",
                            r"Falta el término $z_0$: el último factor es $-(z-z_0)$, no $-z$."),
                        mal(r"$6x+y-z=0$",
                            r"Al expandir $6(x-1)+(y-3)-(z-3)$ queda un término constante: no se anula."),
                    ],
                    "explicacion": r"$6(x-1)+(y-3)-(z-3)=0\Rightarrow 6x+y-z=6$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "plano_2a",
            "nivel": 2,
            "enunciado": (r"La superficie $x^2+2y^2+3z^2=6$ pasa por $P(1,1,1)$. "
                          r"Halla su plano tangente y su recta normal en $P$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Con $F(x,y,z)=x^2+2y^2+3z^2-6$, ¿cuánto vale $\nabla F(1,1,1)$?",
                    "opciones": [
                        ok(r"$\langle 2,\ 4,\ 6\rangle$"),
                        mal(r"$\langle 1,\ 2,\ 3\rangle$",
                            r"Al derivar $x^2$, $2y^2$ y $3z^2$, el exponente baja y multiplica al coeficiente."),
                        mal(r"$\langle 2,\ 2,\ 2\rangle$",
                            r"Los coeficientes $2$ y $3$ se conservan al derivar $2y^2$ y $3z^2$."),
                        mal(r"$\langle 6,\ 4,\ 2\rangle$",
                            r"Cambiaste el orden: la primera componente es $F_x$ y la última es $F_z$."),
                    ],
                    "explicacion": r"$F_x=2x$, $F_y=4y$, $F_z=6z$, evaluadas en $(1,1,1)$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es la ecuación del plano tangente en $P$?",
                    "opciones": [
                        ok(r"$x+2y+3z=6$"),
                        mal(r"$2x+4y+6z=6$",
                            r"Si usas $\langle 2,4,6\rangle$ como coeficientes, la constante también cambia: sale de $\nabla F(P)\cdot P$."),
                        mal(r"$x+2y+3z=0$",
                            r"Este plano no pasa por $P$: reemplaza $P$ para hallar la constante."),
                        mal(r"$x+y+z=3$",
                            r"La normal del plano es $\nabla F(P)$, no el punto $P$."),
                    ],
                    "explicacion": r"$2(x-1)+4(y-1)+6(z-1)=0\Rightarrow x+2y+3z=6$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuáles son las ecuaciones simétricas de la recta normal en $P$?",
                    "opciones": [
                        ok(r"$\dfrac{x-1}{1}=\dfrac{y-1}{2}=\dfrac{z-1}{3}$"),
                        mal(r"$\dfrac{x-1}{1}=\dfrac{y-1}{2}=\dfrac{z-1}{-1}$",
                            r"El $-1$ solo aparece cuando la superficie viene como $z=f(x,y)$. Aquí la dirección es $\nabla F$."),
                        mal(r"$\dfrac{x}{1}=\dfrac{y}{2}=\dfrac{z}{3}$",
                            r"Te faltó restar las coordenadas del punto: la recta debe pasar por $P$."),
                        mal(r"$\dfrac{x-1}{3}=\dfrac{y-1}{2}=\dfrac{z-1}{1}$",
                            r"Invertiste el orden de los números directores."),
                    ],
                    "explicacion": r"La dirección es $\nabla F(P)\parallel\langle 1,2,3\rangle$ y la recta pasa por $P(1,1,1)$.",
                },
            ],
        },
        {
            "id": "plano_2b",
            "nivel": 2,
            "enunciado": (r"El paraboloide $z=x^2+y^2$ se escribe como $F(x,y,z)=x^2+y^2-z=0$. "
                          r"Halla su plano tangente en $P(1,1,2)$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el gradiente $\nabla F(x,y,z)$?",
                    "opciones": [
                        ok(r"$\langle 2x,\ 2y,\ -1\rangle$"),
                        mal(r"$\langle 2x,\ 2y,\ 1\rangle$",
                            r"Revisa el signo: la derivada de $-z$ respecto a $z$ es $-1$."),
                        mal(r"$\langle 2x,\ 2y,\ 0\rangle$",
                            r"El término $-z$ también se deriva: respecto a $z$ no da $0$."),
                        mal(r"$\langle x,\ y,\ -1\rangle$",
                            r"La derivada de $x^2$ es $2x$: el exponente baja y multiplica."),
                    ],
                    "explicacion": r"$F_x=2x$, $F_y=2y$ y $F_z=-1$.",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $P(1,1,2)$: ¿cuánto vale $\nabla F(P)$?",
                    "opciones": [
                        ok(r"$\langle 2,\ 2,\ -1\rangle$"),
                        mal(r"$\langle 2,\ 2,\ -2\rangle$",
                            r"La tercera componente es la constante $-1$: no depende de $z$."),
                        mal(r"$\langle 2,\ 2,\ 1\rangle$",
                            r"Revisa el signo de la tercera componente."),
                        mal(r"$\langle 1,\ 1,\ -1\rangle$",
                            r"Evalúa bien: $2x$ con $x=1$ no vale $1$."),
                    ],
                    "explicacion": r"$\nabla F(1,1,2)=\langle 2\cdot1,\ 2\cdot1,\ -1\rangle$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la ecuación del plano tangente en $P$?",
                    "opciones": [
                        ok(r"$2x+2y-z=2$"),
                        mal(r"$2x+2y+z=6$",
                            r"El coeficiente de $z$ es la tercera componente de $\nabla F(P)$, que es $-1$."),
                        mal(r"$2x+2y-z=0$",
                            r"Este plano no pasa por $P$: al expandir $2(x-1)+2(y-1)-(z-2)$ queda una constante."),
                        mal(r"$x+y-z=0$",
                            r"Los coeficientes son las componentes de $\nabla F(P)$: $2$ y $2$, no $1$ y $1$."),
                    ],
                    "explicacion": r"$2(x-1)+2(y-1)-(z-2)=0\Rightarrow 2x+2y-z=2$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "plano_3a",
            "nivel": 3,
            "enunciado": (r"Halla el punto de la superficie $z=x^2+y^2-2x+4y$ donde el plano tangente "
                          r"es horizontal."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué condición debe cumplirse para que el plano tangente sea horizontal?",
                    "opciones": [
                        ok(r"$f_x=0$ y $f_y=0$"),
                        mal(r"$f_x=1$ y $f_y=1$",
                            r"Un plano horizontal tiene normal vertical: las dos primeras componentes de $\langle f_x,f_y,-1\rangle$ deben ser $0$."),
                        mal(r"$f=0$",
                            r"Eso solo dice que el punto está en $z=0$; no dice nada sobre la inclinación del plano."),
                        mal(r"$f_x=f_y$",
                            r"Que sean iguales no basta: deben ser cero para que no haya inclinación en ninguna dirección."),
                    ],
                    "explicacion": r"La normal $\langle f_x,f_y,-1\rangle$ es vertical cuando $f_x=f_y=0$.",
                },
                {
                    "pregunta": r"**Paso 2.** Resuelve $f_x=0$ y $f_y=0$: ¿cuáles son $(x,y)$?",
                    "opciones": [
                        ok(r"$(1,\ -2)$"),
                        mal(r"$(-1,\ 2)$",
                            r"Revisa los signos al despejar: ambas coordenadas salieron con el signo cambiado."),
                        mal(r"$(2,\ -4)$",
                            r"Despejaste sin dividir entre el coeficiente de la variable."),
                        mal(r"$(1,\ 2)$",
                            r"Revisa $f_y=2y+4=0$: el signo de $y$."),
                    ],
                    "explicacion": r"$f_x=2x-2=0\Rightarrow x=1$ y $f_y=2y+4=0\Rightarrow y=-2$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la altura $z$ de ese punto sobre la superficie?",
                    "opciones": [
                        ok(r"$-5$"),
                        mal(r"$11$",
                            r"Revisa el signo del término $4y$ al evaluar con $y=-2$."),
                        mal(r"$-3$",
                            r"Te faltó el término $-2x$."),
                        mal(r"$15$",
                            r"Parece que usaste el punto $(-1,2)$ en lugar de $(1,-2)$."),
                    ],
                    "explicacion": r"$z=1^2+(-2)^2-2(1)+4(-2)=-5$.",
                },
            ],
        },
        {
            "id": "plano_3b",
            "nivel": 3,
            "enunciado": (r"Halla el punto del paraboloide $z=x^2+y^2$ donde el plano tangente es "
                          r"paralelo al plano $4x+2y-z=7$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el vector normal al plano tangente en un punto $(x,y)$?",
                    "opciones": [
                        ok(r"$\langle 2x,\ 2y,\ -1\rangle$"),
                        mal(r"$\langle 2x,\ 2y,\ 1\rangle$",
                            r"La tercera componente de $\langle f_x,f_y,-1\rangle$ es $-1$."),
                        mal(r"$\langle x,\ y,\ -1\rangle$",
                            r"Las derivadas de $x^2$ y $y^2$ son $2x$ y $2y$."),
                        mal(r"$\langle 2x,\ 2y,\ -z\rangle$",
                            r"La tercera componente es la constante $-1$; no depende de $z$."),
                    ],
                    "explicacion": r"$\mathbf{N}=\langle f_x,f_y,-1\rangle=\langle 2x,\ 2y,\ -1\rangle$.",
                },
                {
                    "pregunta": (r"**Paso 2.** El plano dado tiene normal $\langle 4,\ 2,\ -1\rangle$. "
                                 r"Para que sean paralelos, ¿qué ecuaciones deben cumplirse?"),
                    "opciones": [
                        ok(r"$2x=4$ y $2y=2$"),
                        mal(r"$2x=2$ y $2y=4$",
                            r"Compara cada componente con la suya: la primera con la primera."),
                        mal(r"$x=4$ y $y=2$",
                            r"Falta el factor $2$ de las derivadas: las componentes son $2x$ y $2y$."),
                        mal(r"$2x=-4$ y $2y=-2$",
                            r"Como la tercera componente es $-1$ en ambos vectores, las otras dos deben coincidir sin cambiar de signo."),
                    ],
                    "explicacion": r"Con la tercera componente igual a $-1$ en ambos, deben coincidir $2x=4$ y $2y=2$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es el punto $(x,y,z)$ de la superficie?",
                    "opciones": [
                        ok(r"$(2,\ 1,\ 5)$"),
                        mal(r"$(4,\ 2,\ 20)$",
                            r"Igualaste $x=4$ y $y=2$ sin dividir entre $2$."),
                        mal(r"$(2,\ 1,\ 3)$",
                            r"La altura es $z=x^2+y^2$, no $x+y$."),
                        mal(r"$(-2,\ -1,\ 5)$",
                            r"Revisa los signos: de $2x=4$ sale un valor positivo para $x$."),
                    ],
                    "explicacion": r"$x=2$, $y=1$ y $z=2^2+1^2=5$.",
                },
            ],
        },
    ],

    # ==================================================================
    #  TEMA: Puntos críticos y criterios de la segunda derivada
    # ==================================================================
    "Puntos críticos y criterios de la segunda derivada": [

        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "crit_1a",
            "nivel": 1,
            "enunciado": r"Sea $f(x,y)=x^2+y^2-4x+6y$. Halla su punto crítico y clasifícalo.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el punto crítico?",
                    "opciones": [
                        ok(r"$(2,\ -3)$"),
                        mal(r"$(-2,\ 3)$",
                            r"Revisa los signos al despejar: ambas coordenadas salieron cambiadas."),
                        mal(r"$(4,\ -6)$",
                            r"Despejaste sin dividir entre el coeficiente de la variable."),
                        mal(r"$(2,\ 3)$",
                            r"Revisa el signo de $y$ al resolver $f_y=0$."),
                    ],
                    "explicacion": r"$f_x=2x-4=0\Rightarrow x=2$ y $f_y=2y+6=0\Rightarrow y=-3$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $\Delta=f_{xx}f_{yy}-f_{xy}^2$.",
                    "opciones": [
                        ok(r"$4$"),
                        mal(r"$2$",
                            r"$\Delta$ no es una sola segunda derivada: es $f_{xx}f_{yy}-f_{xy}^2$."),
                        mal(r"$0$",
                            r"$f_{xy}=0$ anula solo el término que se resta, no el producto $f_{xx}f_{yy}$."),
                        mal(r"$-4$",
                            r"Revisa el signo: aquí $f_{xy}=0$, así que $\Delta$ es el producto $f_{xx}f_{yy}$."),
                    ],
                    "explicacion": r"$f_{xx}=2$, $f_{yy}=2$, $f_{xy}=0\Rightarrow\Delta=4$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué clase de punto es?",
                    "opciones": [
                        ok(r"Mínimo relativo"),
                        mal(r"Máximo relativo",
                            r"Con $\Delta>0$ decide el signo de $f_{xx}$: si es positivo, es mínimo."),
                        mal(r"Punto de silla",
                            r"El punto de silla ocurre cuando $\Delta<0$."),
                        mal(r"El criterio no decide",
                            r"El criterio solo falla cuando $\Delta=0$."),
                    ],
                    "explicacion": r"$\Delta=4>0$ y $f_{xx}=2>0$: mínimo relativo.",
                },
            ],
        },
        {
            "id": "crit_1b",
            "nivel": 1,
            "enunciado": r"Sea $f(x,y)=-x^2-y^2+2x-4y$. Halla su punto crítico y clasifícalo.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el punto crítico?",
                    "opciones": [
                        ok(r"$(1,\ -2)$"),
                        mal(r"$(-1,\ 2)$",
                            r"Revisa los signos al despejar: ambas coordenadas salieron cambiadas."),
                        mal(r"$(1,\ 2)$",
                            r"Revisa el signo de $y$ al resolver $f_y=0$."),
                        mal(r"$(2,\ -4)$",
                            r"Despejaste sin dividir entre el coeficiente de la variable."),
                    ],
                    "explicacion": r"$f_x=-2x+2=0\Rightarrow x=1$ y $f_y=-2y-4=0\Rightarrow y=-2$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $\Delta=f_{xx}f_{yy}-f_{xy}^2$.",
                    "opciones": [
                        ok(r"$4$"),
                        mal(r"$-4$",
                            r"El producto de dos números negativos es positivo."),
                        mal(r"$-2$",
                            r"$\Delta$ no es solo $f_{xx}$: es $f_{xx}f_{yy}-f_{xy}^2$."),
                        mal(r"$0$",
                            r"$f_{xy}=0$ anula solo el término que se resta, no el producto $f_{xx}f_{yy}$."),
                    ],
                    "explicacion": r"$f_{xx}=-2$, $f_{yy}=-2$, $f_{xy}=0\Rightarrow\Delta=4$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué clase de punto es?",
                    "opciones": [
                        ok(r"Máximo relativo"),
                        mal(r"Mínimo relativo",
                            r"Con $\Delta>0$ decide el signo de $f_{xx}$: aquí es negativo."),
                        mal(r"Punto de silla",
                            r"El punto de silla ocurre cuando $\Delta<0$."),
                        mal(r"El criterio no decide",
                            r"El criterio solo falla cuando $\Delta=0$."),
                    ],
                    "explicacion": r"$\Delta=4>0$ y $f_{xx}=-2<0$: máximo relativo.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "crit_2a",
            "nivel": 2,
            "enunciado": (r"Sea $f(x,y)=x^3+y^3-3x-12y+20$. Halla sus puntos críticos y "
                          r"clasifica el punto $(-1,-2)$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuáles son todos los puntos críticos?",
                    "opciones": [
                        ok(r"$(1,2),\ (1,-2),\ (-1,2),\ (-1,-2)$"),
                        mal(r"$(1,4),\ (1,-4),\ (-1,4),\ (-1,-4)$",
                            r"De $3y^2-12=0$ sale $y^2=$ un número que debes calcular antes de sacar la raíz."),
                        mal(r"$(1,2)$ y $(-1,-2)$",
                            r"Cada valor de $x$ se combina con cada valor de $y$: salen más puntos."),
                        mal(r"$(0,0)$",
                            r"$(0,0)$ no cumple $f_x=3x^2-3=0$."),
                    ],
                    "explicacion": r"$f_x=3x^2-3=0\Rightarrow x=\pm1$ y $f_y=3y^2-12=0\Rightarrow y=\pm2$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es $\Delta=f_{xx}f_{yy}-f_{xy}^2$ como expresión en $x$ e $y$?",
                    "opciones": [
                        ok(r"$36xy$"),
                        mal(r"$6xy$",
                            r"Con $f_{xx}=6x$ y $f_{yy}=6y$, al multiplicar también se multiplican los dos $6$."),
                        mal(r"$6x+6y$",
                            r"$\Delta$ multiplica $f_{xx}\cdot f_{yy}$; no los suma."),
                        mal(r"$36(x+y)$",
                            r"Se multiplican $f_{xx}$ y $f_{yy}$: el resultado lleva $xy$, no $x+y$."),
                    ],
                    "explicacion": r"$f_{xx}=6x$, $f_{yy}=6y$, $f_{xy}=0\Rightarrow\Delta=36xy$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué clase de punto es $(-1,-2)$?",
                    "opciones": [
                        ok(r"Máximo relativo"),
                        mal(r"Mínimo relativo",
                            r"Revisa el signo de $f_{xx}=6x$ en ese punto."),
                        mal(r"Punto de silla",
                            r"En $(-1,-2)$, $\Delta=36xy$ resulta positivo: el producto de dos negativos es positivo."),
                        mal(r"El criterio no decide",
                            r"El criterio solo falla cuando $\Delta=0$."),
                    ],
                    "explicacion": r"$\Delta=36(-1)(-2)=72>0$ y $f_{xx}=-6<0$: máximo relativo.",
                },
            ],
        },
        {
            "id": "crit_2b",
            "nivel": 2,
            "enunciado": r"Sea $f(x,y)=x^2+xy+y^2-3x$. Halla su punto crítico y clasifícalo.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Resuelve $f_x=0$ y $f_y=0$: ¿cuál es el punto crítico?",
                    "opciones": [
                        ok(r"$(2,\ -1)$"),
                        mal(r"$(-2,\ 1)$",
                            r"Revisa los signos al resolver el sistema: ambas coordenadas salieron cambiadas."),
                        mal(r"$(\tfrac32,\ 0)$",
                            r"Solo usaste una ecuación ($f_x=0$ con $y=0$); el punto debe cumplir las dos."),
                        mal(r"$(1,\ -2)$",
                            r"Comprueba tu punto en $f_x=2x+y-3=0$: no se cumple."),
                    ],
                    "explicacion": r"$f_x=2x+y-3=0$ y $f_y=x+2y=0$: de la segunda, $x=-2y$, y queda $y=-1$, $x=2$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $\Delta=f_{xx}f_{yy}-f_{xy}^2$.",
                    "opciones": [
                        ok(r"$3$"),
                        mal(r"$4$",
                            r"Falta restar $f_{xy}^2$: aquí $f_{xy}=1$ no es cero."),
                        mal(r"$5$",
                            r"Es una resta: $\Delta=f_{xx}f_{yy}-f_{xy}^2$."),
                        mal(r"$-3$",
                            r"Revisa el orden de la resta: primero el producto $f_{xx}f_{yy}$, luego se resta $f_{xy}^2$."),
                    ],
                    "explicacion": r"$f_{xx}=2$, $f_{yy}=2$, $f_{xy}=1\Rightarrow\Delta=4-1=3$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué clase de punto es?",
                    "opciones": [
                        ok(r"Mínimo relativo"),
                        mal(r"Máximo relativo",
                            r"Con $\Delta>0$ decide el signo de $f_{xx}$: aquí es positivo."),
                        mal(r"Punto de silla",
                            r"El punto de silla ocurre cuando $\Delta<0$."),
                        mal(r"El criterio no decide",
                            r"El criterio solo falla cuando $\Delta=0$."),
                    ],
                    "explicacion": r"$\Delta=3>0$ y $f_{xx}=2>0$: mínimo relativo.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "crit_3a",
            "nivel": 3,
            "enunciado": (r"Sea $f(x,y)=x^3+3xy^2-15x-12y$. Clasifica el punto crítico $(2,1)$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Al igualar $f_x=0$ y $f_y=0$ y simplificar, ¿qué sistema resulta?",
                    "opciones": [
                        ok(r"$x^2+y^2=5$ y $xy=2$"),
                        mal(r"$x^2+y^2=15$ y $xy=12$",
                            r"Divide cada ecuación entre su factor común ($3$ y $6$ respectivamente)."),
                        mal(r"$x^2-y^2=5$ y $xy=2$",
                            r"Revisa el signo: $f_x=3x^2+3y^2-15$."),
                        mal(r"$x^2+y^2=5$ y $xy=12$",
                            r"En $f_y=6xy-12=0$ divide entre $6$ en los dos lados."),
                    ],
                    "explicacion": r"$f_x=3x^2+3y^2-15=0$ y $f_y=6xy-12=0$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es $\Delta=f_{xx}f_{yy}-f_{xy}^2$ como expresión?",
                    "opciones": [
                        ok(r"$36x^2-36y^2$"),
                        mal(r"$36x^2+36y^2$",
                            r"$\Delta$ resta $f_{xy}^2$, y aquí $f_{xy}=6y$ no es cero."),
                        mal(r"$36x^2$",
                            r"No olvides restar $f_{xy}^2$."),
                        mal(r"$36xy$",
                            r"Revisa: $f_{xx}=6x$, $f_{yy}=6x$ y $f_{xy}=6y$."),
                    ],
                    "explicacion": r"$f_{xx}=6x$, $f_{yy}=6x$, $f_{xy}=6y\Rightarrow\Delta=36x^2-36y^2$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué clase de punto es $(2,1)$?",
                    "opciones": [
                        ok(r"Mínimo relativo"),
                        mal(r"Máximo relativo",
                            r"Revisa el signo de $f_{xx}=6x$ en $x=2$."),
                        mal(r"Punto de silla",
                            r"En $(2,1)$, $\Delta=36(x^2-y^2)$ resulta positivo."),
                        mal(r"El criterio no decide",
                            r"El criterio solo falla cuando $\Delta=0$."),
                    ],
                    "explicacion": r"$\Delta=36(4-1)=108>0$ y $f_{xx}=12>0$: mínimo relativo.",
                },
            ],
        },
        {
            "id": "crit_3b",
            "nivel": 3,
            "enunciado": r"Sea $f(x,y)=x^4+y^4$. Analiza el origen con el criterio de la segunda derivada.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es el punto crítico?",
                    "opciones": [
                        ok(r"$(0,\ 0)$"),
                        mal(r"$(1,\ 1)$",
                            r"Evalúa $f_x=4x^3$ en tu punto: no es cero."),
                        mal(r"$(1,\ 0)$",
                            r"Evalúa $f_x=4x^3$ en tu punto: no es cero."),
                        mal(r"No tiene puntos críticos",
                            r"$f_x=4x^3$ y $f_y=4y^3$ se anulan los dos en algún punto."),
                    ],
                    "explicacion": r"$f_x=4x^3=0$ y $f_y=4y^3=0$ solo en $(0,0)$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $\Delta=f_{xx}f_{yy}-f_{xy}^2$ en $(0,0)$.",
                    "opciones": [
                        ok(r"$0$"),
                        mal(r"$12$",
                            r"Evalúa $f_{xx}=12x^2$ y $f_{yy}=12y^2$ en $(0,0)$ antes de combinarlas."),
                        mal(r"$144$",
                            r"Evalúa $f_{xx}=12x^2$ y $f_{yy}=12y^2$ en el punto antes de multiplicar."),
                        mal(r"$-12$",
                            r"Evalúa $f_{xx}$, $f_{yy}$ y $f_{xy}$ en $(0,0)$ y vuelve a calcular."),
                    ],
                    "explicacion": r"$f_{xx}=12x^2$, $f_{yy}=12y^2$, $f_{xy}=0$: todo vale $0$ en el origen, así que $\Delta=0$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué concluye el criterio de la segunda derivada?",
                    "opciones": [
                        ok(r"No permite concluir (el criterio falla)"),
                        mal(r"Hay un mínimo relativo",
                            r"Con $\Delta=0$ el criterio no puede asegurarlo: hay que analizar de otra forma (aquí, $f\geq 0=f(0,0)$)."),
                        mal(r"Hay un punto de silla",
                            r"El punto de silla requiere $\Delta<0$."),
                        mal(r"Hay un máximo relativo",
                            r"El máximo requiere $\Delta>0$ y $f_{xx}<0$."),
                    ],
                    "explicacion": r"Con $\Delta=0$ el criterio falla. (Aquí el origen sí es mínimo, pero porque $x^4+y^4\geq 0$, no por el criterio.)",
                },
            ],
        },
    ],

    # ==================================================================
    #  TEMA: Incremento diferencial total
    # ==================================================================
    "Incremento diferencial total": [

        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "inc_1a",
            "nivel": 1,
            "enunciado": (r"Sea $f(x,y)=x^2y$. Usa la diferencial total para estimar el cambio de $f$ "
                          r"al pasar de $(2,3)$ con $dx=0.1$ y $dy=0.2$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuáles son las derivadas parciales $f_x$ y $f_y$?",
                    "opciones": [
                        ok(r"$f_x=2xy,\ f_y=x^2$"),
                        mal(r"$f_x=x^2,\ f_y=2xy$",
                            r"Cambiaste el orden: $f_x$ es la derivada respecto a $x$."),
                        mal(r"$f_x=2x,\ f_y=x^2$",
                            r"Al derivar respecto a $x$, la $y$ se queda multiplicando: $f_x$ lleva el factor $y$."),
                        mal(r"$f_x=2xy,\ f_y=2x$",
                            r"$f_y$ es la derivada de $x^2y$ respecto a $y$ con $x$ constante: queda $x^2$."),
                    ],
                    "explicacion": r"$f_x=2xy$ y $f_y=x^2$.",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $(2,3)$: ¿cuánto valen $f_x$ y $f_y$?",
                    "opciones": [
                        ok(r"$f_x=12,\ f_y=4$"),
                        mal(r"$f_x=4,\ f_y=12$",
                            r"Cambiaste el orden de los valores."),
                        mal(r"$f_x=6,\ f_y=4$",
                            r"Revisa $f_x=2xy$ en $(2,3)$: te falta un factor."),
                        mal(r"$f_x=12,\ f_y=9$",
                            r"$f_y=x^2$ depende de $x$, no de $y$: evalúa con $x=2$."),
                    ],
                    "explicacion": r"$f_x(2,3)=2\cdot2\cdot3=12$ y $f_y(2,3)=2^2=4$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $df=f_x\,dx+f_y\,dy$.",
                    "opciones": [
                        ok(r"$2.0$"),
                        mal(r"$2.8$",
                            r"Cambiaste $dx$ y $dy$: $f_x$ multiplica a $dx$ y $f_y$ multiplica a $dy$."),
                        mal(r"$1.2$",
                            r"Te faltó el segundo término $f_y\,dy$."),
                        mal(r"$0.8$",
                            r"Te faltó el primer término $f_x\,dx$."),
                    ],
                    "explicacion": r"$df=12(0.1)+4(0.2)=1.2+0.8=2.0$.",
                },
            ],
        },
        {
            "id": "inc_1b",
            "nivel": 1,
            "enunciado": (r"Sea $f(x,y)=3x^2-2y^2$. Estima con $df$ el cambio de $f$ al pasar de $(1,2)$ "
                          r"con $dx=-0.1$ y $dy=0.05$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuáles son $f_x$ y $f_y$?",
                    "opciones": [
                        ok(r"$f_x=6x,\ f_y=-4y$"),
                        mal(r"$f_x=6x,\ f_y=4y$",
                            r"Revisa el signo de $f_y$: el término es $-2y^2$."),
                        mal(r"$f_x=3x,\ f_y=-2y$",
                            r"Al derivar $x^2$ y $y^2$ el exponente baja y multiplica."),
                        mal(r"$f_x=-4y,\ f_y=6x$",
                            r"Cambiaste el orden: $f_x$ es la derivada respecto a $x$."),
                    ],
                    "explicacion": r"$f_x=6x$ y $f_y=-4y$.",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $(1,2)$: ¿cuánto valen $f_x$ y $f_y$?",
                    "opciones": [
                        ok(r"$f_x=6,\ f_y=-8$"),
                        mal(r"$f_x=6,\ f_y=8$",
                            r"Revisa el signo de $f_y$ al evaluar."),
                        mal(r"$f_x=3,\ f_y=-4$",
                            r"Parece que no multiplicaste por el coeficiente al derivar."),
                        mal(r"$f_x=-8,\ f_y=6$",
                            r"Cambiaste el orden de los valores."),
                    ],
                    "explicacion": r"$f_x(1,2)=6\cdot1=6$ y $f_y(1,2)=-4\cdot2=-8$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $df=f_x\,dx+f_y\,dy$.",
                    "opciones": [
                        ok(r"$-1.0$"),
                        mal(r"$0.2$",
                            r"Revisa el signo del primer término: $6\cdot(-0.1)$ es negativo."),
                        mal(r"$-0.6$",
                            r"Te faltó el segundo término $f_y\,dy$."),
                        mal(r"$-0.4$",
                            r"Te faltó el primer término $f_x\,dx$."),
                    ],
                    "explicacion": r"$df=6(-0.1)+(-8)(0.05)=-0.6-0.4=-1.0$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "inc_2a",
            "nivel": 2,
            "enunciado": (r"Sea $f(x,y)=x^2y$ y el punto $(2,3)$ con $dx=0.1$ y $dy=-0.1$. "
                          r"Compara $df$ con el incremento real $\Delta f$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Calcula $df=f_x\,dx+f_y\,dy$ (con $f_x=12$ y $f_y=4$ en el punto).",
                    "opciones": [
                        ok(r"$0.8$"),
                        mal(r"$1.6$",
                            r"Revisa el signo del segundo término: $dy=-0.1$ es negativo."),
                        mal(r"$1.2$",
                            r"Te faltó el segundo término $f_y\,dy$."),
                        mal(r"$-0.8$",
                            r"Revisa el signo del primer término: $dx=0.1$ es positivo."),
                    ],
                    "explicacion": r"$df=12(0.1)+4(-0.1)=1.2-0.4=0.8$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula el incremento real $\Delta f=f(2.1,\,2.9)-f(2,3)$.",
                    "opciones": [
                        ok(r"$0.789$"),
                        mal(r"$12.789$",
                            r"Te faltó restar el valor inicial $f(2,3)=12$."),
                        mal(r"$1.671$",
                            r"Usaste $y=3.1$: como $dy=-0.1$, el nuevo valor de $y$ es $2.9$."),
                        mal(r"$-1.531$",
                            r"Usaste $x=1.9$: como $dx=0.1$, el nuevo valor de $x$ es $2.1$."),
                    ],
                    "explicacion": r"$f(2.1,2.9)=4.41\cdot2.9=12.789$, y $\Delta f=12.789-12=0.789$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Qué relación hay entre $df$ y $\Delta f$?",
                    "opciones": [
                        ok(r"$df$ aproxima bien a $\Delta f$ porque $dx$ y $dy$ son pequeños"),
                        mal(r"$df$ es exactamente igual a $\Delta f$",
                            r"Aquí $0.8\neq 0.789$: $df$ es solo una aproximación lineal."),
                        mal(r"$\Delta f$ es la aproximación lineal de $df$",
                            r"Es al revés: $df$ es la aproximación lineal y $\Delta f$ es el cambio real."),
                        mal(r"Son muy distintos y la aproximación no sirve",
                            r"Los valores son muy cercanos: para incrementos pequeños la diferencial funciona bien."),
                    ],
                    "explicacion": r"$df=0.8$ y $\Delta f=0.789$: $df\approx\Delta f$.",
                },
            ],
        },
        {
            "id": "inc_2b",
            "nivel": 2,
            "enunciado": (r"Sea $f(x,y)=x^2y-3y$. Al pasar de $(4,3)$ con $dx=-0.01$ y $dy=0.02$, "
                          r"compara $df$ con $\Delta f$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto valen $f_x$ y $f_y$ en $(4,3)$?",
                    "opciones": [
                        ok(r"$f_x=24,\ f_y=13$"),
                        mal(r"$f_x=13,\ f_y=24$",
                            r"Cambiaste el orden de los valores."),
                        mal(r"$f_x=24,\ f_y=16$",
                            r"Revisa $f_y$: la derivada de $-3y$ respecto a $y$ es $-3$."),
                        mal(r"$f_x=8,\ f_y=13$",
                            r"Revisa $f_x=2xy$: te falta un factor al evaluar."),
                    ],
                    "explicacion": r"$f_x=2xy\Rightarrow24$ y $f_y=x^2-3\Rightarrow13$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $df=f_x\,dx+f_y\,dy$.",
                    "opciones": [
                        ok(r"$0.02$"),
                        mal(r"$0.50$",
                            r"Revisa el signo del primer término: $24\cdot(-0.01)$ es negativo."),
                        mal(r"$0.26$",
                            r"Te faltó el primer término $f_x\,dx$."),
                        mal(r"$-0.24$",
                            r"Te faltó el segundo término $f_y\,dy$."),
                    ],
                    "explicacion": r"$df=24(-0.01)+13(0.02)=-0.24+0.26=0.02$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sabiendo que $f(3.99,\,3.02)=39.018702$ y $f(4,3)=39$, ¿cuánto vale $\Delta f$?",
                    "opciones": [
                        ok(r"$0.018702$"),
                        mal(r"$0.02$",
                            r"Ese es $df$, la aproximación. $\Delta f$ es la resta de los valores de la función."),
                        mal(r"$39.018702$",
                            r"Te faltó restar el valor inicial $f(4,3)=39$."),
                        mal(r"$-0.018702$",
                            r"Revisa el orden de la resta: valor nuevo menos valor inicial."),
                    ],
                    "explicacion": r"$\Delta f=39.018702-39=0.018702\approx df=0.02$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "inc_3a",
            "nivel": 3,
            "enunciado": (r"Una caja sin tapa se construye con tablas de madera de $\tfrac23$ pulg de espesor. "
                          r"Sus dimensiones interiores son $x=6$ (largo), $y=3$ (ancho) y $z=4$ (profundidad). "
                          r"Estima con $dV$ la madera usada, con $V=xyz$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuáles son los incrementos $dx$, $dy$ y $dz$?",
                    "opciones": [
                        ok(r"$dx=\tfrac43,\ dy=\tfrac43,\ dz=\tfrac23$"),
                        mal(r"$dx=\tfrac23,\ dy=\tfrac23,\ dz=\tfrac23$",
                            r"En el largo y el ancho hay dos paredes: el espesor se suma dos veces."),
                        mal(r"$dx=\tfrac43,\ dy=\tfrac43,\ dz=\tfrac43$",
                            r"La caja no tiene tapa: en la profundidad solo suma el fondo."),
                        mal(r"$dx=\tfrac23,\ dy=\tfrac43,\ dz=\tfrac43$",
                            r"Revisa cuántas paredes hay en cada dirección: largo y ancho tienen dos, la profundidad solo el fondo."),
                    ],
                    "explicacion": r"Dos paredes en el largo y en el ancho ($2\cdot\tfrac23$) y solo el fondo en la profundidad.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto valen $V_x$, $V_y$ y $V_z$ en $(6,3,4)$?",
                    "opciones": [
                        ok(r"$V_x=12,\ V_y=24,\ V_z=18$"),
                        mal(r"$V_x=18,\ V_y=24,\ V_z=12$",
                            r"Cada derivada omite su propia variable: $V_x=yz$, $V_y=xz$, $V_z=xy$."),
                        mal(r"$V_x=6,\ V_y=3,\ V_z=4$",
                            r"Esas son las dimensiones, no las derivadas parciales."),
                        mal(r"$V_x=72,\ V_y=72,\ V_z=72$",
                            r"Evaluaste $V=xyz$ en lugar de sus derivadas parciales."),
                    ],
                    "explicacion": r"$V_x=yz=12$, $V_y=xz=24$ y $V_z=xy=18$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $dV=V_x\,dx+V_y\,dy+V_z\,dz$.",
                    "opciones": [
                        ok(r"$60$"),
                        mal(r"$72$",
                            r"El incremento en la profundidad es $\tfrac23$, no $\tfrac43$."),
                        mal(r"$48$",
                            r"Te faltó el tercer término $V_z\,dz$."),
                        mal(r"$54$",
                            r"Falta multiplicar cada derivada por su incremento."),
                    ],
                    "explicacion": r"$dV=12\cdot\tfrac43+24\cdot\tfrac43+18\cdot\tfrac23=16+32+12=60$ pulg$^3$.",
                },
                {
                    "pregunta": r"**Paso 4.** El volumen exacto de madera es $\approx 76.3$ pulg$^3$, mucho mayor que $dV$. ¿Por qué?",
                    "opciones": [
                        ok(r"Los incrementos no son pequeños frente a las dimensiones y la aproximación lineal pierde precisión"),
                        mal(r"La diferencial $dV$ siempre es igual a $\Delta V$",
                            r"$dV$ es una aproximación lineal: coincide con $\Delta V$ solo cuando los incrementos tienden a cero."),
                        mal(r"Se equivocó el cálculo del volumen interior",
                            r"El volumen interior no interviene en $dV$: la diferencia viene de la aproximación lineal."),
                        mal(r"Es normal aunque los incrementos sean muy pequeños",
                            r"Con incrementos muy pequeños, $dV$ y $\Delta V$ serían casi iguales."),
                    ],
                    "explicacion": r"Los incrementos ($\tfrac43$, $\tfrac43$, $\tfrac23$) son grandes comparados con $6$, $3$ y $4$.",
                },
            ],
        },
        {
            "id": "inc_3b",
            "nivel": 3,
            "enunciado": (r"La resistencia es $R=\dfrac{V}{I}$. Se mide $V=120\pm0.05$ voltios e $I=20\pm0.1$ amperios. "
                          r"Estima el error máximo de $R$ con la diferencial."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es la diferencial $dR$?",
                    "opciones": [
                        ok(r"$dR=\dfrac{1}{I}\,dV-\dfrac{V}{I^2}\,dI$"),
                        mal(r"$dR=\dfrac{1}{I}\,dV+\dfrac{V}{I^2}\,dI$",
                            r"La derivada de $V/I$ respecto a $I$ es negativa."),
                        mal(r"$dR=\dfrac{1}{I}\,dV-\dfrac{V}{I}\,dI$",
                            r"Al derivar $V\,I^{-1}$ respecto a $I$ el exponente queda $-2$: el denominador es $I^2$."),
                        mal(r"$dR=V\,dV-I\,dI$",
                            r"Calcula las derivadas parciales de $V/I$: $\partial R/\partial V$ y $\partial R/\partial I$."),
                    ],
                    "explicacion": r"$\dfrac{\partial R}{\partial V}=\dfrac1I$ y $\dfrac{\partial R}{\partial I}=-\dfrac{V}{I^2}$.",
                },
                {
                    "pregunta": r"**Paso 2.** Sustituye $V=120$ e $I=20$: ¿cuál es $dR$ con números?",
                    "opciones": [
                        ok(r"$dR=0.05\,dV-0.3\,dI$"),
                        mal(r"$dR=0.05\,dV-6\,dI$",
                            r"Usaste $V/I=6$ en lugar de $V/I^2$."),
                        mal(r"$dR=20\,dV-400\,dI$",
                            r"Invertiste las fracciones: $\tfrac1I$ con $I=20$ no es $20$."),
                        mal(r"$dR=0.05\,dV+0.3\,dI$",
                            r"Revisa el signo del segundo término."),
                    ],
                    "explicacion": r"$\tfrac{1}{20}=0.05$ y $\tfrac{120}{20^2}=0.3$.",
                },
                {
                    "pregunta": r"**Paso 3.** Con $|dV|\leq0.05$ y $|dI|\leq0.1$, ¿cuál es el error máximo $|dR|$?",
                    "opciones": [
                        ok(r"$0.0325\ \Omega$"),
                        mal(r"$0.0275\ \Omega$",
                            r"Restaste los aportes: el máximo se obtiene sumando los valores absolutos de cada término."),
                        mal(r"$0.03\ \Omega$",
                            r"Falta el aporte de $dV$."),
                        mal(r"$0.0025\ \Omega$",
                            r"Falta el aporte de $dI$."),
                    ],
                    "explicacion": r"$|dR|\leq0.05(0.05)+0.3(0.1)=0.0025+0.03=0.0325\ \Omega$.",
                },
            ],
        },
    ],

    # ==================================================================
    #  TEMA: Regla de la cadena
    # ==================================================================
    "Regla de la cadena": [

        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "cad_1a",
            "nivel": 1,
            "enunciado": r"Si $w=x^2y$, con $x=t^2$ e $y=t^3$, halla $\dfrac{dw}{dt}$ en $t=1$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es la regla de la cadena para $w(x(t),y(t))$?",
                    "opciones": [
                        ok(r"$\dfrac{dw}{dt}=\dfrac{\partial w}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial w}{\partial y}\dfrac{dy}{dt}$"),
                        mal(r"$\dfrac{dw}{dt}=\dfrac{\partial w}{\partial x}\dfrac{dy}{dt}+\dfrac{\partial w}{\partial y}\dfrac{dx}{dt}$",
                            r"Cada derivada parcial se multiplica por la derivada de su propia variable."),
                        mal(r"$\dfrac{dw}{dt}=\dfrac{\partial w}{\partial x}+\dfrac{\partial w}{\partial y}$",
                            r"Falta multiplicar por $\tfrac{dx}{dt}$ y $\tfrac{dy}{dt}$: cómo cambian $x$ e $y$ con $t$."),
                        mal(r"$\dfrac{dw}{dt}=\dfrac{\partial w}{\partial x}\dfrac{dx}{dt}\cdot\dfrac{\partial w}{\partial y}\dfrac{dy}{dt}$",
                            r"Los aportes de cada variable se suman, no se multiplican."),
                    ],
                    "explicacion": r"Cada variable aporta $\tfrac{\partial w}{\partial\,\cdot}\cdot\tfrac{d\,\cdot}{dt}$ y los aportes se suman.",
                },
                {
                    "pregunta": r"**Paso 2.** En $t=1$ (donde $x=1$, $y=1$): ¿cuánto valen $w_x,\ w_y,\ x',\ y'$?",
                    "opciones": [
                        ok(r"$2,\ 1,\ 2,\ 3$"),
                        mal(r"$1,\ 2,\ 2,\ 3$",
                            r"Cambiaste $w_x$ y $w_y$: $w_x=2xy$ y $w_y=x^2$."),
                        mal(r"$2,\ 1,\ 1,\ 1$",
                            r"Usaste $x(1)$ e $y(1)$ en lugar de sus derivadas $x'=2t$ e $y'=3t^2$."),
                        mal(r"$2,\ 2,\ 2,\ 3$",
                            r"$w_y$ es la derivada de $x^2y$ respecto a $y$: queda $x^2$, no $2x$."),
                    ],
                    "explicacion": r"$w_x=2xy=2$, $w_y=x^2=1$, $x'=2t=2$ e $y'=3t^2=3$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $\dfrac{dw}{dt}$ en $t=1$.",
                    "opciones": [
                        ok(r"$7$"),
                        mal(r"$4$",
                            r"Te faltó el segundo término."),
                        mal(r"$3$",
                            r"Te faltó el primer término."),
                        mal(r"$12$",
                            r"Los términos se suman, no se multiplican."),
                    ],
                    "explicacion": r"$\dfrac{dw}{dt}=2\cdot2+1\cdot3=7$.",
                },
            ],
        },
        {
            "id": "cad_1b",
            "nivel": 1,
            "enunciado": r"Si $w=x^2-y$, con $x=t+1$ e $y=t^2$, halla $\dfrac{dw}{dt}$ en $t=2$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** En $t=2$ (donde $x=3$, $y=4$): ¿cuánto valen $w_x$ y $w_y$?",
                    "opciones": [
                        ok(r"$w_x=6,\ w_y=-1$"),
                        mal(r"$w_x=6,\ w_y=1$",
                            r"Revisa el signo de $w_y$: el término es $-y$."),
                        mal(r"$w_x=3,\ w_y=-4$",
                            r"Esos son los valores de $x$ e $y$; falta derivar."),
                        mal(r"$w_x=2,\ w_y=-1$",
                            r"La derivada de $x^2$ es $2x$: evalúa con $x=3$."),
                    ],
                    "explicacion": r"$w_x=2x=6$ y $w_y=-1$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto valen $x'(2)$ e $y'(2)$?",
                    "opciones": [
                        ok(r"$x'=1,\ y'=4$"),
                        mal(r"$x'=3,\ y'=4$",
                            r"Esos son $x(2)$ e $y(2)$; falta derivar respecto a $t$."),
                        mal(r"$x'=1,\ y'=2$",
                            r"$y'=2t$: evalúa en $t=2$."),
                        mal(r"$x'=0,\ y'=4$",
                            r"La derivada de $t+1$ respecto a $t$ es $1$."),
                    ],
                    "explicacion": r"$x'=1$ e $y'=2t=4$ en $t=2$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $\dfrac{dw}{dt}=w_x\,x'+w_y\,y'$.",
                    "opciones": [
                        ok(r"$2$"),
                        mal(r"$10$",
                            r"Revisa el signo del segundo término: $w_y=-1$ es negativo."),
                        mal(r"$6$",
                            r"Te faltó el segundo término."),
                        mal(r"$-4$",
                            r"Te faltó el primer término."),
                    ],
                    "explicacion": r"$\dfrac{dw}{dt}=6\cdot1+(-1)\cdot4=2$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "cad_2a",
            "nivel": 2,
            "enunciado": r"Si $w=\dfrac{1}{u^2+v^2}$, con $u=\cos 2t$ y $v=\operatorname{sen}2t$, halla $\dfrac{dw}{dt}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale $\dfrac{\partial w}{\partial u}$?",
                    "opciones": [
                        ok(r"$\dfrac{-2u}{(u^2+v^2)^2}$"),
                        mal(r"$\dfrac{-2u}{u^2+v^2}$",
                            r"Al derivar $(u^2+v^2)^{-1}$ el exponente baja a $-2$: el denominador queda al cuadrado."),
                        mal(r"$\dfrac{2u}{(u^2+v^2)^2}$",
                            r"Revisa el signo: el exponente $-1$ baja con signo negativo."),
                        mal(r"$\dfrac{-u}{(u^2+v^2)^2}$",
                            r"Falta el factor $2$ de la derivada de $u^2$."),
                    ],
                    "explicacion": r"$w=(u^2+v^2)^{-1}\Rightarrow w_u=-\dfrac{2u}{(u^2+v^2)^2}$ (y $w_v$ igual con $v$).",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto valen $\dfrac{du}{dt}$ y $\dfrac{dv}{dt}$?",
                    "opciones": [
                        ok(r"$u'=-2\operatorname{sen}2t,\ v'=2\cos 2t$"),
                        mal(r"$u'=-\operatorname{sen}2t,\ v'=\cos 2t$",
                            r"Falta el factor $2$ de la derivada interna de $2t$."),
                        mal(r"$u'=-2\cos 2t,\ v'=2\operatorname{sen}2t$",
                            r"La derivada del coseno es seno (con signo) y la del seno es coseno: no se quedan en la misma función."),
                        mal(r"$u'=2\operatorname{sen}2t,\ v'=-2\cos 2t$",
                            r"Revisa los signos: $(\cos)'=-\operatorname{sen}$ y $(\operatorname{sen})'=+\cos$."),
                    ],
                    "explicacion": r"$u'=-2\operatorname{sen}2t$ y $v'=2\cos2t$.",
                },
                {
                    "pregunta": r"**Paso 3.** Combina con la regla de la cadena: ¿cuánto vale $\dfrac{dw}{dt}$?",
                    "opciones": [
                        ok(r"$0$"),
                        mal(r"$8\operatorname{sen}2t\cos2t$",
                            r"Revisa el signo del segundo término: $\partial w/\partial v$ también es negativo."),
                        mal(r"$1$",
                            r"Ese es el valor de $w$, no el de su derivada."),
                        mal(r"$-8\operatorname{sen}2t\cos2t$",
                            r"Revisa el signo del primer término: $\partial w/\partial u$ es negativo y $u'$ también."),
                    ],
                    "explicacion": r"Los dos términos se cancelan: $\dfrac{4\operatorname{sen}2t\cos2t-4\operatorname{sen}2t\cos2t}{(u^2+v^2)^2}=0$ (además $u^2+v^2=1$, así que $w$ es constante).",
                },
            ],
        },
        {
            "id": "cad_2b",
            "nivel": 2,
            "enunciado": r"Si $z=2xy$, con $x=s^2+t^2$ e $y=\dfrac{s}{t}$, halla $\dfrac{\partial z}{\partial s}$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto valen $z_x$ y $z_y$?",
                    "opciones": [
                        ok(r"$z_x=2y,\ z_y=2x$"),
                        mal(r"$z_x=2x,\ z_y=2y$",
                            r"Al derivar $2xy$ respecto a $x$ queda $2y$ ($y$ es constante)."),
                        mal(r"$z_x=y,\ z_y=x$",
                            r"El factor $2$ se conserva al derivar."),
                        mal(r"$z_x=2,\ z_y=2$",
                            r"Al derivar respecto a $x$, el factor $y$ se queda multiplicando."),
                    ],
                    "explicacion": r"$z_x=2y$ y $z_y=2x$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto valen $x_s$ e $y_s$ (derivadas respecto a $s$)?",
                    "opciones": [
                        ok(r"$x_s=2s,\ y_s=\dfrac1t$"),
                        mal(r"$x_s=2s+2t,\ y_s=\dfrac1t$",
                            r"Al derivar respecto a $s$, $t$ es constante: la derivada de $t^2$ es $0$."),
                        mal(r"$x_s=2s,\ y_s=1$",
                            r"$y=s/t$: al derivar respecto a $s$, el $t$ del denominador se conserva."),
                        mal(r"$x_s=2s,\ y_s=-\dfrac{s}{t^2}$",
                            r"Esa es la derivada respecto a $t$ ($y_t$). Aquí se deriva respecto a $s$."),
                    ],
                    "explicacion": r"$x_s=2s$ e $y_s=\tfrac1t$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $\dfrac{\partial z}{\partial s}=z_x\,x_s+z_y\,y_s$ en términos de $s$ y $t$.",
                    "opciones": [
                        ok(r"$\dfrac{6s^2+2t^2}{t}$"),
                        mal(r"$\dfrac{4s^2}{t}$",
                            r"Falta el aporte de $y$: el término $z_y\,y_s$."),
                        mal(r"$\dfrac{2s^2+2t^2}{t}$",
                            r"Falta el aporte de $x$: el término $z_x\,x_s$."),
                        mal(r"$\dfrac{6s^2-2t^2}{t}$",
                            r"Revisa el signo al sumar: los dos aportes son positivos."),
                    ],
                    "explicacion": r"$2\cdot\tfrac{s}{t}\cdot2s+2(s^2+t^2)\cdot\tfrac1t=\tfrac{4s^2}{t}+\tfrac{2s^2+2t^2}{t}=\tfrac{6s^2+2t^2}{t}$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "cad_3a",
            "nivel": 3,
            "enunciado": (r"El volumen de un cono es $V=\tfrac13\pi r^2h$. En cierto instante $r=20$ y $h=30$ pulg, "
                          r"con $\tfrac{dr}{dt}=1$ y $\tfrac{dh}{dt}=2$ pulg/s. ¿A qué rapidez cambia el volumen?"),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuáles son $V_r$ y $V_h$?",
                    "opciones": [
                        ok(r"$V_r=\tfrac23\pi rh,\ V_h=\tfrac13\pi r^2$"),
                        mal(r"$V_r=\tfrac13\pi r^2,\ V_h=\tfrac23\pi rh$",
                            r"Cambiaste el orden: $V_r$ es la derivada respecto a $r$."),
                        mal(r"$V_r=\tfrac13\pi h,\ V_h=\tfrac13\pi r^2$",
                            r"La derivada de $r^2$ es $2r$: el exponente baja y multiplica."),
                        mal(r"$V_r=\tfrac23\pi rh,\ V_h=\tfrac13\pi r$",
                            r"Al derivar respecto a $h$, el factor $r^2$ se conserva completo."),
                    ],
                    "explicacion": r"$V_r=\tfrac23\pi rh$ y $V_h=\tfrac13\pi r^2$.",
                },
                {
                    "pregunta": r"**Paso 2.** Evalúa en $r=20$, $h=30$: ¿cuánto valen $V_r$ y $V_h$?",
                    "opciones": [
                        ok(r"$V_r=400\pi,\ V_h=\tfrac{400\pi}{3}$"),
                        mal(r"$V_r=\tfrac{400\pi}{3},\ V_h=400\pi$",
                            r"Cambiaste el orden de los valores."),
                        mal(r"$V_r=200\pi,\ V_h=\tfrac{400\pi}{3}$",
                            r"Revisa $V_r=\tfrac23\pi rh$: $\tfrac23\cdot20\cdot30$."),
                        mal(r"$V_r=400\pi,\ V_h=400\pi$",
                            r"Revisa $V_h=\tfrac13\pi r^2$: no olvides el $\tfrac13$."),
                    ],
                    "explicacion": r"$V_r=\tfrac23\pi(20)(30)=400\pi$ y $V_h=\tfrac13\pi(20)^2=\tfrac{400\pi}{3}$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $\dfrac{dV}{dt}=V_r\dfrac{dr}{dt}+V_h\dfrac{dh}{dt}$.",
                    "opciones": [
                        ok(r"$\tfrac{2000\pi}{3}$ pulg$^3$/s"),
                        mal(r"$\tfrac{1600\pi}{3}$ pulg$^3$/s",
                            r"Falta multiplicar $V_h$ por $\tfrac{dh}{dt}=2$."),
                        mal(r"$\tfrac{800\pi}{3}$ pulg$^3$/s",
                            r"Te faltó el primer término $V_r\,\tfrac{dr}{dt}$."),
                        mal(r"$400\pi$ pulg$^3$/s",
                            r"Te faltó el segundo término $V_h\,\tfrac{dh}{dt}$."),
                    ],
                    "explicacion": r"$400\pi(1)+\tfrac{400\pi}{3}(2)=\tfrac{1200\pi+800\pi}{3}=\tfrac{2000\pi}{3}\approx2094.4$.",
                },
            ],
        },
        {
            "id": "cad_3b",
            "nivel": 3,
            "enunciado": (r"Si $z=3x^2+xy-2y^2+3x-y$, con $x=2u-3v$ e $y=u+v$, halla $\dfrac{\partial z}{\partial u}$ "
                          r"en términos de $u$ y $v$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto valen $z_x$ y $z_y$?",
                    "opciones": [
                        ok(r"$z_x=6x+y+3,\ z_y=x-4y-1$"),
                        mal(r"$z_x=6x+y,\ z_y=x-4y$",
                            r"Faltan los términos lineales $3x$ y $-y$ al derivar."),
                        mal(r"$z_x=x-4y-1,\ z_y=6x+y+3$",
                            r"Cambiaste el orden: $z_x$ es la derivada respecto a $x$."),
                        mal(r"$z_x=6x+y+3,\ z_y=x-2y-1$",
                            r"La derivada de $-2y^2$ respecto a $y$ es $-4y$."),
                    ],
                    "explicacion": r"$z_x=6x+y+3$ y $z_y=x-4y-1$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto valen $x_u$ e $y_u$?",
                    "opciones": [
                        ok(r"$x_u=2,\ y_u=1$"),
                        mal(r"$x_u=-3,\ y_u=1$",
                            r"Ese $-3$ es la derivada de $x$ respecto a $v$, no a $u$."),
                        mal(r"$x_u=1,\ y_u=2$",
                            r"Cambiaste los valores: $x=2u-3v$ da $x_u=2$."),
                        mal(r"$x_u=2u,\ y_u=u$",
                            r"Al derivar respecto a $u$ queda el coeficiente de $u$, sin la variable."),
                    ],
                    "explicacion": r"$x=2u-3v\Rightarrow x_u=2$ e $y=u+v\Rightarrow y_u=1$.",
                },
                {
                    "pregunta": r"**Paso 3.** Aplica $\dfrac{\partial z}{\partial u}=z_x\,x_u+z_y\,y_u$: ¿cuál es el resultado en $x$ e $y$?",
                    "opciones": [
                        ok(r"$13x-2y+5$"),
                        mal(r"$13x+2y+5$",
                            r"Revisa el signo: $2(y)+(-4y)=-2y$."),
                        mal(r"$12x+2y+6$",
                            r"Te faltó sumar el aporte de $z_y\,y_u$."),
                        mal(r"$x-4y-1$",
                            r"Te faltó el aporte de $z_x\,x_u$."),
                    ],
                    "explicacion": r"$2(6x+y+3)+1(x-4y-1)=13x-2y+5$.",
                },
                {
                    "pregunta": r"**Paso 4.** Sustituye $x=2u-3v$ e $y=u+v$: ¿cuál es $\dfrac{\partial z}{\partial u}$ en términos de $u$ y $v$?",
                    "opciones": [
                        ok(r"$24u-41v+5$"),
                        mal(r"$28u-37v+5$",
                            r"Revisa el signo de $-2y$ al sustituir $y=u+v$."),
                        mal(r"$24u-41v$",
                            r"No olvides la constante $+5$."),
                        mal(r"$26u-39v+5$",
                            r"Falta sustituir también el término $-2y$."),
                    ],
                    "explicacion": r"$13(2u-3v)-2(u+v)+5=24u-41v+5$.",
                },
            ],
        },
    ],

    # ==================================================================
    #  TEMA: Multiplicadores de Lagrange
    #  (se usa F = f + λ·g, con la restricción escrita como g = 0)
    # ==================================================================
    "Multiplicadores de Lagrange": [

        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "lag_1a",
            "nivel": 1,
            "enunciado": (r"Halla el mínimo de $f(x,y)=x^2+y^2$ sujeto a $3x+2y=6$. "
                          r"Usa $F=f+\lambda\,g$ con $g=3x+2y-6$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué sistema resulta de $F_x=0,\ F_y=0,\ F_\lambda=0$?",
                    "opciones": [
                        ok(r"$2x+3\lambda=0,\ \ 2y+2\lambda=0,\ \ 3x+2y-6=0$"),
                        mal(r"$2x+\lambda=0,\ \ 2y+\lambda=0,\ \ 3x+2y-6=0$",
                            r"Las derivadas de la restricción son sus coeficientes: $g_x=3$ y $g_y=2$."),
                        mal(r"$2x+3\lambda=0,\ \ 2y+2\lambda=0,\ \ 3x+2y=0$",
                            r"$F_\lambda=g$: la restricción completa es $3x+2y-6=0$."),
                        mal(r"$x+3\lambda=0,\ \ y+2\lambda=0,\ \ 3x+2y-6=0$",
                            r"La derivada de $x^2$ es $2x$ y la de $y^2$ es $2y$."),
                    ],
                    "explicacion": r"$F_x=2x+3\lambda$, $F_y=2y+2\lambda$ y $F_\lambda=3x+2y-6$.",
                },
                {
                    "pregunta": r"**Paso 2.** Despeja $\lambda$ en las dos primeras ecuaciones e iguálalas: ¿qué relación queda entre $x$ e $y$?",
                    "opciones": [
                        ok(r"$y=\tfrac23\,x$"),
                        mal(r"$y=\tfrac32\,x$",
                            r"Invertiste la relación: de $\lambda=-\tfrac{2x}{3}$ y $\lambda=-y$ sale $y$ en función de $x$."),
                        mal(r"$y=x$",
                            r"Los coeficientes de $\lambda$ son distintos ($3$ y $2$): $x$ e $y$ no quedan iguales."),
                        mal(r"$y=-\tfrac23\,x$",
                            r"Revisa el signo: las dos expresiones de $\lambda$ llevan el mismo signo."),
                    ],
                    "explicacion": r"$\lambda=-\tfrac{2x}{3}$ y $\lambda=-y$, así que $y=\tfrac23 x$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sustituye en $3x+2y=6$: ¿cuál es el punto y el valor mínimo de $f$?",
                    "opciones": [
                        ok(r"$\left(\tfrac{18}{13},\ \tfrac{12}{13}\right)$ con $f=\tfrac{36}{13}$"),
                        mal(r"$\left(\tfrac65,\ \tfrac65\right)$ con $f=\tfrac{72}{25}$",
                            r"Ese punto cumple la restricción, pero no cumple la relación entre $x$ e $y$ del paso 2."),
                        mal(r"$\left(\tfrac{18}{13},\ \tfrac{12}{13}\right)$ con $f=\tfrac{30}{13}$",
                            r"Sumaste las coordenadas: $f=x^2+y^2$ se evalúa con los cuadrados."),
                        mal(r"$\left(\tfrac{12}{13},\ \tfrac{18}{13}\right)$ con $f=\tfrac{36}{13}$",
                            r"Intercambiaste las coordenadas: $y=\tfrac23 x$ implica que $y<x$."),
                    ],
                    "explicacion": r"$3x+\tfrac43x=6\Rightarrow x=\tfrac{18}{13}$, $y=\tfrac{12}{13}$ y $f=\tfrac{324+144}{169}=\tfrac{36}{13}$.",
                },
            ],
        },
        {
            "id": "lag_1b",
            "nivel": 1,
            "enunciado": (r"Halla el extremo de $f(x,y)=3x^2+3y^2+5$ sujeto a $x-y=1$. "
                          r"Usa $F=f+\lambda\,g$ con $g=x-y-1$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué sistema resulta de $F_x=0,\ F_y=0,\ F_\lambda=0$?",
                    "opciones": [
                        ok(r"$6x+\lambda=0,\ \ 6y-\lambda=0,\ \ x-y-1=0$"),
                        mal(r"$6x+\lambda=0,\ \ 6y+\lambda=0,\ \ x-y-1=0$",
                            r"Para $g=x-y-1$ se tiene $g_y=-1$: el término de $\lambda$ en $F_y$ lleva signo negativo."),
                        mal(r"$3x+\lambda=0,\ \ 3y-\lambda=0,\ \ x-y-1=0$",
                            r"Al derivar $3x^2$ y $3y^2$ el exponente baja y multiplica: $6x$ y $6y$."),
                        mal(r"$6x+\lambda=0,\ \ 6y-\lambda=0,\ \ x-y=0$",
                            r"$F_\lambda=g$: la restricción completa es $x-y-1=0$."),
                    ],
                    "explicacion": r"$F_x=6x+\lambda$, $F_y=6y-\lambda$ y $F_\lambda=x-y-1$.",
                },
                {
                    "pregunta": r"**Paso 2.** Despeja $\lambda$ en las dos primeras ecuaciones e iguálalas: ¿qué relación queda?",
                    "opciones": [
                        ok(r"$y=-x$"),
                        mal(r"$y=x$",
                            r"$\lambda$ aparece con signos opuestos en las dos ecuaciones: revisa los signos."),
                        mal(r"$y=-6x$",
                            r"Los coeficientes de $x$ e $y$ son iguales ($6$): el factor $6$ se cancela."),
                        mal(r"$y=-\tfrac{x}{6}$",
                            r"Los coeficientes de $x$ e $y$ son iguales ($6$): el factor $6$ se cancela."),
                    ],
                    "explicacion": r"$\lambda=-6x$ y $\lambda=6y$, así que $y=-x$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sustituye en $x-y=1$: ¿cuál es el punto y el valor de $f$ en él?",
                    "opciones": [
                        ok(r"$\left(\tfrac12,\ -\tfrac12\right)$ con $f=\tfrac{13}{2}$"),
                        mal(r"$(1,\ 0)$ con $f=8$",
                            r"Ese punto cumple la restricción, pero no la relación $y=-x$."),
                        mal(r"$\left(\tfrac12,\ -\tfrac12\right)$ con $f=\tfrac32$",
                            r"No olvides sumar la constante $5$ de la función."),
                        mal(r"$\left(-\tfrac12,\ \tfrac12\right)$ con $f=\tfrac{13}{2}$",
                            r"Revisa el punto: no cumple $x-y=1$."),
                    ],
                    "explicacion": r"$x-(-x)=1\Rightarrow x=\tfrac12$, $y=-\tfrac12$ y $f=\tfrac34+\tfrac34+5=\tfrac{13}{2}$.",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Qué tipo de extremo condicionado es?",
                    "opciones": [
                        ok(r"Mínimo, porque $f$ es un paraboloide que se abre hacia arriba"),
                        mal(r"Máximo, porque $f$ es un paraboloide",
                            r"Este paraboloide se abre hacia arriba (coeficientes positivos), así que no tiene máximo."),
                        mal(r"Punto de silla",
                            r"Con $x^2$ e $y^2$ ambos positivos, la superficie no tiene forma de silla."),
                        mal(r"No se puede saber",
                            r"Se puede decidir por la forma de la superficie: $f=3x^2+3y^2+5\geq 5$."),
                    ],
                    "explicacion": r"$f=3x^2+3y^2+5$ se abre hacia arriba, así que el único punto crítico condicionado es un mínimo.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "lag_2a",
            "nivel": 2,
            "enunciado": (r"Halla los extremos de $z=6-4x-3y$ sujeta a $x^2+y^2=1$. "
                          r"Usa $F=z+\lambda\,(x^2+y^2-1)$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué sistema resulta de $F_x=0,\ F_y=0,\ F_\lambda=0$?",
                    "opciones": [
                        ok(r"$-4+2\lambda x=0,\ \ -3+2\lambda y=0,\ \ x^2+y^2-1=0$"),
                        mal(r"$-4+\lambda x=0,\ \ -3+\lambda y=0,\ \ x^2+y^2-1=0$",
                            r"La derivada de $x^2+y^2-1$ respecto a $x$ es $2x$ (y respecto a $y$, $2y$)."),
                        mal(r"$4+2\lambda x=0,\ \ 3+2\lambda y=0,\ \ x^2+y^2-1=0$",
                            r"Revisa los signos: la derivada de $-4x$ es $-4$ y la de $-3y$ es $-3$."),
                        mal(r"$-4+2\lambda x=0,\ \ -3+2\lambda y=0,\ \ x^2+y^2=0$",
                            r"$F_\lambda=g$: la restricción completa es $x^2+y^2-1=0$."),
                    ],
                    "explicacion": r"$F_x=-4+2\lambda x$, $F_y=-3+2\lambda y$ y $F_\lambda=x^2+y^2-1$.",
                },
                {
                    "pregunta": r"**Paso 2.** De las dos primeras ecuaciones, ¿qué relación hay entre $x$ e $y$?",
                    "opciones": [
                        ok(r"$y=\tfrac34\,x$"),
                        mal(r"$y=\tfrac43\,x$",
                            r"Invertiste la relación: $2\lambda=\tfrac4x$ y $2\lambda=\tfrac3y$."),
                        mal(r"$y=x$",
                            r"Los términos constantes son distintos ($4$ y $3$): $x$ e $y$ no quedan iguales."),
                        mal(r"$y=-\tfrac34\,x$",
                            r"Revisa el signo: $\tfrac4x=\tfrac3y$ no cambia de signo."),
                    ],
                    "explicacion": r"$2\lambda=\tfrac4x=\tfrac3y\Rightarrow y=\tfrac34x$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sustituye en $x^2+y^2=1$: ¿cuáles son los puntos críticos?",
                    "opciones": [
                        ok(r"$\left(\tfrac45,\tfrac35\right)$ y $\left(-\tfrac45,-\tfrac35\right)$"),
                        mal(r"$\left(\tfrac35,\tfrac45\right)$ y $\left(-\tfrac35,-\tfrac45\right)$",
                            r"Intercambiaste las coordenadas: $y=\tfrac34x$ implica que $y<x$."),
                        mal(r"$\left(\tfrac45,\tfrac35\right)$ y $\left(-\tfrac45,\tfrac35\right)$",
                            r"Con $y=\tfrac34 x$, si $x$ cambia de signo, $y$ también."),
                        mal(r"$\left(\tfrac{1}{\sqrt2},\tfrac{1}{\sqrt2}\right)$ y $\left(-\tfrac{1}{\sqrt2},-\tfrac{1}{\sqrt2}\right)$",
                            r"Esos puntos cumplen $x^2+y^2=1$ pero no la relación $y=\tfrac34 x$."),
                    ],
                    "explicacion": r"$x^2+\tfrac{9}{16}x^2=1\Rightarrow x=\pm\tfrac45$ y $y=\pm\tfrac35$.",
                },
                {
                    "pregunta": r"**Paso 4.** Evalúa $z$ en los dos puntos: ¿cuál es el mínimo y cuál el máximo?",
                    "opciones": [
                        ok(r"Mínimo $z=1$ en $\left(\tfrac45,\tfrac35\right)$; máximo $z=11$ en $\left(-\tfrac45,-\tfrac35\right)$"),
                        mal(r"Mínimo $z=11$ en $\left(\tfrac45,\tfrac35\right)$; máximo $z=1$ en $\left(-\tfrac45,-\tfrac35\right)$",
                            r"Intercambiaste el mínimo y el máximo: con $x,y$ positivos se resta más y $z$ baja."),
                        mal(r"Mínimo $z=1$ en $\left(\tfrac45,\tfrac35\right)$; máximo $z=6$ en $\left(-\tfrac45,-\tfrac35\right)$",
                            r"Evalúa bien el segundo punto: $6-4(-\tfrac45)-3(-\tfrac35)$ suma ambos términos."),
                        mal(r"Los dos puntos dan el mismo valor de $z$",
                            r"Evalúa cada punto por separado: uno resta y el otro suma los términos $-4x-3y$."),
                    ],
                    "explicacion": r"$z\left(\tfrac45,\tfrac35\right)=6-\tfrac{16}{5}-\tfrac95=1$ y $z\left(-\tfrac45,-\tfrac35\right)=6+\tfrac{16}{5}+\tfrac95=11$.",
                },
            ],
        },
        {
            "id": "lag_2b",
            "nivel": 2,
            "enunciado": (r"Halla las dimensiones de la caja rectangular **sin tapa** de volumen máximo si el área "
                          r"de su superficie (sin contar la tapa) es $12$. Usa $V=xyz$ y la restricción $xy+2xz+2yz=12$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Con $F=xyz+\lambda\,(xy+2xz+2yz-12)$, ¿cuáles son $F_x$, $F_y$ y $F_z$?",
                    "opciones": [
                        ok(r"$F_x=yz+\lambda(y+2z),\ \ F_y=xz+\lambda(x+2z),\ \ F_z=xy+\lambda(2x+2y)$"),
                        mal(r"$F_x=yz+\lambda y,\ \ F_y=xz+\lambda x,\ \ F_z=xy+\lambda(2x+2y)$",
                            r"Al derivar la restricción respecto a $x$ aparecen dos términos: $xy$ y $2xz$."),
                        mal(r"$F_x=yz+\lambda(y+2z),\ \ F_y=xz+\lambda(x+2z),\ \ F_z=xy+\lambda(x+y)$",
                            r"En $F_z$, los términos $2xz$ y $2yz$ conservan su factor $2$."),
                        mal(r"$F_x=xyz+\lambda(y+2z),\ \ F_y=xyz+\lambda(x+2z),\ \ F_z=xyz+\lambda(2x+2y)$",
                            r"Al derivar $xyz$ respecto a $x$ queda $yz$ (y análogamente en los demás)."),
                    ],
                    "explicacion": r"Cada derivada de $F$ suma la derivada de $xyz$ más $\lambda$ por la derivada de la restricción.",
                },
                {
                    "pregunta": r"**Paso 2.** Despejando $\lambda$ en las tres ecuaciones y comparándolas, ¿qué relaciones se obtienen?",
                    "opciones": [
                        ok(r"$x=y$ y $y=2z$"),
                        mal(r"$x=y$ y $z=2y$",
                            r"Invertiste la segunda relación: la altura es la dimensión más pequeña."),
                        mal(r"$x=2y$ y $y=z$",
                            r"Compara con cuidado: de las dos primeras ecuaciones sale una relación entre $x$ e $y$ sin factor $2$."),
                        mal(r"$x=y=z$",
                            r"Si las tres dimensiones fueran iguales, $F_x$ y $F_z$ no darían el mismo $\lambda$."),
                    ],
                    "explicacion": r"De $F_x$ y $F_y$ sale $x=y$; al combinar con $F_z$ resulta $y=2z$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sustituye $x=y=2z$ en la restricción: ¿qué valor de $z$ tiene sentido físico?",
                    "opciones": [
                        ok(r"$z=1$"),
                        mal(r"$z=-1$",
                            r"Una dimensión de la caja no puede ser negativa."),
                        mal(r"$z=2$",
                            r"Revisa la suma: $4z^2+4z^2+4z^2=12z^2$, y $12z^2=12$."),
                        mal(r"$z=\tfrac12$",
                            r"Revisa la suma: $4z^2+4z^2+4z^2=12z^2$, y $12z^2=12$."),
                    ],
                    "explicacion": r"$4z^2+4z^2+4z^2=12z^2=12\Rightarrow z=1$ (se descarta $z=-1$).",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Cuáles son las dimensiones y el volumen máximo?",
                    "opciones": [
                        ok(r"$x=y=2,\ z=1$ y $V=4$"),
                        mal(r"$x=y=1,\ z=2$ y $V=2$",
                            r"Invertiste las dimensiones: $x=y=2z$, con $z=1$."),
                        mal(r"$x=y=2,\ z=1$ y $V=12$",
                            r"El valor $12$ es el área de la superficie; el volumen es $V=xyz$."),
                        mal(r"$x=y=4,\ z=2$ y $V=32$",
                            r"Con $z=1$ y $x=y=2z$, las dimensiones de la base son $2$."),
                    ],
                    "explicacion": r"$x=y=2z=2$, $z=1$ y $V=2\cdot2\cdot1=4$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "lag_3a",
            "nivel": 3,
            "enunciado": (r"Una placa circular $x^2+y^2\leq1$ tiene temperatura $T(x,y)=x^2+2y^2-x$. "
                          r"Halla los puntos más caliente y más frío de la placa."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** En el **interior** ($x^2+y^2<1$), ¿cuál es el punto crítico y su temperatura?",
                    "opciones": [
                        ok(r"$\left(\tfrac12,\ 0\right)$ con $T=-\tfrac14$"),
                        mal(r"$\left(\tfrac12,\ 0\right)$ con $T=\tfrac14$",
                            r"Revisa la evaluación: $\left(\tfrac12\right)^2-\tfrac12$ es negativo."),
                        mal(r"$\left(-\tfrac12,\ 0\right)$ con $T=\tfrac34$",
                            r"Revisa $T_x=2x-1=0$: el signo de $x$."),
                        mal(r"$(0,\ 0)$ con $T=0$",
                            r"$(0,0)$ no cumple $T_x=2x-1=0$."),
                    ],
                    "explicacion": r"$T_x=2x-1=0$ y $T_y=4y=0$ dan $\left(\tfrac12,0\right)$, y $T=\tfrac14-\tfrac12=-\tfrac14$.",
                },
                {
                    "pregunta": r"**Paso 2.** En la **frontera** $x^2+y^2=1$, con $F=T+\lambda(x^2+y^2-1)$, la ecuación $F_y=4y+2\lambda y=0$ se factoriza como $y\,(4+2\lambda)=0$. ¿Qué casos hay?",
                    "opciones": [
                        ok(r"$y=0$ o $\lambda=-2$"),
                        mal(r"Solo $y=0$",
                            r"El otro factor, $4+2\lambda$, también puede anularse."),
                        mal(r"$y=0$ o $\lambda=2$",
                            r"Resuelve $4+2\lambda=0$: revisa el signo."),
                        mal(r"$\lambda=0$ o $y=-2$",
                            r"Factoriza: $y\,(4+2\lambda)=0$ da $y=0$ o $4+2\lambda=0$."),
                    ],
                    "explicacion": r"$y(4+2\lambda)=0\Rightarrow y=0$ o $\lambda=-2$. Cada caso da puntos candidatos.",
                },
                {
                    "pregunta": r"**Paso 3.** Caso $\lambda=-2$: ¿cuáles son los puntos de la frontera y su temperatura?",
                    "opciones": [
                        ok(r"$\left(-\tfrac12,\ \pm\tfrac{\sqrt3}{2}\right)$ con $T=\tfrac94$"),
                        mal(r"$\left(\tfrac12,\ \pm\tfrac{\sqrt3}{2}\right)$ con $T=\tfrac54$",
                            r"Con $\lambda=-2$, $F_x=2x-1-4x=-2x-1=0$: revisa el signo de $x$."),
                        mal(r"$\left(-\tfrac12,\ \pm\tfrac{\sqrt3}{2}\right)$ con $T=\tfrac74$",
                            r"Te faltó el término $-x$ al evaluar: con $x=-\tfrac12$ suma $\tfrac12$."),
                        mal(r"$\left(-\tfrac{\sqrt3}{2},\ \pm\tfrac12\right)$ con $T=\tfrac54+\tfrac{\sqrt3}{2}$",
                            r"Intercambiaste $x$ e $y$: de $-2x-1=0$ sale el valor de $x$."),
                    ],
                    "explicacion": r"$-2x-1=0\Rightarrow x=-\tfrac12$, $y=\pm\tfrac{\sqrt3}{2}$ y $T=\tfrac14+\tfrac32+\tfrac12=\tfrac94$.",
                },
                {
                    "pregunta": r"**Paso 4.** El caso $y=0$ en la frontera da $(1,0)$ con $T=0$ y $(-1,0)$ con $T=2$. Comparando todos los candidatos, ¿cuáles son el más caliente y el más frío?",
                    "opciones": [
                        ok(r"Más caliente: $\left(-\tfrac12,\pm\tfrac{\sqrt3}{2}\right)$ con $\tfrac94$; más frío: $\left(\tfrac12,0\right)$ con $-\tfrac14$"),
                        mal(r"Más caliente: $(-1,0)$ con $2$; más frío: $\left(\tfrac12,0\right)$ con $-\tfrac14$",
                            r"Compara: $\tfrac94=2.25$ es mayor que $2$."),
                        mal(r"Más caliente: $\left(-\tfrac12,\pm\tfrac{\sqrt3}{2}\right)$ con $\tfrac94$; más frío: $(1,0)$ con $0$",
                            r"Compara con el punto interior: su temperatura $-\tfrac14$ es menor que $0$."),
                        mal(r"Más caliente: $\left(\tfrac12,0\right)$ con $-\tfrac14$; más frío: $\left(-\tfrac12,\pm\tfrac{\sqrt3}{2}\right)$ con $\tfrac94$",
                            r"Invertiste el más caliente y el más frío: la temperatura mayor es la más caliente."),
                    ],
                    "explicacion": r"Candidatos: $-\tfrac14,\ 0,\ 2,\ \tfrac94$. El mayor es $\tfrac94$ y el menor es $-\tfrac14$.",
                },
            ],
        },
        {
            "id": "lag_3b",
            "nivel": 3,
            "enunciado": (r"Un recipiente cilíndrico cerrado tiene capacidad de $2$ litros ($2\ \text{dm}^3$). "
                          r"Halla el radio $r$ y la altura $h$ que usan la **mínima cantidad de material** (área total). "
                          r"Usa $F=2\pi rh+2\pi r^2+\lambda\,(\pi r^2h-2)$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué sistema resulta de $F_r=0,\ F_h=0,\ F_\lambda=0$?",
                    "opciones": [
                        ok(r"$2\pi h+4\pi r+2\lambda\pi rh=0,\ \ 2\pi r+\lambda\pi r^2=0,\ \ \pi r^2h-2=0$"),
                        mal(r"$2\pi h+2\pi r+2\lambda\pi rh=0,\ \ 2\pi r+\lambda\pi r^2=0,\ \ \pi r^2h-2=0$",
                            r"La derivada de $2\pi r^2$ respecto a $r$ es $4\pi r$."),
                        mal(r"$2\pi h+4\pi r+2\lambda\pi rh=0,\ \ 2\pi r+2\lambda\pi rh=0,\ \ \pi r^2h-2=0$",
                            r"$F_h$ se deriva respecto a $h$: de $\pi r^2h$ queda $\pi r^2$."),
                        mal(r"$2\pi h+4\pi r+2\lambda\pi rh=0,\ \ 2\pi r+\lambda\pi r^2=0,\ \ \pi r^2h=0$",
                            r"$F_\lambda=g$: la restricción completa es $\pi r^2h-2=0$."),
                    ],
                    "explicacion": r"$F_r=2\pi h+4\pi r+2\lambda\pi rh$, $F_h=2\pi r+\lambda\pi r^2$ y $F_\lambda=\pi r^2h-2$.",
                },
                {
                    "pregunta": r"**Paso 2.** De $F_h=0$ se obtiene $\lambda=-\tfrac{2}{r}$. Al sustituir en $F_r=0$, ¿qué relación queda entre $h$ y $r$?",
                    "opciones": [
                        ok(r"$h=2r$"),
                        mal(r"$r=2h$",
                            r"Invertiste la relación: al sustituir $\lambda$ queda $4\pi r-2\pi h=0$."),
                        mal(r"$h=r$",
                            r"Revisa la sustitución: $2\lambda\pi rh$ con $\lambda=-\tfrac2r$ vale $-4\pi h$."),
                        mal(r"$h=\pi r$",
                            r"El $\pi$ aparece en todos los términos y se cancela."),
                    ],
                    "explicacion": r"$2\pi h+4\pi r-4\pi h=0\Rightarrow 4\pi r=2\pi h\Rightarrow h=2r$.",
                },
                {
                    "pregunta": r"**Paso 3.** Sustituye $h=2r$ en $\pi r^2h=2$: ¿cuáles son $r$ y $h$?",
                    "opciones": [
                        ok(r"$r=\pi^{-1/3},\ \ h=2\pi^{-1/3}$"),
                        mal(r"$r=1,\ \ h=2$",
                            r"Al sustituir queda $2\pi r^3=2$: no olvides el $\pi$."),
                        mal(r"$r=2\pi^{-1/3},\ \ h=\pi^{-1/3}$",
                            r"Invertiste los valores: $h=2r$, no $r=2h$."),
                        mal(r"$r=\pi^{-1/3},\ \ h=\pi^{-1/3}$",
                            r"Recuerda la relación del paso 2: $h$ es el doble de $r$."),
                    ],
                    "explicacion": r"$\pi r^2(2r)=2\Rightarrow r^3=\tfrac1\pi\Rightarrow r=\pi^{-1/3}$ y $h=2r$.",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Cuál es el área mínima $A=2\pi rh+2\pi r^2$?",
                    "opciones": [
                        ok(r"$6\sqrt[3]{\pi}\ \text{dm}^2$"),
                        mal(r"$4\sqrt[3]{\pi}\ \text{dm}^2$",
                            r"Te faltaron las dos tapas: $2\pi r^2$."),
                        mal(r"$6\pi\ \text{dm}^2$",
                            r"Ese valor sale con $r=1$, no con $r=\pi^{-1/3}$."),
                        mal(r"$12\sqrt[3]{\pi}\ \text{dm}^2$",
                            r"Revisa la suma con $h=2r$: $A=4\pi r^2+2\pi r^2=6\pi r^2$."),
                    ],
                    "explicacion": r"$A=6\pi r^2=6\pi\cdot\pi^{-2/3}=6\pi^{1/3}\approx8.79\ \text{dm}^2$.",
                },
            ],
        },
    ],

    # =====================================================================
    # TEMA NUEVO (Semana 7): cambio de variable en integrales dobles
    # =====================================================================
    "Cambio de variable: polares y Jacobiano": [
        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "cam_1a",
            "nivel": 1,
            "enunciado": r"Evalúa $\iint_R (x^2+y^2)\,dA$, donde $R$ es el disco $x^2+y^2\leq4$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cómo se describe $R$ en coordenadas polares?",
                    "opciones": [
                        ok(r"$0\leq r\leq2,\ \ 0\leq\theta\leq2\pi$"),
                        mal(r"$0\leq r\leq4,\ \ 0\leq\theta\leq2\pi$",
                            r"Como $x^2+y^2=r^2$, la condición $x^2+y^2\leq4$ es $r^2\leq4$, o sea $r\leq2$."),
                        mal(r"$0\leq r\leq2,\ \ 0\leq\theta\leq\pi$",
                            r"Un disco completo da la vuelta entera: $\theta$ llega hasta $2\pi$ (hasta $\pi$ sería solo un semidisco)."),
                        mal(r"$0\leq r\leq2,\ \ 0\leq\theta\leq\tfrac\pi2$",
                            r"Ese rango describe solo el primer cuadrante. El disco ocupa los cuatro."),
                    ],
                    "explicacion": r"$x^2+y^2=r^2\leq4\Rightarrow r\leq2$, y el disco completo recorre $\theta$ de $0$ a $2\pi$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿En qué integral iterada se convierte? (recuerda que $dA=r\,dr\,d\theta$)",
                    "opciones": [
                        ok(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r^3\,dr\,d\theta$"),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r^2\,dr\,d\theta$",
                            r"Te faltó el Jacobiano: $dA=r\,dr\,d\theta$, así que el integrando es $r^2\cdot r$."),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r^4\,dr\,d\theta$",
                            r"$x^2+y^2$ ya es $r^2$ y el Jacobiano aporta un solo $r$: en total $r^3$, no $r^4$."),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^2 r\,dr\,d\theta$",
                            r"El integrando $x^2+y^2$ se convierte en $r^2$, no en $r$; y todavía falta el $r$ del Jacobiano."),
                    ],
                    "explicacion": r"$(x^2+y^2)\,dA=r^2\cdot r\,dr\,d\theta=r^3\,dr\,d\theta$.",
                },
                {
                    "pregunta": r"**Paso 3.** Evalúa la integral.",
                    "opciones": [
                        ok(r"$8\pi$"),
                        mal(r"$\tfrac{16\pi}{3}$",
                            r"Eso sale de integrar $r^2$: olvidaste el $r$ del Jacobiano."),
                        mal(r"$4\pi$",
                            r"Integraste $\theta$ solo de $0$ a $\pi$, y eso da la mitad."),
                        mal(r"$32\pi$",
                            r"$\int r^3\,dr=\tfrac{r^4}{4}$: no olvides dividir entre $4$."),
                    ],
                    "explicacion": r"$\int_0^2 r^3\,dr=4$ y $\int_0^{2\pi}d\theta=2\pi$, así que el resultado es $8\pi$.",
                },
            ],
        },
        {
            "id": "cam_1b",
            "nivel": 1,
            "enunciado": r"Evalúa $\displaystyle\int_0^2\!\!\int_0^{\sqrt{4-y^2}}\sqrt{x^2+y^2}\,dx\,dy$ pasando a polares.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Observa los límites: ¿qué región es y cómo se describe en polares?",
                    "opciones": [
                        ok(r"Cuarto de disco del primer cuadrante: $0\leq r\leq2,\ \ 0\leq\theta\leq\tfrac\pi2$"),
                        mal(r"Cuarto de disco: $0\leq r\leq4,\ \ 0\leq\theta\leq\tfrac\pi2$",
                            r"El límite $x=\sqrt{4-y^2}$ equivale a $x^2+y^2=4$, o sea $r=2$ (no $4$)."),
                        mal(r"Semidisco derecho: $0\leq r\leq2,\ \ -\tfrac\pi2\leq\theta\leq\tfrac\pi2$",
                            r"Ese semidisco incluye $y<0$. Aquí $y$ va de $0$ a $2$, así que solo hay primer cuadrante."),
                        mal(r"Semidisco superior: $0\leq r\leq2,\ \ 0\leq\theta\leq\pi$",
                            r"Eso incluiría $x<0$. Aquí $x$ empieza en $0$: solo hay primer cuadrante."),
                    ],
                    "explicacion": r"$x\geq0$, $y\geq0$ y $x^2+y^2\leq4$: el cuarto de disco de radio $2$ en el primer cuadrante.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuál es la integral en polares?",
                    "opciones": [
                        ok(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 r^2\,dr\,d\theta$"),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 r\,dr\,d\theta$",
                            r"Te faltó el Jacobiano: $\sqrt{x^2+y^2}=r$ y además $dA=r\,dr\,d\theta$."),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 r^3\,dr\,d\theta$",
                            r"La raíz de $x^2+y^2=r^2$ es $r$, no $r^2$. Con el Jacobiano queda $r\cdot r=r^2$."),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 r^2\sin\theta\,dr\,d\theta$",
                            r"No aparece ningún seno: $\sqrt{x^2+y^2}=r$ depende solo de $r$."),
                    ],
                    "explicacion": r"$\sqrt{x^2+y^2}\,dA=r\cdot r\,dr\,d\theta=r^2\,dr\,d\theta$.",
                },
                {
                    "pregunta": r"**Paso 3.** Evalúa la integral.",
                    "opciones": [
                        ok(r"$\tfrac{4\pi}{3}$"),
                        mal(r"$\tfrac83$",
                            r"Te faltó integrar en $\theta$: multiplica por $\tfrac\pi2$."),
                        mal(r"$\pi$",
                            r"Eso sale de integrar $r$ (sin Jacobiano): $\int_0^2 r\,dr=2$ y $2\cdot\tfrac\pi2=\pi$."),
                        mal(r"$\tfrac{16\pi}{3}$",
                            r"Usaste $\theta$ de $0$ a $2\pi$, pero la región es solo un cuarto de disco."),
                    ],
                    "explicacion": r"$\int_0^2 r^2\,dr=\tfrac83$ y $\int_0^{\pi/2}d\theta=\tfrac\pi2$, así que el resultado es $\tfrac{4\pi}{3}$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "cam_2a",
            "nivel": 2,
            "enunciado": r"Evalúa $\displaystyle\iint_R (x^2+y^2)\,dA$, donde $R$ es el disco $x^2+y^2\leq2x$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cómo queda la frontera $x^2+y^2=2x$ en polares?",
                    "opciones": [
                        ok(r"$r=2\cos\theta$"),
                        mal(r"$r=2$",
                            r"Al sustituir, $r^2=2r\cos\theta$: el $\cos\theta$ no desaparece. Al dividir entre $r$ queda $r=2\cos\theta$."),
                        mal(r"$r=2\sin\theta$",
                            r"A la derecha aparece $2x$, y $x=r\cos\theta$. Con $\sin\theta$ sería la circunferencia $x^2+y^2=2y$."),
                        mal(r"$r=\cos\theta$",
                            r"Al dividir $r^2=2r\cos\theta$ entre $r$ queda $r=2\cos\theta$: no pierdas el $2$."),
                    ],
                    "explicacion": r"$r^2=2r\cos\theta\Rightarrow r=2\cos\theta$ (circunferencia de centro $(1,0)$ y radio $1$).",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Qué valores recorre $\theta$ para cubrir el disco completo?",
                    "opciones": [
                        ok(r"$-\tfrac\pi2\leq\theta\leq\tfrac\pi2$"),
                        mal(r"$0\leq\theta\leq2\pi$",
                            r"Para $\theta$ entre $\tfrac\pi2$ y $\tfrac{3\pi}{2}$ el valor $2\cos\theta$ es negativo y $r$ no puede serlo. El disco está a la derecha del origen."),
                        mal(r"$0\leq\theta\leq\pi$",
                            r"Entre $\tfrac\pi2$ y $\pi$ el coseno es negativo: ahí no hay disco."),
                        mal(r"$0\leq\theta\leq\tfrac\pi2$",
                            r"Eso es solo la mitad superior del disco. Se extiende también hacia $y<0$."),
                    ],
                    "explicacion": r"El disco queda a la derecha del origen y es tangente al eje $y$: $\theta$ va de $-\tfrac\pi2$ a $\tfrac\pi2$.",
                },
                {
                    "pregunta": r"**Paso 3.** Pasa el integrando y $dA$ a polares y resuelve la integral en $r$: ¿qué queda en función de $\theta$?",
                    "opciones": [
                        ok(r"$4\cos^4\theta$"),
                        mal(r"$2\cos^2\theta$",
                            r"Integraste $r$, pero el integrando es $r^2\cdot r=r^3$."),
                        mal(r"$\tfrac83\cos^3\theta$",
                            r"Integraste $r^2$: olvidaste el $r$ del Jacobiano. El integrando es $r^3$."),
                        mal(r"$16\cos^4\theta$",
                            r"$\int r^3\,dr=\tfrac{r^4}{4}$: no olvides dividir entre $4$, o sea $\tfrac{(2\cos\theta)^4}{4}$."),
                    ],
                    "explicacion": r"$\int_0^{2\cos\theta}r^3\,dr=\tfrac{(2\cos\theta)^4}{4}=4\cos^4\theta$.",
                },
                {
                    "pregunta": r"**Paso 4.** Integra en $\theta$: ¿cuánto vale la integral?",
                    "opciones": [
                        ok(r"$\tfrac{3\pi}{2}$"),
                        mal(r"$\tfrac{3\pi}{4}$",
                            r"Integraste $\theta$ solo de $0$ a $\tfrac\pi2$: eso da la mitad."),
                        mal(r"$3\pi$",
                            r"Usaste $\theta$ de $0$ a $2\pi$, pero el disco solo existe para $-\tfrac\pi2\leq\theta\leq\tfrac\pi2$."),
                        mal(r"$\tfrac{3\pi}{8}$",
                            r"Olvidaste el factor $4$: $\int_{-\pi/2}^{\pi/2}\cos^4\theta\,d\theta=\tfrac{3\pi}{8}$, y hay que multiplicarlo por $4$."),
                    ],
                    "explicacion": r"$\int_{-\pi/2}^{\pi/2}4\cos^4\theta\,d\theta=4\cdot\tfrac{3\pi}{8}=\tfrac{3\pi}{2}$.",
                },
            ],
        },
        {
            "id": "cam_2b",
            "nivel": 2,
            "enunciado": r"Evalúa $\displaystyle\iint_R y\,dA$, donde $R$ es la mitad superior del anillo $1\leq x^2+y^2\leq4$, con $y\geq0$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cómo se describe $R$ en polares?",
                    "opciones": [
                        ok(r"$1\leq r\leq2,\ \ 0\leq\theta\leq\pi$"),
                        mal(r"$0\leq r\leq2,\ \ 0\leq\theta\leq\pi$",
                            r"Es un anillo: el hueco central hace que $r$ empiece en $1$, no en $0$."),
                        mal(r"$1\leq r\leq4,\ \ 0\leq\theta\leq\pi$",
                            r"$x^2+y^2\leq4$ significa $r^2\leq4$, o sea $r\leq2$."),
                        mal(r"$1\leq r\leq2,\ \ 0\leq\theta\leq\tfrac\pi2$",
                            r"$y\geq0$ incluye el primer y el segundo cuadrante: $\theta$ llega hasta $\pi$."),
                    ],
                    "explicacion": r"$1\leq r^2\leq4\Rightarrow1\leq r\leq2$, y $y\geq0$ corresponde a $0\leq\theta\leq\pi$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cómo queda $y\,dA$ en polares?",
                    "opciones": [
                        ok(r"$r^2\sin\theta\,dr\,d\theta$"),
                        mal(r"$r\sin\theta\,dr\,d\theta$",
                            r"Te faltó el Jacobiano: $y\,dA=(r\sin\theta)\cdot r\,dr\,d\theta$."),
                        mal(r"$r^2\cos\theta\,dr\,d\theta$",
                            r"$y=r\sin\theta$. El coseno corresponde a $x$."),
                        mal(r"$r^3\sin\theta\,dr\,d\theta$",
                            r"$y=r\sin\theta$ aporta un $r$ y el Jacobiano otro: en total $r^2$."),
                    ],
                    "explicacion": r"$y=r\sin\theta$ y $dA=r\,dr\,d\theta$, por lo que $y\,dA=r^2\sin\theta\,dr\,d\theta$.",
                },
                {
                    "pregunta": r"**Paso 3.** Evalúa $\displaystyle\int_0^\pi\!\!\int_1^2 r^2\sin\theta\,dr\,d\theta$.",
                    "opciones": [
                        ok(r"$\tfrac{14}{3}$"),
                        mal(r"$\tfrac73$",
                            r"Usaste $\theta$ de $0$ a $\tfrac\pi2$: la región llega hasta $\pi$."),
                        mal(r"$3$",
                            r"Eso sale de integrar $r\sin\theta$ (sin Jacobiano): $\int_1^2 r\,dr=\tfrac32$ y $\int_0^\pi\sin\theta\,d\theta=2$."),
                        mal(r"$0$",
                            r"Eso pasaría con $\theta$ de $0$ a $2\pi$ (el seno se cancela). La región es solo la mitad superior."),
                    ],
                    "explicacion": r"$\int_1^2r^2\,dr=\tfrac73$ y $\int_0^\pi\sin\theta\,d\theta=2$, así que el resultado es $\tfrac{14}{3}$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "cam_3a",
            "nivel": 3,
            "enunciado": (r"Evalúa $\displaystyle\iint_R (x^2-y^2)\,dA$, donde $R$ está limitada por $x+y=1$, $x+y=3$, "
                          r"$x-y=0$ y $x-y=2$. Usa el cambio $u=x+y$, $v=x-y$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** Despeja $x$ e $y$ en términos de $u$ y $v$.",
                    "opciones": [
                        ok(r"$x=\tfrac{u+v}{2},\ \ y=\tfrac{u-v}{2}$"),
                        mal(r"$x=u+v,\ \ y=u-v$",
                            r"Al sumar, $u+v=2x$, no $x$: falta dividir entre $2$."),
                        mal(r"$x=\tfrac{u-v}{2},\ \ y=\tfrac{u+v}{2}$",
                            r"Al restar, $u-v=2y$ (no $2x$): están intercambiadas."),
                        mal(r"$x=\tfrac{u+v}{2},\ \ y=\tfrac{v-u}{2}$",
                            r"$u-v=(x+y)-(x-y)=2y$, así que $y=\tfrac{u-v}{2}$ (cuidado con el signo)."),
                    ],
                    "explicacion": r"$u+v=2x$ y $u-v=2y$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto vale $\left|\dfrac{\partial(x,y)}{\partial(u,v)}\right|$?",
                    "opciones": [
                        ok(r"$\tfrac12$"),
                        mal(r"$2$",
                            r"Calculaste el determinante al revés: $\partial(u,v)/\partial(x,y)=-2$. En la integral va $\partial(x,y)/\partial(u,v)$."),
                        mal(r"$-\tfrac12$",
                            r"El determinante sí da $-\tfrac12$, pero en el cambio de variable se usa su valor absoluto."),
                        mal(r"$\tfrac14$",
                            r"Te faltó restar el segundo producto: $\tfrac12\cdot\left(-\tfrac12\right)-\tfrac12\cdot\tfrac12=-\tfrac12$."),
                    ],
                    "explicacion": r"$x_uy_v-x_vy_u=\tfrac12\cdot\left(-\tfrac12\right)-\tfrac12\cdot\tfrac12=-\tfrac12$, y se usa $|J|=\tfrac12$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la integral en $u,v$ (región e integrando)?",
                    "opciones": [
                        ok(r"$\displaystyle\int_0^2\!\!\int_1^3 uv\cdot\tfrac12\,du\,dv$"),
                        mal(r"$\displaystyle\int_0^2\!\!\int_1^3 (u^2-v^2)\cdot\tfrac12\,du\,dv$",
                            r"$x^2-y^2=(x+y)(x-y)=uv$. No se cambia $x$ por $u$ y $y$ por $v$: $u$ y $v$ son otras combinaciones."),
                        mal(r"$\displaystyle\int_0^2\!\!\int_1^3 uv\,du\,dv$",
                            r"Falta multiplicar por $|J|=\tfrac12$: $dA=|J|\,du\,dv$."),
                        mal(r"$\displaystyle\int_0^1\!\!\int_1^3 uv\cdot\tfrac12\,du\,dv$",
                            r"$x-y$ va de $0$ a $2$, así que $v$ llega hasta $2$ (no $1$)."),
                    ],
                    "explicacion": r"$R'$: $1\leq u\leq3$, $0\leq v\leq2$; además $x^2-y^2=uv$ y $dA=\tfrac12\,du\,dv$.",
                },
                {
                    "pregunta": r"**Paso 4.** Evalúa la integral.",
                    "opciones": [
                        ok(r"$4$"),
                        mal(r"$8$",
                            r"Olvidaste multiplicar por $|J|=\tfrac12$."),
                        mal(r"$2$",
                            r"Usaste $|J|=\tfrac14$: te faltó un sumando en el determinante."),
                        mal(r"$16$",
                            r"Usaste $|J|=2$, el determinante inverso."),
                    ],
                    "explicacion": r"$\tfrac12\left(\int_1^3u\,du\right)\left(\int_0^2v\,dv\right)=\tfrac12\cdot4\cdot2=4$.",
                },
            ],
        },
        {
            "id": "cam_3b",
            "nivel": 3,
            "enunciado": (r"Evalúa $\displaystyle\iint_R\left(\tfrac{x^2}{4}+\tfrac{y^2}{9}\right)dA$, "
                          r"donde $R$ es la región $\tfrac{x^2}{4}+\tfrac{y^2}{9}\leq1$."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Qué cambio de variable simplifica la región?",
                    "opciones": [
                        ok(r"$x=2r\cos\theta,\ \ y=3r\sin\theta$, con $0\leq r\leq1,\ 0\leq\theta\leq2\pi$"),
                        mal(r"$x=4r\cos\theta,\ \ y=9r\sin\theta$, con $0\leq r\leq1,\ 0\leq\theta\leq2\pi$",
                            r"Los semiejes son $2$ y $3$ (las raíces de $4$ y $9$), no $4$ y $9$."),
                        mal(r"$x=3r\cos\theta,\ \ y=2r\sin\theta$, con $0\leq r\leq1,\ 0\leq\theta\leq2\pi$",
                            r"Los semiejes están intercambiados: $x$ lleva el $2$ (de $x^2/4$) y $y$ lleva el $3$."),
                        mal(r"$x=2r\cos\theta,\ \ y=3r\sin\theta$, con $0\leq r\leq2,\ 0\leq\theta\leq2\pi$",
                            r"Con este cambio $\tfrac{x^2}{4}+\tfrac{y^2}{9}=r^2$, así que la frontera es $r=1$ (no $2$)."),
                    ],
                    "explicacion": r"$\tfrac{x^2}{4}+\tfrac{y^2}{9}=r^2\cos^2\theta+r^2\sin^2\theta=r^2\leq1$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto vale el Jacobiano $\dfrac{\partial(x,y)}{\partial(r,\theta)}$?",
                    "opciones": [
                        ok(r"$6r$"),
                        mal(r"$r$",
                            r"Ese es el Jacobiano de las polares simples. Aquí las escalas $2$ y $3$ también multiplican: $2\cdot3\cdot r$."),
                        mal(r"$6$",
                            r"Te faltó el factor $r$: el determinante da $6r\cos^2\theta+6r\sin^2\theta=6r$."),
                        mal(r"$5r$",
                            r"Es el producto de las escalas, $2\cdot3$, no la suma."),
                    ],
                    "explicacion": r"$J=(2\cos\theta)(3r\cos\theta)-(-2r\sin\theta)(3\sin\theta)=6r(\cos^2\theta+\sin^2\theta)=6r$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es la integral en $r,\theta$?",
                    "opciones": [
                        ok(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1 r^2\cdot6r\,dr\,d\theta$"),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1 r^2\cdot r\,dr\,d\theta$",
                            r"Usaste el Jacobiano de las polares simples. Aquí es $6r$."),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1 r^2\cdot6\,dr\,d\theta$",
                            r"Falta el factor $r$ del Jacobiano: es $6r$, no $6$."),
                        mal(r"$\displaystyle\int_0^{2\pi}\!\!\int_0^1 (4r^2\cos^2\theta+9r^2\sin^2\theta)\cdot6r\,dr\,d\theta$",
                            r"Al sustituir, $\tfrac{x^2}{4}=\tfrac{4r^2\cos^2\theta}{4}=r^2\cos^2\theta$: el $4$ se cancela (y el $9$ también)."),
                    ],
                    "explicacion": r"El integrando $\tfrac{x^2}{4}+\tfrac{y^2}{9}$ se vuelve $r^2$ y $dA=6r\,dr\,d\theta$.",
                },
                {
                    "pregunta": r"**Paso 4.** Evalúa la integral.",
                    "opciones": [
                        ok(r"$3\pi$"),
                        mal(r"$12\pi$",
                            r"$\int_0^1 6r^3\,dr=\tfrac{6r^4}{4}$: te faltó dividir entre $4$."),
                        mal(r"$\tfrac\pi2$",
                            r"Eso sale con Jacobiano $r$ en vez de $6r$: te faltó el factor $6$."),
                        mal(r"$4\pi$",
                            r"Eso sale con Jacobiano $6$ (sin $r$): el integrando correcto es $6r^3$."),
                    ],
                    "explicacion": r"$\int_0^1 6r^3\,dr=\tfrac32$ y $\int_0^{2\pi}d\theta=2\pi$, así que el resultado es $3\pi$.",
                },
            ],
        },
    ],

    # =====================================================================
    # TEMA NUEVO (Semana 8): masa y centro de masa de láminas
    # =====================================================================
    "Masa y centro de masa de láminas": [
        # ---------------------------------------------------------- NIVEL 1
        {
            "id": "masa_1a",
            "nivel": 1,
            "enunciado": r"Una lámina rectangular ocupa $0\leq x\leq4,\ 0\leq y\leq3$, con densidad $\rho(x,y)=y+1$. Halla su centro de masa.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale la masa $M=\iint_R\rho\,dA$?",
                    "opciones": [
                        ok(r"$30$"),
                        mal(r"$12$",
                            r"Ese es el área del rectángulo. La masa se obtiene integrando la densidad $\rho=y+1$."),
                        mal(r"$18$",
                            r"Usaste $\rho=y$. La densidad es $y+1$: no pierdas el $+1$."),
                        mal(r"$\tfrac{15}{2}$",
                            r"Integraste solo en $y$. Falta integrar en $x$ (multiplicar por $4$)."),
                    ],
                    "explicacion": r"$M=\int_0^4\!\int_0^3(y+1)\,dy\,dx=4\cdot\tfrac{15}{2}=30$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula los momentos estáticos $M_x=\iint y\rho\,dA$ y $M_y=\iint x\rho\,dA$.",
                    "opciones": [
                        ok(r"$M_x=54,\ \ M_y=60$"),
                        mal(r"$M_x=60,\ \ M_y=54$",
                            r"Están intercambiados: $M_x$ usa la distancia al eje $X$, es decir $y$ ($M_x=\iint y\rho\,dA$)."),
                        mal(r"$M_x=18,\ \ M_y=24$",
                            r"Olvidaste la densidad. Hay que integrar $y\rho$ y $x\rho$, no solo $y$ y $x$."),
                        mal(r"$M_x=\tfrac{27}{2},\ \ M_y=60$",
                            r"A $M_x$ le falta el factor $4$ de la integral en $x$: $\int_0^3y(y+1)\,dy=\tfrac{27}{2}$, y todavía se integra en $x$."),
                    ],
                    "explicacion": r"$M_x=\int_0^4\!\int_0^3y(y+1)\,dy\,dx=4\cdot\tfrac{27}{2}=54$ y $M_y=\int_0^4x\,dx\cdot\int_0^3(y+1)\,dy=8\cdot\tfrac{15}{2}=60$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$\left(2,\ \tfrac95\right)$"),
                        mal(r"$\left(\tfrac95,\ 2\right)$",
                            r"Intercambiaste las coordenadas: $\bar x=\tfrac{M_y}{M}$ y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(2,\ \tfrac32\right)$",
                            r"Ese sería el centro con densidad constante (el centro del rectángulo). Como $\rho=y+1$ crece hacia arriba, $\bar y>\tfrac32$."),
                        mal(r"$(60,\ 54)$",
                            r"Esos son $M_y$ y $M_x$. Falta dividir entre la masa $M=30$."),
                    ],
                    "explicacion": r"$\bar x=\tfrac{M_y}{M}=\tfrac{60}{30}=2$ y $\bar y=\tfrac{M_x}{M}=\tfrac{54}{30}=\tfrac95$.",
                },
            ],
        },
        {
            "id": "masa_1b",
            "nivel": 1,
            "enunciado": r"Halla el centro de masa de la lámina homogénea ($\rho=1$) con forma de triángulo de vértices $(0,0)$, $(3,0)$ y $(0,6)$.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** La hipotenusa une $(3,0)$ con $(0,6)$. ¿Cuánto vale la masa $M$?",
                    "opciones": [
                        ok(r"$9$"),
                        mal(r"$18$",
                            r"Ese número es base por altura. El área del triángulo lleva el factor $\tfrac12$."),
                        mal(r"$\tfrac{27}{2}$",
                            r"Usaste la recta $y=6-x$. La hipotenusa es $y=6-2x$ (pasa por $(3,0)$ y $(0,6)$)."),
                        mal(r"$\tfrac92$",
                            r"Tomaste altura $3$. El vértice está en $(0,6)$: la altura es $6$."),
                    ],
                    "explicacion": r"Con $\rho=1$, $M$ es el área: $\int_0^3(6-2x)\,dx=9$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $M_x=\iint y\,dA$ y $M_y=\iint x\,dA$.",
                    "opciones": [
                        ok(r"$M_x=18,\ \ M_y=9$"),
                        mal(r"$M_x=9,\ \ M_y=18$",
                            r"Están intercambiados: $M_x=\iint y\,dA$ y $M_y=\iint x\,dA$."),
                        mal(r"$M_x=36,\ \ M_y=9$",
                            r"En $M_x$ olvidaste el $\tfrac12$ de $\int y\,dy=\tfrac{y^2}{2}$."),
                        mal(r"$M_x=18,\ \ M_y=27$",
                            r"En $M_y$ usaste altura $6$ en lugar de la recta $6-2x$: $\int_0^3x(6-2x)\,dx=9$."),
                    ],
                    "explicacion": r"$M_x=\int_0^3\tfrac{(6-2x)^2}{2}\,dx=18$ y $M_y=\int_0^3x(6-2x)\,dx=9$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$(1,\ 2)$"),
                        mal(r"$(2,\ 1)$",
                            r"Intercambiaste las coordenadas: $\bar x=\tfrac{M_y}{M}$ y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(\tfrac32,\ 3\right)$",
                            r"Eso es la mitad de cada cateto. El centro de masa de un triángulo está a un tercio de cada cateto, medido desde el ángulo recto."),
                        mal(r"$(9,\ 18)$",
                            r"Esos son $M_y$ y $M_x$. Falta dividir entre $M=9$."),
                    ],
                    "explicacion": r"$\bar x=\tfrac99=1$ y $\bar y=\tfrac{18}{9}=2$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 2
        {
            "id": "masa_2a",
            "nivel": 2,
            "enunciado": r"Una lámina triangular de vértices $(0,0)$, $(3,0)$ y $(0,2)$ tiene densidad $\rho(x,y)=xy$. Halla su centro de masa.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** La hipotenusa une $(3,0)$ con $(0,2)$. ¿Cómo se describe la región?",
                    "opciones": [
                        ok(r"$0\leq x\leq3,\ \ 0\leq y\leq2-\tfrac23x$"),
                        mal(r"$0\leq x\leq3,\ \ 0\leq y\leq2-\tfrac32x$",
                            r"Invertiste la pendiente. La recta baja de $2$ a $0$ en $3$ unidades de $x$: pendiente $-\tfrac23$."),
                        mal(r"$0\leq x\leq3,\ \ 0\leq y\leq3-\tfrac32x$",
                            r"Esa recta pasa por $(2,0)$ y $(0,3)$: intercambiaste los cortes con los ejes."),
                        mal(r"$0\leq x\leq3,\ \ 0\leq y\leq2-x$",
                            r"Esa recta corta el eje $x$ en $2$, no en $3$."),
                    ],
                    "explicacion": r"La recta por $(3,0)$ y $(0,2)$ es $y=2-\tfrac23x$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto vale la masa $M=\iint xy\,dA$?",
                    "opciones": [
                        ok(r"$\tfrac32$"),
                        mal(r"$3$",
                            r"Ese es el área del triángulo. Falta multiplicar por la densidad $xy$."),
                        mal(r"$2$",
                            r"Usaste $\rho=y$. La densidad es el producto $xy$."),
                        mal(r"$9$",
                            r"Integraste sobre el rectángulo $[0,3]\times[0,2]$, no sobre el triángulo."),
                    ],
                    "explicacion": r"$M=\int_0^3x\cdot\tfrac12\left(2-\tfrac23x\right)^2dx=\tfrac32$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $M_x=\iint y\rho\,dA$ y $M_y=\iint x\rho\,dA$.",
                    "opciones": [
                        ok(r"$M_x=\tfrac65,\ \ M_y=\tfrac95$"),
                        mal(r"$M_x=\tfrac95,\ \ M_y=\tfrac65$",
                            r"Están intercambiados: $M_x=\iint y\rho\,dA=\iint xy^2\,dA$ y $M_y=\iint x\rho\,dA=\iint x^2y\,dA$."),
                        mal(r"$M_x=2,\ \ M_y=3$",
                            r"Olvidaste la densidad $xy$: esos valores son $\iint y\,dA$ y $\iint x\,dA$."),
                        mal(r"$M_x=\tfrac65,\ \ M_y=3$",
                            r"En $M_y$ también hay que multiplicar por la densidad: $M_y=\iint x\cdot xy\,dA$."),
                    ],
                    "explicacion": r"$M_x=\iint xy^2\,dA=\tfrac65$ y $M_y=\iint x^2y\,dA=\tfrac95$.",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$\left(\tfrac65,\ \tfrac45\right)$"),
                        mal(r"$\left(\tfrac45,\ \tfrac65\right)$",
                            r"Intercambiaste las coordenadas: $\bar x=\tfrac{M_y}{M}$ y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(1,\ \tfrac23\right)$",
                            r"Ese es el centro del triángulo con densidad constante. Con $\rho=xy$ la masa se concentra lejos de los ejes, así que ambas coordenadas son mayores."),
                        mal(r"$\left(\tfrac95,\ \tfrac65\right)$",
                            r"Esos son $M_y$ y $M_x$. Falta dividir entre $M=\tfrac32$."),
                    ],
                    "explicacion": r"$\bar x=\tfrac{9/5}{3/2}=\tfrac65$ y $\bar y=\tfrac{6/5}{3/2}=\tfrac45$.",
                },
            ],
        },
        {
            "id": "masa_2b",
            "nivel": 2,
            "enunciado": r"Una lámina ocupa la región bajo la parábola $y=x^2$, con $0\leq x\leq2$, y su densidad es $\rho(x,y)=x$. Halla su centro de masa.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuánto vale la masa $M=\iint x\,dA$ sobre la región?",
                    "opciones": [
                        ok(r"$4$"),
                        mal(r"$\tfrac83$",
                            r"Ese es el área bajo la parábola. Falta la densidad $\rho=x$."),
                        mal(r"$8$",
                            r"Integraste hasta $y=4$ (el rectángulo). La región llega solo hasta $y=x^2$."),
                        mal(r"$2$",
                            r"Te faltó la altura: para cada $x$, $y$ va de $0$ a $x^2$, y ahí se integra $x\,dy=x\cdot x^2$."),
                    ],
                    "explicacion": r"$M=\int_0^2\!\int_0^{x^2}x\,dy\,dx=\int_0^2x^3\,dx=4$.",
                },
                {
                    "pregunta": r"**Paso 2.** Calcula $M_x=\iint y\rho\,dA$ y $M_y=\iint x\rho\,dA$.",
                    "opciones": [
                        ok(r"$M_x=\tfrac{16}{3},\ \ M_y=\tfrac{32}{5}$"),
                        mal(r"$M_x=\tfrac{32}{5},\ \ M_y=\tfrac{16}{3}$",
                            r"Están intercambiados: $M_x=\iint y\rho\,dA$ y $M_y=\iint x\rho\,dA$."),
                        mal(r"$M_x=\tfrac{16}{5},\ \ M_y=4$",
                            r"Olvidaste la densidad: esos valores son $\iint y\,dA$ y $\iint x\,dA$."),
                        mal(r"$M_x=\tfrac{32}{3},\ \ M_y=\tfrac{32}{5}$",
                            r"En $M_x$ olvidaste el $\tfrac12$ de $\int y\,dy=\tfrac{y^2}{2}$."),
                    ],
                    "explicacion": r"$M_x=\int_0^2x\cdot\tfrac{x^4}{2}\,dx=\tfrac{16}{3}$ y $M_y=\int_0^2x^2\cdot x^2\,dx=\tfrac{32}{5}$.",
                },
                {
                    "pregunta": r"**Paso 3.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$\left(\tfrac85,\ \tfrac43\right)$"),
                        mal(r"$\left(\tfrac43,\ \tfrac85\right)$",
                            r"Intercambiaste las coordenadas: $\bar x=\tfrac{M_y}{M}$ y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(\tfrac32,\ \tfrac65\right)$",
                            r"Ese es el centro con densidad constante. Como $\rho=x$ crece hacia la derecha, $\bar x$ es mayor que $\tfrac32$."),
                        mal(r"$\left(\tfrac{32}{5},\ \tfrac{16}{3}\right)$",
                            r"Esos son $M_y$ y $M_x$. Falta dividir entre $M=4$."),
                    ],
                    "explicacion": r"$\bar x=\tfrac{32/5}{4}=\tfrac85$ y $\bar y=\tfrac{16/3}{4}=\tfrac43$.",
                },
            ],
        },

        # ---------------------------------------------------------- NIVEL 3
        {
            "id": "masa_3a",
            "nivel": 3,
            "enunciado": r"Una lámina homogénea ($\rho=k$) tiene forma de semicírculo $x^2+y^2\leq9,\ y\geq0$. Halla su centro de masa usando polares.",
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cómo se describe la lámina en polares?",
                    "opciones": [
                        ok(r"$0\leq r\leq3,\ \ 0\leq\theta\leq\pi$"),
                        mal(r"$0\leq r\leq3,\ \ 0\leq\theta\leq2\pi$",
                            r"Eso es el círculo completo. Con $y\geq0$ solo se recorre de $0$ a $\pi$."),
                        mal(r"$0\leq r\leq3,\ \ 0\leq\theta\leq\tfrac\pi2$",
                            r"Eso es un cuarto de círculo; $y\geq0$ incluye también el segundo cuadrante."),
                        mal(r"$0\leq r\leq9,\ \ 0\leq\theta\leq\pi$",
                            r"$x^2+y^2\leq9$ equivale a $r^2\leq9$, o sea $r\leq3$."),
                    ],
                    "explicacion": r"$r^2\leq9\Rightarrow r\leq3$ y $y\geq0\Rightarrow0\leq\theta\leq\pi$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto vale la masa $M=\iint k\,dA$?",
                    "opciones": [
                        ok(r"$\tfrac{9\pi k}{2}$"),
                        mal(r"$9\pi k$",
                            r"Es la masa del círculo completo. Esta lámina es solo el semicírculo."),
                        mal(r"$\tfrac{9\pi k}{4}$",
                            r"Eso es un cuarto de círculo: $\theta$ llega hasta $\pi$, no hasta $\tfrac\pi2$."),
                        mal(r"$3\pi k$",
                            r"$\int_0^3r\,dr=\tfrac{r^2}{2}=\tfrac92$, no $3$: hay que integrar el $r$ del Jacobiano."),
                    ],
                    "explicacion": r"$M=k\int_0^\pi\!\int_0^3r\,dr\,d\theta=k\cdot\tfrac92\cdot\pi$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $M_x=\iint y\,k\,dA$ (usa $y=r\sin\theta$).",
                    "opciones": [
                        ok(r"$18k$"),
                        mal(r"$9k$",
                            r"Te faltó el $r$ del Jacobiano: $y\,dA=r^2\sin\theta\,dr\,d\theta$ (no $r\sin\theta$)."),
                        mal(r"$6k$",
                            r"$\int_0^3r^2\,dr=\tfrac{r^3}{3}=9$, no $3$."),
                        mal(r"$0$",
                            r"Ese valor corresponde a $M_y$ (usa $\cos\theta$ y se anula por simetría). $M_x$ usa $y=r\sin\theta$."),
                    ],
                    "explicacion": r"$M_x=k\int_0^\pi\sin\theta\,d\theta\int_0^3r^2\,dr=k\cdot2\cdot9=18k$.",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$\left(0,\ \tfrac4\pi\right)$"),
                        mal(r"$\left(\tfrac4\pi,\ 0\right)$",
                            r"Intercambiaste las coordenadas: por simetría respecto al eje $y$ se tiene $\bar x=0$, y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(0,\ \tfrac32\right)$",
                            r"Ese es el punto medio de la altura. En un semicírculo el centro de masa está más abajo, en $\tfrac{4r}{3\pi}$."),
                        mal(r"$\left(0,\ \tfrac2\pi\right)$",
                            r"Dividiste entre la masa del círculo completo ($9\pi k$). Hay que usar la del semicírculo, $\tfrac{9\pi k}{2}$."),
                    ],
                    "explicacion": r"$M_y=0$ por simetría, así que $\bar x=0$, y $\bar y=\tfrac{18k}{9\pi k/2}=\tfrac4\pi$.",
                },
            ],
        },
        {
            "id": "masa_3b",
            "nivel": 3,
            "enunciado": (r"Una lámina ocupa el cuarto de disco $x^2+y^2\leq4,\ x\geq0,\ y\geq0$, y su densidad es proporcional "
                          r"a la distancia al eje $y$: $\rho=kx$. Halla su centro de masa usando polares."),
            "pasos": [
                {
                    "pregunta": r"**Paso 1.** ¿Cuál es la integral de la masa $M$ en polares?",
                    "opciones": [
                        ok(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 k\,r^2\cos\theta\,dr\,d\theta$"),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 k\,r\cos\theta\,dr\,d\theta$",
                            r"Te faltó el Jacobiano: $\rho\,dA=kr\cos\theta\cdot r\,dr\,d\theta$."),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 k\,r^2\,dr\,d\theta$",
                            r"La densidad es $kx=kr\cos\theta$: no pierdas el $\cos\theta$. Con $kr$ sería otra lámina (densidad proporcional a la distancia al origen)."),
                        mal(r"$\displaystyle\int_0^{\pi/2}\!\!\int_0^2 k\,r^3\cos\theta\,dr\,d\theta$",
                            r"$x=r\cos\theta$ aporta un $r$ y el Jacobiano otro: en total $r^2$, no $r^3$."),
                    ],
                    "explicacion": r"$\rho\,dA=k(r\cos\theta)\,r\,dr\,d\theta=kr^2\cos\theta\,dr\,d\theta$.",
                },
                {
                    "pregunta": r"**Paso 2.** ¿Cuánto vale la masa $M$?",
                    "opciones": [
                        ok(r"$\tfrac{8k}{3}$"),
                        mal(r"$2k$",
                            r"Eso sale sin el Jacobiano ($\int_0^2r\,dr=2$). Falta el $r$ de $dA$."),
                        mal(r"$\tfrac{4\pi k}{3}$",
                            r"Eso sería con $\rho=kr$ (sin el $\cos\theta$). Aquí $\int_0^{\pi/2}\cos\theta\,d\theta=1$."),
                        mal(r"$4k$",
                            r"Usaste $r^3$: $\int_0^2r^2\,dr=\tfrac83$, no $4$."),
                    ],
                    "explicacion": r"$M=k\int_0^2r^2\,dr\int_0^{\pi/2}\cos\theta\,d\theta=k\cdot\tfrac83\cdot1$.",
                },
                {
                    "pregunta": r"**Paso 3.** Calcula $M_x=\iint y\rho\,dA$ y $M_y=\iint x\rho\,dA$.",
                    "opciones": [
                        ok(r"$M_x=2k,\ \ M_y=\pi k$"),
                        mal(r"$M_x=\pi k,\ \ M_y=2k$",
                            r"Están intercambiados: $M_x$ usa $y$ ($\iint y\rho\,dA$) y $M_y$ usa $x$."),
                        mal(r"$M_x=4k,\ \ M_y=\pi k$",
                            r"En $M_x$ el ángulo es $\int_0^{\pi/2}\sin\theta\cos\theta\,d\theta=\tfrac12$, no $1$."),
                        mal(r"$M_x=2k,\ \ M_y=2\pi k$",
                            r"En $M_y$ el ángulo es $\int_0^{\pi/2}\cos^2\theta\,d\theta=\tfrac\pi4$, no $\tfrac\pi2$."),
                    ],
                    "explicacion": r"$M_x=k\int_0^2r^3\,dr\int_0^{\pi/2}\sin\theta\cos\theta\,d\theta=k\cdot4\cdot\tfrac12=2k$ y $M_y=k\cdot4\cdot\tfrac\pi4=\pi k$.",
                },
                {
                    "pregunta": r"**Paso 4.** ¿Cuál es el centro de masa $(\bar x,\bar y)$?",
                    "opciones": [
                        ok(r"$\left(\tfrac{3\pi}{8},\ \tfrac34\right)$"),
                        mal(r"$\left(\tfrac34,\ \tfrac{3\pi}{8}\right)$",
                            r"Intercambiaste las coordenadas: $\bar x=\tfrac{M_y}{M}$ y $\bar y=\tfrac{M_x}{M}$."),
                        mal(r"$\left(\tfrac{8}{3\pi},\ \tfrac{8}{3\pi}\right)$",
                            r"Ese es el centro con densidad constante. Aquí $\rho=kx$ empuja la masa hacia la derecha: $\bar x$ es mayor y $\bar y$ menor."),
                        mal(r"$(\pi k,\ 2k)$",
                            r"Esos son $M_y$ y $M_x$. Falta dividir entre $M=\tfrac{8k}{3}$."),
                    ],
                    "explicacion": r"$\bar x=\tfrac{\pi k}{8k/3}=\tfrac{3\pi}{8}$ y $\bar y=\tfrac{2k}{8k/3}=\tfrac34$.",
                },
            ],
        },
    ],
}