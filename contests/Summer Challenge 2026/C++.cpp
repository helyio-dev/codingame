#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {-1, 0, 1, 0};

int W, H, myId, oppId;
int reg[30][30], typ[30][30];
bool hasTown[30][30];

struct Town { int id, x, y; };
vector<Town> towns;
map<int, int> tid2i;

vector<pair<int,int>> desiredPairs;

vector<pair<int,int>> bfsPath(int ax, int ay, int bx, int by,
                              const vector<vector<bool>>& ink) {
    if (ax == bx && ay == by) return {};
    vector<vector<int>> dist(H, vector<int>(W, INF));
    vector<vector<pair<int,int>>> par(H, vector<pair<int,int>>(W, {-1,-1}));
    queue<pair<int,int>> q;
    dist[ay][ax] = 0;
    q.push({ax, ay});
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        if (x == bx && y == by) break;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= W || ny < 0 || ny >= H) continue;
            if (ink[ny][nx]) continue;
            if (dist[ny][nx] > dist[y][x] + 1) {
                dist[ny][nx] = dist[y][x] + 1;
                par[ny][nx] = {x, y};
                q.push({nx, ny});
            }
        }
    }
    if (dist[by][bx] == INF) return {};
    vector<pair<int,int>> path;
    pair<int,int> c = {bx, by};
    while (c.first != -1) { path.push_back(c); c = par[c.second][c.first]; }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    cin >> myId; oppId = 1 - myId;
    cin >> W >> H;
    memset(hasTown, 0, sizeof(hasTown));

    for (int y = 0; y < H; y++)
        for (int x = 0; x < W; x++)
            cin >> reg[y][x] >> typ[y][x];

    int tc; cin >> tc;
    towns.resize(tc);
    for (int i = 0; i < tc; i++) {
        cin >> towns[i].id >> towns[i].x >> towns[i].y;
        string dc; cin >> dc;
        hasTown[towns[i].y][towns[i].x] = true;
        tid2i[towns[i].id] = i;
        if (dc != "x") {
            stringstream ss(dc); string tk;
            while (getline(ss, tk, ',')) {
                int b = stoi(tk);
                desiredPairs.push_back({towns[i].id, b});
            }
        }
    }

    while (true) {
        int myScore, foeScore;
        if (!(cin >> myScore >> foeScore)) break;

        vector<vector<int>> ow(H, vector<int>(W));
        vector<vector<int>> inst(H, vector<int>(W));
        vector<vector<bool>> ink(H, vector<bool>(W));
        vector<vector<int>> cellActives(H, vector<int>(W, 0));

        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++) {
                int iv;
                cin >> ow[y][x] >> inst[y][x] >> iv;
                ink[y][x] = (iv == 1);
                string aoc; cin >> aoc;
                if (aoc != "x") {
                    stringstream ss(aoc); string tk;
                    while (getline(ss, tk, ',')) cellActives[y][x]++;
                }
            }
        }

        vector<vector<pair<int,int>>> paths;
        vector<int> rem, owned, oppOwner;
        vector<vector<vector<int>>> cellPaths(H, vector<vector<int>>(W));

        for (auto& pr : desiredPairs) {
            int fi = tid2i[pr.first], ti = tid2i[pr.second];
            auto pa = bfsPath(towns[fi].x, towns[fi].y,
                              towns[ti].x, towns[ti].y, ink);
            if (pa.empty()) continue;
            int idx = paths.size();
            paths.push_back(pa);
            rem.push_back(0); owned.push_back(0); oppOwner.push_back(0);
            for (auto& c : pa) cellPaths[c.second][c.first].push_back(idx);
        }

        int P = paths.size();
        for (int p = 0; p < P; p++) {
            for (auto& c : paths[p]) {
                int o = ow[c.second][c.first];
                if (o == -1 && !hasTown[c.second][c.first]) rem[p]++;
                else if (o == myId) owned[p]++;
                else if (o == oppId) oppOwner[p]++;
            }
        }

        string output = "";
        vector<vector<bool>> used(H, vector<bool>(W, false));
        int remaining = 3;
        for (int iter = 0; iter < 3 && remaining > 0; iter++) {
            int bestV = -1;
            pair<int,int> bc = {-1, -1};
            for (int y = 0; y < H; y++) {
                for (int x = 0; x < W; x++) {
                    if (ow[y][x] != -1) continue;
                    if (ink[y][x]) continue;
                    if (hasTown[y][x]) continue;
                    if (used[y][x]) continue;
                    if (cellPaths[y][x].empty()) continue;
                    int c = typ[y][x] + 1;
                    if (c > remaining) continue;
                    int v = 0;
                    for (int p : cellPaths[y][x]) {
                        if (rem[p] == 1)
                            v += max(0, 40 + owned[p] + 1 - oppOwner[p]);
                        else
                            v += 4;
                    }
                    if (v > bestV) { bestV = v; bc = {x, y}; }
                }
            }
            if (bc.first == -1 || bestV <= 0) break;
            int x = bc.first, y = bc.second;
            int cost = typ[y][x] + 1;
            remaining -= cost;
            used[y][x] = true;
            if (!output.empty()) output += ";";
            output += "PLACE_TRACKS " + to_string(x) + " " + to_string(y);
            for (int p : cellPaths[y][x]) { rem[p]--; owned[p]++; }
        }

        map<int,int> oppScore, oppFuture, mySc, myFut;
        map<int,int> rInst;
        map<int,bool> rInk;
        set<int> allR, townR;
        for (auto& t : towns) townR.insert(reg[t.y][t.x]);

        for (int y = 0; y < H; y++) {
            for (int x = 0; x < W; x++) {
                int r = reg[y][x];
                allR.insert(r);
                rInst[r] = inst[y][x];
                rInk[r] = ink[y][x];
                if (ow[y][x] == oppId) {
                    if (cellActives[y][x] > 0) oppScore[r]++;
                    else oppFuture[r]++;
                } else if (ow[y][x] == myId) {
                    if (cellActives[y][x] > 0) mySc[r]++;
                    else myFut[r]++;
                }
            }
        }

        int bestR = -1, bestVal = -1e9;
        for (int r : allR) {
            if (townR.count(r)) continue;
            if (rInk[r] || rInst[r] >= 4) continue;
            int val = oppScore[r]*8 + oppFuture[r]*2
                    - mySc[r]*4 - myFut[r]*1 + rInst[r]*3;
            if (val > bestVal) { bestVal = val; bestR = r; }
        }

        if (bestR != -1 && bestVal > 10) {
            if (!output.empty()) output += ";";
            output += "DISRUPT " + to_string(bestR);
        }

        cout << (output.empty() ? "WAIT" : output) << endl;
    }
    return 0;
}