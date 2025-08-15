from secrets import randbelow, token_hex

from flask import Flask, render_template, request

from data import data

app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)

img, country_name, full_country_name, country_flag = [None] * 4


@app.route('/', methods=['POST', 'GET'])
def start():
    global img, country_name, full_country_name, country_flag
    if request.method == 'GET':
        random_number = randbelow(192)
        country_name = data[random_number]['Страна']
        full_country_name = data[random_number]['Полное название страны']
        country_flag = str(random_number) + '.svg'
        print(country_name)
        return render_template('flags.html', img=country_flag)

    elif request.method == 'POST':
        answer = request.form['check_field']
        if answer.lower() == country_name.lower():
            message = f"Правильно! Это {country_name}. \n\n{full_country_name}."
            border_color = 'green'
        else:
            message = f"Нет! Это {country_name}. \n\n{full_country_name}."
            border_color = 'red'
        print(answer)
        return render_template('flags.html', img=country_flag, message=message, bc=border_color)


if __name__ == '__main__':
    app.run(debug=False)
