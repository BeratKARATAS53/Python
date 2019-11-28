import csv
import matplotlib.pyplot as plt


file = open("weather.txt","w")

date_time = []
temp = []
weather2 = []
with open("weather_2012.csv","r") as csvfile:
    reading = csv.reader(csvfile,delimiter=",")
    header = next(reading)
    for row in reading:
        date_time.append(row[0])
        temp.append(row[1])
        weather2.append(row[7])

for j in range(len(date_time)):
    file.write(str(date_time[j])+"!"+str(temp[j])+"!"+str(weather2[j])+"\n")
    j += 1

file.close()
file2 = open("weather.txt","r")

january,february,march,april,may,june,july,august,september,october,november,december = [],[],[],[],[],[],[],[],[],[],[],[]

### ALL OF WEATHERS: -- EXAMPLE : w1(CLEAR) or w8(FOG)
w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,w28,w29,w30,w31,w32,w33,\
w34,w35,w36,w37,w38,w39,w40,w41,w42,w43,w44,w45,w46,w47,w48,w49,w50 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],\
[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
###

t = []
for line in file2:
    item = line.rstrip("\n").split("!")
    global t
    t.append(float(item[1])) # temperature Ex: (1.8)
    if item[2] == "Clear":
        w1.append(item[1])
    elif item[2] == "Cloudy":
        w2.append(item[1])
    elif item[2] == "Drizzle":
        w3.append(item[1])
    elif item[2] == "Drizzle,Fog":
        w4.append(item[1])
    elif item[2] == "Drizzle,Ice Pellets,Fog":
        w5.append(item[1])
    elif item[2] == "Drizzle,Snow":
        w6.append(item[1])
    elif item[2] == "Drizzle,Snow,Fog":
        w7.append(item[1])
    elif item[2] == "Fog":
        w8.append(item[1])
    elif item[2] == "Freezing Drizzle":
        w9.append(item[1])
    elif item[2] == "Freezing Drizzle,Fog":
        w10.append(item[1])
    elif item[2] == "Freezing Drizzle,Haze":
        w11.append(item[1])
    elif item[2] == "Freezing Drizzle,Snow":
        w12.append(item[1])
    elif item[2] == "Freezing Fog":
        w13.append(item[1])
    elif item[2] == "Freezing Rain":
        w14.append(item[1])
    elif item[2] == "Freezing Rain,Fog":
        w15.append(item[1])
    elif item[2] == "Freezing Rain,Haze":
        w16.append(item[1])
    elif item[2] == "Freezing Rain,Ice Pellets,Fog":
        w17.append(item[1])
    elif item[2] == "Freezing Rain,Snow Grains":
        w18.append(item[1])
    elif item[2] == "Haze":
        w19.append(item[1])
    elif item[2] == "Mainly Clear":
        w20.append(item[1])
    elif item[2] == "Moderate Rain,Fog":
        w21.append(item[1])
    elif item[2] == "Moderate Snow":
        w22.append(item[1])
    elif item[2] == "Moderate Snow,Blowing Snow":
        w23.append(item[1])
    elif item[2] == "Mostly Cloudy":
        w24.append(item[1])
    elif item[2] == "Rain":
        w25.append(item[1])
    elif item[2] == "Rain Showers":
        w26.append(item[1])
    elif item[2] == "Rain Showers,Fog":
        w27.append(item[1])
    elif item[2] == "Rain Showers,Snow Showers":
        w28.append(item[1])
    elif item[2] == "Rain,Fog":
        w29.append(item[1])
    elif item[2] == "Rain,Haze":
        w30.append(item[1])
    elif item[2] == "Rain,Ice Pellets":
        w31.append(item[1])
    elif item[2] == "Rain,Snow":
        w32.append(item[1])
    elif item[2] == "Rain,Snow Grains":
        w33.append(item[1])
    elif item[2] == "Rain,Snow,Fog":
        w34.append(item[1])
    elif item[2] == "Rain,Snow,Ice Pellets":
        w35.append(item[1])
    elif item[2] == "Snow":
        w36.append(item[1])
    elif item[2] == "Snow Pellets":
        w37.append(item[1])
    elif item[2] == "Snow Showers":
        w38.append(item[1])
    elif item[2] == "Snow Showers,Fog":
        w39.append(item[1])
    elif item[2] == "Snow,Blowing Snow":
        w40.append(item[1])
    elif item[2] == "Snow,Fog":
        w41.append(item[1])
    elif item[2] == "Snow,Haze":
        w42.append(item[1])
    elif item[2] == "Snow,Ice Pellets":
        w43.append(item[1])
    elif item[2] == "Thunderstorms":
        w44.append(item[1])
    elif item[2] == "Thunderstorms,Heavy Rain Showers":
        w45.append(item[1])
    elif item[2] == "Thunderstorms,Moderate Rain Showers,Fog":
        w46.append(item[1])
    elif item[2] == "Thunderstorms,Rain":
        w47.append(item[1])
    elif item[2] == "Thunderstorms,Rain Showers":
        w48.append(item[1])
    elif item[2] == "Thunderstorms,Rain Showers,Fog":
        w49.append(item[1])
    elif item[2] == "Thunderstorms,Rain,Fog":
        w50.append(item[1])

january.extend(t[:744])
february.extend(t[745:1440])
march.extend(t[1441:2184])
april.extend(t[2185:2904])
may.extend(t[2905:3648])
june.extend(t[3649:4368])
july.extend(t[4369:5112])
august.extend(t[5113:5856])
september.extend(t[5857:6576])
october.extend(t[6577:7320])
november.extend(t[7321:8040])
december.extend(t[8041:8784])

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

max_temp = [max(january),max(february),max(march),max(april),max(may),max(june),max(july),
            max(august),max(september),max(october),max(november),max(december)]

space1 = 12*" "
print("\n","MONTHS",space1,"MAX  TEMPERATURE")
for j in range(len(months)):
    k = len(months[j])
    space1 = (20-k)*" "
    print("{}".format(months[j]),space1,"{}".format(max_temp[j]))

weather = ["Clear","Cloudy","Drizzle","Drizzle,Fog","Drizzle,Ice Pellets,Fog","Drizzle,Snow","Drizzle,Snow,Fog","Fog",
"Freezing Drizzle","Freezing Drizzle,Fog","Freezing Drizzle,Haze","Freezing Drizzle,Snow","Freezing Fog","Freezing Rain",
"Freezing Rain,Fog","Freezing Rain,Haze","Freezing Rain,Ice Pellets,Fog","Freezing Rain,Snow Grains","Haze","Mainly Clear",
"Moderate Rain,Fog","Moderate Snow","Moderate Snow,Blowing Snow","Mostly Cloudy","Rain","Rain Showers","Rain Showers,Fog",
"Rain Showers,Snow Showers","Rain,Fog","Rain,Haze","Rain,Ice Pellets","Rain,Snow","Rain,Snow Grains","Rain,Snow,Fog",
"Rain,Snow,Ice Pellets","Snow","Snow Pellets","Snow Showers","Snow Showers,Fog","Snow,Blowing Snow","Snow,Fog","Snow,Haze",
"Snow,Ice Pellets","Thunderstorms","Thunderstorms,Heavy Rain Showers","Thunderstorms,Moderate Rain Showers,Fog",
"Thunderstorms,Rain","Thunderstorms,Rain Showers","Thunderstorms,Rain Showers,Fog","Thunderstorms,Rain,Fog"]

def m(x): # MEAN TEMPERATURE
    total = 0
    for i in range(len(x)):
        total += float(x[i])
    return total/len(x)

means = [m(w1),m(w2),m(w3),m(w4),m(w5),m(w6),m(w7),m(w8),m(w9),m(w10),m(w11),m(w12),m(w13),m(w14),m(w15),m(w16),m(w17),
m(w18),m(w19),m(w20),m(w21),m(w22),m(w23),m(w24),m(w25),m(w26),m(w27),m(w28),m(w29),m(w30),m(w31),m(w32),m(w33),m(w34),
m(w35),m(w36),m(w37),m(w38),m(w39),m(w40),m(w41),m(w42),m(w43),m(w44),m(w45),m(w46),m(w47),m(w48),m(w49),m(w50)]

x_pos1 = [x for x in range(len(max_temp))]
x_pos2 = [x for x in range(len(means))]

plt.bar(x_pos1,max_temp,align="center",color="greenyellow")
plt.xticks(x_pos1,months,rotation=45)
plt.title("Max  Temperature  For  Months")
plt.tight_layout()
plt.savefig("maxtemp.png")
plt.show()

space2 = 32*" "
print("\n","WEATHER",space2,"MEAN  TEMPERATURE")
for i in range(len(weather)):
    k = len(weather[i])
    space2 = (40-k)*" "
    print("{}".format(weather[i]),space2,"{:.6f}".format(means[i]))

plt.figure(figsize=(17,10))
plt.bar(x_pos2,means,align="center",color="cyan",alpha=0.5)
plt.xticks(x_pos2,weather,rotation=45)
plt.title("Mean  Temperature  For  Weathers")
plt.xlim(-1,len(weather)+1)
plt.tight_layout()
plt.savefig("meantemp.png")
plt.show()
