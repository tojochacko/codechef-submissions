#include<stdio.h>
#include<vector>

using namespace std;

int main() {
	int N,R;
	scanf("%d", &N);
	vector<int> v(N);
	for(int i = 1;i<=N; i++) {
		scanf("%d", &R);
		if(R != 0){
			v[R-1] = 1;
		}	
	}

	for(int j = 0; j<v.size(); j++) {
		if(v[j] == 0) {
			printf("%d ", j+1);
		}
	}
	printf("\n");
	return 0;
}
