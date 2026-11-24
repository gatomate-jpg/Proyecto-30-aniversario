from flask import Flask, url_for, request
import html

app = Flask(__name__)

def render_pantalla(titulo_pestana, ruta_actual, es_inicio, cuerpo_html):
    css_url = url_for('static', filename='estilos.css')

    if es_inicio:
        logo_url = url_for('static', filename='logo1.jpeg')
        barra_html = f'''
        <header class="topbar topbar-inicio">
            <div class="brand-box">
                <div class="logo-marco">
                    <img src="{logo_url}" alt="Logo">
                </div>
                <div class="brand-text">
                    <strong>CECyTE</strong>
                    <span>30 Aniversario</span>
                </div>
            </div>
            <div class="badge-30">30</div>
        </header>
        '''
    else:
        barra_html = '''
        <header class="topbar">
            <a href="/" class="nav-icon" aria-label="Inicio">&#8592; Volver</a>
            <a href="/" class="nav-icon" aria-label="Inicio">&#8962; Inicio</a>
        </header>
        '''

    enlaces = [
        ('/', 'Inicio'),
        ('/pantalla2', 'Historia'),
        ('/pantalla3', 'Egresados'),
        ('/pantalla4', 'Logros'),
        ('/pantalla5', 'Eventos'),
        ('/pantalla6', 'Futuro'),
    ]

    nav_items = []
    for href, texto in enlaces:
        activo = ' class="active"' if href == ruta_actual else ''
        nav_items.append(f'<a href="{href}"{activo}>{texto}</a>')
    nav_html = f'<nav class="rutas-bar">{"".join(nav_items)}</nav>'

    return f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo_pestana}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{css_url}">
</head>
<body>
    <main class="desktop-container">
        {barra_html}
        {nav_html}
        <section class="pantalla-contenido">
            {cuerpo_html}
        </section>
    </main>
</body>
</html>'''

@app.route('/')
def inicio():
    cuerpo = '''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">30 años formando generaciones, construyendo oportunidades</h1>
            <p class="subtitulo">En esta página se mostrará todo lo que ha logrado CECyTEJ en estos 30 años: sus logros, mejoras, egresados y actividades extracurriculares</p>
        </div>

        <div class="grid-2 uniforme-inicio">
            <div class="tarjeta-bloque">
                <p class="texto-base">Estos botones sirven para redireccionarte a partes específicas de la página.</p>
                <div class="lista-menu">
                    <a href="/pantalla2" class="item-menu"><span>Historia</span><span class="flecha">&rsaquo;</span></a>
                    <a href="/pantalla3" class="item-menu"><span>Egresados</span><span class="flecha">&rsaquo;</span></a>
                    <a href="/pantalla4" class="item-menu"><span>Logros</span><span class="flecha">&rsaquo;</span></a>
                    <a href="/pantalla5" class="item-menu"><span>Eventos</span><span class="flecha">&rsaquo;</span></a>
                    <a href="/pantalla6" class="item-menu"><span>Futuro</span><span class="flecha">&rsaquo;</span></a>
                </div>
            </div>

            <div class="tarjeta-bloque">
                <div class="marco-imagen hero-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-68bd4017-04c4-4c89-a5bc-c23c87b533a5.jpg" alt="Imagen principal">
                </div>
            </div>
        </div>
    '''
    return render_pantalla('Pantalla 1', '/', True, cuerpo)

@app.route('/pantalla2')
def pantalla_2():
    cuerpo = '''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">Nuestra Historia</h1>
            <p class="subtitulo">En esta pantalla se mostrará lo que es la historia de CECyTEJ</p>
        </div>

        <div class="bloque-divisor"><span>RECUERDOS DEL PLANTEL</span></div>

        <div class="grid-2">
            <div class="tarjeta-bloque timeline-fila">
                <div class="timeline-dato">
                    <span class="punto"></span>
                    <div>
                        <strong>21 DE MARZO DE 2025</strong>
                        <p>En esta imagen se muestra una actividad recreativa</p>
                    </div>
                </div>
                <div class="marco-imagen mini-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-4c624fe2-63b2-4ace-8819-4a8ebd626a19.jpg" alt="Imagen 2A">
                </div>
            </div>

            <div class="tarjeta-bloque timeline-fila">
                <div class="timeline-dato">
                    <span class="punto"></span>
                    <div>
                        <strong>21 DE MARZO 2025</strong>
                        <p>En esta imagen se muestra un momento donde se fomenta la actividad física</p>
                    </div>
                </div>
                <div class="marco-imagen mini-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-9f2aceec-ce53-4e2f-97db-59ece4a09b81.jpg" alt="Imagen 2B">
                </div>
            </div>
        </div>

        <div class="bloque-divisor"><span>HISTORIA</span></div>

        <div class="grid-4">
            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-43f57099-7a90-46de-b490-adc88e0a462d.jpg" alt="Espacio 1"></div>
                <span class="etiqueta-item">Esta línea de tiempo muestra el avance de CECyTE</span>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-9f26f2f3-61c3-4b7a-be42-a30ec7a274dd.jpg" alt="Espacio 2"></div>
                <span class="etiqueta-item">Este es nuestro plantel en 2007-2010</span>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-ea011426-4979-4bda-9886-85f7c0105512.jpg" alt="Espacio 3"></div>
                <span class="etiqueta-item">Este es el plantel actualmente</span>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-0d9acb70-460e-4afb-9438-e9720212ab0e.jpg" alt="Espacio 4"></div>
                <span class="etiqueta-item">En esta imagen se muestra una pequeña parte del desfile que se celebra anualmente en el mes de Septiembre.</span>
            </div>
        </div>

        <div class="banner-verde">
            <span>CECyTE atravesó muchas dificultades para poder ser la institución que hoy en día es, como las bases legales, etc.</span>
            <span class="sello-30">30</span>
        </div>
    '''
    return render_pantalla('Pantalla 2', '/pantalla2', False, cuerpo)

@app.route('/pantalla3')
def pantalla_3():
    cuerpo = '''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">Voces que dejan huella</h1>
            <p class="subtitulo">Presentamos alumnos egresados que dieron su opinión sobre su estancia aquí en CECyTE.</p>
        </div>

        <div class="grid-2">
            <article class="tarjeta-bloque tarjeta-perfil">
                <div class="marco-imagen retrato-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-099c2816-75b0-458a-a8c9-ac4cffbb6073.jpg" alt="Perfil 1">
                </div>
                <div class="perfil-texto">
                    <strong>Maira Guadalupe Suárez Sánchez</strong>
                    <span>Egresada</span>
                    <p>"Adquirir conocimientos, aprender a ser responsables y a trabajar en equipo, y encontrar amistades que forman parte de lo que soy hoy"</p>
                </div>
            </article>

            <article class="tarjeta-bloque tarjeta-perfil">
                <div class="marco-imagen retrato-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-099c2816-75b0-458a-a8c9-ac4cffbb6073.jpg" alt="Perfil 2">
                </div>
                <div class="perfil-texto">
                    <strong>Erik Samuel Espinoza</strong>
                    <span>Egresado</span>
                    <p>"Les diría que aprovechen cada oportunidad al máximo. A veces las materias o los proyectos parecen difíciles, pero todo ese esfuerzo forma el carácter. Que no tengan miedo de preguntar, de equivocarse y de acercarse a sus maestros para aprender más."</p>
                </div>
            </article>

            <article class="tarjeta-bloque tarjeta-perfil">
                <div class="marco-imagen retrato-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-099c2816-75b0-458a-a8c9-ac4cffbb6073.jpg" alt="Perfil 3">
                </div>
                <div class="perfil-texto">
                    <strong>Azucena Valdez Camacho</strong>
                    <span>Egresada</span>
                    <p>"Que valoren el tiempo que pasan aquí. El bachillerato técnico pasa volando. Les aconsejo que le pongan empeño a sus prácticas y talleres, porque esa experiencia práctica es justo lo que marca la diferencia cuando sales al mundo real."</p>
                </div>
            </article>

            <article class="tarjeta-bloque tarjeta-perfil">
                <div class="marco-imagen retrato-img">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-099c2816-75b0-458a-a8c9-ac4cffbb6073.jpg" alt="Perfil 4">
                </div>
                <div class="perfil-texto">
                    <strong>Ramon Reyes Lopez</strong>
                    <span>Egresado</span>
                    <p>"Valoren sus estudios, amistades y disfruten la vida."</p>
                </div>
            </article>
        </div>

        <div class="grid-2">
            <div class="tarjeta-bloque tarjeta-frase">
                <div class="comillas">&ldquo;</div>
                <p>Vida solo hay una, y hay que vivirla al máximo y valorar lo que tenemos.</p>
            </div>

            <div class="tarjeta-bloque sin-padding">
                <div class="banner-foto">
                    <img src="https://cdn.phototourl.com/anon/2026-11-23-4e5a0e7e-afc8-4206-8383-4cf6236f4a5d.jpg" alt="Imagen banner">
                    <div class="banner-overlay">
                        <p></p>
                    </div>
                </div>
            </div>
        </div>
    '''
    return render_pantalla('Pantalla 3', '/pantalla3', False, cuerpo)

@app.route('/pantalla4')
def pantalla_4():
    cuerpo = '''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">Orgullo CECyTE</h1>
            <p class="subtitulo">Subtítulo de categorías y proyectos.</p>
        </div>

        <div class="grid-4">
            <div class="tarjeta-bloque tarjeta-centrada">
                <span class="cat-etiqueta">Platicas de Egresados</span>
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-100b99f4-00f4-4d7c-9340-117a3743b6d5.jpg" alt="Cat 1"></div>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <span class="cat-etiqueta">Inaguración de escaleras</span>
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-d0cabad5-e905-4da6-80ea-281eb1f5bd9f.jpg" alt="Cat 2"></div>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <span class="cat-etiqueta">Alumnos</span>
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-21cbe36d-d06b-4a46-876f-fe9dfef32723.jpg" alt="Cat 3"></div>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <span class="cat-etiqueta">Director</span>
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-3f1f9fd5-00ab-4e21-ae84-88105da3e674.jpg" alt="Cat 4"></div>
            </div>
        </div>

        <div class="grid-2">
            <div class="tarjeta-bloque">
                <h3>DEFINICIONES</h3>
                <ul>
                    <li>Plática: Fue un egresado a dar una plática sobre como fue estudiar en CECyTE, convivir con los docentes, y como esos estudios lo llevaron a poder completar su carrera medica</li>
                    <li>Alumnos: Cada alumno logra demostrar en lo que destaca, ya fuera en cultura digital, matemáticas, pensamiento filosófico, etc</li>
                    <li>Deportes: CECyTE logra destacar por todos sus premios ganados en deportes, en su mayoría voleibol</li>
                    <li>Director: Con la llegada del nuevo director también llegaron nuevos cambios importantes para CECyTE</li>
                    <li>Escalera: Uno de las mejoras en CECyTE fueron la implementación de una escalera nueva para que los alumnos tuvieras más facilidad al momento de subir</li>
                </ul>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <h3>DESTACADO</h3>
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-daedb824-fae8-4b76-aa87-6f665ab145db.jpg" alt="Destacado"></div>
            </div>
        </div>
    '''
    return render_pantalla('Pantalla 4', '/pantalla4', False, cuerpo)

@app.route('/pantalla5')
def pantalla_5():
    cuerpo = '''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">Eventos realizados en el plantel</h1>
        </div>

        <div class="grid-4">
            <div class="tarjeta-bloque">
                <h3>Candidatas para Reina</h3>
                <p class="texto-base centrado">Esta actividad se realiza en la comunidad donde se invitan a las estudiantes a participar en un concurso para encontrar quien será la que represente al plantel como reina CECyTE.</p>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-e9e0714b-c722-4474-9a6f-0af64853d269.jpg" alt="Bloque 2"></div>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <h3>San Valentín</h3>
                <p class="texto-base centrado">En nuestro plantel en febrero se celebra el Día del amor y la amistad de un modo muy especial, los padres de los estudiantes llevan al plantel regalos para sus hijos para demostrarles su amor, también los mismos estudiantes pueden dejar regalos para sus amigos cercanos del plantel.</p>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-ebb85df3-f05b-4374-99de-e9dd8926a567.jpg" alt="Bloque 4"></div>
            </div>
        </div>
        <div class="grid-4">
            <div class="tarjeta-bloque">
                <h3>Día del estudiante</h3>
                <p class="texto-base centrado">En el día del estudiante se realizan diferentes actividades, ya sea con harina, agua, balones, fuerza física etc, todo con la finalidad de pasar un buen día y ganar diversos premios.</p>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-bcb0d74f-cbd6-4967-a834-c20441a8b0d9.jpg" alt="Bloque 2"></div>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <h3>Día de muertos</h3>
                <p class="texto-base centrado">El día de muertos se realizan dos eventos, lo que es el concurso de catrines y altares. Y el desfile que es iniciado con el catrín ganador</p>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-478254e2-bb6b-47cd-ac2f-aa12645ad1d2.jpg" alt="Bloque 4"></div>
            </div>
            <div class="tarjeta-bloque tarjeta-centrada">
                <h3>Pastorela</h3>
                <p class="texto-base centrado">En generaciones pasadas se realizaban pastorelas por las fechas navideñas, actualmente no se realizan pero hay concursos de piñatas, números navideños (ya sea cantar, bailar, actuar)</p>
            </div>

            <div class="tarjeta-bloque tarjeta-centrada">
                <div class="marco-imagen cuadro-img"><img src="https://cdn.phototourl.com/anon/2026-11-23-ff2f80d6-688e-4eb4-9469-3e8e632a8cd6.jpg" alt="Bloque 4"></div>
            </div>
        </div>
    '''
    return render_pantalla('Pantalla 5', '/pantalla5', False, cuerpo)

@app.route('/pantalla6', methods=['GET', 'POST'])
def pantalla_6():
    preguntas = [
        ('p1', '1. Visión a 30 años', '¿Cómo imaginas la institución y la comunidad dentro de los próximos 30 años?'),
        ('p2', '2. Mejoras', '¿Qué mejoras principales propones en instalaciones, procesos o formación?'),
        ('p3', '3. Tecnología educativa', '¿Cómo debe integrarse la tecnología educativa en el aprendizaje diario?'),
        ('p4', '4. Metas', '¿Cuáles son las metas más importantes a alcanzar a corto y mediano plazo?'),
        ('p5', '5. Mensajes', '¿Qué mensaje deseas compartir con estudiantes, docentes, egresados y familias?'),
        ('p6', '6. Compromiso ambiental/social', '¿Cuál es el compromiso ambiental y social que se debe asumir?'),
        ('p7', '7. Frase final exacta', 'Escribe la frase final exacta de cierre:'),
    ]

    resumen_html = ''
    if request.method == 'POST':
        items_resumen = []
        for campo, etiqueta, _ in preguntas:
            valor = request.form.get(campo, '').strip() or 'Sin respuesta'
            valor_seguro = html.escape(valor)
            items_resumen.append(f'''
                <div class="respuesta-item">
                    <strong>{etiqueta}</strong>
                    <p>{valor_seguro}</p>
                </div>
            ''')
        resumen_html = f'''
            <div class="tarjeta-bloque resumen-cuestionario">
                <h3>RESPUESTAS REGISTRADAS</h3>
                <div class="resumen-lista">
                    {"".join(items_resumen)}
                </div>
            </div>
        '''

    campos_html = []
    for campo, etiqueta, texto_pregunta in preguntas:
        valor_actual = html.escape(request.form.get(campo, '')) if request.method == 'POST' else ''
        campos_html.append(f'''
            <div class="tarjeta-bloque pregunta-card">
                <label class="pregunta-titulo" for="{campo}">{etiqueta}</label>
                <p class="texto-base">{texto_pregunta}</p>
                <textarea id="{campo}" name="{campo}" class="campo-respuesta" rows="3" placeholder="Escribe tu respuesta aquí...">{valor_actual}</textarea>
            </div>
        ''')

    cuerpo = f'''
        <div class="encabezado-pantalla">
            <h1 class="titulo-seccion">Cuestionario de Futuro</h1>
            <p class="subtitulo">Responde los 7 puntos clave para construir la sección.</p>
        </div>

        {resumen_html}

        <form method="POST" class="cuestionario-form">
            <div class="grid-2">
                {"".join(campos_html)}
            </div>
            <div class="acciones-cuestionario">
                <button type="submit" class="btn-enviar">Guardar respuestas</button>
            </div>
        </form>

        <div class="banner-cierre">
            <p>7 puntos desarrollados para proyectar el futuro.</p>
            <span class="sello-30">30</span>
        </div>
    '''
    return render_pantalla('Pantalla 6 - Cuestionario', '/pantalla6', False, cuerpo)

if __name__ == '__main__':
    app.run(debug=True)