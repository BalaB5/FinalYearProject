from flask import Flask ,render_template,request, jsonify

from chat import get_response

app =Flask(__name__)

@app.get('/')
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text  = request.get_json().get("message")
    response = get_response(text)

    message ={"answer":response}
    return jsonify(message)

# User Login API
@app.route('/login', methods=['POST'])
def login():
    # Validate credentials
    username = request.json['username']
    password = request.json['password']

    # Authenticate against database or authentication mechanism
    # Add your authentication logic here

    # Return appropriate response
    if ("authenticated"=="uu"):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

# Interview API based on Department
@app.route('/interviews/<department>', methods=['GET'])
def get_interviews_by_department(department):
    # Retrieve interview details based on department
    # Add your logic to fetch interview details here

    # Return interview details
    return jsonify({'interviews': "interview_details"})

# Employee Details Add and Update API
@app.route('/employees', methods=['POST'])
def add_or_update_employee():
    # Parse employee details from request body
    employee_data = request.json

    # Process and update employee data in the database
    # Add your logic to handle employee details here

    # Return success message
    return jsonify({'message': 'Employee details updated successfully'})

# Employee Details Check APIs
@app.route('/employees/<employee_id>', methods=['GET'])
def get_employee_details(employee_id):
    # Retrieve employee details based on employee ID
    # Add your logic to fetch employee details here

    # Return employee details
    return jsonify({'employee': "employee_details"})


if __name__ =="__main__":
    app.run(debug=True) 