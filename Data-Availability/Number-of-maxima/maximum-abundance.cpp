////////// HEADER //////////////////// HEADER //////////////////// HEADER //////////////////// HEADER //////////////////// HEADER //////////////////// HEADER //////////


//	05/07/2022

//	Diego Cavalcante Cirne
//	0000-0003-0315-8690
//	diego.cirne@ufpe.br

//	Federal University of Pernambuco
//	Physics Department
//	Evolutionary Dynamics Lab


////////// LIBRARIES //////////////////// LIBRARIES //////////////////// LIBRARIES //////////////////// LIBRARIES //////////////////// LIBRARIES //////////////////// LIBRARIES //////////


using namespace std;

#include<iostream>
#include<math.h>
#include<gsl/gsl_randist.h>


gsl_rng *generator_landscape;


////////// STRUCTURES //////////////////// STRUCTURES //////////////////// STRUCTURES //////////////////// STRUCTURES //////////////////// STRUCTURES //////////////////// STRUCTURES //////////


struct genotype{
	int N;			// genotype length					(L)
	int **bin_coe;		// binary strings/genomes
	int **nei_seq;		// neighboring sequences
};

struct phenotype{
	int N;			// number of traits					(n)
	double mut_sig;		// mutation effect magnitude				(sigma)
	double *opt_loc;	// global optimum phenotype/location
	double *anc_seq;	// ancestral sequence phenotype
	double **uni_mut;	// point mutations phenotype effect
};

struct topography{
	int max_num;		// number of local maxima
	int *loc_max;		// local maxima
	int **fit_nei;		// fitter neighborhood
	double *seq_fit;	// sequence fitnesses
};

struct sampling{
	int lan_N;		// number of landscapes
	int seed;		// random generator seed
};


////////// PROTOTYPES //////////////////// PROTOTYPES //////////////////// PROTOTYPES //////////////////// PROTOTYPES //////////////////// PROTOTYPES //////////////////// PROTOTYPES //////////


int P(int i);
void binary_coefficients(struct genotype *gen);
void neighborhood_sequences(struct genotype *gen);
void unitary_mutations(struct genotype *gen, struct phenotype *phe);
void landscape(struct genotype *gen, struct phenotype *phe, struct topography *top);
void fitter_neighborhood(struct genotype *gen, struct topography *top);
void local_maxima(struct genotype *gen, struct topography *top);


////////// INT MAIN //////////////////// INT MAIN //////////////////// INT MAIN //////////////////// INT MAIN //////////////////// INT MAIN //////////////////// INT MAIN //////////


int main()
{

	genotype gen;
	phenotype phe;
	topography top;
	sampling sam;


	//*** INPUT ***//
  	cout << endl;
	cout << "n:" << '\t';
  	cin >> phe.N;
	cout << "L:" << '\t';
  	cin >> gen.N;
  	cout << endl;
	cout << "number of landscapes:" << '\t';
  	cin >> sam.lan_N;
  	cout << endl;


	phe.mut_sig = 0.05;
	sam.seed = 0;


	FILE * file = fopen("data.dat", "w");


	generator_landscape = gsl_rng_alloc(gsl_rng_mt19937);
	gsl_rng_set(generator_landscape, sam.seed);			// setup of landscape random generator


	gen.bin_coe = new int*[P(gen.N)];
	for(int i=0; i<P(gen.N); i++)
		gen.bin_coe[i] = new int[gen.N];
	gen.nei_seq = new int*[P(gen.N)];
	for(int i=0; i<P(gen.N); i++)
		gen.nei_seq[i] = new int[gen.N];

	phe.anc_seq = new double[phe.N];
	phe.uni_mut = new double*[gen.N];
	for(int i=0; i<gen.N; i++)
		phe.uni_mut[i] = new double[phe.N];

	top.loc_max = new int[P(gen.N)];
	top.fit_nei = new int*[P(gen.N)];
	for(int i=0; i<P(gen.N); i++)
		top.fit_nei[i] = new int[gen.N];
	top.seq_fit = new double[P(gen.N)];


	binary_coefficients(&gen);
	neighborhood_sequences(&gen);


	for(int i=0; i<phe.N; i++)					// setup of global optimum phenotype at origin
		phe.opt_loc[i] = 0;


	for(int i=0; i<phe.N; i++)					// setup of ancestral phenotype at origin
		phe.anc_seq[i] = 0;


	for(int i=0; i<sam.lan_N; i++)					// landscape generation loop
	{
		unitary_mutations(&gen, &phe);
		landscape(&gen, &phe, &top);
		fitter_neighborhood(&gen, &top);
		local_maxima(&gen, &top);


		fprintf(file, "%d\n", top.max_num);
	}

	delete[] top.seq_fit;
	for(int i=0; i<P(gen.N); i++)
		delete[] top.fit_nei[i];
	delete[] top.fit_nei;
	delete[] top.loc_max;

	for(int i=0; i<gen.N; i++)
		delete[] phe.uni_mut[i];
	delete[] phe.uni_mut;
	delete[] phe.anc_seq;

	for(int i=0; i<P(gen.N); i++)
		delete[] gen.nei_seq[i];
	delete[] gen.nei_seq;
	for(int i=0; i<P(gen.N); i++)
		delete[] gen.bin_coe[i];
	delete[] gen.bin_coe;


	fclose(file);
}


////////// FUNCTIONS //////////////////// FUNCTIONS //////////////////// FUNCTIONS //////////////////// FUNCTIONS //////////////////// FUNCTIONS //////////////////// FUNCTIONS //////////


int P(int i)
{ 
	return pow(2,i);
}


void binary_coefficients(genotype *gen)
{
	for(int i=0; i<P(gen->N); i++)
	{
		int a = i;

		for(int j=0; j<gen->N; j++)
		{
			gen->bin_coe[i][j] = a%2;
			a /= 2;
		}
	}
}


void neighborhood_sequences(genotype *gen)
{
	for(int i=0; i<P(gen->N); i++)
		for(int j=0; j<gen->N; j++)
			gen->nei_seq[i][j] = i + (!gen->bin_coe[i][j] - gen->bin_coe[i][j])*P(j);
}


void unitary_mutations(genotype *gen, phenotype *phe)
{
	for(int i=0; i<gen->N; i++)
		for(int j=0; j<phe->N; j++)
			phe->uni_mut[i][j] = gsl_ran_gaussian(generator_landscape, phe->mut_sig);
}


void landscape(genotype *gen, phenotype *phe, topography *top)
{
	for(int i=0; i<P(gen->N); i++)
	{
		double a = 0;

		for(int j=0; j<phe->N; j++)
		{
			double b = phe->anc_seq[j];
	
			for(int k=0; k<gen->N; k++)
				b += gen->bin_coe[i][k]*phe->uni_mut[k][j];
	
			b -= phe->opt_loc[j];

			a += pow(b, 2);
		}

		top->seq_fit[i] = exp((-1)*a);
	}
}


void fitter_neighborhood(genotype *gen, topography *top)
{
	for(int i=0; i<P(gen->N); i++)
		for(int j=0; j<gen->N; j++)
			if(top->seq_fit[gen->nei_seq[i][j]] < top->seq_fit[i])
				top->fit_nei[i][j] = 0;
			else
				top->fit_nei[i][j] = 1;
}


void local_maxima(genotype *gen, topography *top)
{
	top->max_num = 0;

	for(int i=0; i<P(gen->N); i++)
		top->loc_max[i] = 0;

	for(int i=0; i<P(gen->N); i++)
	{
		int j = 0;
		int W = 1;
		while(W and j<gen->N)
		{
			if(top->fit_nei[i][j])
				W--;
			j++;
		}

		if(W)
		{
			top->max_num++;
			top->loc_max[i]++;
		}
	}
}


////////// BOTTOM //////////////////// BOTTOM //////////////////// BOTTOM //////////////////// BOTTOM //////////////////// BOTTOM //////////////////// BOTTOM //////////
