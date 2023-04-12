import streamlit as st

# Definimos los grupos de departamentos en base a su topografía
st.title("Estimación del área de afectación de explosiones de cilindros de gas GLP en Colombia mediante un modelo matemático de difusión en medios heterogéneos.")
grupo_1 = ["Antioquia", "Bolívar", "Boyacá", "Caldas", "Cauca", "Cundinamarca", "Huila", "Nariño", "Quindío", "Risaralda", "Santander", "Tolima", "Valle del Cauca"]
grupo_2 = ["Amazonas", "Caquetá", "Chocó", "Guainía", "Guaviare", "Meta", "Putumayo", "Vaupés", "Vichada"]
grupo_3 = ["Arauca", "Atlántico", "Casanare", "Cesar", "Córdoba", "La Guajira", "Magdalena", "Norte de Santander", "San Andrés y Providencia", "Sucre"]

st.header('A continuación seleccione un Grupo y su correspondiente departamento para determinar la afectacion de la explosion del tanque de GLP:')

# opcion_seleccionada1 = st.selectbox('Selecciona un departamento del Grupo 1:', grupo_1)
# opcion_seleccionada2 = st.selectbox('Selecciona un departamento del Grupo 2:', grupo_2)
# opcion_seleccionada3 = st.selectbox('Selecciona un departamento del Grupo 3:', grupo_3)
opciones = {
    'Grupo 1': grupo_1,
    'Grupo 2': grupo_2,
    'Grupo 3': grupo_3
}

seleccion = st.selectbox('Primero el Grupo y luego el departamento', opciones.items(), format_func=lambda x: x[0], key='grupo')
# grupo_seleccionado = st.selectbox('Selecciona un grupo', options=list(opciones.keys()), index=0)
# departamentos = opciones[grupo_seleccionado]
# titulo = 'Selecciona un departamento' if grupo_seleccionado != 'Grupo 2' else 'Selecciona un departamento del grupo 2'
# seleccion = st.selectbox(titulo, options=departamentos, index=0, key=grupo_seleccionado, disabled=grupo_seleccionado == 'Grupo 2')


if seleccion:
    departamento = st.selectbox('', seleccion[1])
    # st.write(f'Se ha seleccionado el departamento {departamento}')
    
if grupo_1.count(departamento):
    jerarquia = 1
    descripcion = """\n\n
    Este departamento se encuentra en el grupo con mayor probabilidad de ser 
    afectado gravemente por una explosión, debido a su topografía montañosa y su 
    densa población. Se recomienda tomar medidas de precaución en caso de una emergencia.
    \nRecomendaciones:
    \n1. Realice una evaluación detallada de las zonas de mayor riesgo en el departamento, 
    y se establezcan planes de contingencia para prevenir y responder a emergencias 
    relacionadas con explosiones de cilindros de gas GLP.
    \n2. Es importante que se implementen medidas preventivas, como la capacitación de la 
    población en el manejo adecuado de cilindros de gas GLP, la verificación periódica 
    de las instalaciones de gas y la promoción de la cultura de seguridad en la comunidad.
    \n3. Se debe fortalecer la capacidad de respuesta de las autoridades locales y nacionales 
    ante emergencias, mediante la dotación de equipos y herramientas necesarios, y la 
    actualización constante de los planes de contingencia."""
elif grupo_2.count(departamento):
    jerarquia = 2
    descripcion = """\n\n
    Este departamento se encuentra en el grupo intermedio de probabilidad de ser
    afectado por una explosión, debido a su topografía relativamente plana y 
    baja densidad poblacional. Se recomienda mantenerse alerta en caso de una emergencia.
    \nRecomendaciones:
    \n1. Mantener una actitud preventiva y estar atento a las señales de peligro en caso 
    de una emergencia, evitando situaciones de riesgo innecesarias y tomando medidas para
    proteger su seguridad y la de las personas a su alrededor.
    \n2. Informarse sobre las medidas de seguridad y los protocolos de evacuación en caso
    de una emergencia relacionada con el GLP, y estar preparado para actuar de manera rápida
    y segura.
    \n3. Asegurarse de tener un plan de emergencia en caso de una explosión, incluyendo la 
    identificación de las salidas de emergencia y los puntos de reunión."""
else:
    jerarquia = 3
    descripcion = """\n\n
    Este departamento se encuentra en el grupo con menor probabilidad de ser 
    afectado por una explosión, debido a su topografía plana y baja densidad poblacional. 
    Aunque el riesgo es bajo, se recomienda estar informado y preparado en caso de una emergencia.
    \nRecomendaciones:
    \n1. Aunque el riesgo de una explosión en este departamento sea bajo, es importante mantenerse 
    informado sobre los riesgos de manejar y almacenar gas GLP. Conocer las medidas de seguridad 
    recomendadas para el transporte y uso del gas GLP puede ayudar a prevenir accidentes y reducir 
    riesgos.
    \n2. A pesar de que el riesgo de una explosión sea bajo, es importante estar preparado en caso 
    de una emergencia. Familiarizarse con las medidas de seguridad recomendadas en caso de una 
    explosión de gas GLP y tener un plan de acción en caso de emergencia puede ayudar a reducir 
    los riesgos y aumentar la seguridad.
    \n3. Aunque la topografía del departamento y su densidad poblacional sugieran un menor riesgo 
    de explosión, es importante tomar en cuenta que ningún lugar está completamente exento de riesgos. 
    Por lo tanto, es fundamental mantener una actitud vigilante y estar alerta ante cualquier situación 
    que pueda representar un peligro."""

# Mostramos la información del departamento seleccionado
st.write(f"\nEl departamento seleccionado es: {departamento}")
st.write(f"\nEste departamento pertenece al grupo de jerarquía {jerarquia}. {descripcion}")

# Código para alcance de afectación de la explosión de un cilindro de gas

st.header("Alcance de afectación de la explosión de un cilindro de gas")
desden = """\n
    def bst_model(distance, pressure_initial, pressure_burst, mass):
    
        # Constantes del modelo
        k = 1.4  # Coeficiente de isentrópica
        C = 1.5  # Coeficiente empírico
        
        # Cálculo de la energía total de la explosión
        energy = (k / (k - 1)) * mass * (pressure_burst / pressure_initial) * (1 - math.pow(1 / (pressure_burst / pressure_initial), (k - 1) / k))
        
        # Cálculo del alcance de afectación
        radius = C * math.pow(energy, 1/3) * math.pow(distance, 2/3)
        
        #Devolviendo como valor el alcance de afectación
        return radius
"""
st.write(f"\nUtilizando el Modelo de Baker-Strehlow-Tang. {desden}")
import math

def bst_model(distance, pressure_initial, pressure_burst, mass):
    """Función que calcula el alcance de afectación de una explosión de un cilindro de gas GLP
    utilizando el modelo de Baker-Strehlow-Tang."""
    
    # Constantes del modelo
    k = 1.4  # Coeficiente de isentrópica
    C = 1.5  # Coeficiente empírico
    
    # Cálculo de la energía total de la explosión
    energy = (k / (k - 1)) * mass * (pressure_burst / pressure_initial) * (1 - math.pow(1 / (pressure_burst / pressure_initial), (k - 1) / k))
    
    # Cálculo del alcance de afectación
    radius = C * math.pow(energy, 1/3) * math.pow(distance, 2/3)
    
    return radius



# Opciones de cilindros y masas
cilindros = {
    "100 lb": {"descripcion": "Cilindro de 100 lb","masa": 45},
    "40 lb": {"descripcion": "Cilindro de 40 lb", "masa": 18},
    "33 lb": {"descripcion": "Cilindro de 33 lb", "masa": 15},
    "20 lb": {"descripcion": "Cilindro de 20 lb", "masa": 9},
    "10 lb": {"descripcion": "Cilindro de 10 lb", "masa": 5}
}
opciones2 = ['Cilindro de 100 lb (masa = 45 kg)', 'Cilindro de 40 lb (masa = 18 kg)', 'Cilindro de 33 lb (masa = 15 kg)', 'Cilindro de 20 lb (masa = 9 kg)', 'Cilindro de 10 lb (masa = 5 kg)']
opcion_seleccionada2 = st.selectbox("\n\nSeleccione el cilindro que exploto: \n", cilindros)

# Ejecutar cálculo con la selección del usuario
distance = 1.5  # Distancia en metros desde el cilindro de gas GLP hasta los objetos cercanos
pressure_initial = 750000  # Presión inicial del gas en Pascales
pressure_burst = 7.2E6  # Presión de rotura del cilindro en Pascales
mass = cilindros[opcion_seleccionada2]['masa']  # Masa total del gas en kilogramos

radius = bst_model(distance, pressure_initial, pressure_burst, mass)

st.write(f"""\nEl radio de la afectación de la explosión es de {radius:.2f} metros.

Consecuencias:

1. Lesiones graves: Las personas pueden sufrir quemaduras, cortes, fracturas, 
lesiones de órganos internos y otros tipos de lesiones graves debido a la 
explosión y a los objetos que vuelan por el aire.

2. Pérdida de vidas humanas: Las explosiones de gas pueden ser mortales, 
especialmente si la explosión es de gran magnitud o si las personas se 
encuentran muy cerca del lugar de la explosión.

3. Daños materiales: Las explosiones de gas pueden causar daños materiales 
importantes, destruyendo edificios, vehículos y otras estructuras cercanas 
al lugar de la explosión.

Recomendaciones: 

1. Mantener el cilindro en buen estado: Asegurarse de que el cilindro de gas 
esté en buen estado y sea manipulado correctamente. Realizar inspecciones 
periódicas para detectar posibles fugas o daños en el cilindro.

2. Almacenamiento adecuado: Almacenar los cilindros de gas GLP en lugares 
bien ventilados, alejados de fuentes de calor y en posición vertical. 
Mantenerlos en áreas al aire libre y protegerlos de la lluvia y el sol directo.

3. Capacitación del personal: Capacitar al personal en el manejo de cilindros 
de gas GLP, incluyendo el proceso de transporte, almacenamiento y manipulación 
segura. Así mismo, tener un plan de acción en caso de una emergencia.

4. Instalaciones adecuadas: Asegurarse de que las instalaciones de gas estén 
diseñadas y construidas adecuadamente para evitar fugas de gas y tener medidas 
de seguridad, como detectores de gas y sistemas de ventilación.

5. Sensibilización a la comunidad: Realizar campañas de sensibilización para 
informar a la comunidad sobre los riesgos de los cilindros de gas y cómo tomar 
medidas preventivas en caso de una emergencia.""")



st.write("Hola :D")