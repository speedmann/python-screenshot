from selenium import webdriver
import time
import imageio, os
from datetime import datetime


loop = 0 # Loop indefinetly, Change to another int value to set number of loops (e.g. 1 only loops once)
duration = 1.0 # Have every frame displayed for 1 second
path = './' # where to store the images e.g. /var/www




options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size=1200x600')
options.add_argument('window-size=800x600')
driver = webdriver.Chrome(chrome_options=options)





def make_shot():
  driver.get('http://cryptomaps.org/') # whatever reachable url
  minute_start = datetime.now().strftime('%H')  
  minute_now = datetime.now().strftime('%H')  
  now = datetime.now().strftime('%Y-%m-%d-%H')
  #out='movie' + now + '.gif'
  out=path + 'movie' + now + '.gif'
  try:
    os.symlink(out, path + 'current.gif')
  except OSError:
    os.unlink(path + 'current.gif')
    os.symlink(out, path + 'current.gif')
    
  with imageio.get_writer(out, mode='I', subrectangles=True, duration=duration, loop=loop) as writer:
    while minute_now == minute_start:
      print(minute_now)
      minute_now = datetime.now().strftime('%H')
      driver.implicitly_wait(20)
      driver.save_screenshot('screen.png') 
      image = imageio.imread('screen.png')
      writer.append_data(image)
      driver.refresh()
      time.sleep(60)
      print('sleep 60 secods')


while True:
  make_shot()
  print('change min')

driver.quit()

print "png file created"
