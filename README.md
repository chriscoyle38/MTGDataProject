# MTGDataProject


Motivation:
This project is to explore and examine Magic the Gathering card pricing data available from MTGJson to find attributes of cards that make them hold their value and make them good for resale. I also examined if "chase" cards are better for reselling vs other Magic cards by comparing how well they hold their value(% change over 90 days) and their potential profit(market price - buylist price - fees).

Code Style:
Jupyter Notebook

EDA:
Navigating the TCGPlayer API was difficult due to little documentation and only being able to pull 100 records at a time with 300 max calls per hour. I eventually was able to create a program that pulled magic cards out by set.

I also ran into issues with JSON files from MTGJSON and the pricing data being nested in dictionaries in a single column. The final data I worked with after pulling and cleaning was 47,355 rows and 18 columns. This is the data that I examined to try and reject of accept my null hypothesis.

NULL HYPOTHESIS:

Magic the Gathering 'chase' cards do not go up in value more than other Magic cards. A reseller cannot make more profit selling 'chase' cards than other Magic cards.

Alternative Hypothesis:

Magic the Gathering 'chase' cards are in high demand. They consistantly go up in value more than other Magic cards and a reseller can make more money buying and selling them.

Findings:

I looked at foil and normal Magic cards separately comparing 'chase' cards and every other Magic card (that has a normal and foil version). I looked at the % change over 90 days and potential profit for each category. I got a very low p-value, well within the alpha I set at .05 for all categories. So, my final conclusion is to reject my null hypothesis and say that 'chase' cards are better for buying and reselling.

Features:

Put MTGJson pricing and card data into a useable datafrmae to be able to examine card pricing data and find what cards are the best to buy at buylist prices and resell at market prices.
