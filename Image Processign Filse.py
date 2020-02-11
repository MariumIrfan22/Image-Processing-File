#!/usr/bin/env python
# coding: utf-8

# # Image Processing Files

# In[1]:


import PIL.Image
im=PIL.Image.open('img.jpg')
print(im.show())


# In[2]:


print(im.size)


# In[3]:


print(im.format)


# In[4]:


print(im.mode)


# In[5]:


copied=im.copy()
copied.show()


# In[6]:


rotation=im.rotate(360)
rotation.show()


# In[ ]:


box=(100,100,400,400)
cropped=im.crop(box)
cropped.show()


# In[18]:


import PIL.Image
import PIL.ImageFilter
im=PIL.Image.open('img.jpg')
smoothed=im.filter(PIL.ImageFilter.SMOOTH)
smoothed.paste(cropped,(300,300,600,600))
smoothed.show()


# In[19]:


im2=PIL.Image.new('RGB',(400,400))
im2.paste(cropped,(box))
im2.save('new.jpg')
im2.show()


# In[24]:


import PIL.Image
import PIL.ImageFilter
im=PIL.Image.open('img.jpg')
w,h=im.size
res=PIL.Image.new(im.mode,(2*w,2*h))
res.paste(im,(0,0,w,h))
contour=im.filter(PIL.ImageFilter.CONTOUR)
res.paste(contour,(w,0,2*w,h))
emboss=im.filter(PIL.ImageFilter.EMBOSS)
res.paste(emboss,(0,h,w,2*h))
edges=im.filter(PIL.ImageFilter.FIND_EDGES)
res.paste(edges,(w,h,2*w,2*h))
res.show()


# In[23]:


def warhol(pic):
    photo=PIL.Image.open(pic)
    width, height = photo.size    
    res = PIL.Image.new(photo.mode, (2*width, 2*height))
    res.paste(photo, (0, 0, width, height))
    contour = photo.filter(PIL.ImageFilter.CONTOUR)
    res.paste(contour, (width, 0, 2*width, height))
    emboss = photo.filter(PIL.ImageFilter.EMBOSS)
    res.paste(emboss, (0, height, width, 2*height))
    edges = photo.filter(PIL.ImageFilter.FIND_EDGES)
    res.paste(edges, (width, height, 2*width, 2*height))
    return res
warhol('img.jpg')


# In[26]:


photo=PIL.Image.open('img.jpg')
width, height = photo.size    
res = PIL.Image.new(photo.mode, (2*width, 2*height))
res.paste(photo, (0, 0, width, height))
contour = photo.filter(PIL.ImageFilter.CONTOUR)
res.paste(contour, (width, 0, 2*width, height))
emboss = photo.filter(PIL.ImageFilter.EMBOSS)
res.paste(emboss, (0, height, width, 2*height))
edges = photo.filter(PIL.ImageFilter.FIND_EDGES)
res.paste(edges, (width, height, 2*width, 2*height))
res.show()
res.save('edit.jpg')


# In[27]:


im=PIL.Image.open('img.jpg')
print(f'the size of the picture is:{im.size}')
print(f'the format of the picture is: {im.format}')
print(f'the mode of the picture is: {im.mode}')


# In[30]:


def resize(x,y):
    photo=PIL.Image.open('img.jpg')
    img=photo.resize((x,y))
    print(img.show())
    print(img.size)

resize(600,600)


# In[33]:


import PIL.Image
def convert(file):
    im=PIL.Image.open(file)
    cropped=im.crop((200,200,500,500))
    cropped.show()
    cropped.save('crop.gif')
convert('img.jpg')


# In[41]:


import PIL.Image
im=PIL.Image.open('spir.gif')
cropped=im.crop((150,150,300,300))
cropped.show()
cropped.save('cs.22.png')


# In[42]:


import PIL.Image
im=PIL.Image.open('cs.22.png')
#im.show()
im2=PIL.Image.open('cycle.jpg')
im2.paste(im,(150,150,300,300))
im2.show()
im2.save('cs.23.jpg')


# In[ ]:




