# SIG_Scraper
The Special Interest Group (SIG) defines a few standard Generic Attribute Profiles which serve as the foundation for the design of any Bluetooth Low Energy (BLE) System.

### Mongo Server
    1. Download and install the MongoDB Community Server from the following link: https://www.mongodb.com/download-center/community

    2. To start the mongo server run the mongod process within your mongodb folder and specify your data directory with the following command:
        /Users/******/mongodb/bin/mongod --dbpath=/Users/*******/mongodb-data
        
### Scraping
The scraping scripts search the Bluetooth GATT specifications pages for all the XML links containing the relevant bluetooth services and characteristics.

### Parsing
The parsing scripts extract the relevant data from the downloaded XML files and build objects that
can be used to populate a noSQL database for GATT profiles.

### ChromeDriver
To run the scraper, check your google chrome version at the following link: https://www.whatismybrowser.com.
Then download the appropriate driver and extract the file into the root of the repository. Chrome Drivers are available at the following url: http://chromedriver.chromium.org/downloads. The current repo uses version 75 but use the appropriate driver for your version of chrome.
