from flask import Flask, render_template, request
from random import randint
from data import data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['POST', 'GET'])
def start():
    global img, country_name, full_country_name, country_flag
    if request.method == 'GET':
        random_number = randint(1, 192)
        country_name = data[random_number]['Страна']
        full_country_name = data[random_number]['Полное название страны']
        country_flag = str(random_number) + '.svg'
        print(country_name)
        return render_template('flags.html', img=country_flag)

    elif request.method == 'POST':
        answer = request.form['check_field']
        if answer.lower() == country_name.lower():
            dec = f"Правильно! Это {country_name}. \n\n{full_country_name}."
            bc='green'
        else:
            dec = f"Нет! Это {country_name}. \n\n{full_country_name}."
            bc='red'
        print(answer)
        return render_template('flags.html', img=country_flag, dec=dec,bc=bc)


if __name__ == '__main__':
    app.run(debug=True)
