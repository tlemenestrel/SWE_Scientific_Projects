#ifndef matvecops
#define matvecops

#include <vector>

std::vector<double> addVecsWithCoef(
	const std::vector<double> &vec1, 
	const std::vector<double> &vec2,
	double coef
	);

double L2Norm(
	const std::vector<double> &vec);

double dotPrd(
	const std::vector<double> &vec1, 
	const std::vector<double> &vec2);

std::vector<double> multiplyVecByScalar(
	std::vector<double> &vec, 
	double scalar);

std::vector<double> matVecPrd(
	std::vector<double> &val,
	std::vector<int> &row_idx,
	std::vector<int> &col_idx,
	std::vector<double> &vec);

#endif /* matvecops */
