var num1=prompt("enter the number");
var num2=prompt("enter the number");
var num3=prompt("enter the number");
if(num1>num2 && num1>num3){
if(num2>num3){
alert("num2 is the second largest"+num2)
}
      }
else if(num2>num1 && num2>num3){
if(num1>num3){
alert("num1 is second largest"+num1)
}

}
else if(num3>num1 && num3>num2){
if(num3>num2){
alert("num3 is the second "+num3)
}
}
else{
alert("nothing")
}
