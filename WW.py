import pystray
import datetime
import time
from PIL import Image, ImageDraw, ImageFont

width = 32
height = 32
color1 = "white"
color2 = "black"

def run_loop(icon, count=0):
    if count % 30 == 0:
        icon.visible = True
        icon.icon = create_image(icon)
        count = 0
    time.sleep(5)
    run_loop(icon, count+5)

def create_image(icon=None):
    # Generate an image and draw a pattern
    week = datetime.datetime.now().isocalendar()[1]
    wwtxt = '{week:02d}'.format(week=week)
#    wwtxt = '{}'.format(int(time.time())%52)
    if icon == None:
        image = Image.new('RGB', (width, height), color2)
    else:
        image = icon.icon
    fnt = ImageFont.truetype('consolab.ttf', 18)
    dc = ImageDraw.Draw(image)
    dc.rectangle([(0,0),(width,height)], fill=color2)
    dc.text((0,0), "WW", font=fnt, fill=color1)
    dc.text((0,16), wwtxt, font=fnt, fill=color1)
    return image

icon = pystray.Icon('systray-workweek', run_loop)
icon.icon = create_image()

try:
    icon.run(run_loop)
except KeyboardInterrupt:
    sys.exit(0)
except Exception as e:
    print("Exception Occured \n" + str(e))
    sys.exit(1)
finally:
    icon.stop()
    sys.exit(0)
