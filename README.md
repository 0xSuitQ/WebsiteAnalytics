# Website Analytics

## Task
You are a developer of a website that sells some products, like Amazon. The marketing department asked you to collect some analytics. You have two CSV files with data about visiting pages with products. Each file represents some day. Your task is to find all the users that:
- Visited some pages on both days
- On the second day visited the page that hadn’t been visited by this user on the first day

Create a console app that finds all the users according to the description.
As input, you will have two CSV files with the following structure: `user_id, product_id, timestamp`. Each file represents a separate day. Duplicates are possible, which means the user may visit the same page.

## Result

The program will log into the console with all user IDs that meet the criteria.

## How to run

1. Clone the repository from GitHub.
2. Open a terminal and navigate to the project directory.
3. Run the program by typing `python main.py`.
4. If you don't want to use custom data, enter `y` and then enter the filenames of the CSV files. If you don't want to use custom data, the program will use the provided test files.


## Efficiency

The solution is efficient in terms of both storage and execution time. Here are some reasons why:

- In both `find_users_from_both_days` and `find_users_new_pages`, elements from the `csv_reader` row (`user_id`, `product_id`) are directly accessed instead of creating an intermediate list. This avoids unnecessary list creation and improves performance.
- Checking for specific conditions before adding users to `day2` avoids unnecessary processing.
- Usage of a set in the first task is more efficient compared to iterating through a list.

Approximate amount of time spent on the task: 30min
