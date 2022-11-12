# Testing

# Browser Compatibility

## Chrome

## Edge

## Safari (Mobile)

# Code Validation

## HTML

Prior to displaying the results of the screeshots, I would like to make a note of the errors displayed for the following pages:
- add_category
- add_condition
- add_listing
- edit_category
- edit_condition
- edit_listing
- profile

The errors are caused by stray start tags ```<th>```, ```<tr>``` and ```<td>``` as well as stray end tags ```</th>```, ```</tr>``` and ```</td>```. All of the above pages utilise ```{{ form }}``` within the code where this issue arises from as shown in the screenshot below.

![Error Justification Screenshot](documentation/testing/jti-html-testing-stray-tag-justification.png)

Again, I feel that these errors are out of my control and must unfortunately be accepted.

### basket.html

![Basket](documentation/testing/jti-html-testing-basket.png)

### checkout_success.html

![Checkout Success](documentation/testing/jti-html-testing-checkout-success.png)

### checkout.html

![Checkout](documentation/testing/jti-html-testing-checkout.png)

### index.html

![Index](documentation/testing/jti-html-testing-index.png)

### add_category.html

![Add Category](documentation/testing/jti-html-testing-add_category.png)

### add_condition.html

![Add Condition](documentation/testing/jti-html-testing-add_condition.png)

### add_listing.html

![Add Listing](documentation/testing/jti-html-testing-add_listing.png)

### categories_conditions.html

![Categories Conditions](documentation/testing/jti-html-testing-categories_conditions.png)

### edit_category.html

![Edit Category](documentation/testing/jti-html-testing-edit_category.png)

### edit_condition.html

![Edit Condition](documentation/testing/jti-html-testing-edit_condition.png)

### edit_listing.html

![Edit Listing](documentation/testing/jti-html-testing-edit_listing.png)

### listing_info.html

![Listing Info](documentation/testing/jti-html-testing-listing_info.png)

### lisitngs.html

![Listings](documentation/testing/jti-html-testing-listings.png)

### edit_seller_status.html

![Edit Seller Status](documentation/testing/jti-html-testing-edit_seller_status.png)

### profile_admin.html

![Profile Admin](documentation/testing/jti-html-testing-profile_admin.png)

### profile.html

![Profile Admin](documentation/testing/jti-html-testing-profile.png)

### base.html

As there are no errors arising from my own code across all pages where base.html is extended, it is assumed that there are no errors in base.html.

## CSS

Although the [CSS Validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjust-tri-it.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors) one error and numerous warnings. All of these are from Materialize CSS. Unfortunately, these errors have to be accepted as they are inherited from the vendor extension selected for this project. I have found Materialize difficult to work with during this project and will utilise Bootstrap in future.

![CSS Validation Screenshot](documentation/testing/jti-css-validation.png)

## JavaScript

![JS Hint Validation Screenshot](documentation/testing/jti-testing-js-stripe-elements.png)

## Python

- As the website pep8online.com was not available to be used for validation. I utilised the python pycodestyle validation features built into the gitpod terminal.
- If the PROBLEMS tab showed that _no problems have been detected in the workspace_, I took this to mean that my python code was valid.
- I opened up all python files within a specific app and ensured that the terminal did not return any PROBLEMS.
- The results are documented in the screenshots below.
- Note: For certain lines of code greater than 79 characters, I had to use the # noqa decorator as breaking the code over two lines returned a syntax error.

### Basket App

![Basket Python Validation](documentation/testing/just-tri-it-python-validation-basket.png)

### Checkout App

![Checkout Python Validation](documentation/testing/just-tri-it-python-validation-checkout.png)

### Home App

![Home Python Validation](documentation/testing/just-tri-it-python-validation-home.png)

### Listings App

![Listings Python Validation](documentation/testing/just-tri-it-python-validation-listings.png)

### Main App

![Main Python Validation](documentation/testing/just-tri-it-python-validation-main.png)

### Profiles App

![Profiles Python Validation](documentation/testing/just-tri-it-python-validation-profiles.png)

### custom_storages.py, env.py and manage.py

![No App Python Validation](documentation/testing/just-tri-it-python-validation-custom-storages-env-manage.png)

# Lightouse

Due to the numerous number of pages available to test, spot checks were conducted on the Home page and the All Listings page. The results are summarised in the screenshot below.

### Home Page Lighthouse

![Home Page Lighthouse](documentation/testing/jti-lighthouse.png)

### Listings Page Lighthouse
![Listings Page Lighthouse](documentation/testing/jti-lighthouse-listings.png)

# Responsiveness

Due to the numerous number of pages available to test, spot checks were conducted on XXX. The results are summarised in the screenshot below.



# Error Handling

# Unfixed Bugs