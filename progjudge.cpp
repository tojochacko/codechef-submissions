#include "spoj_interactive.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <utility>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int max_N = 110;
const int max_K = 110;

int dist[max_N][max_N], vis[max_N][max_N], s[max_N][max_N];
int grid[max_N][max_N], solution_grid[max_N][max_N];
pii death[max_K];
queue<pii> bfq;

void update_point(int x, int y, int state, int other_dist);
int num_used(int N);
bool valid(int N);

int main()
{
    spoj_init();

    int N, K;
    int jury_blocks;
    fscanf(spoj_p_out, "%d", &jury_blocks);
    int num_read = fscanf(spoj_p_in, "%d%d", &N, &K);
    if (num_read < 2) {
        fprintf(spoj_u_info, "problem input does not contain N and K");
        return SPOJ_RV_IE;
    }
    for (int i = 0; i < K; ++i) {
        int x, y;
        num_read = fscanf(spoj_p_in, "%d%d", &x, &y);
        if (num_read < 2) {
            fprintf(spoj_u_info, "problem input does not contain %d-th pair of coordinates or beyond", i + 1);
            return SPOJ_RV_IE;
        }
        grid[x][y] = 1;
    }
    char c;
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j) {
            num_read = fscanf(spoj_t_out, " %c", &c);
            if (num_read < 1) {
                fprintf(spoj_u_info, "participant output does not fit format string");
                return SPOJ_RV_WA;
            }
            solution_grid[i][j] = (c == '#');
        }
    if (valid(N)) {
        int participant_blocks = num_used(N);
        double score;
        if (participant_blocks <= jury_blocks) {
            score = 10.0L;
        } else {
            score = max(0.0L, 10.0L - (participant_blocks - jury_blocks) / (1.0L * (jury_blocks + 1)));
        }

        fprintf(spoj_score, "%F\n", score);
        return SPOJ_RV_AC;
    } else {
        return SPOJ_RV_WA;
    }

    spoj_finalize();
}

bool valid(int N)
{
    int mid = N / 2 + 1;
    assert(N % 2);
    assert(solution_grid[1][mid]); //not blocked.

    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j)
            s[i][j] = 1;

    pii source = {1, mid};
    vis[1][mid] = 1;
    s[1][mid] = 0;
    bfq.push(source);

    int x, y;
    while(!bfq.empty()) {
        tie(x, y) = bfq.front();
        bfq.pop();
        int state = s[x][y] | grid[x][y];
        update_point(x - 1, y, state, dist[x][y]);
        update_point(x + 1, y, state, dist[x][y]);
        update_point(x, y - 1, state, dist[x][y]);
        update_point(x - 1, y + 1, state, dist[x][y]);
    }
    return (s[N][mid] || grid[N][mid]) && vis[N][mid];
}

void update_point(int x, int y, int state, int other_dist)
{
    if (solution_grid[x][y] == 1)
        return;
    if (!vis[x][y]) {
        vis[x][y] = 1;
        dist[x][y] = other_dist + 1;
        s[x][y] = state;
        bfq.push({x, y});
        return;
    }
    if (dist[x][y] == other_dist + 1) {
        s[x][y] &= state;
    }
}

int num_used(int N)
{
    int ans = 0;
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= N; ++j)
            ans += solution_grid[i][j];
    return ans;
}
