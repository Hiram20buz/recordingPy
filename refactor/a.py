import commonSteps

duration = 10 
fps = 5 

commonSteps.createDir()
commonSteps.captureSS((duration * fps), (1 / fps), fps)
commonSteps.gifToMp4("screenshots/temp.gif", "screenshots/output_video.mp4")
'''
commonSteps.createDir()
commonSteps.captureSS((duration * fps), 0.01, fps)
commonSteps.gifToMp4("screenshots/temp.gif", "screenshots/output_video.mp4")
'''

'''
commonSteps.createDir()
commonSteps.captureSS(100, 0.01, fps)
commonSteps.gifToMp4("screenshots/temp.gif", "screenshots/output_video.mp4")
'''