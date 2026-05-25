import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'DejaVu Sans'

# 페이지 설정
st.set_page_config(page_title="이차함수 그래프", layout="wide")

# 제목
st.title("📊 이차함수 그래프")
st.markdown("---")

# 탭 생성
tab1, tab2, tab3 = st.tabs(["개념 학습", "그래프 탐험", "퀴즈"])

# ==================== 탭 1: 개념 학습 ====================
with tab1:
    st.header("이차함수의 기본 개념")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📐 이차함수의 표준형")
        st.latex(r"y = ax^2 + bx + c")
        st.write("여기서 a, b, c는 상수이고, **a ≠ 0** 입니다.")
        
        st.subheader("🎯 꼭짓점의 좌표")
        st.latex(r"x = -\frac{b}{2a}")
        st.latex(r"y = -\frac{b^2 - 4ac}{4a}")
        
    with col2:
        st.subheader("📈 그래프의 특징")
        st.info("**a > 0일 때**: 위로 볼록한 포물선 (최솟값 존재)")
        st.info("**a < 0일 때**: 아래로 볼록한 포물선 (최댓값 존재)")
        
        st.subheader("🔍 판별식 (D = b² - 4ac)")
        st.success("**D > 0**: 서로 다른 두 실근")
        st.warning("**D = 0**: 중근 (한 개의 실근)")
        st.error("**D < 0**: 실근 없음 (근이 없음)")

# ==================== 탭 2: 그래프 탐험 ====================
with tab2:
    st.header("🎮 슬라이더로 조절하며 배우기")
    
    # 슬라이더
    col1, col2, col3 = st.columns(3)
    
    with col1:
        a = st.slider("a 값 조절", -5.0, 5.0, 1.0, 0.1, help="a > 0이면 위로 볼록, a < 0이면 아래로 볼록")
    
    with col2:
        b = st.slider("b 값 조절", -10.0, 10.0, 0.0, 0.1, help="꼭짓점의 x 좌표에 영향")
    
    with col3:
        c = st.slider("c 값 조절", -10.0, 10.0, 0.0, 0.1, help="y절편의 값")
    
    # 계산
    discriminant = b**2 - 4*a*c
    vertex_x = -b / (2*a)
    vertex_y = a*vertex_x**2 + b*vertex_x + c
    
    # 그래프 그리기
    x = np.linspace(-10, 10, 200)
    y = a*x**2 + b*x + c
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # 그래프
    ax.plot(x, y, 'b-', linewidth=2.5, label=f'y = {a:.1f}x² + {b:.1f}x + {c:.1f}')
    
    # 꼭짓점 표시
    ax.plot(vertex_x, vertex_y, 'ro', markersize=10, label=f'꼭짓점 ({vertex_x:.2f}, {vertex_y:.2f})', zorder=5)
    
    # y절편 표시
    ax.plot(0, c, 'go', markersize=8, label=f'y절편 (0, {c:.1f})', zorder=5)
    
    # x절편 표시 (실근이 있는 경우)
    if discriminant >= 0:
        x1 = (-b + np.sqrt(discriminant)) / (2*a)
        x2 = (-b - np.sqrt(discriminant)) / (2*a)
        ax.plot(x1, 0, 'mo', markersize=8, zorder=5)
        ax.plot(x2, 0, 'mo', markersize=8, zorder=5)
        if abs(x1 - x2) > 0.01:
            ax.legend([f'x절편: ({x1:.2f}, 0), ({x2:.2f}, 0)'], loc='upper right', fontsize=9)
        else:
            ax.legend([f'중근: ({x1:.2f}, 0)'], loc='upper right', fontsize=9)
    
    # 격자 및 축
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-15, 20)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(f'이차함수: y = {a:.1f}x² + {b:.1f}x + {c:.1f}', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    
    st.pyplot(fig)
    
    # 정보 표시
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("꼭짓점 (최솟값/최댓값)", f"({vertex_x:.2f}, {vertex_y:.2f})")
        if a > 0:
            st.info("✓ a > 0 → 최솟값을 가집니다")
        else:
            st.info("✓ a < 0 → 최댓값을 가집니다")
    
    with col2:
        st.metric("y절편", f"{c:.1f}")
        st.write(f"x = 0일 때의 y 값입니다")
    
    with col3:
        st.metric("판별식 D", f"{discriminant:.2f}")
        if discriminant > 0:
            st.success("✓ D > 0 → 서로 다른 두 실근")
            x1 = (-b + np.sqrt(discriminant)) / (2*a)
            x2 = (-b - np.sqrt(discriminant)) / (2*a)
            st.write(f"x절편: x = {x1:.2f}, {x2:.2f}")
        elif discriminant == 0:
            st.warning("✓ D = 0 → 중근 (한 개의 실근)")
            st.write(f"x절편: x = {vertex_x:.2f}")
        else:
            st.error("✓ D < 0 → 실근 없음")
            st.write("x축과 만나지 않습니다")

# ==================== 탭 3: 퀴즈 ====================
with tab3:
    st.header("❓ 이차함수 퀴즈")
    
    # 세션 상태 초기화
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    if 'quiz_a' not in st.session_state:
        st.session_state.quiz_a = 1
    if 'quiz_b' not in st.session_state:
        st.session_state.quiz_b = 0
    if 'quiz_c' not in st.session_state:
        st.session_state.quiz_c = 0
    if 'correct_count' not in st.session_state:
        st.session_state.correct_count = 0
    if 'total_count' not in st.session_state:
        st.session_state.total_count = 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎲 새로운 퀴즈 생성"):
            st.session_state.quiz_a = np.random.randint(-3, 4)
            if st.session_state.quiz_a == 0:
                st.session_state.quiz_a = 1
            st.session_state.quiz_b = np.random.randint(-6, 7)
            st.session_state.quiz_c = np.random.randint(-5, 6)
            st.session_state.quiz_generated = True
    
    with col2:
        st.metric("정답률", f"{st.session_state.correct_count}/{st.session_state.total_count}" if st.session_state.total_count > 0 else "0/0")
    
    if st.session_state.quiz_generated:
        qa = st.session_state.quiz_a
        qb = st.session_state.quiz_b
        qc = st.session_state.quiz_c
        
        # 퀴즈 그래프 표시
        x_quiz = np.linspace(-10, 10, 200)
        y_quiz = qa*x_quiz**2 + qb*x_quiz + qc
        
        fig_quiz, ax_quiz = plt.subplots(figsize=(8, 6))
        ax_quiz.plot(x_quiz, y_quiz, 'b-', linewidth=2.5)
        ax_quiz.grid(True, alpha=0.3, linestyle='--')
        ax_quiz.axhline(y=0, color='k', linewidth=0.5)
        ax_quiz.axvline(x=0, color='k', linewidth=0.5)
        ax_quiz.set_xlim(-10, 10)
        ax_quiz.set_ylim(-15, 20)
        ax_quiz.set_xlabel('x', fontsize=12)
        ax_quiz.set_ylabel('y', fontsize=12)
        ax_quiz.set_title('다음 그래프의 정보를 구하세요', fontsize=14, fontweight='bold')
        
        st.pyplot(fig_quiz)
        
        # 퀴즈 1: 꼭짓점
        st.subheader("❶ 꼭짓점의 x 좌표는?")
        vertex_x_quiz = -qb / (2*qa)
        answer1 = st.number_input("x 좌표 (소수점 2자리)", value=0.0, step=0.1, key="answer1")
        if st.button("확인 - 꼭짓점 x좌표", key="check1"):
            if abs(answer1 - vertex_x_quiz) < 0.1:
                st.success(f"✓ 정답! 꼭짓점의 x좌표는 {vertex_x_quiz:.2f}입니다")
                st.session_state.correct_count += 1
            else:
                st.error(f"✗ 틀렸어요. 정답은 {vertex_x_quiz:.2f}입니다")
            st.session_state.total_count += 1
        
        # 퀴즈 2: 판별식
        st.subheader("❷ 판별식 D는?")
        discriminant_quiz = qb**2 - 4*qa*qc
        answer2 = st.number_input("판별식 D 값", value=0, step=1, key="answer2")
        if st.button("확인 - 판별식", key="check2"):
            if answer2 == discriminant_quiz:
                st.success(f"✓ 정답! 판별식 D = {discriminant_quiz}입니다")
                st.session_state.correct_count += 1
            else:
                st.error(f"✗ 틀렸어요. 정답은 {discriminant_quiz}입니다")
            st.session_state.total_count += 1
        
        # 퀴즈 3: y절편
        st.subheader("❸ y절편은?")
        answer3 = st.number_input("y절편 값", value=0.0, step=0.1, key="answer3")
        if st.button("확인 - y절편", key="check3"):
            if abs(answer3 - qc) < 0.01:
                st.success(f"✓ 정답! y절편은 {qc}입니다")
                st.session_state.correct_count += 1
            else:
                st.error(f"✗ 틀렸어요. 정답은 {qc}입니다")
            st.session_state.total_count += 1
        
        # 해설
        st.markdown("---")
        st.subheader("📚 해설")
        st.write(f"**주어진 함수**: y = {qa}x² + {qb}x + {qc}")
        st.write(f"**꼭짓점의 x좌표**: x = -b/2a = -{qb}/(2×{qa}) = {vertex_x_quiz:.2f}")
        st.write(f"**판별식 D**: D = b² - 4ac = {qb}² - 4×{qa}×{qc} = {discriminant_quiz}")
        if discriminant_quiz > 0:
            st.write("→ 서로 다른 두 실근을 가집니다")
        elif discriminant_quiz == 0:
            st.write("→ 중근을 가집니다")
        else:
            st.write("→ 실근을 가지지 않습니다")
        st.write(f"**y절편**: x = 0일 때 y = {qc}")
