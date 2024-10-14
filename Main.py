from flask import Flask
import random

app = Flask(__name__)

dt = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
      "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
      "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
      "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
      "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
      "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
      "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
      "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]
       
KG = ["Minecraft: es el numero 1 con mas 350 millones de copas vendidas desde su lanzamiento en 2011",
      "Grand Theft Auto: segundo lugar con mas de 215 millones de copas vendidas",
      "Tetris: tercer lugar con 170 millones de copias.",
      "Wii Sports: superan los 83 millones de copias vendidas",
      "PUBG Batllegrounds: con nada menos que 75 millones de copias vendidas",
      "Mario Kart 8 Deluxe: con mas de 70 millones de copas vendidas",
      "Red Dead Redemption: antepenultimo lugar con mas de 64 millones de unidades vendidas",
      "Super Mario Bros: con más de 58 millones de copias vendidas",
      "Pokemon Rojo/Verde/Azul/Amarillo: en penultimo lugar con mas de 47 millones de copias vendidas",
      "Pac-man: ultimo lugar con mas 45 millones de copias vendidas"
      ]

@app.route("/")
def hello_world():
    return """<h1>Pagina Principal, me gusta la pizza</hi>  <a href="/ddldt"> Ver datos aleatorios</a>  <a href="/games"> ver clasificacion de Juegos mas vendidos</a> """

@app.route("/ddldt")
def datoale():
    return f"""<p>{random.choice(dt)}</p>
            <button onclick="Window.location.href='/' "> Ir a la pagina princpal</button>"""

@app.route("/games")
def Knowgames():
    return f"""<p>{random.choice(KG)}</p>"""


app.run(debug=True)