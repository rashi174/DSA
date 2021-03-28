#include<iostream>
using namespace std;
int partition(int arr[],int l,int r);
void swapp(int arr[],int l,int r);

void QuickSort(int arr[], int l, int r){
    if (l<r){
        int pi=partition(arr,l,r);
        QuickSort(arr,l,pi-1);
        QuickSort(arr,pi+1,r);
    }
}

int partition(int arr[],int l,int r){
    int pivot=arr[r];  // Taking Last element is pivot  
    int i=l-1;

    for(int j=l;j<r;j++){
        if (arr[j]<pivot){
            i++;
            swapp(arr,i,j);
        }
    }
    swapp(arr,i+1,r);
    return i+1;
}

void swapp(int arr[],int i ,int j){
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}

int main(){
    int arr[5]={5,3,8,2,7};
    int size=5;
    cout<<"Before Sorting"<<endl;
    for(int x=0;x<5;x++) cout<<arr[x]<<" ";
    cout<<endl;
    cout<<"After Sorting"<<endl;
    QuickSort(arr,0,size-1);
    for(int x=0;x<5;x++) cout<<arr[x]<<" ";
    return 0;
}