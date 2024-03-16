#define IS_RUNTIME_POLYGON true
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
#define MAIN_ARGC_REQUIRED 2
#define ERR_COMMENT_REQUIRED_ARG_NOT_ENOUGH "There are not enough parameters provided compared to what the program requires."
#define ERR_COMMNET_NS_OUT_OF_RANGE "Argument Ns is out of range."
#define ERR_COMMNET_ND_OUT_OF_RANGE "Argument Nd is out of range."

#include <bits/stdc++.h>
#if IS_RUNTIME_POLYGON
#include "testlib.h"
#endif

using namespace std;

/**
 * gen_random
 * @param init `int`
 * @param fin `fint`
 * @return result of generating random int
*/
inline int gen_random(int init, int fin) {
  #if IS_RUNTIME_POLYGON
  return rnd.next(init, fin);
  #else
  random_device rnd;
  mt19937 gen(rnd());
  uniform_int_distribution<> dist(init, fin);
  return dist(gen);
  #endif
}

set<pair<int, int>> pair_set;
set<pair<int, int>>::iterator pair_set_iter;
inline pair<int, int> gen_unique_pair(int init_x, int fin_x, int init_y, int fin_y) {
  int x, y;
  while (true) {
    x = gen_random(init_x, fin_x), y = gen_random(init_y, fin_y);
    pair<int, int> _pair = make_pair(x, y);
    pair_set_iter = pair_set.find(_pair);
    if (pair_set_iter == pair_set.end()) {
      pair_set.insert(_pair);
      return _pair;
    }
  }
}

/**
 * Main
 * @param argv[0] Ns
 * @param argv[1] Nd
*/
int main(int argc, char* argv[]) {
  #if IS_RUNTIME_POLYGON
  registerGen(argc, argv, 1);
  #endif

  if (argc < MAIN_ARGC_REQUIRED + 1) {
    cerr << ERR_COMMENT_REQUIRED_ARG_NOT_ENOUGH << '\n';
    return 1;
  }

  int ns = stoi(argv[1]), nd = stoi(argv[2]);
  #if IS_RUNTIME_POLYGON
  ensuref(NS_MIN <= ns && ns <= NS_MAX, ERR_COMMNET_NS_OUT_OF_RANGE);
  ensuref(ND_MIN <= nd && nd <= ND_MAX, ERR_COMMNET_ND_OUT_OF_RANGE);
  #else
  if (!(NS_MIN <= ns && ns <= NS_MAX)) {
    cerr << ERR_COMMNET_NS_OUT_OF_RANGE << '\n'; 
    return 1;
  }
  if (!(ND_MIN <= nd && nd <= ND_MAX)) {
    cerr << ERR_COMMNET_ND_OUT_OF_RANGE << '\n'; 
    return 1;
  }
  #endif

  // line 1
  int tt = gen_random(TT_MIN, TT_MAX), tc = gen_random(TC_MIN, TC_MAX);
  cout << tt << ' ' << tc << '\n';
  
  // line 2
  int a = gen_random(A_MIN, A_MAX), b = gen_random(B_MIN, B_MAX), c = gen_random(C_MIN, C_MAX), m = gen_random(M_MIN, M_MAX);
  cout << a << ' ' << b << ' ' << c << ' ' << m << '\n';

  // line 3
  cout << ns << ' ' << nd << '\n';

  // line 4 ~ 4 + ns
  for (int i = 0; i < ns; i++) {
    pair<int, int> gen = gen_unique_pair(SCREW_X_MIN, SCREW_X_MAX, SCREW_Y_MIN, SCREW_Y_MAX);
    int x = gen.first, y = gen.second;
    cout << x << ' ' << y << '\n';
  }

  // line (4 + ns) + 1 ~ (4 + ns) + nd
  for (int i = 0; i < nd; i++) {
    pair<int, int> gen = gen_unique_pair(SCREW_X_MIN, SCREW_X_MAX, SCREW_Y_MIN, SCREW_Y_MAX);
    int x = gen.first, y = gen.second;
    cout << x << ' ' << y << '\n';
  }

  return 0;
}
