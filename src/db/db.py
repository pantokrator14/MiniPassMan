import pymongo as pym

client = pym.MongoClient("mongodb+srv://minipassman-admin:password@minipassman.ouhpb.mongodb.net/name?retryWrites=true&w=majority")
db = client.MiniPassMan