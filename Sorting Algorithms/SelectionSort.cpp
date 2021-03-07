/*

Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire list.

The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.

This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where n is the number of items.

*/

//find the minimum element every time and swap it


#include<stdio.h>
#include<iostream>
#include<conio.h>

using namespace std;

void selectionsort(int arr[],int n){
    for(int i=0;i<n-1;i++)
        {
        int min_index=i;
        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[min_index])
            {
                min_index=j;
            }
        }
        swap(arr[i],arr[min_index]);
    }

}

int main(){
    int n;
    cout<<"Enter Number of Elements: ";
    cin>>n;
    int nums[n];
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }
    selectionsort(nums,n);
    cout<<"Sorted Array is ";
    for(int i=0;i<n;i++){
        cout<<nums[i]<<' ';
    }
}
