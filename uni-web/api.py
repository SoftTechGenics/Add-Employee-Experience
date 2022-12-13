from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

'''
Examples:
GET request to /api/employees returns the details of all employees
POST request to /api/employees creates a employee with the ID 4 (As per request body)
Sample request body -
{
        "employee_id": "1",
        "name" : "Bella",
        "email": "bella22@gamil.com",
        "mobile": "09865434",
        "job_title" : "HOD"
        "experience":"Bella carries multiple technical degrees in nuclear physics and worked at CERN as a Python developer, implementing dynamic performance optimizations for complex web applications. She rapidly integrates reliable web technologies and achieves flexible software architecture designs. Her strong theoretical and practical background in IT, business consulting, and project management make her extremely capable of projects of any size."
}
GET request to /api/employee/4 returns the details of employee 4
PUT request to /api/employee/4 to update fields of employee 4
DELETE request to /api/employee/4 deletes employee 4
'''

table = db['employees']



def fetch_db(employee_id):  # Each employee scnerio
    return table.find_one(employee_id=employee_id)


def fetch_db_all():
    employees = []
    for employee in table:
        employees.append(employee)
    return employees


@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    table.insert({
        "employee_id": "1",
        "name" : "Bella",
        "email": "bella22@gamil.com",
        "mobile": "09865434",
        "job_title" : "HOD"
        "experience":"Bella carries multiple technical degrees in nuclear physics and worked at CERN as a Python developer, implementing dynamic performance optimizations for complex web applications. She rapidly integrates reliable web technologies and achieves flexible software architecture designs. Her strong theoretical and practical background in IT, business consulting, and project management make her extremely capable of projects of any size."
    })

    table.insert({
        "employee_id": "2",
        "name" : "Zoran Melis",
        "email": "zoraan2@gamil.com",
        "mobile": "09885434",
        "job_title" : "Teacher"
        "experience":"Zoran is a software engineer with over ten years of professional experience with a wide range of technologies. He has worked with C/C++, Python, Go, JavaScript, Java, and more. Currently focusing on full-stack, scalable applications development, he has been a part of teams of all sizes in environments ranging from small private companies to Google"
        
    })

    table.insert({
       "employee_id": "3",
        "name" : "Alexander",
        "email": "alexander554@gamil.com",
        "mobile": "09844334",
        "job_title" : "cleark"
        "experience":"Professional, efficient office clerk with 6+ years experience working for a large corporate organization. Promoted to executive secretary in 2017. Introduced a time management system and increased the efficiency of the office by 15%. "
    })

    return make_response(jsonify(fetch_db_all()),
                         200)


@app.route('/api/employees', methods=['GET', 'POST'])
def api_employees():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        employee_id = content['employee_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(employee_id)), 201)  # 201 = Created


@app.route('/api/employees/<employee_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_employee(employee_id):
    if request.method == "GET":
        employee_obj = fetch_db(employee_id)
        if employee_obj:
            return make_response(jsonify(employee_obj), 200)
        else:
            return make_response(jsonify(employee_obj), 404)
    elif request.method == "PUT":  # Updates the employee
        content = request.json
        table.update(content, ['employee_id'])

        employee_obj = fetch_db(employee_id)
        return make_response(jsonify(employee_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=employee_id)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)








