#Feature: Myntra Positive And Negative Test Cases
#
#  Background:
#    Given User opens Myntra website
#
#
#  @positive
#  Scenario: Verify Kurti Navigation
#
#    When User clicks on Women section
#    And User opens Kurtis page
#    Then User should navigate to Kurtis page
#
#
#  @positive
#  Scenario: Verify Pink Tshirt Filter
#
#    When User searches for Tshirts
#    And User applies Pink color filter
#    Then Pink Tshirts should display
#
#
#  @positive
#  Scenario: Verify Earrings Add To Bag
#
#    When User searches for Earrings
#    And User selects first earrings product
#    And User adds earrings product to bag
#    Then Earrings product should add successfully
#
#
#  @positive
#  Scenario: Verify Flats Sorting
#
#    When User searches for Flats
#    And User sorts flats by Better Discount
#    Then Flats products should display properly
#
#
#  @negative
#  Scenario: Verify Size Validation
#
#    When User opens tshirt product
#    And User clicks Add to Bag without size
#    Then User should see size validation message
#
#
#  @negative
#  Scenario: Verify Pincode Validation
#
#    When User enters invalid pincode
#    Then User should see invalid pincode validation