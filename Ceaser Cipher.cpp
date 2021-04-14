#include <iostream>
#include<string>
using namespace std;

void encrypt(int key,string s){
    int i,j,k;
    string t;
    for(i=0;i<s.size();i++){
        t+=(s[i]-'A'+key)%26+'A';
    }
    cout<<"\nEncrypted message is "<<t<<'\n';
    
}

void decrypt(int key,string s){
    int i,j,k;
    string t;
    for(i=0;i<s.size();i++){
        t+=(s[i]-'A'-key+26)%26+'A';
    }
    cout<<"\nDecrypted message is "<<t<<'\n';
    
}

int main(){
    int n,key;
    cout<<"\nEnter the choice\n1 Encrypt \n2 Decrypt"<<endl;
   	cin>>n;
    string s,t;
    cout<<"Enter the key\n";
    cin>>key;
    cout<<"Enter the message to Encrypt/Decrypt\n";
    cin>>s;
    if(n==1){
        encrypt(key,s);
    }
    else{
        decrypt(key,s);
    }
    return 0;
}
