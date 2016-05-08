#include <stdio.h>
#define CHAR_BIT 8

long long int T;
long long int n1,n2,m;

int min(int x, int y) {
  return  y + ((x - y) & ((x - y) >> 
            (sizeof(int) * CHAR_BIT - 1))); 
}

int main() {
	scanf("%lld", &T);	
	
	while(T > 0) {
		scanf("%lld %lld %lld", &n1, &n2, &m);
		for(int j = m; j >= 1; j--) {
			if(n1-j >= 0 && n2-j >= 0) {
				n1 = n1-j;
				n2 = n2-j;
			}	
			else {
				if(n1 > 0 && n2 > 0) {
					j = min(n1,n2);
					n1 = n1-j;
					n2 = n2-j;
				}
				break;
			}
		}	
		printf("%lld\n", n1+n2);
		T--;	
	}
	return 0;
}
