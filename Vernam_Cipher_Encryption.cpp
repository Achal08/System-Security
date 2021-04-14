//Encryption 
#include<bits/stdc++.h>
using namespace std;
void enc();
void enc(string m,string key){
	int i;
	string ans="";
    for(i=0;i<m.size();i++){
        ans += (key[i]-'A'+m[i]-'A')%26+'A';
    }
    cout<<"Encrypted message: "<<ans<<'\n';

}  

int main(){
    int t,n,i,j,k,sum=0;
    string m,cipher;
    cout<<"Enter the message"<<'\n';
    cin>>m;
    string key;
    cout<<"Enter the key"<<'\n';
    cin>>key;
    int mod = key.size();
    j=0;
    for(i=key.size();i<m.size();i++){
        key+=key[j%mod];
        j++;
        
    }
	enc(m,key);
    return 0;
}

/*
//Decryption
#include<bits/stdc++.h>
using namespace std;
void dec();
void dec(string m,string key){
	int i;
	string ans1="";
    for(i=0;i<m.size();i++){
        ans1 += (m[i]-key[i]+26)%26+'A';
    }
    cout<<"Decrypted message: "<<ans1<<'\n';
}
int main(){
    int t,n,i,j,k,sum=0;
    string m,cipher;
    cout<<"Enter the message"<<'\n';
    cin>>m;
    string key;
    cout<<"Enter the key"<<'\n';
    cin>>key;
    int mod = key.size();
    j=0;
    for(i=key.size();i<m.size();i++){
        key+=key[j%mod];
        j++;
        
    }
	dec(m,key);
    return 0;
}
*/
