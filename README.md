#LoadSmart Final Project squad 1

## How to Develop?
1. Clone repository
2. Create a virtualenv with python 3.6
3. Activate virtualenv
4. Install the dependencies
5. Set instance .env
6. Run the tests

```console
git clone git@github.com:belaeifert/Loadsmart-final-project.git finalProject
cd finalProject
python -m venv .finalProject
source .finalProject/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## How to activate Google API services
1. Create a project on https://console.developers.google.com
2. Enable Places API, Distance Matrix API and Maps JavaScript API to your project
3. Create credentials
3. Create API key

## How to deploy?
1. Create an instance in heroku
2. Send settings to heroku
3. Set a secure SECRET_KEY for the instance
4. Set DEBUG=FALSE
5. Send the code to heroku

```console
heroku create instancename
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
git push heroku master --force
```

## About

Loadsmart is a New York company that facilitates how shippers and freight brokers find the right carriers to move their shipments.

## Objective

You will create a platform that on one side (Shipper/ Freight Broker) allows them to post loads that they need to find a truck for (eg New York, NY - Albany, NY), and on the other side allows carriers to have access to these loads and accept them.


## Attributes required in the Register

- on the Shipper/ Freight Broker side: Name, Last Name, Email and Password; 
- on the Carrier side: Name, Last Name, MC Number (you can see examples of MC Numbers at FMCSA website), Email, Password

## External API URLs

Integrate with google maps API to autocomplete name of cities when posting a load.

## Pricing

The price for a load should be $1.50 per mile and the Loadsmart’s margin should be 5% of the total value. For example:

> If the total miles from pickup to delivery is 100 miles, the shipper should see the load cost as $150,00 and the carrier should see the value as $142.5 => $150,00 - $7.50 (margin).
Loadsmart would receive $150,00 from the Shipper; Loadsmart would pay $142.5 for the Carrier; Loadsmart would earn $7.50 in this transaction.

## Shipper/ Freight Broker Page

- Once user clicks “Add New”, popup should allow user to enter load info:

    - Pickup date
    - Ref #
    - Origin City
    - Destination City
    - Price
    - Suggested Price from Data Science Model
    - “Post Load” button.

- Once Posted, Load shows up in “Available Loads” list.
- Once Posted, Load shows up in Carrier Page.
- When “Report Drop” button is triggered, saved info to database and delete row 
- Edit rate: allows user to edit price 
- Book Carrier: allows user to insert manually a Carrier name and MC that will be deemed as accepted the load. 
- Once a Load is accepted on the Carrier side, move it to “Accepted” section with the name of MC, scraped from FMCSA. 

## API

There are some Shippers that don’t want to access the Loadsmart platform to post a load. This happens mainly when they want to post a lot of loads at the same time. They don’t want to visit the website and click button by button for each load. They want to post a load directly from their systems. For that, you will need to build an API that possibility them to:

- Post a load;
- List the Shipper’s accepted loads;
- List the Shipper’s available loads.

Using the same logic, there are some Carriers that don’t want to access the Loadsmart platform to accept a load. For that, your API must also possibility the Carriers to:

- Accept a load;
- Drop a load;
- List all accepted loads;
- List all dropped loads;
- List all available loads (the loads the carrier can still accept or drop).

You also need to provide a documentation of how to use the API.
