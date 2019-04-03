import csv
import json

open("outputData.csv", "w").close()

def main():
	dates = {}
	with open('GymData.txt') as json_file:
		#variable to ensure proper data order
		prevDate = '3-4-19'
		onOff = 'off'

		data = json.load(json_file)
		startTime = 0

		for p in data['list']:
			#Check for errors in data order
			if(p['date'] == prevDate):
				print('Two dates in a row at ' + p['date'])
			if(p['power'] == onOff):
				print('On off at' + p['date'])

			#Set start time
			if (p['power'] == "on"):
				startTime = int(p['sec'])
				onOff = 'on'

			#Calculate total time with start and end time
			elif (p['power'] == "off"):
				dates[p['date']] = (int(p['sec']) - startTime)/60
				prevDate = p['date']
				onOff = 'off'

			else:
				print('Power is not on or off')


			#print('Power: ' + p['power'])
			#print('Date: ' + p['date'])
			#print('Time: ' + p['time'])
			#print('')

		with open('outputData.csv', 'a') as f:
			for key, value in dates.items():
				print(key +' '+ str(value))
				f.write(key + "," + str(value) + "\n")



main()
