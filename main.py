from flask import Flask,render_template,request,Response
import tank_copy
import math
import pigpio
#from camera import Camera
# import cv2

tank = tank_copy.Tank()
pi = pigpio.pi()


app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",speed=90)

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
    print("POST received")
    if request.method == "POST":
        posX = int(request.form['positionX'])
        posY = int(request.form['positionY'])
        print("X:"+str(posX)+" Y:"+str(posY))
        distanceX = int(math.fabs(posX))
        distanceY = int(math.fabs(posY))

        print("fabX:"+str(distanceX)+" fabY:"+str(distanceY))
        speed = math.floor(math.sqrt((distanceX**2)+(distanceY**2)))
        deviation = 0
        if posY != 0:
            deviation = math.floor(math.degrees(math.atan(math.fabs(posX/posY))))

        directionX = "null"
        directionY = "null"

        if posY > 0:
            directionY = "forward"
        elif posY < 0:
            directionY = "backward"
        else:
            directionY = "stop"

        if posX > 0:
            directionX = "right"
        elif posX < 0:
            directionX = "left"
        else:
            directionX = "straight"

        print("[directionX:"+directionX+"][directionY:"+directionY+"]")
        ################################
        if speed != None:
            print("[speed_origin:"+str(speed)+"]     [deviation_origin:"+str(deviation)+"]")
            speed_per = math.floor(100*(int(speed)/142))
            if deviation == 0:
                deviation_per = 100
            else:
                deviation_per = 100 - math.floor(deviation/0.9)
            print("[speed_per:"+str(speed_per)+"]        [deviation_per:"+str(deviation_per)+"]")
            speed_higher = math.floor(speed_per)
            speed_lower = math.floor(speed_per*deviation_per/100)

            if "forward"==directionY:
                if "right"==directionX:
                    #tank.forward(speed_lower,speed_higher)
                    speed_rightside = speed_lower
                    speed_leftside = speed_higher
                elif "left"==directionX:
                    #tank.forward(speed_higher,speed_lower)
                    speed_rightside = speed_higher
                    speed_leftside = speed_lower
                elif "straight"==directionX:
                    #tank.forward(speed_higher,speed_higher)
                    speed_rightside = speed_higher
                    speed_leftside = speed_higher
                else:
                    print("error")

                tank.forward(speed_rightside,speed_leftside)
                print("-"*20)
                print("forwarding,[right:"+str(speed_rightside)+"][left:"+str(speed_leftside)+"]")
                print("-"*20)
                

            elif "backward"==directionY:
                if "right"==directionX:
                    #tank.backward(speed_lower,speed_higher)
                    speed_rightside = speed_lower
                    speed_leftside = speed_higher
                elif "left"==directionX:
                    #tank.backward(speed_higher,speed_lower)
                    speed_rightside = speed_higher
                    speed_leftside = speed_lower
                elif "straight"==directionX:
                    #tank.backward(speed_higher,speed_higher)
                    speed_rightside = speed_higher
                    speed_leftside = speed_higher
                else:
                    print("error")
                tank.backward(speed_rightside,speed_leftside)
                print("-"*20)
                print("backwarding,[right:"+str(speed_rightside)+"][left:"+str(speed_leftside)+"]")
                print("-"*20)

            elif "stop" == directionY:
                if "straight" == directionX:
                    tank.stop()
                    print("-"*20)
                    print("stopping")
                    print("-"*20)
                elif "right" == directionX:
                    tank.turnright(speed_higher)
                    print("-"*20)
                    print("turning right,["+speed_higher+"]")
                    print("-"*20)
                elif "left" == directionX:
                    tank.turnleft(speed_higher)
                    print("-"*20)
                    print("turning left,["+ speed_higher+"]")
                    print("-"*20)
            else:
                print("-"*20)
                print("error")
                tank.close()
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



            return render_template('index.html',speed = 40)


#@app.route("/video_feed")
#def video_feed():
    #return Response(gen(Camera()),
            #mimetype="multipart/x-mixed-replace; boundary=frame")



app.run("10.4.100.209",debug = True)


