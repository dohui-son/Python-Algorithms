// 소스코드 출철
// https://youtu.be/E7JV9XUYSKE

1.
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
#define NM 25
priority_queue<int> map[NM][NM];
struct P {
    int x, y, d, atk;
    int gun, score;
    bool operator<(const P& ot) const {
        if (atk + gun != ot.atk + ot.gun) return atk + gun < ot.atk + ot.gun;
        return atk < ot.atk;
    }
    int operator-(const P& ot) {
        return atk + gun - ot.atk - ot.gun;
    }
}fighters[35];
int N, M, K;
void input() {
    // Input
    cin >> N >> M >> K;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int x;
            cin >> x;
            map[i][j].push(x);
        }
    }
    for (int i = 1; i <= M; i++) {
        cin >> fighters[i].x >> fighters[i].y >> fighters[i].d >> fighters[i].atk;
    }
}
int dir[4][2] = { {-1 ,0}, {0, 1},{1, 0}, {0, -1} };
void move(int i) {
    // i 번 사람이 규칙에 맞게 이동함
    int d = fighters[i].d;
    int nx = fighters[i].x + dir[d][0], ny = fighters[i].y + dir[d][1];
    if (nx < 1 || ny < 1 || nx > N || ny > N) {
        d ^= 2;
        fighters[i].d ^= 2;
        nx = fighters[i].x + dir[d][0], ny = fighters[i].y + dir[d][1];
    }
    fighters[i].x = nx, fighters[i].y = ny;
}
int conflict(int x, int y, int i) {
    // 현재 (x, y)에 있는 사람
    for (int j = 1; j <= M; j++) {
        if (i == j) continue;
        if (x == fighters[j].x &&
            y == fighters[j].y) {
            return j;
        }
    }
    return 0;
}
void pick_gun(int i) {
    // i 번 사람이 현재 위치에서 총을 주움
    int x = fighters[i].x, y = fighters[i].y;
    if (map[x][y].empty()) {
        fighters[i].gun = 0;
    }
    else {
        fighters[i].gun = map[x][y].top();
        map[x][y].pop();
    }
}
void drop_gun(int i) {
    // i 번 사람이 현재 위치에 총을 내려놓음
    int x = fighters[i].x, y = fighters[i].y;
    map[x][y].push(fighters[i].gun);
    fighters[i].gun = 0;
}
void loser(int i) {
    // 패배자에 대한 처리
    // 1. 총 떨구기
    drop_gun(i);
    // 2. 네 방향을 시계 방향으로 돌면서 갈 곳을 찾음
    int d = fighters[i].d;
    int nx = fighters[i].x + dir[d][0], ny = fighters[i].y + dir[d][1];
    while (nx < 1 || ny < 1 || nx > N || ny > N || conflict(nx, ny, i) != 0) {
        d = (d + 1) % 4;
        nx = fighters[i].x + dir[d][0], ny = fighters[i].y + dir[d][1];
    }
    fighters[i].d = d;
    fighters[i].x = nx, fighters[i].y = ny;
    // 3.
    pick_gun(i);
}
void winner(int i) {
    // 승리자에 대한 처리
    drop_gun(i);
    pick_gun(i);
}
void fight(int i, int j) {
    // i번 사람이랑 j번 사람이 싸움!
    if (fighters[i] < fighters[j]) {  // j 번 승리
        fighters[j].score += fighters[j] - fighters[i];
        loser(i);
        winner(j);
    }
    else {
        fighters[i].score += fighters[i] - fighters[j];
        loser(j);
        winner(i);
    }
}
void pro() {
    while (K--) {
        for (int i = 1; i <= M; i++) {
            move(i);
            int j = conflict(fighters[i].x, fighters[i].y, i);
            if (j != 0) { // 만약 싸움이 일어났다면
                fight(i, j);
            }
            else {  // 싸움이 일어나지 않았다면,
                drop_gun(i);
                pick_gun(i);
            }
        }
    }
    for (int i = 1; i <= M; i++) {
        cout << fighters[i].score << " ";
    }
}
int main() {
    input();
    pro();
    return 0;
}
2.
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_map>
using namespace std;
int Q, N, M;
struct BOX {
    int idx, belt, weight;
    BOX *prev, *next;
}box[100005];
unordered_map<int, BOX*> box_map;  // id -> BOX 값
int idx[100005], weights[100005];
struct BELT {
    BOX* front, * end;
    bool broken;
}belt[15];// belt[i] := i 번 벨트에서 가장 앞에 있는 박스 번호, 없다면 0
void push_box(int belt_idx, BOX* box) {
    if (belt[belt_idx].front == NULL) {  // 만약 비어있는 벨트 였다면?
        box->prev = box->next = NULL;
        belt[belt_idx].front = belt[belt_idx].end = box;
    }
    else {
        box->prev = belt[belt_idx].end, box->next = NULL;
        belt[belt_idx].end->next = box;
        belt[belt_idx].end = box;
    }
}
void input() {
    cin >> Q;
    int x;
    cin >> x >> N >> M;
    for (int i = 1; i <= N; i++) {
        cin >> idx[i];
    }
    for (int i = 1; i <= N; i++) {
        cin >> weights[i];
    }
    int T = N / M;
    for (int i = 1; i <= M; i++) {
        for (int j = (i - 1) * T + 1; j <= i * T; j++) {
            box[j].idx = idx[j];
            box[j].belt = i;
            box[j].weight = weights[j];
            box_map[idx[j]] = &box[j];
            push_box(i, &box[j]);
        }
    }
}
BOX* drop_box(int i) {
    BOX* box = belt[i].front;
    box->belt = 0;
    box_map.erase(box->idx);
    belt[i].front = box->next;
    box->next = NULL;
    if (belt[i].front != NULL)
        belt[i].front->prev = NULL;
    return box;
}
int query_200(int W) {
    int sum = 0;  // 하차되는 상자들의 무게 총 합
    for (int i = 1; i <= M; i++) {
        if (belt[i].front == NULL) {  // 비어있는 벨트면 무시하기
            continue;
        }
        if (belt[i].front->weight <= W) {
            sum += belt[i].front->weight;
            // 하차하기
            drop_box(i);
        }
        else {
            // 하차 했다가
            BOX* box = drop_box(i);
            // 다시 실기
            push_box(i, box);
        }
    }
    return sum;
}
int query_300(int id) {
    if (box_map.find(id) == box_map.end()) {  // 없는 상자인 경우
        return -1;
    }
    BOX* box = box_map[id];
    BOX* prev = box->prev, * next = box->next;
    int b = box->belt;
    
    if (prev == NULL && next == NULL) {  // 벨트 하나가 통째로 비어버리는 상황
        belt[b].front = belt[b].end = NULL;
    }
    else if (prev == NULL) {  // 벨트의 가장 앞 상자가 바뀌는 상황
        next->prev = NULL;
        belt[b].front = next;
    }
    else if (next == NULL) {  // 벨트의 가장 뒤 상자가 바뀌는 상황
        prev->next = NULL;
        belt[b].end = prev;
    }
    else {
        prev->next = next;
        next->prev = prev;
    }
    box_map.erase(id);
    return id;
}
int query_400(int id) {
    if (box_map.find(id) == box_map.end()) {  // 없는 상자인 경우
        return -1;
    }
    
    BOX* box = box_map[id];
    BOX* prev = box->prev, * next = box->next;
    int b = box->belt;
    BOX* front = belt[b].front, * end = belt[b].end;
    if (prev == NULL && next == NULL) {  // 벨트 하나가 통째로 비어버리는 상황
        // DO NOTHING
    }
    else if (prev == NULL) {  // 벨트의 가장 앞 상자가 바뀌는 상황
        // DO NOTHING
    }
    else if (next == NULL) {  // 벨트의 가장 뒤 상자가 바뀌는 상황
        prev->next = NULL;
        front->prev = box;
        box->next = front;
        box->prev = NULL;
        belt[b].front = box;
        belt[b].end = prev;
    }
    else {
        box->prev = NULL;
        prev->next = NULL;
        end->next = front;
        front->prev = end;
        belt[b].front = box;
        belt[b].end = prev;
    }
    return box_map[id]->belt;
}
int query_500(int b) {
    if (belt[b].broken) {
        return -1;
    }
    if (belt[b].front == NULL) {  // 즉, 삭제한 벨트가 이미 비어있는 친구면, 아무 일도 안해도 됨!
        belt[b].broken = true;
        return b;
    }
    int tgt = b;
    belt[b].broken = true;
    while (belt[tgt].broken){
        tgt++;
        if (tgt > M)
            tgt = 1;
    }
    // 1. belt[b].front 와 belt[tgt].end 사이에 link 생성
    belt[b].front->prev = belt[tgt].end;
    belt[tgt].end->next = belt[b].end;
    // 2. belt[b] 의 상자들의 belt 값을 tgt로 변경
    for (BOX* it = belt[b].front; it; it = it->next) {
        it->belt = tgt;
    }
    // 3. belt[tgt]의 end 를 belt[b].end 로 변경
    belt[tgt].end = belt[b].end;
    return b;
}
void pro() {
    for (int rep = 2; rep <= Q; rep++) {
        int query;
        cin >> query;
        if (query == 200) {
            int W;
            cin >> W;
            cout << query_200(W) << '\n';
        }
        else if (query == 300) {
            int id;
            cin >> id;
            cout << query_300(id) << '\n';
        }
        else if (query == 400) {
            int id;
            cin >> id;
            cout << query_400(id) << '\n';
        }
        else if (query == 500) {
            int b_num;
            cin >> b_num;
            cout << query_500(b_num) << '\n';
        }
    }
}
int main() {
    input();
    pro();
    return 0;
}