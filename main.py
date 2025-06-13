import streamlit as st
from datetime import datetime

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return '♈️ 양자리'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return '♉️ 황소자리'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return '♊️ 쌍둥이자리'
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return '♋️ 게자리'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return '♌️ 사자자리'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 23):
        return '♍️ 처녀자리'
    elif (month == 9 and day >= 24) or (month == 10 and day <= 22):
        return '♎️ 천칭자리'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return '♏️ 전갈자리'
    elif (month == 11 and day >= 23) or (month == 12 and day <= 24):
        return '♐️ 사수자리'
    elif (month == 12 and day >= 25) or (month == 1 and day <= 19):
        return '♑️ 염소자리'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '♒️ 물병자리'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return '♓️ 물고기자리'
    else:
        return '❓ 알 수 없음'

horoscopes = {
    '♈️ 양자리': '🔥 오늘은 열정적으로 도전할 때! 기회를 잡으세요.',
    '♉️ 황소자리': '🌱 꾸준한 노력이 빛을 발하는 하루입니다.',
    '♊️ 쌍둥이자리': '💬 새로운 사람들과의 만남이 행운을 가져다줘요.',
    '♋️ 게자리': '🏠 가족과의 따뜻한 시간이 행복을 줍니다.',
    '♌️ 사자자리': '👑 자신감을 가지고 리더십을 발휘하세요!',
    '♍️ 처녀자리': '🔍 세심한 관찰과 준비가 성공을 부릅니다.',
    '♎️ 천칭자리': '⚖️ 균형 잡힌 마음이 좋은 결정을 이끌어요.',
    '♏️ 전갈자리': '🦂 감정을 잘 다스리면 운이 트입니다.',
    '♐️ 사수자리': '🚀 모험과 배움의 기회가 찾아옵니다.',
    '♑️ 염소자리': '📈 계획을 세우고 꾸준히 나아가세요.',
    '♒️ 물병자리': '💡 창의적인 아이디어가 빛을 발하는 날.',
    '♓️ 물고기자리': '🎨 감성이 풍부해 예술적 영감을 받습니다.',
    '❓ 알 수 없음': '⚠️ 생일을 정확히 입력해주세요!'
}

st.markdown("# ✨ 오늘의 별자리 운세 ✨")
st.markdown("🎂 생일을 입력하면 별자리와 오늘의 운세를 알려드려요!")

birth_date = st.date_input("📅 생일을 선택하세요", min_value=datetime(1900, 1, 1), max_value=datetime.today())

if birth_date:
    sign = get_zodiac_sign(birth_date.month, birth_date.day)
    st.markdown(f"## 🌟 당신의 별자리는 **{sign}** 입니다!")
    st.markdown("### 🔮 오늘의 운세:")
    st.success(horoscopes.get(sign, "운세 정보를 찾을 수 없습니다."))
