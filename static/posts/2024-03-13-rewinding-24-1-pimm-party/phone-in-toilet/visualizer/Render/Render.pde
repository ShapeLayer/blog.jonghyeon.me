import java.util.LinkedList;

import java.awt.Frame;

static class Config {
  static final int ScrewSize = 10;
  static final int WeakSize = 10;
  static final int StrokeWeight = 4;
  static final int ConnStrokeWeight = 4;
  
  static final int ScrewXMin = -1000;
  static final int ScrewXMax = 1000;
  static final int ScrewYMin = -1000;
  static final int ScrewYMax = 1000;

  static final int CanvasMargin = 100;
  
  static final int ColorBlack = 32;
  static final int ColorRed = #ff5f5d;
  static final int ColorBlue = #0099dd;
  static final int ColorGreen = #00ccbf;
  static final int ColorDarkGreen = #026e81;
  static final int ColorLightGrey = 244;

  static final int ColorDefault = ColorLightGrey;
  static final int ColorBackground = ColorLightGrey;
  static final int ColorScrew = ColorBlack;
  static final int ColorWeak = ColorRed;
  static final int ColorNow = ColorGreen;
  static final int ColorPrev = ColorBlack;
}

class ConfigUtil {
  ConfigUtil() {}

  int GetCanvasWidth() { return Config.ScrewXMax - Config.ScrewXMin + Config.CanvasMargin * 2; }
  int GetCanvasHeight() { return Config.ScrewYMax - Config.ScrewYMin + Config.CanvasMargin * 2; }
  Dot GetCanvasPos(Dot dot) { return new Dot(dot.x - Config.ScrewXMin + Config.CanvasMargin, dot.y - Config.ScrewYMin + Config.CanvasMargin); }
}

class Dot {
  int x, y;
  Dot (int _x, int _y) {
    x = _x;
    y = _y;
  }
  Dot () {}
  void fromJSONObject(JSONObject obj) {
    this.x = obj.getInt("x");
    this.y = obj.getInt("y");
  }

  @Override
  String toString() {
    return String.format("Dot (%d %d)", this.x, this.y);
  }
}

class Pair <T1, T2> {
  T1 first;
  T2 second;
  Pair (T1 _first, T2 _second) {
    first = _first;
    second = _second;
  }
}

class Case {
  LinkedList<Dot> screws, weaks;
  LinkedList<LinkedList<Dot>> conns;
  int level;
  Case(LinkedList<Dot> _screws, LinkedList<Dot> _weaks, LinkedList<LinkedList<Dot>> _conns, int _level) {
    screws = _screws;
    weaks = _weaks;
    conns = _conns;
    level = _level;
  }

  /*
  @Override
  String toString() {
    String buf = "";
    String screws = "screws: " + String.join(", ", this.screws);
    String weaks = "weaks: " + String.join(", ", this.weaks);
    LinkedList<String> connsBuf = new LinkedList();
    for (LinkedList<Dot> eachRow : this.conns) {
      connsBuf.add(String.join(", ", eachRow));
    }
    String conns = "conns: \n" + String.join("\n", connsBuf);
  }*/
}

// Define global variables

ConfigUtil cu = new ConfigUtil();
Case gets;

/*
  {
    "screws": [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 4}],
    "weaks": [{"x": 1, "y": 2}, {"x": 2, "y": 3}, {"x": 3, "y": 4}],
    "conns": [
      [
        {"x": -1, "y": -2}, {"x": -3, "y": -4}, {"x": 1, "y": 2}, {"x": 3, "y": 4}
      ],
      [
        {"x": 3, "y": 4}, {"x": 3, "y": 4}
      ]
    ],
    "level": 0
  }
*/

Case load() {
  JSONObject json = loadJSONObject("input.json");

  JSONArray _screws = json.getJSONArray("screws");
  LinkedList<Dot> screws = new LinkedList<Dot>();
  for (int i = 0; i < _screws.size(); i++) {
    Dot _new = new Dot();
    _new.fromJSONObject(_screws.getJSONObject(i));
    screws.add(_new);
  }

  JSONArray _weaks = json.getJSONArray("weaks");
  LinkedList<Dot> weaks = new LinkedList<Dot>();
  for (int i = 0; i < _weaks.size(); i++) {
    Dot _new = new Dot();
    _new.fromJSONObject(_weaks.getJSONObject(i));
    weaks.add(_new);
  }

  JSONArray _conns = json.getJSONArray("conns");
  LinkedList<LinkedList<Dot>> conns = new LinkedList();
  for (int i = 0; i < _conns.size(); i++) {
    LinkedList<Dot> eachLevel = new LinkedList();
    JSONArray _eachLevel = _conns.getJSONArray(i);
    for (int j = 0; j < _eachLevel.size(); j++) {
      Dot each = new Dot();
      each.fromJSONObject(_eachLevel.getJSONObject(j));
      eachLevel.add(each);
    }
    conns.add(eachLevel);
  }

  int level = json.getInt("level");

  Case _new = new Case(screws, weaks, conns, level);
  return _new;
}

void _drawScrew(Dot dot) { circle(dot.x, dot.y, Config.ScrewSize); }
void drawScrew(Dot dot) {
  fill(Config.ColorScrew);
  noStroke();
  _drawScrew(dot);
  fill(Config.ColorDefault);
  stroke(Config.ColorDefault);
}
void _drawWeak(Dot dot) { circle(dot.x, dot.y, Config.WeakSize); }
void drawWeak(Dot dot) {
  fill(Config.ColorWeak);
  noStroke();
  _drawWeak(dot);
  fill(Config.ColorDefault);
  stroke(Config.ColorDefault);
}
void _drawConn(Pair<Dot, Dot> conn) { line(conn.first.x, conn.first.y, conn.second.x, conn.second.y); }
void drawConn(Pair<Dot, Dot> conn) {
  strokeWeight(Config.ConnStrokeWeight);
  _drawConn(conn);
}
void _drawPolygon(LinkedList<Dot> component) {
  beginShape();
  for (Dot _each: component) {
    Dot each = cu.GetCanvasPos(_each);
    vertex(each.x, each.y);
  }
  endShape(CLOSE);
}
void drawPolygon(LinkedList<Dot> component, int fill, int stroke) {
  if (fill != -1) {
    fill(fill);
  } else {
    noFill();
  }
  if (fill != -1) {
    stroke(stroke);
  } else {
    stroke(Config.ColorDefault);
  }
  _drawPolygon(component);
  fill(Config.ColorDefault);
  stroke(Config.ColorDefault);
}
void drawDotComponents() {
  for (Dot _screw: gets.screws) {
    Dot screw = cu.GetCanvasPos(_screw);
    drawScrew(screw);
  }
  for (Dot _weak: gets.weaks) {
    Dot weak = cu.GetCanvasPos(_weak);
    drawWeak(weak);
  }
}

void drawEveryHull() {
  noFill();
  stroke(Config.ColorBlack);

  if (gets.level < 0) {
    noFill();
  } else if (gets.level == 0) {
    background(Config.ColorBlue);
    fill(Config.ColorBlue);
  } else {
    background(Config.ColorBlue);
    fill(Config.ColorBlue);
  }
  rect(Config.CanvasMargin, Config.CanvasMargin, Config.ScrewXMax - Config.ScrewXMin, Config.ScrewYMax - Config.ScrewYMin);

  // Screw: connections
  for (int i = 0; i < gets.conns.size(); i++) {
    if (gets.level < i + 1) {
      fill(Config.ColorBackground);
    } else if (gets.level == i + 1) {
      fill(Config.ColorGreen);
    } else {
      fill(Config.ColorBlue);
    }
    _drawPolygon(gets.conns.get(i));
  }
}

void settings() {
  size(cu.GetCanvasWidth(), cu.GetCanvasHeight());
}

void setup() {
  gets = load();
  noLoop();
  strokeWeight(Config.StrokeWeight);
  background(Config.ColorDefault);

  /* draw */
  drawEveryHull();
  drawDotComponents();

  /* save */
  save("output.png");
  exit();
}
