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


def find_all_images(folder):
    imgs = []
    for fn in os.listdir(settings.images_folder):
        if os.path.isfile(os.path.join(settings.images_folder, fn)):
            if fn.split('.')[-1] in ['JPG', 'jpg']:
                imgs.append(os.path.join(settings.images_folder, fn))
    return imgs

if __name__ == '__main__':
    image_filenames = find_all_images(settings.images_folder)

    # Build the context to pass on to the Jinja template
    context = {
        'width': settings.screen_size['x'],
        'height': settings.screen_size['y'],
        'delay': settings.delay_between_slides,
        'image_filenames': sorted(image_filenames),
        'show_digital_clock': settings.show_digital_clock,
        'show_clock_seconds': str(settings.show_clock_seconds).lower(),
        'clock_pos_left': settings.clock_pos_left,
        'clock_pos_top': settings.clock_pos_top,
        }

    # Load and render the template.
    template_env = Environment(loader=FileSystemLoader('templates'))
    template = template_env.get_template(settings.template)
    result = template.render(context)

    # Save
    with open(settings.output_filename, "w") as fh:
        print "Saving file to {}".format(settings.output_filename)
        fh.write(result)
