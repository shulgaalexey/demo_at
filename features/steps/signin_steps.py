from behave import given, when, then
import requests

BASE_URL = "http://localhost:18080/api"


@given('a user with "{valid_or_not}" credentials')
def user_with_valid_credentials(context, valid_or_not):
    postfix = {"valid": "", "invalid": "garbage"}
    context.username = "valid_username"
    context.password = "valid_password" + postfix[valid_or_not] 


@given('a user with invalid credentials')
def user_with_invalid_credentials(context):
    context.username = "invalid_username"
    context.password = "invalid_password"


@when('the user sends signin request')
def user_sends_signin_request(context):
    data = {
        'username': context.username,
        'password': context.password
    }
    context.response = requests.post(f'{BASE_URL}/signin', json=data)


@then('the response status should be "{resp_code}"')
def resp_code_should_be(context, resp_code):
    print('Expected: ' + resp_code + ' Actual: ' + str(context.response.status_code))
    assert context.response.status_code == int(resp_code)


@then('the response should contain a valid JWT token')
def response_should_contain_valid_jwt(context):
    json_response = context.response.json()
    assert 'token' in json_response
    assert len(json_response['token']) > 0
