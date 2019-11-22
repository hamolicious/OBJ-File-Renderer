# Welcome to my object file renderer, please change these settings as you wish, then run the main.py file
# Enjoy :p

# path to model accepts .OBJ or .TXT files
model_path = '/media/code-black/Kali Live/Python/pygame/MyProjects/Finnished/3D Model Renderer/TestModels/teapot.txt'

# offset model from origin (top left corner)
offsetX = 350
offsetY = 350

# zoom in on the model
zoom = 3

# light location, set all to -1 if no lighting should be simulated or set all to 0 to use mouse pos
lightX = 7000
lightY = 7000
lightZ = 7000

# spin speed
spin_speed = 0.01

# choose how to render the model
# 0 - vertex mode (medium)
# 1 - edge mode (fastest)
# 2 - face mode (slowest)
render_mode = 2
