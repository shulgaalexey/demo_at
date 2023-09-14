from bottle import Bottle, run, request, response

app = Bottle()

# In-memory storage for user data, usually you'd use a database
user_data = {
    'valid_username': {'name': 'Valid Username', 'email': 'valid@example.com', 'recent_usage': 'myteapot'},
    'john.doe': {'name': 'John Doe', 'email': 'john.doe@example.com', 'recent_usage': 'cloudbuild'},
    'jane.doe': {'name': 'Jane Doe', 'email': 'jane.doe@example.com', 'recent_usage': 'cloudtest'},
    # Add more users as needed
}

@app.get('/api/knowledge/<username>')
def get_user_information(username):
    # Look up user data by username
    print('Lookup for user: ' + username)
    user = user_data.get(username)
    
    if user is None:
        response.status = 404
        return {'error': 'User not found'}
    
    return user

if __name__ == '__main__':
    run(app, host='localhost', port=18082)
