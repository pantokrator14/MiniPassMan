import pymongo as pym

client = pym.MongoClient("mongodb+srv://minipassman-admin:hB3U42m6GV7JEGjs@minipassman.ouhpb.mongodb.net/miniPassMan?retryWrites=true&w=majority")
db = client.test