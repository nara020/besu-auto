# Besu Network Automation

🚀 **자동화된 프라이빗 Hyperledger Besu 블록체인 네트워크 생성기**

이 프로젝트는 IBFT2 또는 QBFT 컨센서스를 사용하는 프라이빗 Hyperledger Besu 네트워크를 몇 분 안에 자동으로 구축할 수 있는 도구입니다.

## 🎯 주요 기능

- ✅ **IBFT2/QBFT 컨센서스 지원** - 원하는 컨센서스 알고리즘 선택
- ✅ **완전 자동화** - 키 생성부터 네트워크 시작까지 원클릭
- ✅ **Docker 기반** - 격리된 환경에서 안전한 실행
- ✅ **개발 최적화** - 빠른 블록 생성 (2초) 및 무료 가스
- ✅ **전체 RPC API** - 모든 필요한 Ethereum JSON-RPC API 지원
- ✅ **안정적인 피어 연결** - 고정 IP 기반 네트워크 구성

## 📋 사전 요구사항

### 필수 소프트웨어
- **Docker** & **Docker Compose**
- **Python 3.7+**
- **Hyperledger Besu** (CLI 도구)

### Besu 설치
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install default-jdk
wget https://github.com/hyperledger/besu/releases/latest/download/besu-*.tar.gz
tar -xzf besu-*.tar.gz
sudo mv besu-*/bin/besu /usr/local/bin/

# macOS (Homebrew)
brew install hyperledger/besu/besu

# 설치 확인
besu --version
```

## 🚀 빠른 시작

### 1. 환경 초기화
```bash
python3 clean.py
```

### 2. 네트워크 생성
```bash
python3 setup_besu.py
```
실행 시 컨센서스 선택:
- `1`: IBFT2 (기본)
- `2`: QBFT  (권장)

### 3. 네트워크 시작
```bash
docker-compose up -d
```

### 4. 상태 확인
```bash
# 노드 상태 확인
curl -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}' \
  http://localhost:8545

# 검증자 목록 확인 (IBFT2)
curl -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"ibft_getValidatorsByBlockNumber","params":["latest"],"id":1}' \
  http://localhost:8545

# 검증자 목록 확인 (QBFT)
curl -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"qbft_getValidatorsByBlockNumber","params":["latest"],"id":1}' \
  http://localhost:8545
```

## 🏗️ 네트워크 구성

### 노드 정보
| 노드 | HTTP RPC | P2P | Docker IP |
|------|----------|-----|-----------|
| Node 1 | 8545 | 30303 | 192.168.100.11 |
| Node 2 | 8546 | 30304 | 192.168.100.12 |
| Node 3 | 8547 | 30305 | 192.168.100.13 |
| Node 4 | 8548 | 30306 | 192.168.100.14 |

### 네트워크 설정
- **Chain ID**: 20250707
- **블록 생성 주기**: 2초
- **초기 잔액**: 1,000,000 ETH (검증자당)
- **가스 가격**: 0 (무료)
- **동기화**: 최소 1개 피어

### 활성화된 RPC API
```
ETH, NET, WEB3, DEBUG, ADMIN, TXPOOL, TRACE, PLUGINS, IBFT/QBFT
```

## 📁 프로젝트 구조

```
besu-auto/
├── setup_besu.py          # 메인 설정 스크립트
├── clean.py               # 환경 초기화 스크립트
├── docker-compose.yml     # Docker 구성 (자동 생성)
├── validators.json        # 검증자 정보 (자동 생성)
├── config.json           # Besu CLI 설정 (자동 생성)
├── config/               # Besu 설정 디렉토리 (자동 생성)
│   ├── genesis-ibft2.json # IBFT2 제네시스 파일
│   ├── genesis-qbft.json  # QBFT 제네시스 파일
│   └── keys/             # 검증자 키 파일들
└── node1-4/              # 각 노드의 데이터 디렉토리 (자동 생성)
    └── data/             # 블록체인 데이터
```

## 🔧 고급 사용법

### 네트워크 재시작
```bash
# 네트워크 중지
docker-compose down

# 완전 초기화 후 재시작
python3 clean.py
python3 setup_besu.py
docker-compose up -d
```

### 로그 확인
```bash
# 전체 노드 로그
docker-compose logs -f

# 특정 노드 로그
docker-compose logs -f besu-node1
```

### 네트워크 설정 변경
`setup_besu.py` 파일에서 다음 설정들을 수정할 수 있습니다:

```python
CHAIN_ID = 20250707                    # 체인 ID
INITIAL_BALANCE = 1000000              # 초기 잔액 (ETH)
BASE_HTTP_PORT = 8545                  # HTTP RPC 시작 포트
BASE_P2P_PORT = 30303                  # P2P 시작 포트
```

## 🔐 보안 고려사항

⚠️ **중요**: 이 도구는 **개발 및 테스트 목적**으로 설계되었습니다.

### 개발/테스트 환경
- ✅ 로컬 개발
- ✅ 프로토타입 개발
- ✅ 학습 및 실험
- ✅ 사내 테스트 네트워크

### 프로덕션 환경
프로덕션 사용 시 추가 보안 조치 필요:
- 🔐 하드웨어 보안 모듈 (HSM) 사용
- 🔐 키 관리 시스템 (Vault, KMS) 연동
- 🔐 네트워크 방화벽 및 접근 제어
- 🔐 정기적인 키 로테이션
- 🔐 모니터링 및 로깅 시스템

## 🐛 문제 해결

### 일반적인 문제들

#### 1. Docker 네트워크 충돌
```bash
# 기존 네트워크 제거
docker network rm besu-network

# 다시 시작
docker-compose up -d
```

#### 2. 포트 충돌
다른 서비스가 8545-8548 포트를 사용 중인 경우:
```bash
# 사용 중인 포트 확인
netstat -tulpn | grep :8545

# 해당 프로세스 종료 후 재시작
```

#### 3. Besu CLI 없음
```bash
# Besu 설치 확인
besu --version

# 없다면 위의 "Besu 설치" 섹션 참조
```

#### 4. 권한 문제
```bash
# Docker 권한 추가
sudo usermod -aG docker $USER
newgrp docker
```

### 로그 분석
```bash
# 노드가 시작되지 않는 경우
docker-compose logs besu-node1

# 피어 연결 문제
docker-compose logs | grep -i "peer\|enode"

# API 호출 문제
docker-compose logs | grep -i "rpc\|api"
```

## 📚 추가 리소스

- [Hyperledger Besu 공식 문서](https://besu.hyperledger.org/)
- [IBFT2 컨센서스 가이드](https://besu.hyperledger.org/en/stable/HowTo/Configure/Consensus/IBFT/)
- [QBFT 컨센서스 가이드](https://besu.hyperledger.org/en/stable/HowTo/Configure/Consensus/QBFT/)
- [Ethereum JSON-RPC API](https://ethereum.org/en/developers/docs/apis/json-rpc/)

## 🤝 기여하기

이 프로젝트에 기여하고 싶으시다면:

1. 이슈 리포트 또는 기능 제안
2. 풀 리퀘스트 제출
3. 문서 개선

## 📞 지원

문제가 있거나 질문이 있으시면 **jinhyeok**에게 연락해 주세요.

---

**Happy Blockchain Development!**