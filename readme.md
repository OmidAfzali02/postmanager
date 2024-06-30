# **Falcon  postal service** 
Are you tired of missed deliveries, confusing addresses, and long waits for packages? Look no further than Falcon, your all-in-one postal service app! 📦🚀
## **How Falcon Works:**

 1. Personalized Address Panel: With Falcon, every user gets their own address control panel. Update your address, set preferences, and manage deliveries effortlessly.
 2. Agencies at Your Service: Falcon partners with reliable agencies for seamless package handling. Whether it’s a gift, an online order, or important documents, our agencies ensure safe transit.
 3. Delivery Flexibility: Choose your delivery location! Collect your package at home or swing by your designated agency. It’s all about convenience.

## **Why Choose Falcon?**
-   **Efficiency:**  Say goodbye to missed deliveries. Falcon keeps you informed every step of the way.
    
-   **Security:**  Our agencies follow strict protocols to safeguard your packages.
    
-   **User-Friendly:**  The intuitive interface makes managing addresses and deliveries a breeze.

# Run locally
clone the repository:

    git clone https://github.com/OmidAfzali02/postmanager.git
    
open up a cmd and install the requirements:

    pip install -r requirements.txt
now make migrations and migrate them:

    python manage.py makemigrations
    python manage.py migrate

create a super user if you want access the admin panel:

    python manage.py createsuperuser
now you can run the project:

    python manage.py runserver

Now enjoy 😊

 