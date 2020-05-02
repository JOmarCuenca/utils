#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_THREADS 9

/**
 * Using the example as sudoku_test.txt
 * This code is a way to check with pthreads (multithreading),
 * If the sudoku solution proposed is valid or not.
 */

//Array where the information of the sudoku will be saved.
char sudoku[9][9];

//Array where the threads will save their results in order to tell the others if their section is valid.
char results [9];

//Function to print the values of the sudoku
char prettyPrint(){
    for(int i = 0;i<9;i++){
        for(int j = 0;j<9;j++){
            printf("%d ",sudoku[i][j]);
        }
        printf("\n");
    }
    return 0;
}

//Function that checks if the Row according to the id of the thread is valid, the sum of the numbers is 45.
char checkRow(int id){
    char sum = 0;
    for(char i=0;i<9;i++){
        sum += sudoku[id][i];
    }
    if(sum == 45){
        return 0;
    }
    return 1;
}

//Function that checks if the Column according to the id of the thread is valid, the sum of the numbers is 45.
char checkColumn(int id){
    char sum = 0;
    for(char i=0;i<9;i++){
        sum += sudoku[i][id];
    }
    if(sum == 45){
        return 0;
    }
    return 1;
}

//Function that checks if the Square according to the id of the thread is valid, the sum of the numbers is 45.
char checkSquare(int id){
    char sum = 0;
    char rows[3],columns[3];

    switch (id){//delimitar renglones
    case 0:case 1:case 2:
        rows[0] = 0;
        rows[1] = 1;
        rows[2] = 2;
        break;
    case 3:case 4:case 5:
        rows[0] = 3;
        rows[1] = 4;
        rows[2] = 5;
        break;
    default:
        rows[0] = 6;
        rows[1] = 7;
        rows[2] = 8;
        break;
    }

    switch (id){//delimitar columnas;
    case 0:case 3:case 6:
        columns[0] = 0;
        columns[1] = 1;
        columns[2] = 2;
        break;
    case 1:case 4:case 7:
        columns[0] = 3;
        columns[1] = 4;
        columns[2] = 5;
        break;
    default:
        columns[0] = 6;
        columns[1] = 7;
        columns[2] = 8;
        break;
    }


    for(char i=0;i<3;i++){//iterar sobre los renglones
        char row = rows[i];
        for(char j = 0;j<3;j++){//iterar sobre las columnas
            char column = columns[j];
            sum += sudoku[row][column];
        }
    }
    if(sum == 45){
        return 0;
    }
    return 1;
}

//Controller of the threads, gives the orders to each individual thread to check their own spaces
void *checkThread(void *threadid){
    int id = (long)threadid;
    char result = 0;

    result = checkRow(id);
    if(result){
        //levantar bandera de frenado
        results[id] = 1;
        // return ;
    }
    result = checkColumn(id);
    if(result){
        //levantar bandera de frenado
        results[id] = 1;
        // return ;
    }
    result = checkSquare(id);
    if(result){
        //levantar bandera de frenado
        results[id] = 1;
        // return ;
    }
}

//Function that gets the file and reads the information and saves it in the Array.
char getFile(const char* const fileName){
    FILE* file = fopen(fileName, "r");
    char line[32];
    short x = 0, y = 0;
    while (fgets(line, sizeof(line), file)) {
        for(int i = 0;i<17;i++){
            char temp = line[i];
            if(temp != ' '){
                int valor = atoi(&temp);
                sudoku[x][y] = valor;
                y++;
            }
        }
        x++;
        y = 0;
    }
    fclose(file);
    return 0;
}

int main(int argc, char const *argv[]){
    //Gets the file name
    if(argc<2){
        printf("Not enough arguments");
        return 1;
    }
    
    getFile(argv[1]);//obtener la informacion
    prettyPrint();//imprimir el documento
    //Checar si el sudoku es valido
    pthread_t threads[NUM_THREADS];//Create the threads space
    int rc;
    long t;
    //Create the threads and give orders.
    for(t=0; t<NUM_THREADS; t++){
       rc = pthread_create(&threads[t], NULL, checkThread, (void *)t);
       if (rc){
          printf("ERROR; return code from pthread_create() is %d\n", rc);
       }
    }

    //Wait for all the threads to finish
    for(t=0; t<NUM_THREADS; t++){
       pthread_join(threads[t],NULL);
    }
    //Check the resultss
    for(char i = 0;i<9;i++){
        if(results[i]==1){
            printf("The sudoku doesn't have a valid solution\n");
            return 1;
        }
    }
    printf("The sudoku has a valid solution\n");
    return 0;
}