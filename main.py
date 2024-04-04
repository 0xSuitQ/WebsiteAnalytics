import csv

def find_users_from_both_days(file1, file2):
	day1 = set()
	day2 = set()

	with open(file1, 'r') as file:
		csv_reader = csv.reader(file)
		next(csv_reader)
		for row in csv_reader:
			user_id, product_id = int(row[0]), int(row[1])
			day1.add(user_id)
	with open(file2, 'r') as file:
		csv_reader = csv.reader(file)
		next(csv_reader)
		for row in csv_reader:
			user_id, product_id = int(row[0]), int(row[1])
			if user_id in day1:
				day2.add(user_id)
	print('Users who visited on both days:')
	print(day2)


def find_users_new_pages(file1, file2):
	day1 = {}
	day2 = {}

	with open(file1, 'r') as file:
		csv_reader = csv.reader(file)
		next(csv_reader)
		for row in csv_reader:
			user_id, product_id = int(row[0]), int(row[1])
			day1[user_id] = set()
			day1[user_id].add(product_id)
	with open(file2, 'r') as file:
		csv_reader = csv.reader(file)
		next(csv_reader)
		for row in csv_reader:
			user_id, product_id = int(row[0]), int(row[1])
			if user_id in day1 and product_id not in day1[user_id]:
				day2[user_id] = set()
				day2[user_id].add(product_id)
	print('day1 users who visited new pages on day2:')
	print(list(day2.keys()))


if (input('Do you want to try your own data? (y/n) ').lower() == 'y'):
	file1 = input('Enter the name of the first file: ')
	file2 = input('Enter the name of the second file: ')
else:
	file1 = 'day1.csv'
	file2 = 'day2.csv'


find_users_from_both_days(file1, file2)
find_users_new_pages(file1, file2)