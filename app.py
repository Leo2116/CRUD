from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

alumnos = [
    {'id': 1, 'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 20},
    {'id': 2, 'nombre': 'María', 'apellido': 'Gómez', 'edad': 22},
]
next_id = 3

@app.route('/')
def index():
    return render_template('index.html', alumnos=alumnos)

@app.route('/crear', methods=['GET', 'POST'])
def crear_alumno():
    global next_id
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = int(request.form['edad'])
        
        nuevo_alumno = {
            'id': next_id,
            'nombre': nombre,
            'apellido': apellido,
            'edad': edad
        }
        alumnos.append(nuevo_alumno)
        next_id += 1
        return redirect(url_for('index'))
    return render_template('crear_alumno.html')

@app.route('/editar/<int:alumno_id>', methods=['GET', 'POST'])
def editar_alumno(alumno_id):
    alumno = next((a for a in alumnos if a['id'] == alumno_id), None)
    if not alumno:
        return "Alumno no encontrado", 404
        
    if request.method == 'POST':
        alumno['nombre'] = request.form['nombre']
        alumno['apellido'] = request.form['apellido']
        alumno['edad'] = int(request.form['edad'])
        return redirect(url_for('index'))
        
    return render_template('editar_alumno.html', alumno=alumno)

@app.route('/eliminar/<int:alumno_id>')
def eliminar_alumno(alumno_id):
    global alumnos
    alumnos = [a for a in alumnos if a['id'] != alumno_id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    
    app.run(debug=True)