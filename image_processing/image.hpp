#ifndef image_hpp
#define image_hpp
#include <iostream>
#include <string>

#include <boost/multi_array.hpp>
#include <jpeglib.h>
using namespace std;

#include "hw6.hpp"

class image 
{

    string input_file;
    unsigned int m, n;
    boost::multi_array<unsigned char, 2> img;

   public:

    image(string input_file);
    
    void Convolution(
    	boost::multi_array<unsigned char, 2>& input,
    	boost::multi_array<unsigned char, 2>& output,
    	boost::multi_array<float, 2>& kernel);
    void BoxBlur(
    	unsigned int kernel_size);
    unsigned int Sharpness(
    	void);
    void Save(
    	string output_file);
};

#endif /* image_hpp */
