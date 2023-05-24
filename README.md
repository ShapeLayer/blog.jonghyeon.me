blog.jonghyeon.me
---

[![pages-build-deployment](https://github.com/ShapeLayer/blog.jonghyeon.me/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ShapeLayer/blog.jonghyeon.me/actions/workflows/pages/pages-build-deployment)  

박종현 개인 블로그 아티클 리포지토리

이 리포지토리는 블로그 컨텐츠 부분만 포함하고 있습니다. 블로그 테마와 레이아웃 정의 파일은 이 리포지토리에서 확인할 수 없습니다.  

## 배포
하지만 [blog.jonghyeon.me](https://blog.jonghyeon.me)는 이 리포지토리의 Pages 설정에 따라 동작하고 있습니다. [테마 정의를 다른 리포지토리에 분리](./tools.conf)하고, Github Actions를 사용하여 병합 후 [`deploy`](https://github.com/ShapeLayer/blog.jonghyeon.me/tree/deploy) 브랜치에 게시합니다.  

Github Actions가 수행하는 일부 과정은 [`tools`](./tools/) 디렉토리 하위에 셸 스크립트로 정의하여 해당 디렉토리를 참조하여 확인할 수 있습니다.  
