#region Definition
import datetime
f = open("input.txt", "r")
somme = 0
answerList = list()
seeds = list()
seed_to_soil = list()
seed_to_soil_clear = list()
soil_to_fertilizer = list()
soil_to_fertilizer_clear = list()
fertilizer_to_water = list()
fertilizer_to_water_clear = list()
water_to_light = list()
water_to_light_clear = list()
light_to_temperature = list()
light_to_temperature_clear = list()
temperature_to_humidity = list()
temperature_to_humidity_clear = list()
humidity_to_location = list()
humidity_to_location_clear = list()
#endregion

def readFile():
    data = f.read().split('\n\n')
    for line in data:
        typeLine = line.split(':')[0]
        datas = line.split(':')[1].strip().split('\n')
        match typeLine:
            case 'seeds':
                seeds.extend(datas)
            case 'seed-to-soil map':
                seed_to_soil.extend(datas)
            case 'soil-to-fertilizer map':
                soil_to_fertilizer.extend(datas)
            case 'fertilizer-to-water map':
                fertilizer_to_water.extend(datas)
            case 'water-to-light map':
                water_to_light.extend(datas)
            case 'light-to-temperature map':
                light_to_temperature.extend(datas)
            case 'temperature-to-humidity map':
                temperature_to_humidity.extend(datas)
            case 'humidity-to-location map':
                humidity_to_location.extend(datas)
def processlist():
    for seed in seed_to_soil:
        array = list()
        itemArray = seed.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        seed_to_soil_clear.append(array)
    for soil in soil_to_fertilizer:
        array = list()
        itemArray = soil.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        soil_to_fertilizer_clear.append(array)
    for fertilizer in fertilizer_to_water:
        array = list()
        itemArray = fertilizer.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        fertilizer_to_water_clear.append(array)
    for water in water_to_light:
        array = list()
        itemArray = water.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        water_to_light_clear.append(array)
    for light in light_to_temperature:
        array = list()
        itemArray = light.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        light_to_temperature_clear.append(array)
    for temperature in temperature_to_humidity:
        array = list()
        itemArray = temperature.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        temperature_to_humidity_clear.append(array)
    for humidity in humidity_to_location:
        array = list()
        itemArray = humidity.split(' ')
        array.append(int(itemArray[1]))
        array.append(int(itemArray[1])+int(itemArray[2]))
        array.append(int(itemArray[0]))
        array.append(int(itemArray[0])+int(itemArray[2]))
        array.append(int(itemArray[2]))
        humidity_to_location_clear.append(array) 
        

def processNumber(numberSemence, array):
    filtered =  [row for row in array if numberSemence >= int(row[0]) and numberSemence < int(row[1])]
    if len(filtered) > 0:
        diff = numberSemence - filtered[0][0]
        value = filtered[0][2] + diff
    else:
        value = numberSemence
    return value

readFile()
processlist()
defineRange = list()
seedClear = seeds[0].split(' ')
for i in range(0,len(seedClear),2):
    line = list()
    line.append(int(seedClear[i]))
    line.append(int(seedClear[i]) + int(seedClear[i+1]))
    defineRange.append(line)

solver= {}
diff = defineRange[0][1] - defineRange[0][0]
print(diff)
print(datetime.datetime.now())
for i in range(defineRange[0][0], defineRange[0][1]):
    res = processNumber(int(i), seed_to_soil_clear)
    res = processNumber(res, soil_to_fertilizer_clear)
    res = processNumber(res, fertilizer_to_water_clear)
    res = processNumber(res, water_to_light_clear)
    res = processNumber(res, light_to_temperature_clear)
    res = processNumber(res, temperature_to_humidity_clear)
    res = processNumber(res, humidity_to_location_clear)
    answerList.append(res)
    if i % 1000000 == 0:
       print(datetime.datetime.now())


print(min(answerList))