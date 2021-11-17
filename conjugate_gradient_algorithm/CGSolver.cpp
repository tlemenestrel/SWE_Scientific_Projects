#include <iostream>
#include <vector>

#include "CGSolver.hpp"
#include "matvecops.hpp"

int CGSolver(
	std::vector<double> &val,
    std::vector<int>    &row_ptr,
    std::vector<int>    &col_idx,
    std::vector<double> &b,
    std::vector<double> &x,
    double tol)
{
	// Initial values to compute
	std::vector<double> Ax = matVecPrd(val,row_ptr,col_idx,x);
	std::vector<double> r = addVecsWithCoef(b, Ax, -1);
	double L2normr0 = L2Norm(r);
	std::vector<double> p = r;
	std::size_t niter = 0;
	std::size_t nitermax = row_ptr.size() - 1;

	while (niter < nitermax)
	{
		niter++;
		// Compute Ap and r transpose r in advance, which will be reused later
		std::vector<double> Ap = matVecPrd(val, row_ptr, col_idx, p);
		double r_trans_r = dotPrd(r, r);

		double alpha = r_trans_r/dotPrd(p, Ap);

		// Update x and r here
		x = addVecsWithCoef(x, p, alpha);
		r = addVecsWithCoef(r, Ap, -1 * alpha);

		// Compute the 2-norm of r
		double L2normr = L2Norm(r);

		// Exit condition
		if (L2normr / L2normr0 < tol) 
		{
			return int(niter);
		}

		double beta = dotPrd(r,r) / r_trans_r;
		p = addVecsWithCoef(r, p, beta);
	}
	// Else, the algorithm diverges
	return -1;
}
