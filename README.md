# lineChatBot
ไฟล์ .py สำหรับรัน application server ด้วย Flask
application server ใน code ตัวอย่างนี้ เชื่อมต่อกับ database Firestore ของ Google Firebase
โดยในขั้นตอนการทำ authentication เพื่อเชื่อมต่อกับ Firebase ต้อง download Private key ที่เป็นไฟล์ .json ของ project มาวางใน directory เดียวกันกับ file .py

document สำหรับ json object ที่รับส่ง กับ Dialogflow สามารถอ่านได้ที่
https://developers.google.com/actions/build/json/dialogflow-webhook-json
