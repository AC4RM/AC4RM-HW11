### Introduction
- This is the week 11 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Implement a decorator function called `time_it` that will return the execution time of the decorated function.
   - The decorator should allow the function to take any number of arguments.
   - The decorator should return a string following this format below:
       - `"The function <name of the function> takes <0.00125> seconds"`
   - You may use the functions from the Python [datetime](https://docs.python.org/3/library/datetime.html#timedelta-objects) module to calculate the time used.
2. Write SQL queries to do the following:
    - From the `customers` table, use the last four digits of the phone number as the password. Return the `customer_id` and password columns in your result and order the result by `customer_id` in ascending order.
    - Using the `invoices` tale, return the monthly sales. You should return `month` and `monthly_sales` columns in your result and order the result by `month` in ascending order.
3. Running the Apriori Algorithm is straightforward. However, sometimes the dataset is not in a "clean" format so we need to do some data manipulation to prepare our data.
   - We will be dealing with a grocery shopping dataset in this homework and you can take a look at the data [here](https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/groceries.csv).
   - You can see that it is not really a structured csv file so we have to handle each row separately.
       - Read in all the lines from the file and use the index number as `order_id`
       - Split each line using `,` and concat a new row to the existing dataframe with the new `item` and the same `order_id`. Make sure you remove the newline character `\n` from the item.
       - The head of the dataframe should look like this:
    
         | order_id | item |
         | --- | ----------- |
         | 0 | citrus fruit |
         | 0 | semi-finished bread |
         | 0 | margarine |
         | 0 | ready soups |
         | 1 | tropical fruit |
         | 1 | yogurt |
         | 1 | coffee |
         | 2 | whole milk |

   - Using the dataframe you just cleaned, train an apriori model with the same settings from the lecture and return the result dataframe.
4. Write a regex pattern to detect whether a password meets all the requirements below
    - Contain only `[A-Z]` `[a-z]` `[0-9]` `[_-.]`
    - Does not begin/end with `[_-.]`
    - Minimum length 6, max length 18 
    - `re.search(pattern, 'ASDF123')` => match
    - `re.search(pattern, '.ASDF123')` => not match
    - `re.search(pattern, 'A-S3')` => not match  
