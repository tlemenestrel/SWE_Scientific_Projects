# Image Processing

Image processing is an important category of computations utilized in many science and engineering fields. Some important computations in image processing include focus detection and various filtering operations to smooth or sharpen an image, detect edges, etc.

The goal of this project is to developp a C++ image class that can read and write JPEG files, and has methods to compute the sharpness of the image and smooth the image using a box blur kernel of a specified size.

![Boxblur](https://github.com/tlemenestrel/swe_scientific_projects/blob/master/image_processing/boxblur.png)

## Code description

My code first implements an image class with a constructor that accepts a string
containing the name of the JPEG file to be read. The constructor reads the file 
and stores the image data as a data attribute. It calls a function called
ReadGrayscaleJPEG(), which is pre-defined.

The class also has a Save() method that writes the current version of the image 
to a JPEG file. It takes a string containing the name of the JPEG file to be 
written. However, if the string is empty the original filename is used instead.

Afterwards, the class has a Convolution() method. It has specific requirements
for both the kernel and the input and output. First, the input and output should
 be of the same size. Second, the method only supports square kernels of odd 
 sizes and at least size 3. 

Then, it has a BoxBlur() method that takes an argument specifying the kernel 
size and calls the Convolution() methd to smooth the image. 

Also, it uses a Sharpness() method that returns the sharpness of the image. 

Finally, the main file loads the image stanford.jpg and computes and outputs 
the sharpness for kernel sizes of 3, 7, . . . , 23, 27 and then compute and 
output the sharpness of the resulting images.

![matrix](https://github.com/tlemenestrel/swe_scientific_projects/blob/master/image_processing/matrix.png)
