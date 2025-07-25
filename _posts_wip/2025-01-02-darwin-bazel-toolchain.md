---
layout: post
title: Bazel로 C/C++ 빌드 시 ccache, libtool로부터 오류가 발생될 때 해결 (invalid option -- U, you must specify a MODE)
date: '2025-01-02'
categories: [trouble-shooting]
tags: [trouble-shooting, bazel, c-cpp]
---

## 배경
맥 OS 환경에서 Bazel로 C/C++ 코드를 빌드하면 ccache 혹은 libtool로부터 오류가 발생합니다.  

ccache에 의해 발생하는 경우
```
Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
ccache: invalid option -- U
Target (대상 이름) failed to build
Use --verbose_failures to see the command lines of failed build steps.
```

libtool에 의해 발생하는 경우
```
Use --sandbox_debug to see verbose messages from the sandbox and retain the sandbox build root for debugging
libtool:   error: you must specify a MODE
Usage: /opt/homebrew/opt/libtool/libexec/gnubin/libtool [OPTION]... [MODE-ARG]...
Try 'libtool --help' for more information.
Target (대상 이름) failed to build
Use --verbose_failures to see the command lines of failed build steps.
```

## 상세
Bazel은 C/C++ 코드를 컴파일하는 과정에서 `CC`, `CXX`, `libtool`을 호출합니다. `CC`는 C 컴파일러, `CXX`는 C++ 컴파일러를 호출할 수 있어야 합니다.

### ccache
하지만 homebrew를 이용해 ccache를 의존성으로 갖는 패키지를 설치하는 경우, `CC`는 homebrew 패키지 디렉토리 내의 ccache를 호출할 수 있습니다.  

다시 말해 ccache에 의해 발생하는 오류는 c 컴파일러를 실행해야 하는 상황에서, c 컴파일러가 아닌 ccache를 호출하여 발생합니다. 따라서 아래와 같이 `CC`에 대해 앨리어스를 지정하거나, PATH를 명확하게 설정하여야 합니다.  

```zsh
alias CC=~
```

### libtool
libtool은 Xcode 툴체인에 포함된 것과 homebrew에 의해 설치되는 것이 다릅니다. 

```
❯ /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool: no output file specified (specify with -o output)
Usage: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool -static [-] file [...] [-filelist listfile[,dirname]] [-arch_only arch] [-sacLT] [-no_warning_for_no_symbols]
Usage: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool -dynamic [-] file [...] [-filelist listfile[,dirname]] [-arch_only arch] [-o output] [-install_name name] [-compatibility_version #] [-current_version #] [-seg1addr 0x#] [-segs_read_only_addr 0x#] [-segs_read_write_addr 0x#] [-seg_addr_table <filename>] [-seg_addr_table_filename <file_system_path>] [-all_load] [-noall_load]
```
```
❯ /opt/homebrew/opt/libtool/libexec/gnubin/libtool
Usage: /opt/homebrew/opt/libtool/libexec/gnubin/libtool [OPTION]... [MODE-ARG]...
Try 'libtool --help' for more information.
libtool:   error: you must specify a MODE
```

homebrew로 설치할 수 있는 libtool은 GNU Libtool이나, Xcode 툴체인 libtool은 10년 전이 마지막 커밋인 [opensource-apple/cctools 내의 libtool](https://github.com/opensource-apple/cctools/blob/master/misc/libtool.c)의 최신 버전, 혹은 10년 전 커밋의 빌드인 것으로 보입니다.  

Bazel은 Xcode 툴체인 libtool에 맞춰 명령줄 구문을 생성하고, 생성된 구문은 GNU Libtool과 호환되지 않습니다.  

따라서 ccache의 경우와 같이 Xcode 툴체인 libtool을 호출할 수 있도록 지정해야합니다.  

```zsh
alias CC=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool
```

### ~/.bazelrc
결과적으로 위 두 오류는 homebrew를 사용하는 모든 맥 OS 환경에서 잠재적으로 발생할 수 있습니다.  

하지만 homebrew를 통해 설치한 ccache와 libtool을 사용해야할 수도 있으므로 위와 같이 앨리어스를 지정하기보다 Bazel이 사용할 도구의 경로를 따로 설정하는 편이 더 낫습니다.  

마치 `.bashrc`, `.zprofile`처럼 `~/` 위치에 `.bazelrc` 파일을 생성함으로서 Bazel을 설정할 수 있습니다.
```sh
❯ cat ~/.bazelrc
build --action_env CC=/opt/homebrew/opt/llvm/bin/clang
build --action_env CXX=/opt/homebrew/opt/llvm/bin/clang++
# build --action_env CC=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang
# build --action_env CXX=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++
build --action_env=LIBTOOL=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool
test --action_env=LIBTOOL=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/libtool
```

## 별첨
- [`bazelbuild/bazel` ccache: invalid option -- U #24795](https://github.com/bazelbuild/bazel/issues/24795)
- [`ShapeLayer/dotfiles` - `/bazel/.bazelrc.darwin`](https://github.com/ShapeLayer/dotfiles/blob/main/bazel/.bazelrc.darwin)
