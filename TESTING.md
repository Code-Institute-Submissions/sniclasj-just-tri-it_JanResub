# Testing

# Browser Compatibility

Due to the numerous number of pages available to test, a different page will be showcased for the different browsers below to demonstrate browser compatibility.

## Chrome

![Chrome](documentation/testing/jti-chrome.png)

## Edge

![Edge](documentation/testing/jti-edge.png)

## Safari (Mobile)

![Safari](documentation/testing/jti-safari.png)

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

I was unsure of how to resolve these errors as they were seemingly inherited into my code. As I did not write the code causing these errors, I have included this section to demonstrate that I understand where the errors came from.

Finally, I have not included the html pages inherited from allauth in this section. A spot check of the sign up and sign out page yielded no errors.

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

Due to the numerous number of pages available to test, spot checks were conducted on the Home page, the Listings Page and the Listings Info page. The results are summarised in the screenshots below.

## Home Responsive

![Home Responsive](documentation/testing/jti-home-responsive.jpg)

## Listings Responsive

![Listings Responsive](documentation/testing/jti-listings-responsive.jpg)

## Listing Info Responsive

![Listing Info Responsive](documentation/testing/jti-listing_info-responsive.jpg)


# User Story Tests

- As a user, I want to be able to add various listings to my basket before completing a purchase via a check out.
![User Story A](documentation/testing/user-stroy-a.png)
- As a user, I want to be able to filter listings by the three main triathlon disciplines of Swim, Bike and Run.
![User Story B](documentation/testing/user-stroy-b.png)
- As a user, I want to be able to filter listings by their condition such as New, Excellent, Good or Used.
![User Story C](documentation/testing/user-stroy-c.png)
- As a user, I want to be able to see an overall summary of all listings available to purchase.
![User Story D](documentation/testing/user-stroy-d.png)
- As a user, I want to be able to click on an individual listing to see more information regarding the listing.
![User Story E](documentation/testing/user-stroy-e.png)
- As a user, I want to be able to vary the quantity of a listing I can input into the basket when viewing the listing.
![User Story F](documentation/testing/user-stroy-f.png)
- As a user, I want to be able to update the quantity and/or remove a listing from my basket.
![User Story G](documentation/testing/user-stroy-g.png)
- As a user, I want to be able to create an account/profile.
![User Story H](documentation/testing/user-stroy-h.png)
- As a user, I want to be able to save default information in my account profile.
![User Story I](documentation/testing/user-stroy-i.png)
- As a user, I want to be able to view my previous order history.
![User Story J](documentation/testing/user-stroy-j.png)
- As a user with seller status, in addition to the above, I want to be able to add, edit and delete any listings I have uploaded.
![User Story K](documentation/testing/user-stroy-k.png)
- As a super user, in addition to the above, I want to be able to edit and delete any listing on the site.
![User Story L](documentation/testing/user-stroy-l.png)
- As a super user, in addition to the above, I want to be able to update a registered profile’s seller status.
![User Story M](documentation/testing/user-stroy-m.png)
- As a super user, in addition to the above, I want to be able to add, edit and delete categories and conditions.
![User Story N](documentation/testing/user-stroy-n.png)


# Error Handling

I am relying on Django's built in error handling as I had to prioritise other aspects of the site's functionality.

# Unfixed Bugs

-	Country dropdown on forms is a different colour to other fields, needs a CSS and JS fix.
-	Allauth pages are not formatted in the same style as the rest of the site.
-	If a product is deleted, the Order History on the Athlete Profile page just shows a blank space where the listing name shoud be along with a cost of £0.
-	I made an error at some point in the coding process and the loading-spinner icon no longer overlayed on the page whilst awaiting for checkout success. It was always displaying on the checkout page. It requires a CSS and JS fix but I had to prioritise other functionality over solving this bug.
- The 'Clear' button shows next to a listing's image but it has no functionality. Again, this needs a CSS/JS fix but I had to prioritise other functionality over this.
