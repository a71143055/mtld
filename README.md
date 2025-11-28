# mtld

**Meta Learning Design (mtld)**

이 저장소는 ParaView 6.0.1 스타일의 시각화 파이프라인 특성을 반영한 소프트웨어 중심의 시뮬레이션 및 메타러닝 프로젝트입니다.  
목표는 **줄기세포 배양체를 물리적으로 구현하는 로봇(안드로이드/휴머노이드) 설계 시뮬레이터**를 소프트웨어적으로 모델링하고, ParaView 기반 시각화와 메타러닝 제어 에이전트를 통합하는 것입니다.

**중요:** 실제 생물학적 실험, 배양 절차, 소재 합성 등은 포함하지 않습니다. 이 저장소는 오직 소프트웨어 시뮬레이션, 시각화, 학습 루프, 로봇 제어 인터페이스를 제공합니다.

## 요구사항
- Python 3.9+
- ParaView 6.0.1 (선택적, 시각화 통합용)
- PyTorch
- numpy, pyyaml

설치:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.mtld.main --mode demo
python examples/demo_paraview.py

---

### `requirements.txt`
numpy>=1.21
torch>=1.12
pyyaml
tqdm

---

### `pyproject.toml`
```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mtld"
version = "0.1.0"
description = "Meta Learning Design - simulation + paraview-style integration"
authors = [{name="정구영"}]
dependencies = [
  "numpy>=1.21",
  "torch>=1.12",
  "pyyaml",
  "tqdm"
]

---

### `pyproject.toml`
```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mtld"
version = "0.1.0"
description = "Meta Learning Design - simulation + paraview-style integration"
authors = [{name="정구영"}]
dependencies = [
  "numpy>=1.21",
  "torch>=1.12",
  "pyyaml",
  "tqdm"
]

MIT License
Copyright (c) 2025
Permission is hereby granted...
