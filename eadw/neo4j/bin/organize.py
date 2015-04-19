import re

f = open('export_data.cypher', 'r')
lines = f.readlines()

for line in lines:
	m = re.findall('_\d+', line)
	if m is not None:
		for n in m:
			line = line.replace(n, "_"+str(int(n[1:])-415568))

	print line



f.close()