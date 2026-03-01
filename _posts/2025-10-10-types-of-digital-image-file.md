---
layout: post
title: 디지털 화상 파일의 형식
date: 2025-10-10
category: [image-processing]
---

_〈화상정보처리〉 수업 노트_

현실 세계의 영상은 현실 세계의 아날로그 영상을 양자화, 표본화하여 디지털 화상으로서 컴퓨터 시스템에 저장한다. 이들 디지털 화상은 정지화상, 동화상 뿐 아니라, 어안렌즈로 촬영한 360도 화상, 3D 화상 등, 최근 사례로는 애플에서 비전 프로에 대응해 공간 사진과 공간 비디오 촬영을 아이폰에 추가하는 등의 특수한 화상도 있다. 이러한 디지털 화상은 다양한 형식으로 저장되며, 각 형식은 특정한 용도와 특성을 가지고 있다.

이러한 디지털 화상 파일의 형식은 크게 래스터 이미지 파일, 벡터 이미지 파일로 구분되고, 그 외에 이들을 복합적으로 사용하거나 한다.  

## 래스터 화상 포맷

래스터 형식은 대개 사진을 촬영한 결과로서 획득할 수 있다. 사진 파일 형식으로 대표되는 JPEG를 포함해 PNG, GIF, BMP 등이 있다. 

래스터 화상은 픽셀 단위로 저장되며, 각 픽셀은 색상과 밝기 정보를 포함한다. 래스터 화상은 고해상도에서 세밀한 디테일을 표현할 수 있지만, 확대하면 픽셀이 보이는 단점이 있다.

JPEG/JFIF, JPEG 2000, Exif, TIFF, GIF, BMP, PNG, PPM, PGM, PBM, PNM, WebP, HEIF, BAT, BPG DEEP, DRW, ECW, FITS, FLIF, ICO, ILBM, IMG, JPEG XR, Nrrd, PAM, PCX, PGF, PLBM, SGI, SID, Sun Raster, TGA(TARGA), VICAR, XISF, AFPhoto, CD5, CPT, KRA, MDP, PDN, PSD, PSP, SAI, XCF

## 벡터 화상 포맷

벡터 형식은 수학적 표현을 사용하여 선, 곡선, 도형 등을 정의한다. 벡터 화상은 확대해도 품질이 유지되며, 주로 로고, 아이콘, 일러스트레이션 등에 사용된다. 대표적인 벡터 화상 파일 형식으로는 SVG, AI, EPS 등이 있다.

<br />

2D 벡터 화상 포맷

CGM, Gerber format (RS-274X), SVG, AFDesign, AI, CDR, DrawingML, Graphics Layout Engine, HPGL, HVIF, MathML, NAPLPS, ODG, !DRAW, PGML, PSTricks, PGF/TikZ, QCC, ReGIS, VML, Xar, XPS

<br />

3D 벡터 화상 포맷

AMF, Asymptote, Blender, COLLADA, DGN, DWF, DWG, DXF, eDrawings, flt, FVRML, HSF, IGES, IMML, IPA, JT, MA, MB, Wavefront, OpenGEX, PLY, SDL, PRC, STEP, SKP, STL, U3D, VRML,
XAML, XGL, XVL, xVRML, X3D, 3D, 3DF, 3DM, 3DS, 3DXML, X3D

## 동화상 포맷

동화상은 시간에 따른 연속적인 프레임으로 구성된 화상으로, 비디오 파일 형식으로 대표되는 MP4, AVI, MOV 등이 있다. 동화상은 래스터 화상과 벡터 화상을 모두 포함할 수 있으며, 오디오 트랙도 포함할 수 있다. 동화상은 영화, 애니메이션, 게임 등에서 널리 사용된다.

WebM, Matroska, FLV, F4V, Vob, Ogg, Dirac, Animation GIF, gifv, Multiple-image Network Graphics, AVI, MPEG, QuickTime, Windows Media Video, RealMedia, AMV, MKV, M4V, SVI, 3GPP, MXF, ROQ, Nullsoft Streaming Video, FLV

## 정지화상 파일형식의 스펙

각 정지화상 파일 형식마다 그 사양과 구현, 표준이 모두 상이하다. 현대에 이르러서는 사실상 표준으로 자리잡은 몇 개의 파일 형식이 존재하지만, 각 포맷마다 의도된 사용처와 배경, 또 이에 따라 기술적인 특성이 다르다.  

정지 화상 포맷의 선택에 있어서, 실존하는 모든 화상 파일 형식을 두고 포맷을 한 개 선택해야한다면, 몇 가지 기준을 세울 수 있다.

1. 전용 소프트웨어 유무
2. 이용가능 색상의 수
3. 화질의 손실 정도
4. 압축 방식과 압축률
5. 용도
6. 확장기능

### 전용 소프트웨어의 유무

모든 화상 포맷은 그 데이터를 읽고 화면에 렌더링하는 소프트웨어가 필요하다. 생소한 많은 포맷은 특정한 소프트웨어 전용으로 설계된 바이너리 형식이다. 이 소프트웨어가 운영체제 단계에서 특별한 목적으로 구현된 경우, 대표적으로 애플의 HEIF 포맷의 경우에는 다른 운영체제에서 파일을 사용하는 것에 있어 대책이 요구된다.  

이들 전용 포맷을 렌더하여 표시하는 소프트웨어, 더 나아가 이들 화상을 편집하려면 소위 "포토샵"으로 대표되는 화상 편집 소프트웨어가 이들 포맷을 지원하는지도 확인해야할 수 있다. 만약 이들 소프트웨어가 지원하지 않는 포맷이라면, 이들 형식을 다른 형식으로 변환하는 소프트웨어가 존재하는지 확인, 이들 소프트웨어가 지원하는 포맷으로 변환하여 사용하는 방법도 고려할 수 있다.  

### 이용가능 색상의 수

화상 파일은 형식마다 표현 가능한 색상의 수가 다르다. 대개는 역사적인 배경에 의해 표현 가능한 색상의 수가 결정딘다.  

일반적인 화상 파일은 다차원 값을 사용하여 색상 정보를 표현한다. 이들 값을 각 차원(채널)별로 분리하여 획득한 값을, 그레이스케일 화상으로 렌더링할 수 있다. 이들 각 차원이 표현하는 값은 각 차원이 표현하는 색상의 밝기이다.  

그레이스케일 표현에서, 1비트로 두 가지 색상만 표현하는 PBM 포맷을 제외하고는, 대개 8비트의 256단계 밝기, 혹은 16비트의 65,536단계 밝기를 표현한다. 16비트 그레이스케일을 지원하는 포맷으로는 PNG, TIFF, DICOM 등이 있으며, 의료 영상 등 고정밀 계조가 요구되는 용도에 사용된다.

컬러 표현에서는, 많은 사례에서 RGB 컬러 모델을 사용하여 화상을 표현한다. GIF, PNG 등 일부 포맷은 팔레트 방식을 채택하여 최대 256색(8비트)으로 색상을 표현한다. 반면 TIFF, BMP, JPEG 등은 RGB 각 채널에 8비트를 할당하여 총 24비트로 16,777,216가지 색상을 표현할 수 있다. 24비트로 각 채널을 표현하는 경우, 총 48비트로 281,474,976,710,656가지 색상을 표현할 수 있다.

### 화질과 압축률

화상 파일 포맷은 화질의 손실 여부에 따라 비가역 압축(lossy)과 가역 압축(lossless)으로 구분된다.

비가역 압축은 압축 과정에서 인지하기 어려운 정보를 제거하여 파일 크기를 줄이는 방식이다. 화질 열화를 어느 정도 허용하는 대신 높은 압축률을 실현한다. JPEG가 대표적인데, 압축률을 높일수록 블록 노이즈나 모스키토 노이즈가 발생한다. 이산 코사인 변환(DCT)과 허프만 부호화를 조합하여 압축한다.

![](/static/posts/2025-10-10-types-of-digital-image-file/rle-encoding.png)

가역 압축은 압축 전후의 화질이 완전히 동일하게 유지된다. JPEG를 제외한 대부분의 포맷이 가역 압축을 채택하고 있다. 압축률은 비가역 압축에 비해 낮지만, 화질 열화 없이 원본 데이터를 복원할 수 있다. 런 렝스 부호화나 허프만 부호화 등을 적용하여 압축한다.

그 외에 PBM, PGM, PPM, BIP, BSQ, BIL 등 무압축 형식은 화소값을 그대로 저장하여 화질 손실이 없지만, 파일 크기가 매우 크다.

## 주요 파일 형식

### 범용 파일 형식 (RAW)

헤더 등의 주변 정보 없이 화상 데이터만을 저장하는 형식이다. 바이너리 파일 또는 텍스트 파일로 저장된다. 세로·가로 픽셀 수나 양자화 비트 수 등의 정보가 포함된 헤더가 없는 경우가 대부분이므로, 파일을 개봉할 때 이들 파라미터를 별도로 지정해야 한다. 파라미터를 잘못 지정하면 화상이 올바르게 표시되지 않는다.

### PNM 형식 (PBM / PGM / PPM)

PNM(Portable aNyMap)은 UNIX에서 오랫동안 표준적으로 사용되어 온 화상 형식이다. PBM(Portable BitMap, 2값 화상), PGM(Portable GrayMap, 그레이스케일 화상), PPM(Portable PixMap, 컬러 화상)의 세 종류로 구성된다.

기본 구조는 공통으로, 파일 형식 식별자, 열 수, 행 수, 화소 휘도 최대값, 화소 휘도값의 순으로 공백(스페이스, 탭, 캐리지 리턴, 라인 피드 포함)으로 구분되어 기술된다. PBM 형식에서는 화소 휘도 최대값이 1로 고정되고 이 값은 생략된다. `#` 이후 행 끝까지는 주석으로 무시되며, 1행은 70자를 초과하지 않는다. 

각 포맷은 파일 형식 식별자로 구별된다.

| 형식 | 식별자 (ASCII) | 식별자 (바이너리) | 내용 |
| :-: | :-: | :-: | :-: |
| PBM  | P1 | P4 | 2값 화상 |
| PGM  | P2 | P5 | 그레이스케일 화상 |
| PPM  | P3 | P6 | 컬러 화상 |

### BMP 형식

Windows 초기부터의 표준적인 정지 화상 형식이다.  

BMP는 파일 헤더, 비트맵 헤더, 컬러 맵, 비트맵 데이터의 네 부분으로 구성된다. 비트맵 데이터부는 RLE(런 렝스) 압축을 지원한다. RLE 압축은 색 심도가 4비트 또는 8비트인 경우에 이용된다.

<style>
  table, th, td {
    text-align: center;
  }
</style>

<table>
  <tbody>
    <tr>
      <th>BMP 파일 헤더</th>
      <td>
        <ul>
          <li>파일 식별자(2 bytes): <code>BM</code>고정</li>
          <li>파일 사이즈(4 bytes): [byte]</li>
          <li>확장용 예비 영역(2 bytes): <code>0</code>고정</li>
          <li>확장용 예비 영역(2 bytes): <code>0</code>고정</li>
          <li>비트 이미지 데이터 개시 위치(4 bytes): [byte]</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>BMP 인포 헤더</th>
      <td>
        화상 가로폭, 화상 높이, 비트 심도, 압축 플래그, 팔레트 색수 등...
        <ul>
          <li>비트맵 헤더 사이즈(4 bytes): [byte] (<code>40</code>고정)</li>
          <li>칼럼 사이즈(4 bytes): [pixel]</li>
          <li>라인 사이즈(4 bytes): [pixel]</li>
          <li>이미지 플레인 사이즈(2 bytes) (<code>1</code>고정)</li>
          <li>색 심도(2 bytes): [bit], 1, 4, 8, 24 중 어느 것인가</li>
          <li>압축 형식 식별자(4 bytes)</li>
          <li>압축 이미지 사이즈(4 bytes): [byte]</li>
          <li>수평 해상도(4 bytes): [pixel/m]</li>
          <li>수직 해상도(4 bytes): [pixel/m]</li>
          <li>사용 색수(4 bytes): [색]</li>
          <li>필수 색수(4 bytes): [색]</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>컬러 테이블 (팔레트)</th>
      <td>
        색1, 색2, 색3, 색4, 색5, 색6, ...
      </td>
    </tr>
    <tr>
      <th>픽셀</th>
      <td>
        B G R B G R B G R B G R ...
      </td>
    </tr>
  </tbody>
</table>

RLE 압축이 적용되지 않은 경우, 1픽셀당 색 심도값에 상당하는 크기로 휘도값이 표현된다. 색 심도가 24비트인 경우 BGR 순서로 휘도값 그 자체를, 그 외의 경우 해당 픽셀의 색에 대응하는 컬러 맵 번호가 저장된다.

### GIF 형식

GIF(Graphics Interchange Format)는 미국의 대형 PC통신 서비스였던 CompuServe에서 화상 파일 교환을 위해 표준화된 화상 포맷이다. 최대 256색의 컬러 화상을 지원하며, 투과 표시, 인터레이스, 애니메이션 등 인터넷 이용에 특화된 기능을 갖추고 있다.

1985년에 GIF의 화상 데이터 압축 방식(LZW법)에 대해 Unisys사가 특허를 취득함으로써, 라이센스를 취득하지 않은 소프트웨어로 작성한 GIF 화상이 위법이 된 시기가 있었다. 미국에서는 2003년 6월 20일, 일본에서는 2004년 6월 20일에 특허 보유권이 만료되어 현재는 자유롭게 이용할 수 있다.

GIF 파일은 헤더, 글로벌 컬러 테이블, 각 프레임에 대한 그래픽 제어 확장과 이미지 블록, 트레일러로 구성된다. 

<table>
  <tbody>
    <tr>
      <th>GIF 헤더</th>
      <td>
        <ul>
          <li>Signature: <code>GIF</code></li>
          <li>Version: <code>89a</code></li>
          <li>Logical Screen Width / Height</li>
          <li>Global Color Table Flag / Size</li>
          <li>Delay Time (애니메이션 지연)</li>
          <li>Transparent Color Index (투과색)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>Global Color Table</th>
      <td>
        <ul>
          <li>[0] = <code>#ff0000</code></li>
          <li>[1] = <code>#00ff00</code></li>
          <li>[2] = <code>#0000ff</code></li>
          <li>[3] = <code>#000000</code></li>
          <li>[4] = <code>#000000</code></li>
          <li>[5] = <code>#000000</code></li>
          <li>[6] = <code>#000000</code></li>
          <li>...</li>
          <li>[253] = <code>#000000</code></li>
          <li>[254] = <code>#000000</code></li>
          <li>[255] = <code>#000000</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>Application Extension Block</th>
      <td>
        <ul>
          <li>Extension Introducer = <code>0x21</code></li>
          <li>Extension Label = <code>0xff</code></li>
          <li>Block Size = <code>0xb</code></li>
          <li>Application Identifier = <code>NETSCAPE</code></li>
          <li>Application Authentication Code = <code>2.0</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>Graphic Control Extension Block</th>
      <td>
        <ul>
          <li>Extension Introducer = 0x21</li>
          <li>Graphic Control Label = 0xf9</li>
          <li>Block Size = 4 // 이 블록의 크기</li>
          <li>Disposal Method</li>
          <li>User Input Flag</li>
          <li>Transparent Color Flag</li>
          <li>Delay Time</li>
          <li>Transparent Color Index // 투과색번호</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>Image Block</th>
      <td>
        <ul>
          <li>Image Separetor = 0x2c</li>
          <li>Image Left Position</li>
          <li>Image Top Position</li>
          <li>Image Width</li>
          <li>Image Height</li>
          <li>Local Color Table Flag</li>
          <li>Interlace Flag</li>
          <li>Sort Flag</li>
          <li>Size of Local Color Table</li>
        </ul>
        *이 이후에 로컬 컬러 테이블이나 화상 데이터의 서브블록이 이어진다
      </td>
    </tr>
    <tr>
      <th>Graphic Control Extension Block</th>
      <td>...</td>
    </tr>
    <tr>
      <th>Image Block</th>
      <td>...</td>
    </tr>
    <tr>
      <th>Graphic Control Extension Block</th>
      <td>...</td>
    </tr>
    <tr>
      <td colspan="2">...</td>
    </tr>
    <tr>
      <th>Trailer</th>
      <td></td>
    </tr>
  </tbody>
</table>

### PNG 형식

PNG(Portable Network Graphics)는 zip 등에도 이용되는 Deflate 압축 알고리즘을 채택한 가역 압축 화상 파일 포맷이다. 1996년에 특허 문제로 이용이 제한되었던 GIF의 대체로 등장하였다. 인터넷 환경을 전제로 한 기능과 16비트 그레이스케일, 풀컬러 화상 등 GIF에서 지원하지 못한 폭넓은 사양을 갖추고 있다.  

투과에 대해서는 크로마키에 의한 지정 외에 8비트에서 16비트의 알파 채널을 지원하여 복수 색상의 투과 및 반투명 표현도 가능하다. 표준으로는 애니메이션 기능을 지원하지 않지만, PNG의 발전 포맷인 MNG/APNG 형식을 사용해 애니메이션을 구현할 수 있다.  

PNG 파일은 8바이트의 시그니처로 시작한다. 그 뒤에 청크(chunk) 단위로 데이터가 이어진다.


<table>
  <tbody>
    <tr>
      <th>PNG 시그니쳐</th>
      <td>
        <code>89 50 4E 47 0D 0A 1A 0A</code>
      </td>
    </tr>
    <tr>
      <th>IHDR<br /><small>(이미지 헤더)</small></th>
      <td>
        <table>
          <tbody>
            <tr>
              <th>화상 폭</th>
              <th>화상 높이</th>
              <th>비트 심도</th>
              <th>컬러 타입</th>
              <th>압축 방식</th>
              <th>필터 방식</th>
              <th>인터레이스 방식</th>
            </tr>
            <tr>
              <td>4 bytes</td>
              <td>4 bytes</td>
              <td>1 byte</td>
              <td>1 byte</td>
              <td>1 byte</td>
              <td>1 byte</td>
              <td>1 byte</td>
            </tr>
          </tbody>
        </table>
        <ul>
          <li>
            컬러 타입
            <ul>
              <li>0: 그레이스케일</li>
              <li>2: RGB</li>
              <li>3: 팔레트</li>
              <li>4: 그레이스케일 + 알파</li>
              <li>6: RGB + 알파</li>
            </ul>
          </li>
          <li>압축 방식: 0 (Deflate)</li>
          <li>필터 방식: 0 (Adaptive filtering with five basic filter types)</li>
          <li>인터레이스 방식: 0 (No interlace), 1 (Adam7 interlace)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2"><em>← 보조/부가 청크 삽입 가능 (cHRM, gAMA, sBIT, sRGB, iCCP, ...)</em></td>
    </tr>
    <tr>
      <th>PLTE<br /><small>(팔레트)</small></th>
      <td>
        컬러 타입 3(팔레트)일 때 필수, 2·6일 때 선택적으로 포함.<br />
        RGB 값 3 bytes × 1~256개의 팔레트 항목으로 구성된다.
      </td>
    </tr>
    <tr>
      <td colspan="2"><em>← 보조/부가 청크 삽입 가능 (bKGD, hIST, tRNS, pHYs, sPLT, ...)</em></td>
    </tr>
    <tr>
      <th>IDAT<br /><small>(이미지 데이터)</small></th>
      <td>
        Deflate 압축된 실제 화소 데이터. 여러 개의 IDAT 청크로 분할하여 저장할 수 있다.<br />
        각 청크는 공통 구조를 가진다:
        <table>
          <tbody>
            <tr>
              <th>데이터 길이</th>
              <th>청크 타입</th>
              <th>데이터</th>
              <th>CRC</th>
            </tr>
            <tr>
              <td>4 bytes</td>
              <td>4 bytes</td>
              <td>(데이터 길이) bytes</td>
              <td>4 bytes</td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
    <tr>
      <td colspan="2"><em>← 보조/부가 청크 삽입 가능 (tIME, tEXt, zTXt, iTXt, ...)</em></td>
    </tr>
    <tr>
      <th>IEND<br /><small>(종단 청크)</small></th>
      <td>파일의 끝을 나타낸다. 데이터 없음.</td>
    </tr>
  </tbody>
</table>

PNG 청크는 필수 청크(IHDR, PLTE, IDAT, IEND) 외에, 보조 청크와 부가 청크로 구성된다.

**보조 청크 (補助チャンク)**

보조 청크는 표준 PNG 명세에 정의된 선택적 청크다. 위치에 따라 세 그룹으로 구분된다.

| 청크 | 설명 | 위치 |
| :--: | :-- | :-- |
| `cHRM` | 기본 색도와 백색점 (Chromaticities and white point) | PLTE·IDAT 이전 |
| `gAMA` | 이미지 감마 (Image gamma) | PLTE·IDAT 이전 |
| `sBIT` | 유효 비트 수 (Significant bits) | PLTE·IDAT 이전 |
| `sRGB` | 표준 RGB 색 공간 (Standard RGB colour space) | PLTE·IDAT 이전 |
| `iCCP` | 내장 ICC 프로파일 (Embedded ICC profile) | PLTE·IDAT 이전 |
| `bKGD` | 배경색 (Background colour) | PLTE~IDAT 사이 |
| `hIST` | 이미지 히스토그램 (Image histogram) | PLTE~IDAT 사이 |
| `tRNS` | 투과 (Transparency) | PLTE~IDAT 사이 |
| `pHYs` | 물리적 픽셀 크기 (Physical pixel dimensions) | PLTE~IDAT 사이 |
| `sPLT` | 권장 팔레트 (Suggested palette) | PLTE~IDAT 사이 |
| `tIME` | 이미지 최종 수정 시각 (Image last-modification time) | 어디에나 가능 |
| `tEXt` | 텍스트 데이터 (Textual data) | 어디에나 가능 |
| `zTXt` | 압축 텍스트 데이터 (Compressed textual data) | 어디에나 가능 |
| `iTXt` | 국제 텍스트 데이터 (International textual data) | 어디에나 가능 |

**부가 청크 (付加チャンク)**

부가 청크는 PNG 명세 외부에서 정의된 확장 청크이다.

| 청크 | 설명 | 위치 |
| :--: | :-- | :-- |
| `oFFs` | 이미지 오프셋 (Image offset) | IDAT 이전 |
| `pCAL` | 픽셀값 캘리브레이션 (Calibration of pixel values) | IDAT 이전 |
| `sCAL` | 이미지 물리 크기 (Physical scale of image subject) | IDAT 이전 |
| `gIFg` | GIF 그래픽 제어 확장 (GIF Graphic Control Extension) | 어디에나 가능 |
| `gIFt` | GIF 플레인 텍스트 확장 (GIF Plain Text Extension) | 어디에나 가능 |
| `gIFx` | GIF 응용 확장 (GIF Application Extension) | 어디에나 가능 |
| `fRAc` | 프랙탈 이미지 파라미터 (Fractal image parameters) | 어디에나 가능 |

### JPEG 형식

JPEG(Joint Photographic Experts Group)는 정지화상 디지털 데이터를 압축하는 방식 중 하나로, 이를 책정한 조직(ISO/IEC JTC 1/SC 29/WG 1)의 약칭이기도 하다. 일반적으로 비가역 압축 화상 포맷으로 알려져 있으며, 사진 등 색상이 연속적으로 변화하는 화상의 압축에 적합하다. 가역 압축 방식도 규격상 정의되어 있으나, 특허 등의 이유로 거의 이용되지 않는다.

표준으로는 특정 파일 포맷이 규정되어 있지 않으며, JFIF 형식이 사실상 표준 파일 포맷이 되고 있다. JPEG 파일은 `FFD8`로 시작하고 `FFD9`로 끝나는 마커 구조로 이루어져 있다.

**JFIF 형식**: JFIF(JPEG File Interchange Format)는 JPEG 방식으로 압축된 화상 데이터에 화상 정보 등을 부가하여 파일에 저장하기 위해 C-Cube Microsystems사가 제창한 표준 포맷이다. 단순히 "JPEG 파일"이라고 할 경우 대부분 JFIF 형식의 파일을 의미한다.

**Exif 형식**: Exif(Exchangeable Image File Format)는 1994년에 후지필름이 제창한 디지털 카메라용 화상 파일 규격이다. JEIDA에 의해 표준화되어 각 사의 디지털 카메라에 채용되고 있다. TIFF 형식으로 화상에 관한 정보나 촬영 일시 등의 부가 정보를 기록할 수 있으며, 섬네일 이미지도 기록할 수 있다. 화상 형식은 RGB 무압축 방식이나 JPEG 방식 등 복수의 형식을 지원한다.

### TIFF 형식

TIFF(Tag Image File Format)는 래스터 그래픽이나 화상 정보의 저장에 사용하는 파일 형식이다. 가역 압축 방식이므로 비교적 파일 크기가 크지만 화질이 열화되지 않는다. 레이어 등의 화상 정보나 데이터를 추가로 태그 부여할 수 있으며, 복소수 데이터, GeoTIFF, 16비트 TIFF 등으로의 확장이 가능하다.

파일은 IFD(Image File Directory) 엔트리로 구성된다. 각 IFD 엔트리는 태그(2 bytes), 타입(2 bytes), 값(4 bytes), 오프셋(4 bytes)으로 이루어져 있다.

### SVG 형식

SVG(Scalable Vector Graphics)는 1998년에 PGML과 VML을 기반으로 개발된 벡터 형식의 화상 포맷이다. 벡터 형식이므로 확대·축소가 자유로우며 화질 열화가 없다. XML 기반이므로 HTML, JavaScript, 웹 페이지와의 친화성이 높아 현대 웹에서 광범위하게 사용된다.
