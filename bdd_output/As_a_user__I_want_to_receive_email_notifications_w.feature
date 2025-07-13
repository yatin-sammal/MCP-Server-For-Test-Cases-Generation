Feature: Receive email notifications when order ships

Scenario: User receives email notification when order ships
  Given a user has placed an order
  When the order is shipped
  Then the user receives an email notification that the order has shipped