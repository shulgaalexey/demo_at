from behave import given, when, then
import requests

BASE_URL = "http://localhost:18080/api"


@when('the user gets documentation')
def user_sends_signin_request(context):
    context.response = requests.get(f'{BASE_URL}/docs/myteapot')


@then('the response should contain the documentation content')
def response_should_contain_valid_jwt(context):
    json_response = context.response.json()
    assert 'data' in json_response
    assert json_response['data'] == "Wiki and Documentation for myteapot"


@given('"{valid_or_not}" IcM ticket data')
def given_valid_icm_data(context, valid_or_not):
    icm_data = {
        "valid": {
            "subject": "Need Support",
            "message": "I have an issue with my lovely teapot."
        },
        "invalid": "garbage"
    }
    context.support_data = icm_data[valid_or_not]

@when('the user creates IcM ticket')
def user_creates_icm(context):
    context.response = requests.post(f'{BASE_URL}/icm/myteapot', json=context.support_data)

@then('the response should contain valid IcM ticket ID')
def response_should_contain_icm_ticket_id(context):
    json_response = context.response.json()
    assert 'ticket_id' in json_response
    assert int(json_response['ticket_id']) >= 1

@then('the response should contain user knowledge')
def response_should_contain_user_knowledge(context):
    json_response = context.response.json()
    print(json_response)
    assert 'recent_usage' in json_response