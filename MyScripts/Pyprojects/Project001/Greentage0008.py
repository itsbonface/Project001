#Keylogging simple introduction

#from pynput import keyboard

def on_press(key):
	try:
		print('Alphabetical key {0} is pressed'.format(key.char))
	except AttributeError:
		print('special key {0} is pressed'.format(key))

def on_release(key):
	print('{0} is released'.format(key))
	if key == keyboard.Key.esc:
		return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()


