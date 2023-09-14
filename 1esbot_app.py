from bottle import Bottle, run, request, response
import requests
import time


app = Bottle()

# Dummy user data for demonstration
users = {
    'valid_username': 'valid_password'
}

# Dummy token for demonstration
dummy_token = "some_jwt_token"

# curl -X POST http://localhost:18080/api/signin -H "Content-Type: application/json" -d '{"username":"valid_username", "password":"valid_password"}'
@app.post('/api/signin')
def user_sign_in():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username] == password:
        return {'status': 'success', 'token': dummy_token}
    else:
        response.status = 401
        return {'status': 'unauthorized'}

# curl http://localhost:18080/api/services
@app.get('/api/services')
def get_documentation():
    return {'status': 'success', 'data': 'myteapot, cloudtest, cloudbuild, devbox'}


# curl http://localhost:18080/api/docs/myteapot
@app.get('/api/docs/<service>')
def get_documentation(service):
    return {'status': 'success', 'data': f'Wiki and Documentation for {service}'}

# curl -X POST http://localhost:18080/api/icm/myteapot -H "Content-Type: application/json" -d '{"subject": "Need Support", "message": "I have an issue with my tea pot."}'
@app.post('/api/icm/<service>')
def create_support_ticket(service):
    data = request.json
    if data and "subject" in data and "message" in data:
        

        # Fetching knowledge of the customer
        

        knowledge_response = None
        try:
            knowledge_response = requests.get('http://localhost:18082/api/knowledge/valid_username')    
        except requests.exceptions.Timeout:
            print("Knowledge: Timeout")
        except requests.exceptions.TooManyRedirects:
            print("Knowledge: Too many redirects")
        except requests.exceptions.RequestException as e:
            print(e)
        #raise SystemExit(e)F
        knowledge_json_response = knowledge_response.json()
        print(knowledge_json_response)

        time.sleep(1)

        # Creating IcM ticket
        icm_data = {
            "title": "My Teapot b0rked",
            "body": "My lovely tea pot doesnt teapotting for me.",
            "severity_level": "2"
        }

        icm_response = None
        try:
            icm_response = requests.post('http://localhost:18081/api/icm/ticket', json=icm_data)
        except requests.exceptions.Timeout:
            print("IcM: Timeout")
        except requests.exceptions.TooManyRedirects:
            print("IcM: Too many redirects")
        except requests.exceptions.RequestException as e:
            print(e)
        icm_json_response = icm_response.json()
        response.status = icm_response.status_code
        print(icm_json_response)
        
        return {
            'service': f'{service}',
            'status': 'success',
            'recent_usage': knowledge_json_response['recent_usage'],
            'ticket_id': icm_json_response['id']
        }
    else:
        response.status = 400
        return {'status': 'bad_request', 'message': 'Invalid Data'}

if __name__ == '__main__':
    run(app, host='localhost', port=18080)
