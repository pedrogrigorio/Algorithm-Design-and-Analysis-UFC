#include <iostream>

//Function returns the index of the greatest number in the array

int greatest(int* v, int i, int k){

    if(i == k)
        return i;
    else{
        //Dividir
        int j = (i+k)/2;

        //Conquer
        int l = greatest(v, i, j);
        int r = greatest(v, i+1, k);

        //Combine
        if(v[l] > v[r])
            return l;
        else
            return r;
    }
}

int main(){

    int n = 0;
    std::cout << "Size of array: ";
    std::cin >> n;
    int vector[n];

    std::cout << "Enter elements: ";
    for(int i = 0; i < n; i++)
        std::cin >> vector[i];

    int gr = greatest(vector, 0, n-1);
    std::cout << "The index of the greatest number is: " << gr;
}