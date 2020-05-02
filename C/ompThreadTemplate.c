#include <stdio.h>
#include <omp.h>

//Number of threads, although this can be changed later.
#define NUM_OF_THREADS 15

/**
 * Code in c to set an example on how to use a very simple implementation of parallel programming in C
 * Using the omp library
 * 
 * Reference:
 * https://platzi.com/tutoriales/1469-algoritmos/2010-paraleliza-tu-codigo-en-c-con-openmp/
 * 
 * Must be compiled as follows:
 * gcc program.c -o result -fopenmp
 */

int main(int argc, char const *argv[]){
    
    //Set the number of threads to a certain amount
    omp_set_num_threads(NUM_OF_THREADS);

    #pragma omp parallel
    {
        //In here you must put the code that each individual thread will execute.
        int id = omp_get_thread_num();
        printf("Hello from thread num %d\n",id);
    }
    return 0;
}
