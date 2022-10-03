#Dictonary zip Challenge
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
keysValues = dict(zip(keys, values))
print(keysValues)

#Dictionary Key challenge
sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
                }
            }
        }
    }
print(sampleDict["class"]["student"]["marks"]["history"])

#Dictionary delete challenge
sampleDict = {
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"

}
sampleDict.pop("name")
sampleDict.pop("salary")
print(sampleDict)

#Dictonary rename key
sampleDict = {
    "name": "Kelly",
    "age":25,
    "salary":8000,
    "city": "New york"
}
sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)
