import picamera, time, sched, requests, base64

from PIL import Image

s = sched.scheduler(time.time, time.sleep)
cam = picamera.PiCamera()
url = "http://138.197.175.107/api/fridgecontents/"
def take_picture_save(sc):
    cam.capture('current.jpeg')
    s.enter(600,1,take_picture_save,(sc,))
    # Open file and then go ahead and include it in payload
    img = Image.open('current.jpeg')
    img2 = img.rotate(90)
    img2.save('current1.jpeg')
    img2 = open('current1.jpeg', 'rb')
    img_read = img2.read()
    img_base_64 = base64.encodestring(img_read)
    payload = {'user_name': 'iosAcct', 'img': img_base_64}
    response = requests.request("POST", url, data=payload)
    
s.enter(600,1,take_picture_save,(s,))
s.run()

