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
        if request.form['speed'] != None:
            speed = 100*(int(request.form['speed'])/141) #make speed %
            print("speed_persent:"+speed)
            deviation = 100*(1 - int(request.form['deviation'])/50)# make deviation %
            print("deviation_persent:"+deviation)

        print(request.form['directionY'])
        if "forward"==request.form['directionY']:
            print("-"*20)
            print("forwarding")
            print("-"*20)
            if "right"==request.form['directionX']:
                tank.forward(speed*deviation,speed)
            elif "left"==request.form['directionX']:
                tank.forward(speed,speed*deviation)
            elif "straight"==request.form['directionX']:
                tank.forward(speed,speed)
            

        elif "backward"==request.form['directionY']:
            print("-"*20)
            print("backwarding")
            print("-"*20)
            if "right"==request.form['directionX']:
                tank.backward(speed*deviation,speed)
            elif "left"==request.form['directionX']:
                tank.backward(speed,speed*deviation)
            elif "straight"==request.form['directionX']:
                tank.backward(speed,speed)

        #elif "turnright"==request.form['direction']:
            #print("-"*20)
            #print("turning right")
            #print("-"*20)
            #tank.turnright(speed,speed-deviation)
        
        #elif "turnleft"==request.form['direction']:
            #print("-"*20)
            #print("turning left")
            #print("-"*20)
            #tank.turnleft(speed-deviation,speed)

        elif "stop"==request.form['direction']:
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


app.run("0.0.0.0",debug = True)
