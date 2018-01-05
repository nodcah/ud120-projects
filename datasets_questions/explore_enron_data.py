#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print(len(enron_data["SKILLING JEFFREY K"]))
print(len(filter(lambda person: person['poi'], enron_data.values())))

names_file = open("../final_project/poi_names.txt")
names_str = names_file.read()
num_POIs = len(re.findall('\(.\)', names_str))
print(num_POIs)

print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])
print(enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"])
print(len(filter(lambda x: x['salary'] != 'NaN', enron_data.values())))
print(len(filter(lambda x: x['email_address'] != 'NaN', enron_data.values())))
print(len(filter(lambda x: x['total_payments'] == 'NaN', enron_data.values()))/float(len(enron_data)))
print(len(filter(lambda x: x['total_payments'] == 'NaN' and x['poi'], enron_data.values()))/float(len(enron_data)))
print(len(filter(lambda x: x['total_payments'] == 'NaN', enron_data.values())))

# l = [(name, person['salary']) for name, person in enron_data.items()]
# l.sort(key=lambda x: x[1], reverse=True)

pass