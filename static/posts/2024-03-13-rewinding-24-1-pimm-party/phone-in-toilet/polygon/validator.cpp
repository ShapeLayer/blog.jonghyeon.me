#define IS_RUNTIME_POLYGON true
#include <bits/stdc++.h>
 
#if IS_RUNTIME_POLYGON
#include "testlib.h"
#endif
 
using namespace std;
 
#define TT_SYM "TT"
#define TT_MIN 1
#define TT_MAX 100
#define TC_SYM "TC"
#define TC_MIN 1
#define TC_MAX 100
#define NS_SYM "NS"
#define NS_MIN 0
#define NS_MAX 10'000
#define ND_SYM "ND"
#define ND_MIN 0
#define ND_MAX 10'000
#define SCREW_X_SYM "SCREW_X"
#define SCREW_X_MIN -1'000
#define SCREW_X_MAX 1'000
#define SCREW_Y_SYM "SCREW_Y"
#define SCREW_Y_MIN -1'000
#define SCREW_Y_MAX 1'000
#define WEAK_X_SYM "WEAK_X"
#define WEAK_X_MIN -1'000
#define WEAK_X_MAX 1'000
#define WEAK_Y_SYM "WEAK_Y"
#define WEAK_Y_MIN -1'000
#define WEAK_Y_MAX 1'000
#define A_SYM "A"
#define A_MIN 0
#define A_MAX 40
#define B_SYM "B"
#define B_MIN 0
#define B_MAX 40
#define C_SYM "C"
#define C_MIN 0
#define C_MAX 40
#define M_SYM "M"
#define M_MIN 1
#define M_MAX 40
#define ERR_VALUE_OUT_OF_RANGE "Value is out of range."
#define ERR_POSITION_NOT_UNIQUE "Each position must be unique."
 
set<pair<int, int>> pair_set;
set<pair<int, int>>::iterator pair_set_iter;
 
inline int getInt(int min, int max, string symbol) {
  #if IS_RUNTIME_POLYGON
  return inf.readInt(min, max, symbol);
  #else
  int gets;
  cin >> gets;
  if (min <= gets && gets <= max) {
    return gets;
  }
  cout << ERR_VALUE_OUT_OF_RANGE << endl;
  exit(1);
  #endif
}
 
inline void getSpace() {
  #if IS_RUNTIME_POLYGON
  inf.readSpace();
  #endif
}
 
inline void getEoln() {
  #if IS_RUNTIME_POLYGON
  inf.readEoln();
  #endif
}
 
inline void getEof() {
  #if IS_RUNTIME_POLYGON
  inf.readEof();
  #endif
}
 
inline void assertAbout(bool about, const char* ifnot) {
  #if IS_RUNTIME_POLYGON
  ensuref(about, ifnot);
  #else
  if (!about) {
    cout << ifnot << endl;
    exit(1);
  }
  #endif
}
 
int main(int argc, char* argv[]) {
  #if IS_RUNTIME_POLYGON
  registerValidation(argc, argv);
  #endif
 
  int tt = getInt(TT_MIN, TT_MAX, TT_SYM);
  getSpace();
  int tc = getInt(TC_MIN, TC_MAX, TC_SYM);
  getEoln();
 
  int a = getInt(A_MIN, A_MAX, A_SYM);
  getSpace();
  int b = getInt(B_MIN, B_MAX, B_SYM);
  getSpace();
  int c = getInt(C_MIN, C_MAX, C_SYM);
  getSpace();
  int m = getInt(M_MIN, M_MAX, M_SYM);
  getEoln();
 
  int ns = getInt(NS_MIN, NS_MAX, NS_SYM);
  getSpace();
  int nd = getInt(ND_MIN, ND_MAX, ND_SYM);
  getEoln();
 
  int screw_x, screw_y;
  for (int i = 0; i < ns; i++) {
    screw_x = getInt(SCREW_X_MIN, SCREW_X_MAX, SCREW_X_SYM);
    getSpace();
    screw_y = getInt(SCREW_Y_MIN, SCREW_Y_MAX, SCREW_Y_SYM);
    getEoln();
    pair<int, int> _pair = make_pair(screw_x, screw_y);
    pair_set_iter = pair_set.find(_pair);
    assertAbout(pair_set_iter == pair_set.end(), ERR_POSITION_NOT_UNIQUE);
    pair_set.insert(_pair);
  }
 
  int weak_x, weak_y;
  for (int i = 0; i < nd; i++) {
    weak_x = getInt(WEAK_X_MIN, WEAK_X_MAX, WEAK_X_SYM);
    getSpace();
    weak_y = getInt(WEAK_Y_MIN, WEAK_Y_MAX, WEAK_Y_SYM);
    getEoln();
    pair<int, int> _pair = make_pair(weak_x, weak_y);
    pair_set_iter = pair_set.find(_pair);
    assertAbout(pair_set_iter == pair_set.end(), ERR_POSITION_NOT_UNIQUE);
    pair_set.insert(_pair);
  }
 
  getEof();
 
  return 0;
}
