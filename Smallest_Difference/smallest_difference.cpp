#include <iostream>

// Function return the smallest difference in an array of integers sorted in non-decreasing order

int smallestDifference(int* v, int i, int k){
    if(k-i == 1)
        return v[k]-v[i];
    else{

        //Divide
        int j = (i+k)/2;

        //Conquer
        int l = smallestDifference(v, i, j);
        int m = smallestDifference(v, j, j+1);
        int r = smallestDifference(v, j+1, k);

        //Combine
        if(l <= m and l <= r)
            return l;
        else if(m <= l and m <= r)
            return m;
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

    int dif = smallestDifference(vector, 0, n-1);
    std::cout << "The smallest difference is: " << dif;
}