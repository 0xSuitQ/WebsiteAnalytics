Usage:
Run the program by typing `python websiteAnalytics.py`
If you don't want to use custom data, enter `y` and then filenames
If you don't want to use cystom data, my test files will be used

In both find_users_from_both_days and find_users_new_pages, I directly access elements from the csv_reader row (user_id, product_id) instead of creating an intermediate list. This avoids unnecessary list creation and improves performance.
Checking for specific conditions before adding users to day2 avoids unnecessary processing.
Usage of set in the first task is more efficient compared to iterating through a list.

Approximate amount of time spent on the task: 30min
