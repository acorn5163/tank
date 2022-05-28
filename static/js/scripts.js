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
    let speed = Math.sqrt(posX**2+posY**2);
    let deviation = 0
    if (posY !=0)
    {
        deviation = posX/posY;
    }
    console.log("------------------")
    if (posY>0)
    {
        tankCmd("forward",speed,deviation);
        console.log('f');
    }
    else if (posY<0)
    {
        tankCmd("backward",speed,deviation);
        console.log('b');
    }
    else if (posY==0)
    {
        tankCmd("stop",speed,deviation);
    }
}


function tankCmd(direction,speed=0,deviation=0)
{
    console.log(direction);
    let form = document.createElement("form")
    form.setAttribute("action","/on")
    form.setAttribute("method","post")
    form.setAttribute("target","hiddeniframe")
    form.setAttribute("onsubmit","dosomething();return false")
    form.style.display = "none";
    console.log(speed);
    document.body.appendChild(form);

    let inputdirection;
    inputdirection = document.createElement("inputdirection");
    inputdirection.setAttribute("type","hidden");
    inputdirection.setAttribute("name","direction");
    inputdirection.setAttribute("value",direction);

    let inputspeed;
    inputspeed = document.createElement("inputspeed");
    inputspeed.setAttribute("type","hidden");
    inputspeed.setAttribute("name","speed");
    inputspeed.setAttribute("value",speed);

    let inputdeviation;
    inputdeviation = document.createElement("inputdeviation");
    inputdeviation.setAttribute("type","hidden");
    inputdeviation.setAttribute("name","deviation");
    inputdeviation.setAttribute("value",deviation);
    
    form.appendChild(inputdirection,inputspeed,inputdeviation);
    form.submit();
    return false;
}