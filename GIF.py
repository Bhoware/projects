import imageio.v2 as imageio # type: ignore

filename = ['C:/Users/DELL/Desktop/team-pic1.png','C:/Users/DELL/Desktop/team-pic2.png']
images = []
for name in filename:
    images.append(imageio.imread(name))


imageio.mimsave(r"d:\Anshul\college program\Python\projects\output.gif", images, duration=1000, loop=0)