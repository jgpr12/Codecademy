"""In this project, we'll use Bitwise operators to build a calculator that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

We'll add three methods to the project:

A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle"""

def rgb_hex():
  invalid_msg = "Invalid values were entered..."
  rgb = {"R":0,"G":0,"B":0}
  
  for color in rgb:
    rgb[color] = int(raw_input("Enter an amount for " + color + ":"))
    if rgb[color] < 0 or rgb[color] > 255:
      print invalid_msg
      return
  val = (rgb["R"] << 16) + (rgb["G"] << 8) + rgb["B"]
  print hex(val)[2:].upper()

def hex_rgb():
  rgb = {"R":0,"G":0,"B":0}
  hex_val = raw_input("Enter the hex value: ")
  if not(len(hex_val) == 6):
    print "Invalid value entered..."
    return
  hex_val = int(hex_val,16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print str(red)+str(green)+str(blue)

def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. ENter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == str(1):
      print "RGB to HEX..."
      rgb_hex()
    elif option == str(2):
      print "HEX to RGB..."
      hex_rgb()
    elif option.upper() == "X":
      break
    else:
      print "Error"

convert()