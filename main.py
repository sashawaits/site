from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.", 
            "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.", 
            "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.", 
            "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]


@app.route("/")
def first_page():
    return f'Интересный факт: {random.choice(facts_list)} <a href="/2">Вторая страница</a>'

@app.route("/2")
def second_page():
    return '<h1>Вторая страница</h1> <a href="/">Главная страница</a> <a href="/3">Третья страница</a>'

@app.route("/3")
def third_page():
    return '<h1>Третья страница</h1> <a href="/">Главная страница</a> <a href="/2">Вторая страница</a> <iframe width="560" height="315" src="https://www.youtube.com/embed/oK6qm2NJv7A?si=13KgBc7hMd40w9Xz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

app.run(debug=True)