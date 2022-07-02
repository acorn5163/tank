from flask import Flask,render_template,request,Response
import tank
import math
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
            print("speed_origin"+str(request.form['speed']))
            print("deviation_origin"+str(request.form['deviation']))
            speed_per = math.floor(100*(int(request.form['speed'])/141))
            deviation_per = 100-math.floor(100*(int(request.form['deviation'])/100))
            print("speed_per:"+str(speed_per))
            print("deviation_per:"+str(deviation_per))
            speed_higher = math.floor(speed_per)
            speed_lower = math.floor(speed_per*deviation_per/100)

            if "forward"==request.form['directionY']:
                if "right"==request.form['directionX']:
                    #tank.forward(speed_lower,speed_higher)
                    speed_rightside = speed_lower
                    speed_leftside = speed_higher
                elif "left"==request.form['directionX']:
                    #tank.forward(speed_higher,speed_lower)
                    speed_rightside = speed_higher
                    speed_leftside = speed_lower
                elif "straight"==request.form['directionX']:
                    #tank.forward(speed_higher,speed_higher)
                    speed_rightside = speed_higher
                    speed_leftside = speed_higher
                else:
                    print("error")

                tank.forward(speed_rightside,speed_leftside)
                print("-"*20)
                print("forwarding,[right:"+str(speed_rightside)+"][left:"+str(speed_leftside)+"]")
                print("-"*20)
                

            elif "backward"==request.form['directionY']:
                if "right"==request.form['directionX']:
                    #tank.backward(speed_lower,speed_higher)
                    speed_rightside = speed_lower
                    speed_leftside = speed_higher
                elif "left"==request.form['directionX']:
                    #tank.backward(speed_higher,speed_lower)
                    speed_rightside = speed_higher
                    speed_leftside = speed_lower
                elif "straight"==request.form['directionX']:
                    #tank.backward(speed_higher,speed_higher)
                    speed_rightside = speed_higher
                    speed_leftside = speed_higher
                else:
                    print("error")
                tank.backward(speed_rightside,speed_leftside)
                print("-"*20)
                print("backwarding,[right:"+str(speed_rightside)+"][left:"+str(speed_leftside)+"]")
                print("-"*20)

            # elif "turnright"==request.form['direction']:
            #     print("-"*20)
            #     print("turning right")
            #     print("-"*20)
            #     tank.turnright(speed,speed-deviation)
            
            # elif "turnleft"==request.form['direction']:
            #     print("-"*20)
            #     print("turning left")
            #     print("-"*20)
            #     tank.turnleft(speed-deviation,speed)

            else:
                print("-"*20)
                print("error")
                tank.forward(0,0)
                print("-"*20)

    return render_template('index.html')

#@app.route("/video_feed")
#def video_feed():
    #return Response(gen(Camera()),
            #mimetype="multipart/x-mixed-replace; boundary=frame")



app.run("10.4.100.209",debug = True)


