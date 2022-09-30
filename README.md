# PROXIMA APP

1. Check the exchange rate from Euros to Dollars on 5 different days from the following page https://finance.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX:(Done)
2. Store the exchange value data in a SQL database (Mariadb - own service on line. dont need to configure).(Done)
3. Develop a REST API prototype that allows querying the exchange value stored in the SQL database ( /currency and /scrape_currency ).(Done)
4. At the end of the process hit the webhook at URL: https://webhook.site/8bb140f1-4bf1-4c39-b975-6235b358dd9e with a body that includes the exchange value queried(Done)
Note: The webhook URL must be able to take parameters, you can use https://webhook.site/ to generate a new one. (Done)
5. DESIGN IMPLEMENTATION: Implement the mock design provided to you using ReactJS. (Done) - REST API integration with Reactjs.

Start Python main.py in root folder /proxima
Start Reactjs app in /app

Jorge Prieto.
jorgefprietol@gmail.com
+593-0994203888