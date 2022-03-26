from flask import Flask,render_template,request,Response
import tank
#from camera import Camera
# import cv2

tank = tank.Tank()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#def gen(camera):
    #while True:
        #frame = camera.get_frame()

        #if frame is not None:
            #yield (b"--frame\r\n"
                #b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        #else:
            #print("frame is none")


@app.route('/on',methods=["POST"])
def control():
    if request.method == "POST":
        print(request.form['name'])
        if "forward"==request.form['name']:
            print("-"*20)
            print("forwarding")
            print("-"*20)
            tank.forward()

        elif "backward"==request.form['name']:
            print("-"*20)
            print("backwarding")
            print("-"*20)
            tank.backward()

        elif "turnright"==request.form['name']:
            print("-"*20)
            print("turning right")
            print("-"*20)
            tank.turnright()
        
        elif "turnleft"==request.form['name']:
            print("-"*20)
            print("turning left")
            print("-"*20)
            tank.turnleft()

        elif "stop"==request.form['name']:
            print("-"*20)
            print("stopping")
            print("-"*20)
            tank.stop()

        else:
            print("-"*20)
            print("error")
            print("-"*20)
        

        #prestates=request.form['name']
    return render_template('index.html')

#@app.route("/video_feed")
#def video_feed():
    #return Response(gen(Camera()),
            #mimetype="multipart/x-mixed-replace; boundary=frame")


app.run("0.0.0.0")
