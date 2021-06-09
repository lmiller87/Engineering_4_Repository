# Engineering_4_Repository

## Hangman 







## Strings and Loops

![Screen Shot 2020-11-18 at 10 04 28 AM](https://user-images.githubusercontent.com/54447117/99547455-8ee9ac80-2985-11eb-82a6-ca1e817c1e4d.png)

### Reflection
I made this code somewhat quickly, I also looked around the internet to help me with this project, and it actually came out better than I expected. You essentially just in the initiallizing string, you put in what you want to output, and it creates a vertical string of the letters in the word. Unfortunately my Raspberry pi has kind of been 60-40 and it usually doesnt let me connect to the internet, I had to find an online Python code system, which worked well as a temperary fix to my problem, but im looking into the pi so I can push this assignment to my repo. 

## Quadratic Solver

![Screen Shot 2020-11-18 at 9 52 28 AM](https://user-images.githubusercontent.com/54447117/99545915-da9b5680-2983-11eb-85d5-40244cf35354.png)

### Reflection
I enjoyed this porject because i got to spend time searching the internet for different ways people did it. I found this one on the interent that helped me create a simple input Quadratic Solver. I basically just have to put in values and if they factor out it gives me roots, and if the numbers arent nice, it displays no real numbers in the equation. 

## Calculator

![Screen Shot 2020-11-18 at 10 20 26 AM](https://user-images.githubusercontent.com/54447117/99549574-cc4f3980-2987-11eb-90b5-d05e45715e2b.png)
![Screen Shot 2020-11-18 at 10 20 46 AM](https://user-images.githubusercontent.com/54447117/99549632-dcffaf80-2987-11eb-8200-ffe5484810ce.png)

### Comments that I didnt put into my code:
#The entire first half of this code, is literally just setting up the different types of math the calculator uses(Add,Sub,Mult,Div)
#Lines 11-15 are the input function, that ask what math you want to use in the output. 
#The while statement is establishing what the function will do once you select an option.
#Lines 23-35 are establishing what each math system does (ex Add = x + y, Div = x/y, etc.) This also puts out an input for you to choose which numbers you want to us, because you cant use x and y.
### Reflection
This project took me a long time to perfect. I tried to take a few ideas I saw online and put them together. It essentially has 2 different input sections, one asking if you want to add,subtract,multiply or divide, and the next asking for the two numbers that you want to do this with. It then does what ever you chose to those two numbers and outputs them. The most difficult part was linking the different types of math to the numbers themselves because it originally just added everytime. But that was about the only problem. 

## Dice Roller

![Screenshot 2020-11-04 at 1 12 45 PM](https://user-images.githubusercontent.com/54447117/98152380-a3b34400-1e9f-11eb-8707-5db74a5e6b42.png)

#line 3/4 are setting the random number range.
#Line 5 starts or cancels the function( Yes starts, No stops)
#Line 8 prints the numbers you rolled and adds them together into a sum.
#The last few lines are put their for when you roll doubles, they just congratulate you. 
        
### Reflection 
In this assignment I treid a slighly different code for the porject. I got it to work for about 5 minutes, however it stopped working after that and im trying to fix it. I thought I'd put my code in anyways for a grade and advice. I decided to make two variable, num1 and num2 and these depict the two different dice. Each one is rolled at the same time and each gives a number. My code is suppsoed to display them and add them together to get the sum of the two. It also asks to re roll afterwards. The main issue that I think im having/ had is the second dice rolling and them adding, the first time I did it it only printed the first number, I then messed with it for a little while and relaized I didnt have brackets and qoutations in the right places, so I got it to work from that. Im still working out the bugs and trying to get it working again. 


## Hello Flask

``` ruby
 from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
     return "hello world!"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
```

### Reflection 
I had a little but of trouble with this assignment because I was having trouble getting my pi to connect to the internet at my house, luckily Philip helped me fix the problem and I was able to get this working. 


## GPIO Flask

``` ruby
<!doctype html>
<html>
<head>
     <title>GPIO with Flask!</title>
<style>

button{
	    display: block;
	height: 100px;
	border-style: dashed solid;
	padding: 14px 28px;
	font-size: 16px;
	color: #ecf2f9;
}
button:active{
	position:relative;
	top:1px;
}
.btn1 {
	background-color: #9c9c9c; 
	} 
.btn2 {
	background-color: #9c9c9c;
	}
.btn3 {
	background-color: #9c9c9c;
}
.btn4 {
	background-color: #9c9c9c;
}
body{
background-color: #0A0A0A;
}

</style>
</head>
<body>
{{msg}}

<form method="POST">
     <button type="submit" name="button1" class="button btn1" value="button1">LED 1 On</button>
     <button type="submit" name="button2" class="button btn2" value="button2">LED 1 Off</button>
     <button type="submit" name="button3" class="button btn3" value="button3">LED 2 On</button>
     <button type="submit" name="button4" class="button btn4" value="button4">LED 2 Off</button>

</form>
</body>
</html>
```

### Relfection
Not too bad, I was reffered to (https://w3schools.com/) and I thought it was helpful!

## Headless

```ruby
import time
import Adafruit_SSD1306
import Adafruit_LSM303
import math

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
accelerometer = Adafruit_LSM303.LSM303() 
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) 
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height 
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image) 
draw.rectangle((0,0,width,height), outline=0, fill=0) 


padding = 2
shape_width = 20
top = padding
bottom = height - padding
x = padding
font = ImageFont.load_default()

x_Changer = 0

while True:

	
	x_Value = x + x_Changer


	accel, mag = accelerometer.read() 
	accel_x, accel_y, accel_z = accel 
	mag_x, mag_y, mag_z = mag 
	

	
	dataValue = abs(accel_x/10)
	
	if dataValue <= 3:
		dataValue = 3
	
	print(dataValue)



	draw.text((x, top), "Accel Data:", font=font, fill=255) 
	
	
	draw.text((x_Value, top + dataValue),".", font=font, fill=255) 


	
	disp.image(image) # displays x, y, z, and header
	disp.display()

	
	x_Changer = x_Changer + 1 

	time.sleep(.1) #debug
```


### Reflection
It was fun, It took me a while to understand how to do it and I needed some insight from other sources and people but still fun. 


## CopyPasta

```ruby
from gpiozero import MotionSensor

from picamera import PiCamera

import datetime

pir = MotionSensor(4)
	camera = PiCamera()
	now = datetime.datetime.now()
	filename = "intruder_" + str(now).replace(" ", "_") + ".h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	camera.stop_preview()
```


### Reflection 
Still fun but it took me a while to get my pi working as usual.

## Copypasta2


![python](https://user-images.githubusercontent.com/54447117/121379292-e0518d00-c911-11eb-9176-f2f5722c1987.PNG)




### Reflection	
Needed help with this, difficult.
