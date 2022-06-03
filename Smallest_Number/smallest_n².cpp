#include <iostream>

//Function returns the smallest number in the vector with complexity n^2

int smallest(int* v, int n){
    if(n == 1){
        return v[0];
    }
    else{
        int m = smallest(v, n-1);
        if(m < v[n-1])
            return m;
        else
            return v[n-1];
    }
}

int main(){
 
    int n = 0;
    std::cin >> n;
    int vector[n];

    for(int i = 0; i < n; i++)
        std::cin >> vector[i];

    int m = smallest(vector, n);
    std::cout << m;
}