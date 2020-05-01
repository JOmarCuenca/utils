#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/**
 * This is a c template for the easy implementation of a multithreaded code
 * I made it this way so no one would struggle to find the template for this.
 */

//Max number of defined Threads
#define MAX_THREAD_NUM 80

//Must be compiled as follows:
//gcc file.c -o result.exe -lpthread

void* threadController(void* id){
    long threadId = (long)id;//the threads ID
    //Here you can write whatever you want the thread to do 
    //You can tell the threads what to do according to ID here or in the section below.
    printf("Hello from %ld\n",threadId);
}

int main(int argc, char const *argv[]){

    pthread_t threads[MAX_THREAD_NUM];//The thread object where the thread will live.
    for(long i = 0;i<MAX_THREAD_NUM;i++){
        //thread method to create the thread.
        //first you give the thread Object Pointer,
        //Then you give its special atributes,
        //Then the pointer to the function that this thread will execute.
        //Then you give the parameters to the function you sent.
        pthread_create(&threads[i],NULL,threadController,(void *)i);
    }

    //for cycle to tell the main thread to wait for all its subThreads to finish.
    for(long i = 0;i<MAX_THREAD_NUM;i++){
        pthread_join(threads[i],NULL);
    }

    return 0;
}