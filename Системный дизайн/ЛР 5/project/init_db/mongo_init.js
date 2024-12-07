db.createCollection("messages");
db.messages.createIndex({ folder_id: 1 });