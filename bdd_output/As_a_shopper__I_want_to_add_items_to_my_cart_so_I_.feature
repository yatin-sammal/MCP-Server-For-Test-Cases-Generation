Feature: Add items to cart

Scenario: Add a single item to cart
  Given the shopper is on the product details page
  When the shopper clicks the "Add to cart" button
  Then the item should be added to the cart

Scenario: Add multiple items to cart
  Given the shopper is on the product details page
  When the shopper clicks the "Add to cart" button multiple times
  Then all items should be added to the cart

Scenario: Add an item to cart when cart is empty
  Given the shopper has an empty cart
  When the shopper clicks the "Add to cart" button
  Then the item should be added to the cart

Scenario: Add an item to cart when cart is not empty
  Given the shopper has items in the cart
  When the shopper clicks the "Add to cart" button
  Then the new item should be added to the cart
