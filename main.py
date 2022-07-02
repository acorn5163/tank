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
<<<<<<< HEAD
            speed_per = Math.floor(100*(request.form['speed']/141))
            deviation_per = 100-Math.floor(2*(request.form['deviation']))
            print("speed_per:"+speed_per)
            print("deviation_per"+deviation_per)
            speed_higher = speed_per
            speed_lower = speed_per*deviation_per

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
            speed = math.floor(100*((int(request.form['speed']))/141)) #make speed %
            print("speed_persent:"+str(speed))
            deviation = math.floor(100*(1 - int(request.form['deviation'])/50))# make deviation %
            print("deviation_persent:"+str(deviation))
            speed_higher= speed
            speed_lower = math.floor(speed*deviation/100)
            print("highside:"+str(speed_higher)+"lowside:"+str(speed_lower))

        print(request.form['directionY'])
        if "forward"==request.form['directionY']:
            print("-"*20)
            print("forwarding")
            print("-"*20)
            if "right"==request.form['directionX']:
                tank.forward(speed_lower,speed_higher)
            elif "left"==request.form['directionX']:
                tank.forward(speed_higher,speed_lower)
            else:
                tank.forward(speed_higher,speed_higher)
            

        elif "backward"==request.form['directionY']:
            print("-"*20)
            print("backwarding")
            print("-"*20)
            if "right"==request.form['directionX']:
                tank.backward(speed_lower,speed_higher)
            elif "left"==request.form['directionX']:
                tank.backward(speed_higher,speed_lower)
            else:
                tank.backward(speed_higher,speed_higher)
            

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

        else:
            print("-"*20)
            print("stopping")
            tank.forward(0,0)
            print("-"*20)
>>>>>>> development
        

        #prestates=request.form['name']
    return render_template('index.html')

#@app.route("/video_feed")
#def video_feed():
    #return Response(gen(Camera()),
            #mimetype="multipart/x-mixed-replace; boundary=frame")


<<<<<<< HEAD
app.run("10.4.100.209",debug = True)
=======
app.run("0.0.0.0",debug = True)
>>>>>>> development
