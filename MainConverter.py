#Colour Converter
#ask user input a value for red, green, and blue from (0-255) 
red = int(input("input a color for red from 0-255: ").strip())
green = int(input("input a color for green from 0-255: ").strip())
blue = int(input("input a color for blue from 0-255: ").strip())
#Change RGB to HEX function, while store the RGB value in a tuple, learned from:
#https://www.reddit.com/r/learnpython/comments/kbxbsi/rgb_string_value_to_hex_python_38/
def to_hex():
    rgb_tuple = (colours_rgb[0],colours_rgb[1],colours_rgb[2]) #make the list in to an turple
    colours_hex = "#{:02X}{:02X}{:02X}".format(*rgb_tuple)
    print(f"HEX: {colours_hex}")
#check if the colour is within 0 to 255, If so then add it to a list
colours_rgb = [] 
if 0 <= red <= 255: 
    colours_rgb.append(red) 
    if 0 <= green <= 255: 
        colours_rgb.append(green) 
        if 0 <= blue <= 255: 
            colours_rgb.append(blue)  
        else: 
            print("invalid blue color") 
    else: 
        print("invalid green color") 
else: 
    print("invalid red color")
#Conclusion/Print out the value from this colour converter function
print(f"RGB: {colours_rgb}") 
to_hex()
