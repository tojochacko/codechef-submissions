#include<iostream>
#include<cstdio>

long int n,k,ans = 0;
long long int t;

int main() {
	scanf("%ld %ld", &n, &k);
	while(n > 0) {
		scanf("%lld", &t);
		if(t%k == 0)
			ans++;
		n--;
	}

	printf("%ld", ans);
	return 0;
}
