import rpa as r

r.init(visual_automation = True)
r.keyboard('[win][r][enter]')
r.url('http://192.168.0.1/webpages/login.html?t=1578536041034')
r.type('password.png', 'ppassword[enter]')
