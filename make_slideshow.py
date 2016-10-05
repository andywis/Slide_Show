#!/usr/bin/env python

import os

from jinja2 import Environment, FileSystemLoader

# To customise the settings, copy the file "default_settings.py"
# and save it as "settings.py". See comments in default_settings.py
# for explanations.
if os.path.exists("settings.py"):
    import settings
else:
     import default_settings as settings

# Find all the images
image_filenames = [os.path.join(settings.images_folder, fn) 
    for fn in os.listdir(settings.images_folder) 
    if os.path.isfile(os.path.join(settings.images_folder, fn))]

# Build the context to pass on to the Jinja template
context = {
    'width': settings.screen_size['x'],
    'height': settings.screen_size['y'],
    'delay': settings.delay_between_slides,
    'image_filenames': sorted(image_filenames),
    }

# Load and render the template.
template_env = Environment(loader=FileSystemLoader('templates'))
template = template_env.get_template(settings.template)
result = template.render(context)

# Save
with open(settings.output_filename, "w") as fh:
    print "Saving file to {}".format(settings.output_filename)
    fh.write(result)