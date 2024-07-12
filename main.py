from fastapi import FastAPI 
from fastapi.responses import StreamingResponse 
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 
from picamera2 import Picamera2  
import cv2 
import time 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cam = Picamera2()
config = cam.create_preview_configuration(main={"size": (640, 480)})
cam.configure(config)  
cam.start()  

def generate_frames():
    while True:  
        frame = cam.capture_array()  
        ret, buffer = cv2.imencode('.jpg', frame)  
        frame = buffer.tobytes()  
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.get("/videoFeed")
async def videoFeed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/takeImage")
async def takeImage():
    cam.capture_file(f"{time.time()}.jpg")
    return("captured")

@app.get("/forward")
async def forward():
    pass

@app.get("/backward")
async def forward():
    pass

@app.get("/right")
async def forward():
    pass

@app.get("/left")
async def forward():
    pass

@app.get("/stop")
async def forward():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)