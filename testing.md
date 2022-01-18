# Manual Testing Evidence

### Using Django Framework

- In terms of registration and user accounts – all user stories can be mostly completed using a popular pre-built package called Django-allauth. 
I used this package as it already has all the features needed to create a site, it is customisable and it’s open source so it’s backed by millions of 
developers who keep it secure and current.

### Search function

- I used a special object from Django.db.models called Q to generate the search query. In Django if you use something like product.objects.filter in order to filter a list of products everything will be grouped together. In the case of queries that would mean that when a user submits a query, the term would have to appear in both the product name and the product description. Instead, we want to return results where the query was matched in either the product name or the description so in order to accomplish this, we need to use Q

### Toasts

- To make a better shopping experience for the user the site makes use of a feature of bootstrap called toasts. This gives the site nice notifications that can be customized and the Django messages framework can be used to create the messages needed to communicate with the users as they shop on the store.

- Django messages have ‘levels’ which are classifiers like debug, info, error, etc for different message types. The Django Docs shows that these levels can be represented with an integer. The level put in the code will determine which of the includes is rendered based on the message level. Using a ‘with’ statement the level of the message can be checked and the toast message we want will be rendered.

- In Django, a message of level 40 is an error, Level 30 is a warning, Level 25 is success, and it defaults to using the info toast for everything else.

### Stripe Payments

- Stripe works with payment intents. When a user clicks on the checkout button on the page the checkout view will connect with stripe and create a payment intent for the current amount of the shopping bag. Stripe will create a client_secret that identifies it, which will be returned to the site and sent to the template as the client secret variable. Then in the JavaScript on the client side the confirm card payment method from stripe.js is called using the client_secret which will verify the card number.

- It was important to build some redundancy for making stripe payments in case the users intentionally or accidentally closed the browser window after the payment is confirmed but before the form was submitted. If that happened without redundancy planning there would be a payment in stripe but no order in the site database.

- Also, for a real store that needs to complete post order operations like sending internal email notifications etc, it wouldn’t be triggered because the user never fully completed their order. Which might result in a customer being charged and never receiving a confirmation email or not receiving what they ordered.

- The redundancy added to the code meant that each time an event occurs on stripe such as a payment intent being created or completed etc, stripe sends out a webhook that can be listened for. Webhooks are the signals django sends each time a model is saved or deleted, except that they're sent securely from stripe to a URL specified.

### Creating the order

* This code ensures that when we receive a webhook from stripe that a payment has been processed successfully. The code will try to find an order with the same customer information and the same grand total, which was created with the exact same shopping bag and it's associated with the same payment intent. It will also attempt this multiple times before giving up, to create the order in the webhook. There may still be a rare number of cases where this fails, but in almost all cases this will guarantee that if this order isnt found in the database it's safe to create it here.

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-4_npxgp1.png" style="margin: 0;">


### Webhook payment intent success

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-3_w0wm7r.png" style="margin: 0;">


<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510976/Screenshots/webhooks-5_o7197l.png" style="margin: 0;">


-   ### After commenting out the form submit to test what it would be like if a user closed the page before the form was submitted

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/webhooks-6_x6tsuh.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510976/Screenshots/webhooks-7_anexso.png" style="margin: 0;">

### Setting up emails

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/emails-1_klpeqh.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/emails-2_apby3j.png" style="margin: 0;">

-   ### Creating CRUD functions for superuser (site admin)

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-1_zjaxcr.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-2_lrfqww.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-3_ohrgsg.png" style="margin: 0;">

### Defensive programming for edit/delete - Install login_required from Django

* This is to ensure only site admin have the ability to edit/add/delete products on the store - not any user who knows or guesses the correct url

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/defensive-1_blrwpb.png" style="margin: 0;">


-   ### Adding delete model for admin 

* For security against accidentally deleting products, which cannot be recovered and have to be re-added to the store

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-4_qwetwd.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510974/Screenshots/admin-5_jwouua.png" style="margin: 0;">


### Carousel for displaying multiple images on product details page 

* So the users can see the ‘kit’ that the painting comes with as per the description

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/images-1_dvbffx.png" style="margin: 0;">

<img src="https://res.cloudinary.com/passion4film/image/upload/v1632510975/Screenshots/images-2_es8phs.png" style="margin: 0;">

# Bugs and issues that needed to be overcome:

## The minus quantity button in the bag 

* Expected

    - The minus button is supposed to be disabled when the quantity is 1 - so that the user cannot add 0 or - items into their bags.

* Testing

    - When setting up the bag view to be mobile friendly the quantity-form is created twice, one or the other is hidden depending on the screen size. However, as the quantity-form uses an ID to identify itself, only the first element within the HTML with that ID is picked up by the corresponding code. Even though you can only see one form at a time in the browser, they both exist within the HTML. 

* Result

    - On larger screens the minus quantity button wasnt disabled and caused the user to be able to minus it beyond 1.

* Fix

    - To fix this issue I changed the ID on the quantity-form to a class, and refactor the JavaScript to look for elements with the same class name instead of ID and perform the appropriate actions. I also had to do this for the product details minus button as they shared the same Javascript code.

## Getting the Carousel to work

* Expected

    - I wanted to add in an extra image to the product description page to show what was in the 'kit' as per the description, I wanted the user to be able to change the picture as and when they wanted using directional buttons

* Testing

    - I took the code from Bootstrap initially from their documents page and the html aspect of the Carousel was ok - but I didn't like the format of the directional buttons.

* Result

    - In the first test the directional buttons didnt work, but the images rotated automatically after a time interval.

* Fix

    - I found a site to help me with the bootstap code [as credited in readme](https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-carousel.php), with this I was able to remove the interval rotation of the images and correct the JS to allow the directional buttons to work on the image - the buttons also looked better and has an indicator at the bottom to show only 2 images are available.

## Deletion Confirmation Model (for Admin only)

* Expected

    - There was a security issue with the option to delete the products for the site administrator - if they clicked the 'delete' button the product would be automatically deleted with no way to undo this action - there was therefore a risk that it could be triggered accidentally.

* Testing

    - Again I tried to take the model code from Bootstrap documentation for models.

* Result

    - In the first test I couldnt get the model to trigger as I had the 'delete' option as an anchor tag with a href to delete the product, and the Bootstrap model used buttons.

* Fix

    - I found a site to help me with the bootstap code [as credited in readme](https://www.tutorialrepublic.com/codelab.php?topic=bootstrap&file=delete-confirmation-modal), with this I was able to keep the 'delete' as an anchor tag - but trigger the model to pop open with a warning message - only by clicking the 'delete' button (in red to make it a clear warning) does the delete product activate and the product is deleted properly.

[Return to README](README.md)