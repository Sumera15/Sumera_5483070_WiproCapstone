Feature: Myntra End To End Flow

  Background:
    Given User launches Myntra application

  @e2e @myntra
  Scenario: Successful saree purchase flow

    When User hovers on Women section
    And User opens Fusion Wear page
    And User applies Sarees filter
    And User selects Blue color filter
    And User sorts products by Customer Rating
    And User selects first saree product
    And User adds product to bag
    And User opens bag page
    And User increases quantity to 2
    And User selects quantity Done button
    And User selects donation amount
    And User clicks Place Order
    Then User should navigate to login page