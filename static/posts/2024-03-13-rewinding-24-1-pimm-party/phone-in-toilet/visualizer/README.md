# Phone in Toilet Visualizer

## Requirements
* Processing
* Python
* xvfb

## Getting Started
### Install Requirements
* [Install Processing](https://gist.github.com/utamadonny/3d07d716d760ff6077275b3143995eff)
* Install xvfb
  ```sh
  apt-get install xvfb
  ```

## Transform input to json
```
cat in.in | python solution.py && mv input.json ./Render
```

## Run image builder
```sh
proc_java_path=<processing-java>
xvfb-run $proc_java_path  --sketch=Render --output=Output --force --run
```

## More Information

### Apply injection code to other solution
Get more detail, refer [`injection.py`](./injection.py)
