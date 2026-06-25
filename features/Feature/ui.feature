Feature: UI Test for Amazon Website

Scenario: Home Page Navigation
Given I navigate to the Amazon Home Page
Then I should see navigation elements
And I take screenshot of the full Page


Scenario: Category Navigation
Given I navigate to the Amazon Home Page
When I click on the Category menu
Then I should be redirect to Categorypage
And I take screenshot of the full Page

Scenario: Search functionality
Given I navigate to the Amazon Home Page
When I search for a product
Then I should see search results 
And I take screenshot of the full Page
