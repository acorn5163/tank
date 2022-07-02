let joy = new JoyStick('joyDiv');

setInterval(direction,10000);



function direction(){
    let dir=joy.GetDir();
    console.log(dir);

    console.log("------------------");
    let posX=joy.GetX();
    let posY=joy.GetY();
    console.log("X:"+posX);
    console.log("Y:"+posY);
    console.log("------------------");

    let speed =Math.floor(Math.sqrt(posX**2+posY**2));
    console.log("speed:"+speed);
    let deviation = 1;
    if (posX !=0)
    {
        deviation = Math.abs(Math.floor(posX/posY));
    }
    console.log("deviation:"+deviation);
    console.log("------------------");

    let temp_directionX = "null";
    let temp_directionY = "null";

    if (posY>0)
    {
        temp_directionY = "forward";
        if(posX>0)
        {
            temp_directionX = "right";
            ///tankCmd("forward","right",speed,deviation);
            console.log('script:forward_right');
        }
        else if(posX<0)
        {
            temp_directionX = "left";
            ///tankCmd("forward","left",speed,deviation);
            console.log('script:forward_left');
        }
        else if(posX==0)
        {
            temp_directionX = "straight";
            ///tankCmd("forward","straight",speed,deviation);
            console.log('script:forward_straight');
        }
    }

    else if (posY<0)
    {
        temp_directionY = "backward";
        if(posX>0)
        {
            temp_directionX = "right";
            ///tankCmd("backward","right",speed,deviation);
            console.log('script:backward_right');
        }
        else if(posX<0)
        {
            temp_directionX = "left";
            ///tankCmd("backward","left",speed,deviation);
            console.log('script:backward_left');
        }
        else if(posX==0)
        {
            temp_directionX = "straight";
            ///tankCmd("backward","straight",speed,deviation);
            console.log('script:backward_straight');

        }
    }
    tankCmd(temp_directionY,temp_directionX,speed,deviation)
}
 

function tankCmd(directionY,directionX,speed=0,deviation=0)
{
    console.log(directionY);
    let form = document.createElement("form")
    form.setAttribute("action","/on")
    form.setAttribute("method","post")
    form.setAttribute("target","hiddeniframe")
    form.style.display = "none";
    console.log("speed" + speed);
    console.log("deviation" + deviation);
    document.body.appendChild(form);

    let inputdirectionY;
    inputdirectionY = document.createElement("input");
    inputdirectionY.setAttribute("type","hidden");
    inputdirectionY.setAttribute("name","directionY");
    inputdirectionY.setAttribute("value",directionY);
    form.appendChild(inputdirectionY);

    let inputdirectionX;
    inputdirectionX = document.createElement("input");
    inputdirectionX.setAttribute("type","hidden");
    inputdirectionX.setAttribute("name","directionX");
    inputdirectionX.setAttribute("value",directionX);
    form.appendChild(inputdirectionX);

    let inputspeed;
    inputspeed = document.createElement("input");
    inputspeed.setAttribute("type","hidden");
    inputspeed.setAttribute("name","speed");
    inputspeed.setAttribute("value",speed);
    form.appendChild(inputspeed);

    let inputdeviation;
    inputdeviation = document.createElement("input");
    inputdeviation.setAttribute("type","hidden");
    inputdeviation.setAttribute("name","deviation");
    inputdeviation.setAttribute("value",deviation);
    form.appendChild(inputdeviation);
    
    form.submit();
}