# -*- coding: utf-8 -*-
"""
data/departments.py
마이스터고 · 특성화고 주요 학과 마스터 데이터 및 학과-자격증 매핑 정규화 테이블

※ 여기 포함된 학과 목록은 마이스터고/특성화고에서 흔히 개설되는 대표 학과를
   기준으로 팀이 정리한 것입니다. 학교마다 학과명이 다를 수 있으므로,
   실제 서비스 적용 시 자교(自校) 학과명에 맞춰 DEPARTMENTS 딕셔너리의
   key 값만 교체하면 됩니다.
"""

# 학과명 -> {상위 산업분류, 관련 자격증 코드 리스트}
# 자격증 코드는 data/certifications.py 의 "code" 값과 매핑됩니다.
DEPARTMENTS = {
    "기계과": {
        "category": "기계",
        "cert_codes": ["MC01", "MC02", "MC03", "MC04", "MC05", "MC06"],
    },
    "전기전자과": {
        "category": "전기/전자",
        "cert_codes": ["EL01", "EL02", "EL03", "EL04", "EL05", "EL06"],
    },
    "IT소프트웨어과": {
        "category": "IT/소프트웨어",
        "cert_codes": ["IT01", "IT02", "IT03", "IT04", "IT05", "IT06"],
    },
    "화공과": {
        "category": "화공",
        "cert_codes": ["CH01", "CH02", "CH03", "CH04"],
    },
    "메카트로닉스과": {
        "category": "메카트로닉스",
        "cert_codes": ["MT01", "MT02", "MT03"],
    },
    "건축토목과": {
        "category": "건축/토목",
        "cert_codes": ["CV01", "CV02", "CV03", "CV04", "CV05"],
    },
    "자동차과": {
        "category": "자동차",
        "cert_codes": ["AT01", "AT02", "AT03"],
    },
    "조선과": {
        "category": "조선",
        "cert_codes": ["SB01", "SB02"],
    },
    "식품가공과": {
        "category": "식품가공",
        "cert_codes": ["FD01", "FD02", "FD03"],
    },
}

DEPARTMENT_LIST = list(DEPARTMENTS.keys())
CATEGORY_LIST = sorted({v["category"] for v in DEPARTMENTS.values()})


def get_certs_for_department(dept_name: str):
    """학과명으로 관련 자격증 코드 리스트를 반환한다."""
    return DEPARTMENTS.get(dept_name, {}).get("cert_codes", [])


def get_department_for_category(category: str):
    """산업분류(category)로 해당하는 학과명 리스트를 반환한다."""
    return [name for name, v in DEPARTMENTS.items() if v["category"] == category]
