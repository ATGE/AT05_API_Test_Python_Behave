Feature: Gmail account

  Scenario: Create a new gmail account

    Given I am on form Gmail new account
      And I fill First name with Nombre
      And I fill Last name with Apellido
      And I fill username with UserName
      And I fill password with Passwor123
      And I select Birthday Month on January
      And I fill Day with 1
      And I fill Year with 2000
      And I select Gender on Male
      And I fill Mobile phone with +59170707070
      And I fill Current email address with user@mail.com
