# Amazon-Traffic-Simulation-Application
Amazon's purchase order sizes are tightly correlated to traffic metrics on a product's product detail page. To boost those order sizes, I've built an application that sends traffic to your product's detail page to boost traffic metrics which then boosts order sizes, thereby reducing inventory issues and increasing supplier sales.

It works by opening thousands of sessions per hour and sending traffic to a set of user-provided Amazon product detail pages. The application attempts to click "buy now" if the product is in stock. An e-commerce manager will see this show up in their vendor analytics as a boost in "Glance Views" and in split testing a clicking version vs a non-clicking version of this application, were able to reverse engineer a feature from Amazon's ordering algorithm, namely, "% added to cart". 

By boosting these two metrics, you will see a significant increase in your PO sizes. Additionally, the size of your bulk orders will go up as well.
