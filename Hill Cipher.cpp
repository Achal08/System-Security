//Hill Cipher Encryption-Decryption Code 1
/* 
#include<iostream>
#include<math.h>
 
using namespace std;

float encrypt[3][1], decrypt[3][1], a[3][3], b[3][3], mes[3][1], c[3][3];
 
void encryption();	//encrypts the message
void decryption();	//decrypts the message
void getKeyMessage();	//gets key and message from user
void inverse();		//finds inverse of key matrix
 
int main() {
	getKeyMessage();
	encryption();
	decryption();
}
 
void encryption() {
	int i, j, k;
	
	for(i = 0; i < 3; i++)
		for(j = 0; j < 1; j++)
			for(k = 0; k < 3; k++)
				encrypt[i][j] = encrypt[i][j] + a[i][k] * mes[k][j];
	
	cout<<"\nEncrypted string is: ";
	for(i = 0; i < 3; i++)
		cout<<(char)(fmod(encrypt[i][0], 26) + 97);
}
 
void decryption() {
	int i, j, k;
	
	inverse();
	
	for(i = 0; i < 3; i++)
		for(j = 0; j < 1; j++)
			for(k = 0; k < 3; k++)
				decrypt[i][j] = decrypt[i][j] + b[i][k] * encrypt[k][j];
	
	cout<<"\nDecrypted string is: ";
	for(i = 0; i < 3; i++)
		cout<<(char)(fmod(decrypt[i][0], 26) + 97);
	
	cout<<"\n";
}
 
void getKeyMessage() {
	int i, j;
	char msg[3];
 
	cout<<"Enter 3x3 matrix for key (It should be inversible):\n";
	
	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++) {
			cin>>a[i][j];
			c[i][j] = a[i][j];
		}
	
	cout<<"\nEnter a 3 letter string: ";
	cin>>msg;
	
	for(i = 0; i < 3; i++)
		mes[i][0] = msg[i] - 97;
}
 
void inverse() {
	int i, j, k;
	float p, q;
	
	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++) {
			if(i == j)
				b[i][j]=1;
			else
				b[i][j]=0;
		}
		
	for(k = 0; k < 3; k++) {
		for(i = 0; i < 3; i++) {
			p = c[i][k];
			q = c[k][k];
				
			for(j = 0; j < 3; j++) {
				if(i != k) {
					c[i][j] = c[i][j]*q - p*c[k][j];
					b[i][j] = b[i][j]*q - p*b[k][j];
				}
			}
		}
	}
	
	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++)
			b[i][j] = b[i][j] / c[i][i];
	
	cout<<"\n\nInverse Matrix is:\n";
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++)
			cout<<b[i][j]<<" ";
		
		cout<<"\n";
	}
}*/

//Hill Cipher Encryption-Decryption Code 2
/*
#include<iostream>
#include<math.h>
 
using namespace std;
 
int main() {
    string key, message;
    cout<<"Enter the key: "<<endl;
    cin>>key;
    float keymatrix[3][3];
    int k=0;
    for (int i = 0; i < 3; i++)  
    {
        for (int j = 0; j < 3; j++)  
        { 
            keymatrix[i][j] = (key[k]) % 65; 
            k++; 
        } 
    }
    cout<<"Enter the message: "<<endl;
    cin>>message;
    float messageVector[3][1]; 
    for (int i = 0; i < 3; i++) 
        messageVector[i][0] = (message[i]) % 65; 
    float hillcipher[3][1];
    
    for (int i = 0; i < 3; i++)  
    { 
        for (int j = 0; j < 1; j++) 
        {            
             for (int x = 0; x < 3; x++) 
            { 
                hillcipher[i][j] +=  
                keymatrix[i][x] * messageVector[x][j]; 
            } 
        } 
    }
    string hillciphertext;
    for (int i = 0; i < 3; i++) 
        hillciphertext += (char)(fmod(hillcipher[i][0], 26) + 65);
    cout <<"Hill cipher encrption text:" << hillciphertext; 
    
    float p, q,b[3][3], decrypt[3][1];
	
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++) {
			if(i == j)
				b[i][j]=1;
			else
				b[i][j]=0;
		}
		
	for(int k = 0; k < 3; k++) {
		for(int i = 0; i < 3; i++) {
			p = keymatrix[i][k];
			q = keymatrix[k][k];
				
			for(int j = 0; j < 3; j++) {
				if(i != k) {
					keymatrix[i][j] = keymatrix[i][j]*q - p*keymatrix[k][j];
					b[i][j] = b[i][j]*q - p*b[k][j];
				}
			}
		}
	}
	
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++)
			b[i][j] = b[i][j] / keymatrix[i][i];
	
	cout<<"\n\nInverse Matrix is:\n";
	for(int i = 0; i < 3; i++) {
		for(int j = 0; j < 3; j++)
			cout<<b[i][j]<<" ";
		
		cout<<"\n";
	}
    
    for(int i = 0; i < 3; i++)
		for(int j = 0; j < 1; j++)
			for(int k = 0; k < 3; k++)
				decrypt[i][j] = decrypt[i][j] + b[i][k] * hillcipher[k][j];
		
	string s;		
	for(int i = 0; i < 3; i++)
		s += (char)(fmod(decrypt[i][0], 26) + 65);
	cout <<"hill cypher decryption: "<<s;
	
	cout<<"\n";
    
    
    
}
*/
//Only Encryption Part
#include<iostream>
#include<vector>
using namespace std;
int main(){
    int x,y,i,j,k,n;
    cout<<"Enter the size of key matrix\n";
    cin>>n;
    cout<<"Enter the key matrix\n";
    int a[n][n];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            cin>>a[i][j];
        }
    }
    cout<<"Enter the message to encrypt\n";
    string s;
    cin>>s;
    int temp = (n-s.size()%n)%n;
    for(i=0;i<temp;i++){
        s+='x';
    }
    k=0;
    string ans="";
    while(k<s.size()){
        for(i=0;i<n;i++){
            int sum = 0;
            int temp = k;
            for(j=0;j<n;j++){
                sum += (a[i][j]%26*(s[temp++]-'a')%26)%26;
                sum = sum%26;
            }
            ans+=(sum+'a');
        }
        k+=n;
    }
    cout<<ans<<'\n';
    return 0;    
}
