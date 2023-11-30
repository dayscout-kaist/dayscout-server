# Dayscout Server

![GitHub Pipenv locked Python version (main)][badge/python-version]
[![Code style: black][badge/black]][repo/black]
[![Imports: isort][badge/isort]][isort]
[![pre-commit][badge/pre-commit]][repo/pre-commit]
[![Conventional Commits][badge/conventional-commits]][conventional-commits]

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/1a473e01-f310-496d-95cd-35def5e739a4/e3dff3cc-619e-449a-9a92-a9c33439609c/Untitled.svg)

**DayScout**은 1형 당뇨병 환자들을 위해 영양 정보를 단순화하고 표준화하는 혁신적인 솔루션입니다. 이 앱은 사용자들이 영양 성분을 쉽게 이해하고 계산할 수 있도록 하는 것에 중점을 둡니다.

## **팀 소개**

- 최우정 (팀장) - KAIST 화학과 21학번
- 권순호 - KAIST 전산학부 22학번
- 김건 - KAIST 전산학부 19학번
- 박병찬 - KAIST 전산학부 21학번
- 정재모 - KAIST 전산학부 20학번
- 황인준 - KAIST 전산학부 21학번

## 프로젝트 개요

### **문제 정의**

전세계적으로 당뇨병 유병 인구의 증가는 효과적인 혈당 관리의 필요성을 높였습니다. 하지만, 특히 수입 식품에서 정확한 탄수화물 함량을 찾는 것이 어려워 정보의 파편화 및 누락이 문제가 되고 있습니다. 또한, 영양 성분표를 이해하기 쉬운 단위로 변환하고 음식이 실제로 혈당에 미치는 영향을 평가하는 것도 복잡합니다.

### **우리의 해결책**

- **데이터 통합 및 수정:**
    - 한국 식품의약품 안전처의 영양성분 데이터베이스를 활용하여 표준화된 영양 정보를 제공합니다.
    - 사용자가 데이터를 수정하고 업데이트할 수 있는 기능을 포함합니다.
- **영양 성분 변환:**
    - 100g당, 1회 제공량, 전체 제공량 기준으로 영양 계산을 촉진합니다.
- **커뮤니티 기능:**
    - 음식이 혈당에 미치는 특정 효과에 대한 태그 및 공유를 허용합니다.
    - 경험 및 최선의 방법을 공유할 수 있는 플랫폼을 제공합니다.

## **프로젝트 진행**

- 공식 데이터베이스의 영양 데이터 분석 및 표준화.
- 사용자 중심 설계 접근 방식으로, 이해하기 쉽도록 포커스 그룹 인터뷰를 포함합니다.
- 이미지에서 영양성분 라벨을 분석하기 위한 OCR 및 기본 NLP 구현.

## 프로젝트 결과

### 데모영상

(영상 첨부)

### 사용방법

앱 사용 이미지 + 앱 동작 설명

## **기대 효과**

이 기술 개발은 당뇨병 관리뿐만 아니라 보다 넓은 건강 관리 분야에도 적용될 수 있도록 사용자 친화적 방식으로 영양 정보를 표준화하는 것을 목표로 합니다.

## **설치 및 실행 방법**

### Quick Start

Use pipenv to install packages. (e.g., `pipenv install <package>`)

```bash
pipenv --python 3.11 # Use python 3.11
pipenv shell # Activate virtual environment
pipenv install # Install packages

# Run `pre-commit` automatically on `git commit`
pre-commit install
pre-commit install --hook-type commit-msg
```

### How to Run

```bash
pipenv run dev
```

### How to Contribute

1. Follow [Conventional Commits][conventional-commits] for writing commit messages.
2. Use type hints strictly. (Check [PEP 484][pep-484].)

[badge/python-version]: https://img.shields.io/github/pipenv/locked/python-version/dayscout-kaist/dayscout-server/main
[badge/black]: https://img.shields.io/badge/code%20style-black-000000
[badge/isort]: https://img.shields.io/badge/%20imports-isort-%231674b1?labelColor=ef8336
[badge/pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[badge/conventional-commits]: https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white
[isort]: https://pycqa.github.io/isort
[conventional-commits]: https://conventionalcommits.org
[pep-484]: https://peps.python.org/pep-0484/
[repo/black]: https://github.com/psf/black
[repo/pre-commit]: https://github.com/pre-commit/pre-commit

### Deployment

Copy and fill in the `.env` file.

```bash
cp .env.prod.example .env
```

Run the server.

```bash
docker-compose up -d --build
```

## **개발 환경**

### **앱 개발**

- **언어:** TypeScript
- **프레임워크:** React Native

### **백엔드 개발**

- **언어:** Python
- **프레임워크:** FastAPI

### **버전 관리**

- **Git 브랜치 전략:** PR(Pull Request) 기반의 코드 리뷰 프로세스를 적용. 동료 개발자의 승인이 이뤄진 후에만 메인 브랜치에 머지.
- **릴리즈 관리:** GitHub Issues와 Notion을 통한 프로젝트 관리 및 이슈 추적.

### **데이터베이스**

- **시스템:** MySQL과 ElasticSearch 사용.

### **배포**

- **서버:** SPARCS에서 제공하는 운영적인 물리서버 사용.
- **앱 배포:** 스토어에는 배포하지 않고, apk 형태로 Android만 배포

### **협업 및 커뮤니케이션**

- **이슈 관리:** GitHub 이슈와 Notion을 통한 이슈 및 프로젝트 관리.
- **코드 리뷰:** PR에 대한 코드 리뷰 및 동료의 승인 후 메인 브랜치에 머지.
- **슬랙 통합:** PR이 발생할 때마다 Slack을 통해 팀에 알림.
- **Daily Sync-Up:** Slack에서 'Daily Sync-Up' 채널을 통해 팀원들이 매일 진행한 작업을 공유.
