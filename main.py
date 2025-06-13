import streamlit as st
from datetime import datetime

# 별자리 범위 설정
def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return '양자리'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return '황소자리'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return '쌍둥이자리'
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return '게자리'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return '사자자리'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        return '처녀자리'
    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        return '천칭자리'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return '전갈자리'
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        return '사수자리'
    elif (month == 12 and day >= 25) or (month == 1 and day <= 19):
        return '염소자리'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '물병자리'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return '물고기자리'
    else:
        return '알 수 없음'

# 예시 운세 데이터
horoscopes = {
    '양자리': '오늘은 새로운 도전을 하기에 딱 좋은 날이에요!',
    '황소자리': '안정을 추구하면 좋은 기회가 찾아올 거예요.',
    '쌍둥이자리': '사람들과의 소통에서 좋은 일이 생길 수 있어요.',
    '게자리': '가족이나 친구와의 시간을 소중히 하세요.',
    '사자자리': '당신의 리더십이 빛날 날입니다!',
    '처녀자리': '세심한 관찰력이 오늘 큰 도움이 될 거예요.',
    '천칭자리': '균형 잡힌 판단이 행운을 가져다줄 거예요.',
    '전갈자리': '감정 조절이 중요한 하루가 될 수 있어요.',
    '사수자리': '새로운 지식이나 여행에 행운이 따릅니다.',
    '염소자리': '계획을 세우고 차분히 실천해보세요.',
    '물병자리': '창의력이 넘쳐나는 하루가 될 거예요!',
    '물고기자리': '감성이 풍부해지는 날, 예술 활동에 좋습니다.',
    '알 수 없음': '별자리를 알 수 없어요. 날짜를 확인해주세요.'
}

# Streamlit UI
st.title("⭐ 오늘의 별자리 운세")

birth_date = st.date_input("생일을 입력하세요", min_value=datetime(1900, 1, 1), max_value=datetime.today())

if birth_date:
    sign = get_zodiac_sign(birth_date.month, birth_date.day)
    st.subheader(f"당신의 별자리는 **{sign}**입니다.")
    st.write("🔮 오늘의 운세:")
    st.success(horoscopes.get(sign, "운세 정보를 찾을 수 없습니다."))
