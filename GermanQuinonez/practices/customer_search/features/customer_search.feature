Feature: Customer search

  Background: Search of a total priced for a list clients

    Given I have a list Clients


  Scenario Outline:
    Given I have a list Total price
    When I search  a <client> with <id>
    And A  <total_price>
    Then I should found  this client int the list

    Examples:
      | id   | client | total_price |
      | 1000 | Peter  | $500        |
      | 1001 | Maria  | $550        |
      | 1002 | James  | $600        |

  Scenario:Search a client

    When I search  a Peter in the list
    Then I should found him in the list