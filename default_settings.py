
# The size of the screen: (to find this out, make a slideshow,
# load it onto the destination system in Firefox, and press F11, 
# then F5. The size will be shown at the top of the page.
# (F11 to exit full-screen mode again)
#
screen_size = {'x': 1184, 'y': 620}  # For the Raspberry Pi on my telly.

# Name of the HTML file to generate
output_filename = "out.html"

# Where to find the image files
images_folder = "images"

# How long to show each picture for, in seconds.
delay_between_slides = 5

# Name of the template file (you can usually leave this alone)
template = "slideshow_1.html"

# Whether to display the digital clock
# For the digital clock, ensure flipclock.min.js, flipclock.css
# and jquery-3.2.1.min.js are installed in the images/ folder.
show_digital_clock = True

# Further settings for the digital clock
show_clock_seconds = False
clock_pos_left = '60%'
clock_pos_top = '95%'
