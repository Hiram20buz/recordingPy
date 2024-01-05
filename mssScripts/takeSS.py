import mss

output_filename = 'screenshot.png'

with mss.mss() as mss_instance:
    mss_instance.shot(output=output_filename)
