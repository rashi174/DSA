//https://www.youtube.com/watch?v=P89Y3v-6Its

printf("Mastering C++ pointers!!");

int x=1;

//Adress remains same even after changing the value
printf("Adress of x is %p\n",&x);
x=10;
printf("Adress of x is %p\n",&x);
x=100;
printf("Adress of x is %p\n",&x);
cout<<x;

int *ptr=(int*)0x7f957f2ca038;

printf("My first pointer is = %p\n",ptr);
printf("Values pointed by pointer is = %d\n",*ptr);

*ptr=-100;
printf("ptr now points to = %p\n",ptr);
printf("Value pointed by pointer is = %d\n",*ptr);
printf("Values of variable x is = %d\n",x);

int *ptr2=&x;
char *name= "Rashi";
printf("Size of pointer to an integer is = %lu\n",sizeof(ptr2));
printf("Size of pointer to an character array is = %lu\n",sizeof(name));

//why do we need to define the type of pointer

printf("Content of ptr is %p\n",ptr);   //integer increments by 4
printf("Content of ptr+1 is %p\n",ptr+1);
printf("Content of ptr+2 is %p\n",ptr+2);

printf("-------------------------------------\n");

printf("Content of name is %p\n",name);   //character increments by 1
printf("Content of name+1 is %p\n",name+1);
printf("Content of name+2 is %p\n",name+2);

int arr[3]={10,33,78}; //arr actually becames a pointer

printf("Content of arr %p , val = %d \n",arr,*arr);
printf("Content of arr+1 %p , val = %d\n",arr+1,*(arr+1));
printf("Content of arr+2 %p , val = %d\n",arr+2,*(arr+2)); // *(arr+2)==> arr[2] 


//equality operator in pointers

int *other=arr;  // O(1) space

printf("Content of other %p , val = %d \n",other,*other);
printf("Content of other+1 %p , val = %d\n",other+1,*(other+1));
printf("Content of other+2 %p , val = %d\n",other+2,*(other+2));


struct Real{
    int real,imag;
    void out() { printf("(%d + %di)\n",real,imag); }
};

Real nums={1,1};
nums.out();

Real *p=&nums;
p->out();

printf("Real = %d\n",p->real);
printf("Imaginary = %d\n",p->imag);

Real num2=*p;
num2.real=13;
num2.out();
p->out();

p->real=13;
p->out();

//Null pointers in CPP

np=nullptr;
printf("ptr = %p\n",np);

Real newNumber=*np;  #can't derefrence a NULL pointer

/*

&  -- Adress
*  -- Derefrence
-> -- direct copy of object to which pointer is pointing to

*/


