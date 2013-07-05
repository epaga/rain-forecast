from forecastio import Forecastio
import os
os.system('cls' if os.name=='nt' else 'clear')
forecast = Forecastio("YOUR-API-KEY")
result = forecast.load_forecast(52.502737,13.391036) # your latitude/longitude (this is Berlin)
byHour = forecast.get_hourly()
for hourlyData in byHour.data[:22]:  # this is for the next 22 hours
  prob = hourlyData.precipProbability
  if (prob == None):
     prob = 0
  prob = int(round(prob * 50))
  hour = hourlyData.time.hour
  hourstring = str(hour)
  # intensity descriptions based on the forecast.io docs
  if (hourlyData.precipIntensity == 0):
     intensity = ""
  elif (hourlyData.precipIntensity < 0.006):
     intensity = "very light"
  elif (hourlyData.precipIntensity < 0.055):
     intensity = "light"
  elif (hourlyData.precipIntensity < 0.35):
     intensity = "moderate"
  else:
     intensity = "heavy"
  if (hour < 10):
     hourstring = "0"+hourstring
  print hourstring+" "+(prob*u'\u2588')+((50-prob)*" ")+" "+intensity
print
print " 0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0"
raw_input("")