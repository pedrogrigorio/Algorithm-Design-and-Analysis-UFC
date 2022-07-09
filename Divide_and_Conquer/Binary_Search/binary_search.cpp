#include <iostream>

//Function returns the index of the number searched for in a sorted array.

int binarySearch(int* v, int i, int k, int target){

    int j = (i + k)/2;

    if(i > k)
        return -1;
    else if(v[j] == target)
        return j;
    else if(target > v[j]){
        int index = binarySearch(v, j+1, k, target);
        return index;
    }
    else{
        int index = binarySearch(v, i, j-1, target);
        return index;
    }
}

int main(){

    int n = 0;
    int vector[n];
    std::cout << "Size of array: ";
    std::cin >> n;

    std::cout << "Enter elements: ";
    for(int i = 0; i < n; i++)
        std::cin >> vector[i];

    int target = 0;
    std::cout << "Number searched for: ";
    std::cin >> target;

    int index = binarySearch(vector, 0, n-1, target);
    std::cout << "Number index: " << index;
}