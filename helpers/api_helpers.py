from helpers.validate_response import validate_response

def get_products(api_client):
    response = api_client.get_products()
    return validate_response(response)

def get_single_product(api_client, id):
    response = api_client.get_single_product(id)
    return validate_response(response)

def get_limit_results(api_client, value):
    response = api_client.get_limit_results(value)
    return validate_response(response)

def get_sort_results(api_client, value):
    response = api_client.sort_results(value)
    return validate_response(response)