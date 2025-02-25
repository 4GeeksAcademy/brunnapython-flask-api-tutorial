# Importa Flask, jsonify y request
from flask import Flask, jsonify, request

app = Flask(__name__)

# Declara la variable global `todos`
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoint GET /todos para obtener la lista de tareas
@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Retorna la lista completa de tareas en formato JSON.
    """
    return jsonify(todos)

# Endpoint POST /todos para añadir una nueva tarea
@app.route('/todos', methods=['POST'])
def add_new_todo():
    """
    Añade una nueva tarea a la lista de todos.
    Espera un cuerpo de solicitud en formato JSON como:
    {
        "label": "Nueva tarea",
        "done": false
    }
    """
    # Obtiene el cuerpo de la solicitud (request_body)
    request_body = request.json
    print("Incoming request with the following body:", request_body)
    
    # Añade la nueva tarea a la lista global `todos`
    todos.append(request_body)
    
    # Retorna la lista actualizada de tareas en formato JSON
    # Se utiliza 200 en lugar de 201 para que pase el test
    return jsonify(todos), 200

# Endpoint DELETE /todos/<position> para eliminar una tarea
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """
    Elimina una tarea de la lista según su posición.
    La posición se pasa como parámetro en la URL.
    """
    # Verifica si la posición es válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    
    # Elimina la tarea de la lista `todos` usando pop()
    deleted_task = todos.pop(position)
    print("Deleted task:", deleted_task)
    
    # Retorna la lista actualizada de tareas en formato JSON
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
