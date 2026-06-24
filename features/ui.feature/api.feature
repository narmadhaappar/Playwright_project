Feature: API CRUD operations

Scenario: Create, read, Update and delete operations

Given user has generated resource data
When user Create new resource
Then resource shouold be created
When user retrieves the created resource
Then retrieved resource should match created resource
When user Update the resource
Then resource should be Updated successfully
When user delete the resource
Then resource should be deleted successfully