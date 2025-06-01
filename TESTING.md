# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | [bag.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/bag/templates/bag/bag.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/validation/html-bag.png) | W3C link provided shows validation for empty bag. Full page content checked via text input as item must be added to bag by user to render full page content. |
| checkout | [checkout.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/templates/checkout/checkout.html) | No link provided | ![screenshot](documentation/validation/html-checkout.png) | No W3C link provided. Could not check by URI due to page requiring item to be put into bag to access. |
| checkout | [checkout_success.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/templates/checkout/checkout_success.html) | No link provided | ![screenshot](documentation/validation/html-checkout_success.png) | No WC3 link provided, as validation by URI requires order number. |
| contact | [contact.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/templates/contact/contact.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/validation/html-contact.png) |  |
| faqs | [faqs.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/templates/faqs/faqs.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Ffaqs%2F) | ![screenshot](documentation/validation/html-faqs.png) |  |
| faqs | [edit_faq.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/templates/faqs/edit_faq.html) | No link provided | ![screenshot](documentation/validation/html-edit_faq.png) | No W3C link provided. Could not check by URI due to page requiring authentication. |
| home | [index.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/home/templates/home/index.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2F) | ![screenshot](documentation/validation/html-index.png) |  |
| newsletter | [newsletter.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/templates/newsletter/newsletter.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Fnewsletter%2F) | ![screenshot](documentation/validation/html-newsletter.png) |  |
| products | [products.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/templates/products/products.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Fproducts%2F) | ![screenshot](documentation/validation/html-products.png) |  |
| products | [product_details.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/templates/products/product_details.html) | [HTML W3C Validator Link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2Fproducts%2F1%2F) | ![screenshot](documentation/validation/html-product_details.png) |  |
| products | [add_product.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/templates/products/add_product.html) | No link provided | ![screenshot](documentation/validation/html-products.png) | No W3C link provided. Could not check by URI due to page requiring authentication. |
| products | [edit_product.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/templates/products/edit_product.html) | No link provided | ![screenshot](documentation/validation/html-edit_product.png) | No W3C link provided. Could not check by URI due to page requiring authentication. |
| profiles | [profile.html](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/templates/profiles/profile.html) | No link provided | ![screenshot](documentation/validation/html-profile.png) | No W3C link provided. Could not check by URI due to page requiring authentication. |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| templates | [base.css](https://github.com/Ash-5p/double-whammy-guitars/blob/main/static/css/base.css) | [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdouble-whammy-guitars-47bed68ef1db.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/css-base.png) |  |
| checkout | [checkout.css](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/static/checkout/css/checkout.css) | No link provided | ![screenshot](documentation/validation/css-checkout.png) | Not able to validate via URI |
| products | [products.css](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/static/products/css/products.css) | No link provided | ![screenshot](documentation/validation/css-products.png) | Not able to validate via URI |
| profiles | [profile.css](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/static/profiles/css/profile.css) | No link provided | ![screenshot](documentation/validation/css-profile.png) | Not able to validate via URI |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | [stripe_elements.js](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/static/checkout/js/stripe_elements.js) | ![screenshot](documentation/validation/js-stripe_elements.png) | One unknown variable is from external Stripe library |
| faqs | [faqs.js](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/static/js/faqs.js) | ![screenshot](documentation/validation/js-faqs.png) | One unknown variable is from external bootstrap library |
| products | [products.js](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/static/products/js/products.js) | ![screenshot](documentation/validation/js-products.png) | One unknown variable is from external bootstrap library |
| products | [sorting.js](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/static/products/js/sorting.js) | ![screenshot](documentation/validation/js-sorting.png) | |
| profiles | [countryfield.js](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/static/profiles/js/countryfield.js) | ![screenshot](documentation/validation/js-countryfield.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | [bag_tools.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/main/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/py-bag-bag_tools.png) |  |
| bag | [contexts.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/bag/contexts.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/bag/contexts.py) | ![screenshot](documentation/validation/py-bag-contexts.png) |  |
| bag | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/bag/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/bag/urls.py) | ![screenshot](documentation/validation/py-bag-urls.png) |  |
| bag | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/bag/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/bag/views.py) | ![screenshot](documentation/validation/py-bag-views.png) |  |
| checkout | [admin.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/admin.py) | ![screenshot](documentation/validation/py-checkout-admin.png) |  |
| checkout | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/forms.py) | ![screenshot](documentation/validation/py-checkout-forms.png) |  |
| checkout | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/models.py) | ![screenshot](documentation/validation/py-checkout-models.png) |  |
| checkout | [signals.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/signals.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/signals.py) | ![screenshot](documentation/validation/py-checkout-signals.png) |  |
| checkout | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/urls.py) | ![screenshot](documentation/validation/py-checkout-urls.png) |  |
| checkout | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/views.py) | ![screenshot](documentation/validation/py-checkout-views.png) |  |
| checkout | [webhook_handler.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/py-checkout-webhook_handler.png) |  |
| checkout | [webhooks.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/checkout/webhooks.py) | ![screenshot](documentation/validation/py-checkout-webhooks.png) |  |
| contact | [admin.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/contact/admin.py) | ![screenshot](documentation/validation/py-contact-admin.png) |  |
| contact | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/contact/forms.py) | ![screenshot](documentation/validation/py-contact-forms.png) |  |
| contact | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/contact/models.py) | ![screenshot](documentation/validation/py-contact-models.png) |  |
| contact | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/contact/urls.py) | ![screenshot](documentation/validation/py-contact-urls.png) |  |
| contact | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/contact/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/contact/views.py) | ![screenshot](documentation/validation/py-contact-views.png) |  |
| faqs | [admin.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/faqs/admin.py) | ![screenshot](documentation/validation/py-faqs-admin.png) |  |
| faqs | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/faqs/forms.py) | ![screenshot](documentation/validation/py-faqs-forms.png) |  |
| faqs | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/faqs/models.py) | ![screenshot](documentation/validation/py-faqs-models.png) |  |
| faqs | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/faqs/urls.py) | ![screenshot](documentation/validation/py-faqs-urls.png) |  |
| faqs | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/faqs/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/faqs/views.py) | ![screenshot](documentation/validation/py-faqs-views.png) |  |
| home | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/home/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/home/urls.py) | ![screenshot](documentation/validation/py-home-urls.png) |  |
| home | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/home/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/home/views.py) | ![screenshot](documentation/validation/py-home-views.png) |  |
| main | [settings.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/main/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/main/settings.py) | ![screenshot](documentation/validation/py-main-settings.png) |  |
| main | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/main/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/main/urls.py) | ![screenshot](documentation/validation/py-main-urls.png) |  |
| newsletter | [admin.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/newsletter/admin.py) | ![screenshot](documentation/validation/py-newsletter-admin.png) |  |
| newsletter | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/newsletter/forms.py) | ![screenshot](documentation/validation/py-newsletter-forms.png) |  |
| newsletter | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/newsletter/models.py) | ![screenshot](documentation/validation/py-newsletter-models.png) |  |
| newsletter | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/newsletter/urls.py) | ![screenshot](documentation/validation/py-newsletter-urls.png) |  |
| newsletter | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/newsletter/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/newsletter/views.py) | ![screenshot](documentation/validation/py-newsletter-views.png) |  |
| products | [admin.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/products/admin.py) | ![screenshot](documentation/validation/py-products-admin.png) |  |
| products | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/products/forms.py) | ![screenshot](documentation/validation/py-products-forms.png) |  |
| products | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/products/models.py) | ![screenshot](documentation/validation/py-products-models.png) |  |
| products | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/products/urls.py) | ![screenshot](documentation/validation/py-products-urls.png) |  |
| products | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/products/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/products/views.py) | ![screenshot](documentation/validation/py-products-views.png) |  |
| profiles | [forms.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/profiles/forms.py) | ![screenshot](documentation/validation/py-profiles-forms.png) |  |
| profiles | [models.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/profiles/models.py) | ![screenshot](documentation/validation/py-profiles-models.png) |  |
| profiles | [urls.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/profiles/urls.py) | ![screenshot](documentation/validation/py-profiles-urls.png) |  |
| profiles | [views.py](https://github.com/Ash-5p/double-whammy-guitars/blob/main/profiles/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Ash-5p/double-whammy-guitars/refs/heads/main/profiles/views.py) | ![screenshot](documentation/validation/py-profiles-views.png) |  |

## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| FAQs | ![screenshot](documentation/responsiveness/mobile-faqs.png) | ![screenshot](documentation/responsiveness/tablet-faqs.png) | ![screenshot](documentation/responsiveness/desktop-faqs.png) | Works as expected |
| Edit FAQ | ![screenshot](documentation/responsiveness/mobile-edit-faq.png) | ![screenshot](documentation/responsiveness/tablet-edit-faq.png) | ![screenshot](documentation/responsiveness/desktop-edit-faq.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Edge | Opera | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/edge-register.png) | ![screenshot](documentation/browsers/opera-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/edge-login.png) | ![screenshot](documentation/browsers/opera-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/edge-profile.png) | ![screenshot](documentation/browsers/opera-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/edge-home.png) | ![screenshot](documentation/browsers/opera-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/edge-products.png) | ![screenshot](documentation/browsers/opera-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/edge-product-details.png) | ![screenshot](documentation/browsers/opera-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/edge-bag.png) | ![screenshot](documentation/browsers/opera-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/edge-checkout.png) | ![screenshot](documentation/browsers/opera-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/edge-checkout-success.png) | ![screenshot](documentation/browsers/opera-checkout-success.png) | Works as expected |
| FAQs | ![screenshot](documentation/browsers/chrome-faqs.png) | ![screenshot](documentation/browsers/edge-faqs.png) | ![screenshot](documentation/browsers/opera-faqs.png) | Works as expected |
| Edit FAQ | ![screenshot](documentation/browsers/chrome-edit-faq.png) | ![screenshot](documentation/browsers/edge-edit-faq.png) | ![screenshot](documentation/browsers/opera-edit-faq.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/edge-add-product.png) | ![screenshot](documentation/browsers/opera-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/edge-edit-product.png) | ![screenshot](documentation/browsers/opera-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/edge-newsletter.png) | ![screenshot](documentation/browsers/opera-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/edge-contact.png) | ![screenshot](documentation/browsers/opera-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/edge-404.png) | ![screenshot](documentation/browsers/opera-404.png) | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) | Some performance issues on mobile |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) | Some performance issues on mobile |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) | Some performance issues on mobile |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) | Some performance issues on mobile |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) | Some performance issues. Best practices issues caused by Cloudinary |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) | Some performance issues |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) | Some performance issues on mobile |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) | Some performance issues on mobile |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) | Some performance issues on mobile |
| FAQs | ![screenshot](documentation/lighthouse/mobile-faqs.png) | ![screenshot](documentation/lighthouse/desktop-faqs.png) | Some performance issues on mobile |
| Edit FAQ | ![screenshot](documentation/lighthouse/mobile-edit-faq.png) | ![screenshot](documentation/lighthouse/desktop-edit-faq.png) | Some performance issues on mobile |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) | Some performance issues on mobile |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) | Some performance issues on mobile |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) | Some performance issues on mobile |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) | Some performance issues on mobile |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) | Some performance issues on mobile. Minor issues with best practices & SEO due to 404 error |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot | Screenshot (Additional) |
| --- | --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) | |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) | |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) | |
| | Feature is expected to filter products by subcategory. | Applied subcategory filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering-subcategory.png) | |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) | |
| Products (Admin Features) | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product-before.png) | ![screenshot](documentation/defensive/create-product-after.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product-before.png) | ![screenshot](documentation/defensive/update-product-after.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product-before.png) | ![screenshot](documentation/defensive/delete-product-after.png) |
| Products (Brute Force) | Feature is expected to navigate a guest user to the login page when the attempt to bruteforce a url to add, edit, or delete a product. | Attempt to add, edit, and delete a product by bruteforcing a url while not logged in. | User was redirected to the login page and the brute force attempt was prevented. | ![screenshot](documentation/defensive/product-brute-force-guest.png) | |
| | Feature is expected to navigate a non-superuser user to the home page, and display an error message when the attempt to bruteforce a url to add, edit, or delete a product. | Attempt to add, edit, and delete a product by bruteforcing a url while logged in as a standard user. | User was redirected to the home page, error message was displayed, and the brute force attempt was prevented. | ![screenshot](documentation/defensive/product-brute-force-user.png) | |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) | |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) | |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) | |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) | |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) | |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) | |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) | |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) | |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders-before.png) | ![screenshot](documentation/defensive/view-orders-after.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email address for newsletter registration. | Email address was successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter-before.png) | ![screenshot](documentation/defensive/newsletter-after.png) |
| | Feature is expected to send confirmation email after user signs up for the newsletter. | Submitted newsletter form using valid email address and checked inbox. | Confirmation email was received with welcome message. | ![screenshot](documentation/defensive/newsletter-email.png) | |
| Contact | Feature is expected to allow users to submit a message by providing their name & email address. | Submitted contact form with valid information. | Message, name & email visible on admin panel. | ![screenshot](documentation/defensive/contact-before.png) | ![screenshot](documentation/defensive/contact-after.png) |
| | Feature is expected to send confirmation email after user submits contact form. | Submitted contact form with valid information and checkout email inbox. | Email recieved with confirmation of message. | ![screenshot](documentation/defensive/contact-email.png) | |
| FAQs | Feature is expected to allow users to view FAQs without registration. | Opened FAQs page as a guest user. | FAQs were fully accessible without requiring registration. | ![screenshot](documentation/defensive/faqs.png) | |
| FAQs (Admin Features) | Feature is expected to allow the site owner to create new FAQs. | Created new FAQ with valid data (question & answer). | FAQ was added successfully and displayed on the FAQ page of the site. | ![screenshot](documentation/defensive/create-faq-before.png) | ![screenshot](documentation/defensive/create-faq-after.png) |
| | Feature is expected to allow the site owner to update FAQs. | Edited FAQ as an admin user. | FAQ updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-faq-before.png) | ![screenshot](documentation/defensive/update-faq-after.png) |
| | Feature is expected to allow the site owner to delete FAQs. | Deleted an FAQ from the FAQs page. | FAQ was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-faq-before.png) | ![screenshot](documentation/defensive/delete-faq-after.png) |
| FAQs (Brute Force) | Feature is expected to navigate a guest user to the login page when the attempt to bruteforce a url to add, edit, or delete a FAQ. | Attempt to add, edit, and delete an FAQ by bruteforcing a url while not logged in. | User was redirected to the login page and the brute force attempt was prevented. | ![screenshot](documentation/defensive/faq-brute-force-guest.png) | |
| | Feature is expected to navigate a non-superuser user to the home page, and display an error message when the attempt to bruteforce a url to add, edit, or delete an FAQ. | Attempt to add, edit, and delete an FAQ by bruteforcing a url while logged in as a standard user. | User was redirected to the home page, error message was displayed, and the brute force attempt was prevented. | ![screenshot](documentation/defensive/product-brute-force-user.png) | |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) | |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/product-list.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/checkout-login-register.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/newsletter.png) |
| As a user | I would like to see an FAQs page | so that I can see answers to frequently ask questions which may resolve any potential issues I might have. | ![screenshot](documentation/features/faqs.png) |
| As a user | I would like to be able to submit a contact form | so that I can make enquiries, requests, or ask questions to the site owners. | ![screenshot](documentation/features/contact.png) |
| As a customer | I would like to browse various product categories (guitars, amps, pedals, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/categories.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/sorting.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/features/categories.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/product-details.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/add-to-bag.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/view-bag.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/edit-bag.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/remove-bag.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/checkout.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/order-confirmation-email.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/order-confirmation.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/stripe-payment.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/order-history.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/saved-address.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/create-product.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/update-product.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/delete-product.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/view-orders.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/categories-admin.png) |
| As a site owner | I would like to manage product subcategories | so that I can ensure items can be further filtered by from other products within their category. | ![screenshot](documentation/features/subcategories-admin.png) |
| As a site owner | I would like to manage product brands | so that I can ensure items are correctly organized by brand. | ![screenshot](documentation/features/brands-admin.png) |
| As a site owner | I would like to create faqs | so that I can reduce the number of repeat enquireies by offering answers to the most frequent questions on the site. | ![screenshot](documentation/features/create-faq.png) |
| As a site owner | I would like to update faqs | so that I can change details of an answer or question if there is a change. | ![screenshot](documentation/features/update-faq.png) |
| As a site owner | I would like to delete faqs | so that I can keep the FAQs page relevant by removing entries that are no longer needed as the site changes. | ![screenshot](documentation/features/delete-faq.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/404.png) |
| As a developer | I would like to see a README file | so that I can understand the features & structure of the site if I am making changes/contibutions. | ![screenshot](documentation/features/readme.png) |
| As a developer | I would like to see a TESTING file | so that I can see a documented account of all tests performed on the live site and any known bugs. | ![screenshot](documentation/features/testing.png) |
| As a developer | I would like to see the site deplyed on Heroku | so that it can be used/viewed by the public. | ![screenshot](documentation/features/heroku.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/Ash-5p/double-whammy-guitars/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AAsh-5p%2Fdouble-whammy-guitars%20label%3Abug&label=bugs)](https://www.github.com/Ash-5p/double-whammy-guitars/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Ash-5p/double-whammy-guitars/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Ash-5p/double-whammy-guitars/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

[![GitHub issues](https://img.shields.io/github/issues/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars/issues)

Any remaining open issues can be tracked [here](https://www.github.com/Ash-5p/double-whammy-guitars/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.png) |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.png) |
| The `-`/`+` quantity buttons work well on "product_details.html", but not on "bag.html". | ![screenshot](documentation/issues/quantity-buttons.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

