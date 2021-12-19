from PIL import Image, ImageDraw , ImageFont

import pandas as pd 





##using a csv 

list = pd.read_csv("file.csv")


name_list = list["Name"].to_list()


for i in list:


    img = Image.open("award.jpg")

    d = ImageDraw.Draw(img)

    location = (361,422,675,447)

    text_color = (0, 137 , 209)

    font = ImageFont.truetype("arial.ttf",20)

    d.text(location, i , fill=text_color, font=font)


    img.save("Certificate_" + i + ".pdf")




## passing a name individually 

"""i = "Akinwumi Iyanuoluwa Ayo"
img = Image.open("award.jpg")

d = ImageDraw.Draw(img)

location = (361,422,675,447)

text_color = (0, 0, 0)

font = ImageFont.truetype("arial.ttf",20)

d.text(location, i , fill=text_color, font=font)


img.save("Certificate_" + i + ".pdf")"""