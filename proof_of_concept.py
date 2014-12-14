import time
import csv
tables = [
	{
		'test_table':
		{
			'file_name': 'raw_data.tsv',
			'column_structure': (
				{'id': int},
				{'first_name': str}
			)
		}
	}
]

field_lookups = {
	'first_name':
	{
		'type': str,
		'values': {
			1: 'John',
			2: 'Bob',
			3: 'Robert',
			4: 'Michael',
			5: 'Erin',
			6: 'Victoria',
			7: 'Charles'
		}
	}
}

def dictify_row(row,column_structure):
	dictified_row = {}
	for index, column_meta in enumerate(column_structure):
		column_name = column_meta.keys()[0]
		if column_name in field_lookups:
			dictified_row[column_name] = field_lookups[column_name]['values'][row[index]]
		else:
			dictified_row[column_name] = row[index]
	return dictified_row

def test_mmap():
	for table in tables:
		for table_name, table_structure in table.iteritems():
			cs = table_structure['column_structure']
			with open(table_structure['file_name']) as f:
				reader = csv.reader(f,dialect='excel-tab')
				for record in reader:
					row = [int(i) for i in record]
					row = dictify_row(row,cs)

times_to_test = 5
for i in range(times_to_test):
	t1 = time.time()
	test_mmap()
	t2 = time.time()
	print("Pseudo-Normalized: %f" % (t2-t1))

for i in range(times_to_test):
	t1 = time.time()
	with open('raw_data_with_names.tsv') as f:
		reader = csv.DictReader(f,dialect='excel-tab')
		for line in reader:
			line
	t2 = time.time()
	print("Reading from File: %f" % (t2-t1))