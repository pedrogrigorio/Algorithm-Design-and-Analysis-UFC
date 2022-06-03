#include <iostream>
//Retorna o menor valor do vetor [Funciona] - Otimizado

int smallest(int* v, int i, int k){

    if(i == k)
        return v[i];
    else{

        //Divide
        int j = (i+k)/2;

        //Conquer
        
        int num1 = smallest(v, i, j);
        int num2 = smallest(v, j+1, k);

        //Combine
        if(num1 < num2){
            return num1;
        }
        else{
            return num2;
        }
    }
}

int main(){

    int n = 0;
    std::cin >> n;
    int vector[n];

    for(int i = 0; i < n; i++)
        std::cin >> vector[i];

    int m = smallest(vector, 0, n-1);
    std::cout << m;
}
