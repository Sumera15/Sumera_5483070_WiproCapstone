Feature: Myntra End To End Flow

  Background:
    Given User launches Myntra application

  @e2e @myntra
  Scenario: Successful saree purchase flow

    When User hovers on Women section
    And User opens Saree page
    And User selects Blue saree color
    And User selects first saree product
    And User adds product to bag
    And User opens bag page
    And User increases quantity to 2
    And User clicks Place Order
    Then User should navigate to login page