from pytest_bdd import scenarios, given, when, then
from utils.data_generator import DataGenerator
from utils.api_utils import APIUtils

scenarios('../features/Feature/api.feature')

@given('user has generated resource data')
def generated_resource_data(context):
    context.payload = DataGenerator.generate_random_data()

@when('user Create new resource')
def create_new_resource(api_utils, context):
    context.create_response = api_utils.post("v2/pet", context.payload)
    print(context.create_response.url)
    print("status code:", context.create_response.status)
    print("response body:", context.create_response.text())
    assert context.create_response.status == 200
    context.create_pet = context.create_response.json()

@then('resource shouold be created')
def resource_created_successfully(context):
    assert context.create_response.status == 200
    assert context.create_pet['name'] == context.payload['name']
    assert context.create_pet['category']['name'] == context.payload['category']['name']
    assert context.create_pet['tags'][0]['name'] == context.payload['tags'][0]['name']

@when('user retrieves the created resource')
def retrieve_created_resource(api_utils, context):
    pet_id = context.create_pet['id']
    context.retrieve_response = api_utils.get(f'v2/pet/{pet_id}')
    print("GET URL",context.retrieve_response.url)
    print("GET STATUS",context.retrieve_response.status)
    print("GET Body",context.retrieve_response.text())

    assert context.retrieve_response.status == 200
    context.retrieved_pet = context.retrieve_response.json()

@then('retrieved resource should match created resource')
def retrieved_resource_matches_created_resource(context):
    assert context.retrieved_pet['id'] == context.create_pet['id']
    assert context.retrieved_pet['name'] == context.create_pet['name']
    assert context.retrieved_pet['category']['name'] == context.create_pet['category']['name']
    assert context.retrieved_pet['tags'][0]['name'] == context.create_pet['tags'][0]['name']

@when('user Update the resource')
def update_resource(api_utils, context):
    pet_id = context.create_pet['id']
    updated_payload = context.payload.copy()
    updated_payload['id'] = pet_id
    updated_payload['name'] = "Updated_" + updated_payload['name']
    context.updated_payload = updated_payload
    context.update_response = api_utils.put(f'v2/pet', updated_payload)
    context.updated_pet = context.update_response.json()


@then('resource should be Updated successfully')
def resource_updated_successfully(context):
    print("Update URL",context.update_response.url)
    print("Update STATUS",context.update_response.status)
    print("Update Body",context.update_response.text())
    assert context.update_response.status == 200
    assert context.updated_pet['name'] == context.updated_payload['name']

@when('user delete the resource')
def delete_resource(api_utils, context):
    pet_id = context.create_pet['id']
    context.delete_response = api_utils.delete(f'v2/pet/{pet_id}')    

@then('resource should be deleted successfully')
def resource_deleted_successfully(api_utils, context):
    assert context.delete_response.status == 200
    pet_id = context.create_pet['id']
    retrieve_response = api_utils.get(f'v2/pet/{pet_id}')
    print("GET after deletion", retrieve_response.status)
    print(retrieve_response.text())
    assert retrieve_response.status == 404