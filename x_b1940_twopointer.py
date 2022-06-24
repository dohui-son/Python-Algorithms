#주몽  - 시간초과 투포인터 다시 풀어야함
#투포인터(시간 더 짧음)와 COMBINATION을 서로 착각할 수 있다

#include<bits/stdc++.h> 
using namespace std;     
int n, m, a[150001], cnt;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m; 
	for(int i = 0; i < n; i++) cin >> a[i];
	sort(a, a + n); 
	if(m > 200000) cout << 0 << "\n";
	else{
		int lo = 0, hi = n - 1; 
		while(lo < hi){
			if(a[lo] + a[hi] == m)cnt++, lo++;
			else if(a[lo] + a[hi] < m)lo++;
			else hi--;
		} 
		cout << cnt << "\n";
	} 
}

