#include <cmath>
#include <vector>

#include "matvecops.hpp"

std::vector<double> addVecsWithCoef(
	const std::vector<double> &vec1, 
	const std::vector<double> &vec2,
	double coef
	) 
{	
	std::vector<double> vec;
	for (unsigned int i = 0; i<vec1.size(); i++) {
		double value = vec1.at(i) + coef * vec2.at(i);
		vec.push_back(value);
	}
	return vec;
}

double dotPrd(
	const std::vector<double> &vec1, 
	const std::vector<double> &vec2)
{
	double sum = 0;

	for (unsigned int i = 0; i<vec1.size(); i++) 
	{
		double value = vec1.at(i) * vec2.at(i);
		sum += value;
	}

	return sum;
}

double L2Norm (
	const std::vector<double> &vec)
{
	return sqrt(dotPrd(vec, vec));
}

std::vector<double> multiplyVecByScalar(
	std::vector<double> &vec1, 
	double scalar)
{
	std::vector<double> vec;

	for (unsigned int i = 0; i<vec1.size(); i++) 
	{
		vec.at(i) = vec.at(i) * scalar;
	}
	return vec;
}

std::vector<double> matVecPrd(
	std::vector<double> &val,
	std::vector<int> &row_ptr,
	std::vector<int> &col_idx,
	std::vector<double> &vec)
{
	std::vector<double> result;
	std::size_t dim = row_ptr.size() - 1;

	// Iterate through the rows
	for (unsigned int i=0; i<dim; ++i) 
	{
 		double w = 0;

 		// Compute the partial sum of A[i] * x
 		for (int j=int(row_ptr[i]); j<int(row_ptr[i+1]); ++j) 
 		{
  			w += val[j] * vec[col_idx[j]];
  		}
  		result.push_back(w);
  	}
  	return result;
}
