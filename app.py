from fastapi import FastAPI, Request  # นำเข้าคลาส FastAPI (สำหรับสร้างแอป) และ Request (สำหรับรับข้อมูล) จากไลบรารี fastapi
app = FastAPI()  # สร้าง "แอป" หรือเซิร์ฟเวอร์หลัก โดยใช้คลาส FastAPI และเก็บไว้ในตัวแปรชื่อ app

@app.get("/")  # สร้าง "endpoint" หรือ "เส้นทาง" สำหรับการเชื่อมต่อแบบ GET ที่ URL หลัก ("/")
def root():  # สร้างฟังก์ชันชื่อ root() ที่จะทำงานเมื่อมีคนเรียกเส้นทางด้านบน
    return {"status": "OK"}  # สั่งให้ฟังก์ชันนี้ส่งข้อมูล {"status": "OK"} กลับไป (มักใช้เช็กว่าเซิร์ฟเวอร์ทำงานอยู่)

@app.post("/sensor")  # สร้าง endpoint ที่เส้นทาง "/sensor" แต่สำหรับรับการเชื่อมต่อแบบ POST (ส่งข้อมูลเข้ามา)
async def sensor(req: Request):  # สร้างฟังก์ชัน (แบบ async) ชื่อ sensor ที่จะทำงานเมื่อมีคน POST มาที่ /sensor
    data = await req.json()  # อรับข้อมูลที่ถูกส่งมา (เช่น จาก Insomnium) และแปลงข้อมูล JSON นั้นเป็น Python dictionary
    print(data)

    return {"status": "OK"}  # ส่งการตอบกลับเป็น {"status": "OK"} กลับไปหา Client (Insomnium) เพื่อยืนยันว่าได้รับข้อมูลแล้ว


if __name__ == "__main__":  # ตรวจสอบว่าไฟล์นี้ถูกรันโดยตรง (ไม่ได้ถูก import จากไฟล์อื่น)
    import uvicorn  # นำเข้า uvicorn ซึ่งเป็นโปรแกรมเซิร์ฟเวอร์สำหรับรัน FastAPI
    uvicorn.run(app, host="127.0.0.1", port=8000)  # สั่งให้ uvicorn เริ่มรัน "app" ของเรา โดยให้เปิดรอที่ http://127.0.0.1 (เครื่องตัวเอง) และ Port 8000

