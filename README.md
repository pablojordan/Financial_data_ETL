![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/etl-process.png)


# ETL | Financial Services Institutions 

> The primary objective of this project is to collect data from Financial Services Institutions in the area of commercial banks and insurance. The output of the data extraction and transformation are three databases
>* Bankruptcy DB --> Active and monitored cases of public companies bankruptcy from 2009 to 2011
>* Banks DB -->  Detail on historical banks failures from 1934 to present. 
>* Financials DB --> Collections of daily stocks data for Fortune 500 companies and specifically collection of daily news, weekly historical socks data and last 4 quaters financial statement for all Fortune 500 (20 Companies) in the area of Financial Services - Insurance.

> Sources: 
>* [Source 1 - Public Companies Bankruptcy](https://catalog.data.gov/dataset/public-company-bankruptcy-cases-opened-and-monitored)
>* [Source 2 - Banks failures 1934 to present](https://banks.data.fdic.gov/docs/#/Structure/searchInstitutions)
>* [Source 3 - Financials - Yahoo API](https://rapidapi.com/apidojo/api/yahoo-finance1?endpoint=5c3da178e4b0cc6cdc0ed6)
>* [Source 4 - Financials - IEX Trading API](https://iextrading.com/developer/)
>* [Source 5 - Financials - Fortune 500 Table](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)

## Files Navigation

>* Jupyter Notebooks codes are found in:
>* ETL_Financial_Institutions_Banks --> One file for Extraction, Transformation and Load
>* ETL_Public_Companies_Bankruptcy_2009_2011 --> One file for Extraction, Transformation and Load
>* stocks_API_Code --> Two files. One for Extraction and the second one for Transformation and Load

>* Raw and Clean CSV & JSON data files are found in:
>* 	Stocks_data_files
>* 	bankruptcy_data_files
>* 	Banks_data_files

>* Technical Report - Slides Format under Technical Reports Folder: USE PgUp or PgDn while looking at the .slides.html file
>* 	ETL_Public_Comapnies_Bankruptcy_2009_2011_Final
>* 	ETL_Financial_Institutions_Banks_Final
>* 	ETL_Financial_Institutions_FINAL

---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/Navigation.gif)


## Non-Relational Database - ETL Public Companies Bankruptcy 2009 - 2011

**Database Results**
> Upload of 4 collections to non-relational database MongoDB. Each collection represents data for 2009, 2010 and 2011. A combined data collection is also included. Each collection details company name, assets, liabilities, fiscal year, state and the court district where the case is being handled.

**MongoDB - Non-Relational Bankruptcy Database**
---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/MongoDB.gif)
 
**ETL Public Companies Bankruptcy 2009 - 2011**
---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/bankruptcy.gif)

## Relational Database - ETL Financial Institutions - Banks 

**Database Results**
> Historical data of Bank failures since 1934 to present. The database contains two main tables: Institutions and Locations
 

**PostgreSQL - Relational Database Bank Failures**
---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/PostgreSQL.gif)


**ETL Financial Institutions Banks Failures**
---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/Banks.gif)


## Relational Database - ETL Fortune 500 Financial Institutions - Insurance Industry

**Database Results**

> Database warehouse of:
>* Fortune 500 companies general information 
>* Daily stocks information for Fortune 500 Companies
>* Latest News of Fortune 500 Companies in the Insurance Industry (20 Companies).
>* Weekly Historical Stocks Data of Fortune 500 Companies in the Insurance Industry (20 Companies). Output Prices & Dividends. Date Range 2006 to Present.
>* Financial Statements of the last 4 quarters (balance sheets, cashflow and income statements) of Fortune 500 Companies in the Insurance Industry (20 Companies).
>* Fortune 500 companies in the Insurance Industry (20 Companies) general information.

**Extraction Fortune 500 Companies and Insurance Companies**
---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/export_financials.gif)

---
![](https://github.com/pablojordan/Financial_data_ETL/blob/master/images/transform_financials.gif)




- Copyright 2019 © Pablo Jordan
