let joy = new JoyStick('joyDiv');

setInterval(direction,100);



function direction(){
    let dir=joy.GetDir();
    console.log(dir);
    console.log("------------------")
    let posX=joy.GetX();
    let posY=joy.GetY();
    console.log("X:"+posX);
    console.log("Y:"+posY);

    console.log("------------------")
    let speed = Math.abs(Math.floor(Math.sqrt(posX**2+posY**2)));
    let deviation = 50;
    if (posY !=0)
    {
        deviation = Math.abs(Math.floor(posX/posY));
    }
    console.log("------------------")
    if (posY>=0)
    {
        if(posX>0)
        {
            tankCmd("forward","right",speed,deviation);
            console.log('fr');
        }
        else if(posX<0)
        {
            tankCmd("forward","left",speed,deviation);
            console.log('fl');
        }
        else if(posX==0)
        {
            tankCmd("forward","straight",speed,deviation);
            console.log('f');
        }
    }
    if (posY<0)
    {
        if(posX>0)
        {
            tankCmd("backward","right",speed,deviation);
            console.log('br');
        }
        else if(posX<0)
        {
            tankCmd("backward","left",speed,deviation);
            console.log('bl');
        }
        else if(posX==0)
        {
            tankCmd("backward","straight",speed,deviation);
            console.log('b');
        }
    }
    else if (posY==0 & posX==0)
    {
        tankCmd("stop","straight",speed,deviation);
    }
}


function tankCmd(directionY,directionX,speed=0,deviation=0)
{
    console.log(directionY);
    let form = document.createElement("form")
    form.setAttribute("action","/on")
    form.setAttribute("method","post")
    form.setAttribute("target","hiddeniframe")
    form.setAttribute("onsubmit","dosomething();return false")
    form.style.display = "none";
    console.log("speed" + speed);
    console.log("deviation" + deviation);
    document.body.appendChild(form);

    let inputdirectionY;
    inputdirectionY = document.createElement("input");
    inputdirectionY.setAttribute("type","hidden");
    inputdirectionY.setAttribute("name","directionY");
    inputdirectionY.setAttribute("value",directionY);

    let inputdirectionX;
    inputdirectionX = document.createElement("input");
    inputdirectionX.setAttribute("type","hidden");
    inputdirectionX.setAttribute("name","directionX");
    inputdirectionX.setAttribute("value",directionX);

    let inputspeed;
    inputspeed = document.createElement("input");
    inputspeed.setAttribute("type","hidden");
    inputspeed.setAttribute("name","speed");
    inputspeed.setAttribute("value",speed);

    let inputdeviation;
    inputdeviation = document.createElement("input");
    inputdeviation.setAttribute("type","hidden");
    inputdeviation.setAttribute("name","deviation");
    inputdeviation.setAttribute("value",deviation);
    
    form.appendChild(inputdirectionY,inputdirectionX,inputspeed,inputdeviation);
}