# Output the image files as PNGs


import PIL.Image as pil
import Question2 as out



def outImages(type):
    if(type == 'test'):
        for i in range(len(out.Question1.test_images)):
            myimage = pil.fromarray(out.np.array(out.Question1.test_images[i]))
            mylabel = out.readDataFile.test_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'test_images/test-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)
    if(type == 'train'):
        for i in range(len(out.Question1.train_images)):
            myimage = pil.fromarray(out.np.array(out.Question1.train_images[i]))
            mylabel = out.Question1.train_labels[i]
            # convert image
            myimage = myimage.convert('RGB')
            # save image
            imagename = 'train_images/train-'+str(i)+'-'+str(mylabel)+'.png'
            myimage.save(imagename)

outImages('test')
outImages('train')