#include <bits/stdc++.h>
using namespace std;
typedef vector<uint64_t> Poly;
typedef unsigned long long u64;

void trimP(Poly&p){while(!p.empty() && p.back()==0) p.pop_back();}
int degP(const Poly&p){
    if(p.empty()) return -1;
    int top=(int)p.size()-1;
    u64 v=p[top];
    int b=63;
    while(((v>>b)&1ULL)==0) b--;
    return top*64+b;
}
bool isZeroP(const Poly&p){return p.empty();}
bool isOneP(const Poly&p){return p.size()==1 && p[0]==1;}
Poly intP(u64 v){Poly p; if(v) p.push_back(v); return p;}
bool bitP(const Poly&p,int i){
    if(i<0) return false;
    int limb=i/64,b=i%64;
    if((size_t)limb>=p.size()) return false;
    return ((p[limb]>>b)&1ULL)!=0;
}
Poly addP(const Poly&a,const Poly&b){
    Poly r(max(a.size(),b.size()),0ULL);
    for(size_t i=0;i<a.size();i++) r[i]^=a[i];
    for(size_t i=0;i<b.size();i++) r[i]^=b[i];
    trimP(r);
    return r;
}
Poly shlP(const Poly&a,int k){
    if(isZeroP(a)) return Poly();
    int ls=k/64, bs=k%64;
    Poly r(a.size()+ls+1,0ULL);
    for(size_t i=0;i<a.size();i++){
        u64 v=a[i];
        if(bs==0){
            r[i+ls]^=v;
        } else {
            r[i+ls]^=(v<<bs);
            r[i+ls+1]^=(v>>(64-bs));
        }
    }
    trimP(r);
    return r;
}
Poly mulP(const Poly&a,const Poly&b){
    if(isZeroP(a)||isZeroP(b)) return Poly();
    Poly result;
    int db=degP(b);
    for(int i=0;i<=db;i++){
        if(bitP(b,i)){
            Poly sh=shlP(a,i);
            result=addP(result,sh);
        }
    }
    return result;
}
Poly modP(Poly a,const Poly&m){
    int dm=degP(m);
    while(true){
        int da=degP(a);
        if(da<dm) break;
        int sh=da-dm;
        Poly t=shlP(m,sh);
        a=addP(a,t);
    }
    return a;
}
pair<Poly,Poly> divmodP(Poly a,const Poly&m){
    int dm=degP(m);
    Poly q;
    while(true){
        int da=degP(a);
        if(da<dm) break;
        int sh=da-dm;
        int limb=sh/64,b=sh%64;
        if((size_t)limb>=q.size()) q.resize(limb+1,0ULL);
        q[limb]^=(1ULL<<b);
        Poly t=shlP(m,sh);
        a=addP(a,t);
    }
    trimP(q);
    return make_pair(q,a);
}
Poly gcdP(Poly a,Poly b){
    while(!isZeroP(b)){
        Poly r=modP(a,b);
        a=b; b=r;
    }
    return a;
}
Poly derivP(const Poly&f){
    int d=degP(f);
    Poly r;
    for(int i=1;i<=d;i+=2){
        if(bitP(f,i)){
            int j=i-1;
            int limb=j/64,b=j%64;
            if((size_t)limb>=r.size()) r.resize(limb+1,0ULL);
            r[limb]^=(1ULL<<b);
        }
    }
    trimP(r);
    return r;
}
Poly evenHalfP(const Poly&f){
    int d=degP(f);
    Poly r;
    for(int i=0;i<=d;i+=2){
        if(bitP(f,i)){
            int j=i/2;
            int limb=j/64,b=j%64;
            if((size_t)limb>=r.size()) r.resize(limb+1,0ULL);
            r[limb]^=(1ULL<<b);
        }
    }
    trimP(r);
    return r;
}
vector<pair<Poly,int>> mergeFactors(vector<pair<Poly,int>> v){
    map<Poly,int> mp;
    for(auto&pr:v) mp[pr.first]+=pr.second;
    vector<pair<Poly,int>> res;
    for(auto&pr:mp) res.push_back(make_pair(pr.first,pr.second));
    return res;
}
vector<pair<Poly,int>> squarefreeFactor(Poly f){
    vector<pair<Poly,int>> result;
    if(isOneP(f) || isZeroP(f)) return result;
    Poly fp=derivP(f);
    if(isZeroP(fp)){
        Poly half=evenHalfP(f);
        auto sub=squarefreeFactor(half);
        for(auto&pr:sub) result.push_back(make_pair(pr.first,pr.second*2));
        return mergeFactors(result);
    }
    Poly c=gcdP(f,fp);
    Poly w=divmodP(f,c).first;
    int i=1;
    while(!isOneP(w)){
        Poly y=gcdP(w,c);
        Poly fac=divmodP(w,y).first;
        if(!isOneP(fac)) result.push_back(make_pair(fac,i));
        w=y;
        c=divmodP(c,y).first;
        i++;
    }
    if(!isOneP(c)){
        Poly half=evenHalfP(c);
        auto sub=squarefreeFactor(half);
        for(auto&pr:sub) result.push_back(make_pair(pr.first,pr.second*2));
    }
    return mergeFactors(result);
}
Poly xP(){Poly p; p.push_back(2ULL); return p;}
vector<pair<int,Poly>> DDF(Poly f){
    vector<pair<int,Poly>> result;
    Poly fstar=f;
    Poly h=xP();
    int i=0;
    while(degP(fstar)>0){
        i++;
        h=mulP(h,h);
        h=modP(h,fstar);
        Poly diff=addP(h,xP());
        Poly g=gcdP(diff,fstar);
        if(!isOneP(g)){
            result.push_back(make_pair(i,g));
            fstar=divmodP(fstar,g).first;
            h=modP(h,fstar);
        }
    }
    return result;
}
mt19937_64 rngEngine(88172645463325252ULL);
Poly randPolyLess(int maxDeg){
    int nbits=maxDeg;
    int nlimb=(nbits+63)/64;
    if(nlimb==0) nlimb=1;
    Poly p(nlimb,0ULL);
    for(auto&w:p) w=rngEngine();
    int total=nlimb*64;
    for(int b=nbits;b<total;b++){
        int limb=b/64,bb=b%64;
        p[limb]&=~(1ULL<<bb);
    }
    trimP(p);
    return p;
}
void EDFrec(Poly h,int d,vector<Poly>&out){
    int dh=degP(h);
    if(dh==d){out.push_back(h); return;}
    while(true){
        Poly a=randPolyLess(dh);
        if(isZeroP(a)) continue;
        Poly T=a;
        Poly cur=a;
        for(int k=1;k<d;k++){
            cur=mulP(cur,cur);
            cur=modP(cur,h);
            T=addP(T,cur);
        }
        T=modP(T,h);
        if(isZeroP(T)) continue;
        Poly g=gcdP(T,h);
        int dg=degP(g);
        if(dg>0 && dg<dh){
            Poly hg=divmodP(h,g).first;
            EDFrec(g,d,out);
            EDFrec(hg,d,out);
            return;
        }
    }
}
vector<Poly> EDF(Poly g,int d){
    vector<Poly> out;
    EDFrec(g,d,out);
    return out;
}
vector<pair<Poly,int>> factorPoly(Poly f){
    vector<pair<Poly,int>> finalFactors;
    auto sff=squarefreeFactor(f);
    for(auto&pr:sff){
        Poly g=pr.first; int e=pr.second;
        auto ddfList=DDF(g);
        for(auto&dp:ddfList){
            int d=dp.first; Poly prod=dp.second;
            auto irrs=EDF(prod,d);
            for(auto&h:irrs) finalFactors.push_back(make_pair(h,e));
        }
    }
    return finalFactors;
}
string wordHex(const Poly&p,int w){
    uint32_t v=0;
    for(int b=0;b<32;b++) if(bitP(p,w*32+b)) v|=(1u<<b);
    char buf[16];
    snprintf(buf,sizeof(buf),"%08x",v);
    return string(buf);
}
string formatLine(const Poly&d,const Poly&c,int wordsA){
    string res;
    for(int w=0;w<wordsA;w++){
        if(!res.empty()) res+=" ";
        res+=wordHex(d,w);
    }
    for(int w=0;w<wordsA;w++){
        res+=" ";
        res+=wordHex(c,w);
    }
    return res;
}
int main(){
    int S;
    cin>>S;
    int wcount=S/16;
    int wordsA=S/32;
    vector<uint32_t> bwords(wcount);
    for(int i=0;i<wcount;i++){
        string tok; cin>>tok;
        bwords[i]=(uint32_t)stoul(tok,nullptr,16);
    }
    Poly B;
    for(int w=0;w<wcount;w++){
        for(int b=0;b<32;b++){
            if((bwords[w]>>b)&1u){
                int gb=w*32+b;
                int limb=gb/64,bb=gb%64;
                if((size_t)limb>=B.size()) B.resize(limb+1,0ULL);
                B[limb]|=(1ULL<<bb);
            }
        }
    }
    trimP(B);
    int degB=degP(B);
    int maxDegA=S-1;
    vector<string> lines;
    if(isZeroP(B)){
        Poly z;
        lines.push_back(formatLine(z,z,wordsA));
    } else {
        int lowTarget=max(0,degB-maxDegA);
        int highTarget=min(degB,maxDegA);
        auto factors=factorPoly(B);
        int K=(int)factors.size();
        vector<int> degs(K),mults(K);
        for(int i=0;i<K;i++){degs[i]=degP(factors[i].first); mults[i]=factors[i].second;}
        vector<long long> suffixMax(K+1,0);
        for(int i=K-1;i>=0;i--) suffixMax[i]=suffixMax[i+1]+(long long)degs[i]*mults[i];
        vector<vector<Poly>> pw(K);
        for(int i=0;i<K;i++){
            pw[i].resize(mults[i]+1);
            pw[i][0]=intP(1ULL);
            for(int f=1;f<=mults[i];f++) pw[i][f]=mulP(pw[i][f-1],factors[i].first);
        }
        function<void(int,long long,Poly)> dfs=[&](int idx,long long accDeg,Poly accPoly){
            if(idx==K){
                if(accDeg>=lowTarget && accDeg<=highTarget){
                    Poly d=accPoly;
                    Poly c=divmodP(B,d).first;
                    lines.push_back(formatLine(d,c,wordsA));
                }
                return;
            }
            for(int f=0;f<=mults[idx];f++){
                long long newDeg=accDeg+(long long)f*degs[idx];
                if(newDeg>highTarget) break;
                if(newDeg+suffixMax[idx+1]<lowTarget) continue;
                Poly newPoly=mulP(accPoly,pw[idx][f]);
                dfs(idx+1,newDeg,newPoly);
            }
        };
        dfs(0,0,intP(1ULL));
    }
    sort(lines.begin(),lines.end());
    lines.erase(unique(lines.begin(),lines.end()),lines.end());
    for(auto&l:lines) cout<<l<<"\n";
    return 0;
}