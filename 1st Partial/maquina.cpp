#include <iostream>

using namespace std;
int int main(int argc, char const *argv[]) {
    string alfabeto,cadena,cadena2 ;
    cin>>alfabeto;
    cin>>cadena;
    cin>>cadena2;

    int size=cadena.length();
    int size1=cadena1.length();
    int diferencia=size1-size +1;
    boolean flag=true;
    int count=0;
    for (int i = 0; i < diferencia; i++) {
        for (int j = 0; j < size; j++) {

            flag=cadena1[j+i]==cadena[j];
            if(flag==false){
                count--;
                break;
            }
        }
        count++;
    }
    return 0;
}
