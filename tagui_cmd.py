import rpa as r

r.init(visual_automation = True, chrome_browser = False)
r.keyboard('[win]r')
r.keyboard('[enter]')
r.type('ipconfig')
