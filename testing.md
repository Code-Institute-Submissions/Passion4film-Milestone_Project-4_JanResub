# Manual Testing Evidence

### Using Django Framework

- In terms of registration and user accounts – all user stories can be mostly completed using a popular pre-built package called Django-allauth. 
I used this package as it already has all the features needed to create a site, it is customisable and it’s open source so it’s backed by millions of 
developers who keep it secure and current.

### Search function

- I used a special object from Django.db.models called Q to generate the search query. In Django if you use something like product.objects.filter in order to filter a list of products everything will be ended together. In the case of our queries that would mean that when a user submits a query for it to match the term would have to appear in both the product name and the product description. Instead, we want to return results where the query was matched in either the product name or the description so in order to accomplish this, we need to use Q

### Toasts

- To make a better shopping experience for the user the site makes use of a feature of bootstrap called toasts. This gives the site nice notifications that can be customized and the Django messages framework can be used to create the messages needed to communicate with the users as they shop on the store.

- Django messages have ‘levels’ which are classifiers like debug, info, error, etc for different message types. The Django Docs shows that these levels can be represented with an integer. The level we put in the code will determine which of our includes is rendered based on the message level. Using a ‘with’ statement the level of the message can be checked and the toast message we want will be rendered.

- In Django, a message of level 40 is an error, Level 30 is a warning, Level 25 is success, and it defaults to using the info toast for everything else.

### Stripe Payments

- Stripe works with payment intents. When a user clicks on the checkout button on the page the checkout view will connect with stripe and create a payment intent for the current amount of the shopping bag. Stripe will create a client_secret that identifies it and Which will be returned to the site and sent to the template as the client secret variable. Then in the JavaScript on the client side the confirm card payment method from stripe js is called using the client_secret which will verify the card number.

- It was important to build some redundancy for making stripe payments in case the users intentionally or accidentally closed the browser window after the payment is confirmed but before the form was submitted. If that happened without redundancy planning there would be a payment in stripe but no order in the site database.

- Also, for a real store that needs to complete post order operations like sending internal email notifications etc, it wouldn’t be triggered because the user never fully completed their order. Which might result in a customer being charged and never receiving a confirmation email or not receiving what they ordered.

- The redundancy added to the code meant that each time an event occurs on stripe such as a payment intent being created or completed etc, stripe sends out a webhook we can listen for. Webhooks are like the signals django sends each time a model is saved or deleted, except that they're sent securely from stripe to a URL we specify.

### Creating the order

* This code ensures that when we receive a webhook from stripe that a payment has been processed successfully. The code will try to find an order with the same customer information and the same grand total, which was created with the exact same shopping bag and it's associated with the same payment intent. It will also attempt this multiple times before giving up, to create the order in the webhook. There may still be a rare number of cases where this fails, but in almost all cases this will guarantee that if this order isnt found in the database it's safe to create it here.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-4_npxgp1.png" style="margin: 0;">


### Webhook payment intent success

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-3_w0wm7r.png" style="margin: 0;">


<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510976/Screenshots/webhooks-5_o7197l.png" style="margin: 0;">


### After commenting out the form submit to test what it would be like if a user closed the page before the form was submitted

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-6_x6tsuh.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510976/Screenshots/webhooks-7_anexso.png" style="margin: 0;">

### Setting up emails

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/emails-1_klpeqh.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/emails-2_apby3j.png" style="margin: 0;">

### Creating CRUD functions for superuser (site admin)

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-1_zjaxcr.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-2_lrfqww.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-3_ohrgsg.png" style="margin: 0;">

### Defensive programming for edit/delete - Install login_required from Django

* This is to ensure only site admin have the ability to edit/add/delete products on the store - not any user who knows or guesses the correct url

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/defensive-1_blrwpb.png" style="margin: 0;">


### Adding delete model for admin 

* For security against accidentally deleting products, which cannot be recovered and have to be re-added to the store

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-4_qwetwd.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-5_jwouua.png" style="margin: 0;">


### Carousel for displaying multiple images on product details page 

* So the users can see the ‘kit’ that the painting comes with as per the description

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/images-1_dvbffx.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/images-2_es8phs.png" style="margin: 0;">

# Bugs and issues that needed to be overcome:

## 1

* Expected

    - 

* Testing

    -  

* Result

    - 

* Fix

    - 

## 2

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

## 3

* Expected

    - 

* Testing

    - 

* Result

    - 

* Fix

    - 

[Return to README](README.md)