import csv

with open('dataset.csv', 'w') as csvfile:
    fieldnames = ['bought', 'edu', 'first', 'visited', 'more_info']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows([{'bought': 'false', 'edu': 'true', 'first': 'false', 'visited': 'false', 'more_info': 'true'},
                      {'bought': 'true', 'edu': 'false', 'first': 'true', 'visited': 'false', 'more_info': 'false'},
                      {'bought': 'false', 'edu': 'false', 'first': 'true', 'visited': 'true', 'more_info': 'true'},
                      {'bought': 'false', 'edu': 'false', 'first': 'true', 'visited': 'false', 'more_info': 'false'},
                      {'bought': 'false', 'edu': 'false', 'first': 'false', 'visited': 'true', 'more_info': 'false'},
                      {'bought': 'true', 'edu': 'false', 'first': 'false', 'visited': 'true', 'more_info': 'true'},
                      {'bought': 'true', 'edu': 'false', 'first': 'false', 'visited': 'false', 'more_info': 'true'},
                      {'bought': 'false', 'edu': 'true', 'first': 'true', 'visited': 'true', 'more_info': 'false'},
                      {'bought': 'false', 'edu': 'true', 'first': 'true', 'visited': 'false', 'more_info': 'false'},
                      {'bought': 'true', 'edu': 'true', 'first': 'true', 'visited': 'false', 'more_info': 'true'},
                      {'bought': 'true', 'edu': 'true', 'first': 'false', 'visited': 'true', 'more_info': 'true'},
                      {'bought': 'false', 'edu': 'false', 'first': 'false', 'visited': 'false', 'more_info': 'true'}])
