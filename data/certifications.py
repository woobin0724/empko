# -*- coding: utf-8 -*-
"""
data/certifications.py
국가기술자격 마스터 데이터 (기능사 / 산업기사 / 기사)

※ 중요 안내
한국산업인력공단(Q-Net)이 관리하는 국가기술자격 종목은 500종 이상입니다.
아래 CERTIFICATIONS 리스트는 마이스터고 · 특성화고 9개 주요 학과와 직접
관련된 자격증을 팀이 선별하여 구조화한 "대표 마스터 데이터(약 40종)"이며,
전체 종목을 담은 완전한 DB가 아닙니다.

전체 종목을 실시간으로 채우려면:
  1) 공공데이터포털(data.go.kr)에서 "한국산업인력공단_국가기술자격 종목별
     상세정보" Open API를 신청해 서비스키를 발급받고
  2) services/qnet_api.py 의 fetch_certifications_from_api() 에 키를 연결하면
     아래 정적 데이터를 실시간 API 응답으로 자동 대체합니다. (fallback 구조)
"""

CERTIFICATIONS = [
    # ---------------- 기계 (MC) ----------------
    {"code": "MC01", "name": "컴퓨터응용선반기능사", "level": "기능사", "category": "기계"},
    {"code": "MC02", "name": "컴퓨터응용밀링기능사", "level": "기능사", "category": "기계"},
    {"code": "MC03", "name": "생산자동화산업기사", "level": "산업기사", "category": "기계"},
    {"code": "MC04", "name": "일반기계기사", "level": "기사", "category": "기계"},
    {"code": "MC05", "name": "설비보전기능사", "level": "기능사", "category": "기계"},
    {"code": "MC06", "name": "지게차운전기능사", "level": "기능사", "category": "기계"},

    # ---------------- 전기/전자 (EL) ----------------
    {"code": "EL01", "name": "전기기능사", "level": "기능사", "category": "전기/전자"},
    {"code": "EL02", "name": "전기산업기사", "level": "산업기사", "category": "전기/전자"},
    {"code": "EL03", "name": "전기기사", "level": "기사", "category": "전기/전자"},
    {"code": "EL04", "name": "전자기기기능사", "level": "기능사", "category": "전기/전자"},
    {"code": "EL05", "name": "전자산업기사", "level": "산업기사", "category": "전기/전자"},
    {"code": "EL06", "name": "승강기기능사", "level": "기능사", "category": "전기/전자"},

    # ---------------- IT/소프트웨어 (IT) ----------------
    {"code": "IT01", "name": "정보처리기능사", "level": "기능사", "category": "IT/소프트웨어"},
    {"code": "IT02", "name": "정보처리산업기사", "level": "산업기사", "category": "IT/소프트웨어"},
    {"code": "IT03", "name": "정보처리기사", "level": "기사", "category": "IT/소프트웨어"},
    {"code": "IT04", "name": "정보보안기사", "level": "기사", "category": "IT/소프트웨어"},
    {"code": "IT05", "name": "네트워크관리사2급", "level": "민간(등록)", "category": "IT/소프트웨어"},
    {"code": "IT06", "name": "정보기기운용기능사", "level": "기능사", "category": "IT/소프트웨어"},

    # ---------------- 화공 (CH) ----------------
    {"code": "CH01", "name": "화학분석기능사", "level": "기능사", "category": "화공"},
    {"code": "CH02", "name": "위험물산업기사", "level": "산업기사", "category": "화공"},
    {"code": "CH03", "name": "화공기사", "level": "기사", "category": "화공"},
    {"code": "CH04", "name": "가스기능사", "level": "기능사", "category": "화공"},

    # ---------------- 메카트로닉스 (MT) ----------------
    {"code": "MT01", "name": "생산자동화기능사", "level": "기능사", "category": "메카트로닉스"},
    {"code": "MT02", "name": "메카트로닉스기사", "level": "기사", "category": "메카트로닉스"},
    {"code": "MT03", "name": "로봇기구개발기사", "level": "기사", "category": "메카트로닉스"},

    # ---------------- 건축/토목 (CV) ----------------
    {"code": "CV01", "name": "건축도장기능사", "level": "기능사", "category": "건축/토목"},
    {"code": "CV02", "name": "건축목공기능사", "level": "기능사", "category": "건축/토목"},
    {"code": "CV03", "name": "건축산업기사", "level": "산업기사", "category": "건축/토목"},
    {"code": "CV04", "name": "토목산업기사", "level": "산업기사", "category": "건축/토목"},
    {"code": "CV05", "name": "측량및지형공간정보산업기사", "level": "산업기사", "category": "건축/토목"},

    # ---------------- 자동차 (AT) ----------------
    {"code": "AT01", "name": "자동차정비기능사", "level": "기능사", "category": "자동차"},
    {"code": "AT02", "name": "자동차정비산업기사", "level": "산업기사", "category": "자동차"},
    {"code": "AT03", "name": "자동차차체수리기능사", "level": "기능사", "category": "자동차"},

    # ---------------- 조선 (SB) ----------------
    {"code": "SB01", "name": "조선기능사", "level": "기능사", "category": "조선"},
    {"code": "SB02", "name": "조선산업기사", "level": "산업기사", "category": "조선"},

    # ---------------- 식품가공 (FD) ----------------
    {"code": "FD01", "name": "식품가공기능사", "level": "기능사", "category": "식품가공"},
    {"code": "FD02", "name": "제과기능사", "level": "기능사", "category": "식품가공"},
    {"code": "FD03", "name": "제빵기능사", "level": "기능사", "category": "식품가공"},
]

CERT_CODE_TO_NAME = {c["code"]: c["name"] for c in CERTIFICATIONS}
CERT_NAME_TO_CODE = {c["name"]: c["code"] for c in CERTIFICATIONS}
CERT_LEVELS = sorted({c["level"] for c in CERTIFICATIONS})


def get_certs_by_category(category: str):
    return [c for c in CERTIFICATIONS if c["category"] == category]


def get_cert_names(codes):
    """자격증 코드 리스트를 자격증명 리스트로 변환."""
    return [CERT_CODE_TO_NAME[c] for c in codes if c in CERT_CODE_TO_NAME]
