from bottle import Bottle, run, request, response

app = Bottle()

# Store IcM tickets in a list (only for demonstration purposes; in a real app you'd use a database)
tickets = []

@app.post('/api/icm/ticket')
def create_icm_ticket():
    # Parse JSON body of the request
    try:
        data = request.json
        title = data['title']
        body = data['body']
        severity_level = data['severity_level']
    except TypeError:
        response.status = 400
        return {"error": "Bad Request", "message": "Invalid input data format"}

    # Validate the data (simplified validation for demonstration)
    if not title or not body or not severity_level:
        response.status = 400
        return {"error": "Bad Request", "message": "Missing required fields"}

    # Create a new IcM ticket (again, this would be more sophisticated in a real app)
    ticket_id = len(tickets) + 1
    new_ticket = {
        'id': ticket_id,
        'title': title,
        'body': body,
        'severity_level': severity_level
    }
    tickets.append(new_ticket)

    # Respond with the created IcM ticket
    response.status = 201
    return new_ticket

if __name__ == '__main__':
    run(app, host='localhost', port=18081)
