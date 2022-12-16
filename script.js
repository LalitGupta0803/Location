const successCallBack = (position) =>{
    console.log(position)
    positionMain = [position["coords"]["latitude"],position["coords"]["longitude"]]
};
const errorCallBack = (error) =>{
    console.log(error)
};
navigator.geolocation.getCurrentPosition(successCallBack, errorCallBack);
