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
    '♈️ 양자리': '🔥 오늘은 새로운 도전을 하기에 딱 좋은 날이에요! 힘차게 나아가세요!',
    '♉️ 황소자리': '🌿 안정을 추구하면 좋은 기회가 찾아올 거예요. 천천히 걸어가요.',
    '♊️ 쌍둥이자리': '💬 사람들과의 소통에서 좋은 일이 생길 수 있어요. 활발히 대화하세요!',
    '♋️ 게자리': '🏡 가족이나 친구와의 시간을 소중히 하세요. 마음이 따뜻해질 거예요.',
    '♌️ 사자자리': '👑 당신의 리더십이 빛날 날입니다! 당당하게 나아가세요.',
    '♍️ 처녀자리': '🔍 세심한 관찰력이 오늘 큰 도움이 될 거예요. 집중해보세요!',
    '♎️ 천칭자리': '⚖️ 균형 잡힌 판단이 행운을 가져다줄 거예요. 조화롭게 생각하세요.',
    '♏️ 전갈자리': '🦂 감정 조절이 중요한 하루가 될 수 있어요. 침착하게 행동하세요.',
    '♐️ 사수자리': '🌟 새로운 지식이나 여행에 행운이 따릅니다. 마음을 열고 도전하세요!',
    '♑️ 염소자리': '📅 계획을 세우고 차분히 실천해보세요. 꾸준함이 열쇠입니다.',
    '♒️ 물병자리': '💡 창의력이 넘쳐나는 하루가 될 거예요! 아이디어를 펼치세요.',
    '♓️ 물고기자리': '🎨 감성이 풍부해지는 날, 예술 활동에 좋습니다. 감동을 느껴보세요.',
    '❓ 알 수 없음': '⚠️ 별자리를 알 수 없어요. 날짜를 다시 확인해주세요.'
}

st.markdown("# ✨ 오늘의 별자리 운세 ✨")
st.markdown("🎂 **생일을 입력하면 당신의 별자리와 오늘의 운세를 알려드려요!**")

birth_date = st.date_input("📅 생일을 선택하세요", min_value=datetime(1900, 1, 1), max_value=datetime.today())

if birth_date:
    sign = get_zodiac_sign(birth_date.month, birth_date.day)
    st.markdown(f"## 🌟 당신의 별자리는 **{sign}**입니다!")
    st.markdown("### 🔮 오늘의 운세:")
    st.success(horoscopes.get(sign, "운세 정보를 찾을 수 없습니다."))
