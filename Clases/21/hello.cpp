#include <iostream>
// This is a comment
using namespace std;
// Variable declaration:
extern int a, b;
// function declaration
int func();
typedef int feet;
// Global variable declaration:
int g;

/* This is a comment multiline
    * 1
    * 2
*/
int main() 
{   //count is the output variable
    // Variable definition:
    int a, b;
    
    // Local variable declaration:
    feet d;
    const int  LENGTH = 10;
    // actual initialization
    a = 10;
    d = 2;
    g = a + 12;
    // function call
    int i = func();
    cout << "Hello, World!" << endl; //prints Hello, World
    return 0;
}   //endl is end line ='\n'

// function definition
int func() {
   return 0;
}


enum color { red, green = 5, blue }; //blue as value 6

int    i, j, k; //in Java is same
char   c, ch;
float  f, salary;
double d;

int d = 3, f = 5; //ahhhhhh sha

int max(int num1, int num2) {
   // local variable declaration
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}
