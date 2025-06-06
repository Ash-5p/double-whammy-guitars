# [![image](static/images/logo-oval.png)](https://double-whammy-guitars-47bed68ef1db.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars)

![screenshot](documentation/mockup.png)

source: [double-whammy-guitars amiresponsive](https://ui.dev/amiresponsive?url=https://double-whammy-guitars-47bed68ef1db.herokuapp.com)

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "I Think Therefore I Blog".

> [!IMPORTANT]
> The examples in these templates are strongly influenced by the Code Institute walkthrough project called "Boutique Ado".

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase products.
- Empower site owners to manage the store's inventory and customer orders efficiently.

##### Primary User Needs
- Guest users need to browse products and checkout with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need robust tools for inventory and order management.

##### Business Goals
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date store inventory.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Product details, including name, price, description, category, subcategory, brand, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home, Products, Cart, Newsletter, FAQs, Contact, and Account sections.
- **Hierarchy**:
  - Prominent product categories and filters for easy navigation.
  - Cart and checkout options displayed prominently for convenience.

##### User Flow
1. Guest user browses the store → filters and sorts products by category, price, or name.
2. Guest user adds items to the cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Returning customers log in → view past orders and track purchase history.
5. Site owners manage inventory → add, update, or delete products and categories.
6. Users signup to the newsletter → potentially receive advanced notice of upcoming sales.

#### 4. Skeleton Plane
##### Wireframe Suggestions
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/555555-ffffff-343a40-ff4500) to generate my color palette.

- `#555555` primary text.
- `#FFFFFF` primary highlights.
- `#FFFFFF` secondary text.
- `#343A40` secondary highlights.
- `#FF4500` tertiary highlights.

![screenshot](documentation/coolors.png)

### Typography

- [Radio Canada Big](https://fonts.google.com/specimen/Radio+Canada+Big) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. |
| As a user | I would like to see an FAQs page | so that I can see answers to frequently ask questions which may resolve any potential issues I might have. |
| As a user | I would like to be able to submit a contact form | so that I can make enquiries, requests, or ask questions to the site owners. |
| As a customer | I would like to browse various product categories (guitars, amps, pedals, etc.) | so that I can easily find what I'm looking for. |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. |
| As a site owner | I would like to manage product subcategories | so that I can ensure items can be further filtered by from other products within their category. |
| As a site owner | I would like to manage product brands | so that I can ensure items are correctly organized by brand. |
| As a site owner | I would like to create faqs | so that I can reduce the number of repeat enquireies by offering answers to the most frequent questions on the site. |
| As a site owner | I would like to update faqs | so that I can change details of an answer or question if there is a change. |
| As a site owner | I would like to delete faqs | so that I can keep the FAQs page relevant by removing entries that are no longer needed as the site changes. |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |
| As a developer | I would like to see a README file | so that I can understand the features & structure of the site if I am making changes/contibutions. |
| As a developer | I would like to see a TESTING file | so that I can see a documented account of all tests performed on the live site and any known bugs. |
| As a developer | I would like to see the site deplyed on Heroku | so that it can be used/viewed by the public. |


## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Products | ![screenshot](documentation/wireframes/mobile-products.png) | ![screenshot](documentation/wireframes/tablet-products.png) | ![screenshot](documentation/wireframes/desktop-products.png) |
| Product Details | ![screenshot](documentation/wireframes/mobile-product-details.png) | ![screenshot](documentation/wireframes/tablet-product-details.png) | ![screenshot](documentation/wireframes/desktop-product-details.png) |
| Add Product | ![screenshot](documentation/wireframes/mobile-add-product.png) | ![screenshot](documentation/wireframes/tablet-add-product.png) | ![screenshot](documentation/wireframes/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/wireframes/mobile-edit-product.png) | ![screenshot](documentation/wireframes/tablet-edit-product.png) | ![screenshot](documentation/wireframes/desktop-edit-product.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| FAQs | ![screenshot](documentation/wireframes/mobile-faqs.png) | ![screenshot](documentation/wireframes/tablet-faqs.png) | ![screenshot](documentation/wireframes/desktop-faqs.png) |
| Edit FAQ | ![screenshot](documentation/wireframes/mobile-edit-faq.png) | ![screenshot](documentation/wireframes/tablet-edit-faq.png) | ![screenshot](documentation/wireframes/desktop-edit-faq.png) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.png) | ![screenshot](documentation/wireframes/tablet-newsletter.png) | ![screenshot](documentation/wireframes/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Email Account Activation | When registering for an account, the user is sent a link to their email in order to activate the account. | ![screenshot](documentation/features/register-email.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Product List | Users can browse all available products with sorting, filtering by categories, and search functionality. | ![screenshot](documentation/features/product-list.png) |
| Product Details | Displays detailed information about a selected product, including its name, description, price, and an image. | ![screenshot](documentation/features/product-details.png) |
| Add to Bag | Users can add items to their shopping bag. | ![screenshot](documentation/features/add-to-bag.png) |
| View Bag | Users can view the contents of their shopping bag, adjust quantities, or remove items. | ![screenshot](documentation/features/view-bag.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Confirmation Emails | Users receive an email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation-email.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their past orders and access details of each order, including products purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Product Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/product-management.png) |
| Newsletter | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database & sends a confirmation email. | ![screenshot](documentation/features/newsletter.png) |
| Newsletter Email Confirmation | The user is sent an email confirmation when sigining up to the newsletters. | ![screenshot](documentation/features/newsletter-email.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/contact.png) |
| FAQs | Admins can manage frequently asked questions, which are displayed on the site for users. | ![screenshot](documentation/features/faqs.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding products to the bag, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/marketing.png) ![screenshot](documentation/features/footer.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Product Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Wishlist Functionality**: Enable users to save products to a personal wishlist for future purchases. Notify users if wishlist items go on sale or are back in stock.
- **Stock Control System**: Develop a stock control system that will allow site owners to update the stock of each product & will display the current amout of stock to users.
- **Product Recommendations**: Implement a "Customers who bought this also bought" or "You might also like" feature to suggest related products.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Discount Codes and Vouchers**: Allow the admin to create discount codes or vouchers for promotions and marketing campaigns.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Product Inventory Alerts**: Notify customers when out-of-stock items are back in stock, or when low inventory is approaching.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Social Media Integration**: Enable users to share products directly to social media platforms or implement a social login for quick account creation.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Product Video Demos**: Support product videos to better showcase features, especially for high-tech or complex items.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER ||--o{ USERPROFILE : has
    USERPROFILE ||--o{ ORDER : places
    ORDER ||--|{ ORDERLINEITEM : contains
    ORDERLINEITEM }|--|| PRODUCT : includes
    ORDER }|--|| COUNTRY : ships_to

    PRODUCT }|--|| CATEGORY : belongs_to
    PRODUCT }|--|| SUBCATEGORY : belongs_to
    PRODUCT }|--|| BRAND : made_by
    CATEGORY ||--o{ SUBCATEGORY : groups

    CONTACT {
        string name
        string email
        text message
        datetime sent_on
    }

    FAQ {
        text question
        text answer
        datetime updated_on
    }

    NEWSLETTER {
        string email
    }

    USERPROFILE {
        string default_phone_number
        string default_street_address1
        string default_street_address2
        string default_town_or_city
        string default_county
        string default_postcode
        country default_country
    }

    ORDER {
        string order_number
        string full_name
        string email
        string phone_number
        country country
        string postcode
        string town_or_city
        string street_address1
        string street_address2
        string county
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        string stripe_pid
    }

    ORDERLINEITEM {
        int quantity
        decimal lineitem_total
    }

    PRODUCT {
        string name
        text description
        decimal price
        image image
    }

    CATEGORY {
        string name
        string friendly_name
    }

    SUBCATEGORY {
        string name
        string friendly_name
    }

    BRAND {
        string name
        string friendly_name
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVcFu2zAM_RVD57RIHLdpfRs6DBg2bB2GXYYAhmIxjlBZcimqqdvk3yfbSVPHceP5kBh8TyRFPtKvLDUCWMwAP0ueIc_nOvDPHwsYvDbv1SM1BVIE998OpieO6Ypj4DxV8xy6CORcqq654NauDYoG2c71IeQ9mqVUMDCygCV3ipJiZTQk2uULwH6WJQSghAuBYO1kKDHsJ5JZ68Rgkkoq-1mpcfojvDCWqiac8YDliXoFm83FxWbTql0crLhNfEX2xDtOkBksB1b1dC-XKEELVSYH-C0TH1m4lAb6tw_uXFCCZ_K3tynKgqTRB2RhjKrvZ-UL2INdQCpzroICZQpdM3KSOuuG9WAGicN3Kq1NzW_PNauam82hrHGwAGV0Zr0g9tyfKAYPkKm4vfJdOqWS_5uvD8ehJabWsV4dfqzzs3N1dp6OJ0T4ypLMoX7pNlOAkk-ApZ8LS124KScZ4qoL-g2nxTFYy82gzKTmKlnw7OQdZAFJIY-3Vt3o71LDV4L8TMMr06Pjmlp13KemvBPpnRxn99afRn618k8lsddlO6NmG-Rcl6fy3R3ZK7tfyTtie890yT9gbRUQDdb-Owm_3ebOaOKD18mg0ag7nHv1daf6y6dfAyM9OrDtbVS75dqu94O2ZSOWA_rgwn9Ta7dzRivwKbLYvwqOD3M21xWPOzK_S52ymNDBiLmikvvuK8ziJVfWWwuuWfzKnlk8jSaXN9ez8HoyHc_C8TiajVjJ4ovp5XUUTqMovLqdXd2Et-FsO2Ivxngfk8vxZBpGkT_m_zxW-_tbY01QNC5b7YJt_wE0ZoQj)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/Ash-5p/double-whammy-guitars/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/Ash-5p/double-whammy-guitars/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/Ash-5p/double-whammy-guitars)](https://www.github.com/Ash-5p/double-whammy-guitars/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

[GitHub Milestones](https://github.com/Ash-5p/double-whammy-guitars/milestones) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [GitHub open milestones](https://github.com/Ash-5p/double-whammy-guitars/milestones?state=open) | ![screenshot](documentation/gh-milestones-open.png) |
| [GitHub closed milestones](https://github.com/Ash-5p/double-whammy-guitars/milestones?state=closed) | ![screenshot](documentation/gh-milestones-closed.png) |

## Ecommerce Business Model

This site sells guitar related goods to individual customers, and therefore follows a **Business to Customer** model. It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter and contact page.

Social media can potentially build a community of users around the business, and boost site visitor numbers, especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users. For example, what items are on special offer, new items in stock, updates to business hours, notifications of events, and much more!

## SEO & Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users when searching online to find my page easily from a search engine. This included a series of the following keyword types:

- Short-tail (head terms) keywords
- Long-tail keywords

I've also played around with [Word Tracker](https://www.wordtracker.com) a bit to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://double-whammy-guitars-47bed68ef1db.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://double-whammy-guitars-47bed68ef1db.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their email address if they are interested in learning more. 

**Custom Django Model Newsletter**

    class Newsletter(models.Model):
    """
    Stores a single newsletter subscription
    """
    email = models.EmailField(blank=False, unique=True)

    class Meta:
        verbose_name_plural = 'Newsletter Subscribers'
    ```

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://double-whammy-guitars-47bed68ef1db.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url|
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user-inserts-own-gmail-api-key |
| `EMAIL_HOST_USER` | user-inserts-own-gmail-email-address |
| `SECRET_KEY` | any-random-secret-key |
| `STRIPE_PUBLIC_KEY` | user-inserts-own-stripe-public-key |
| `STRIPE_SECRET_KEY` | user-inserts-own-stripe-secret-key |
| `STRIPE_WH_SECRET` | user-inserts-own-stripe-webhook-secret |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://double-whammy-guitars-47bed68ef1db.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `double-whammy-guitars`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("EMAIL_HOST_PASS", "user-inserts-own-gmail-host-api-key")
os.environ.setdefault("EMAIL_HOST_USER", "user-inserts-own-gmail-email-address")
os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user-inserts-own-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "user-inserts-own-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "user-inserts-own-stripe-webhook-secret")  # only if using Stripe Webhooks

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/Ash-5p/double-whammy-guitars).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/Ash-5p/double-whammy-guitars.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/Ash-5p/double-whammy-guitars)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/Ash-5p/double-whammy-guitars).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Boutique Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary](https://cloudinary.com/) | Cloud storage for image files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |
| [Stack Overflow](https://stackoverflow.com/questions/23843619/js-for-smooth-scroll-to-the-bottom-of-the-page) | Code borrowed for faqs.js `window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});` |
| [Boutique Ado - bag.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/bag/templates/bag/bag.html#L1-L150) | Code borrowed as base template for bag.html |
| [Boutique Ado - bag/context.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/bag/contexts.py#L1-L57) | Code borrowed as base template for bag/context.py |
| [Boutique Ado - bag/views.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/bag/views.py#L1-L139) | Code borrowed as base template for bag/views.py |
| [Boutique Ado - checkout.css](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/static/checkout/css/checkout.css#L1-L67) | Code borrowed as base template for checkout.css |
| [Boutique Ado - stripe_elements.js](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/static/checkout/js/stripe_elements.js#L1-L119) | Code borrowed as base template for stripe_elements.js |
| [Boutique Ado - checkout.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/templates/checkout/checkout.html#L1-L152) | Code borrowed as base template for checkout.html |
| [Boutique Ado - checkout_success.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/templates/checkout/checkout_success.html#L1-L218) | Code borrowed as base template for checkout_success.html |
| [Boutique Ado - checkout/admin.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/admin.py#L1-L32) | Code borrowed as base template for checkout/admin.py |
| [Boutique Ado - checkout/forms.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/forms.py#L1-L39) | Code borrowed as base template for checkout/forms.py |
| [Boutique Ado - checkout/models.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/models.py#L1-L106) | Code borrowed as base template for checkout/models.py |
| [Boutique Ado - checkout/signals.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/signals.py#L1-L20) | Code borrowed as base template for checkout/signals.py |
| [Boutique Ado - checkout/views.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/views.py#L1-L188) | Code borrowed as base template for checkout/views.py |
| [Boutique Ado - checkout/webhook_handler.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/webhook_handler.py#L1-L164) | Code borrowed as base template for checkout/webhook_handler.py |
| [Boutique Ado - checkout/webhooks.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/checkout/webhooks.py#L1-L61) | Code borrowed as base template for checkout/webhooks.py |
| [Boutique Ado - index.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/home/templates/home/index.html#L1-L28) | Code borrowed as base template for index.html |
| [Boutique Ado - quantity_input_scripts.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/templates/products/includes/quantity_input_script.html#L1-L83) | Code borrowed as base template for quantity_input_scripts.html |
| [Boutique Ado - add_product.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/templates/products/add_product.html#L1-L53) | Code borrowed as base template for add_product.html |
| [Boutique Ado - edit_product.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/templates/products/edit_product.html#L1-L53) | Code borrowed as base template for edit_product.html |
| [Boutique Ado - product_details.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/templates/products/product_detail.html#L1-L121) | Code borrowed as base template for product_details.html |
| [Boutique Ado - products.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/templates/products/products.html#L1-L154) | Code borrowed as base template for products.html |
| [Boutique Ado - products/admin.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/admin.py#L1-L28) | Code borrowed as base template for products/admin.py |
| [Boutique Ado - products/forms.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/forms.py#L1-L22) | Code borrowed as base template for products/forms.py |
| [Boutique Ado - products/models.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/models.py#L1-L33) | Code borrowed as base template for products/models.py |
| [Boutique Ado - products/views.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/products/views.py#L1-L145) | Code borrowed as base template for products/views.py |
| [Boutique Ado - profile.css](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/static/profiles/css/profile.css#L1-L21) | Code borrowed as base template for profile.css |
| [Boutique Ado - countryfield.js](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/static/profiles/js/countryfield.js#L1-L12) | Code borrowed as base template for countryfield.js |
| [Boutique Ado - profile.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/templates/profiles/profile.html#L1-L81) | Code borrowed as base template for profile.html |
| [Boutique Ado - profiles/forms.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/forms.py#L1-L37) | Code borrowed as base template for profiles/forms.py |
| [Boutique Ado - profiles/models.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/models.py#L1-L42) | Code borrowed as base template for profiles/models.py |
| [Boutique Ado - profiles/views.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/profiles/views.py#L1-L52) | Code borrowed as base template for profiles/view.py |
| [Boutique Ado - base.css](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/static/css/base.css#L1-L329) | Code borrowed as base template for base.css|
| [Boutique Ado - base.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/templates/base.html#L1-L162) | Code borrowed as base template for base.html |
| [Boutique Ado - main-nav.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/templates/includes/main-nav.html#L1-L55) | Code borrowed as base template for main-nav.html |
| [Boutique Ado - mobile-top-header.html](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode/blob/main/21-shopping-bag-bug-fix/templates/includes/mobile-top-header.html#L1-L56) | Code borrowed as base template for mobile-top-header.html |

### Media

| Source | Notes |
| --- | --- |
| [GettyImages](https://media.gettyimages.com/id/523372460/photo/electric-guitars-and-amplifiers-in-music-store.jpg?s=2048x2048&w=gi&k=20&c=IpZSlijZndrWJUbFSnsZ30KjRc0pz5AwKaeD15c8Lq4=) | Homepage background image |
| [Crescendo](https://www.crescendo.co.za/wp-content/uploads/2025/01/placeholder-guiter-image.png) | Placeholder image for products |
| [Andertons](https://www.andertons.co.uk/) | All product images & descriptions |
| [Dribbble](https://cdn.dribbble.com/userupload/20486597/file/original-c8139c62c9997caec7ae59d860909670.gif) | Loading image for payment |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Image Resizer](https://imageresizer.com/) | Resize images used throughout the site |
| [Mediamodifier](https://mediamodifier.com/) | Oval crop logo for README file |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, Lorna, for believing in me, and allowing me to make this transition into software development.

