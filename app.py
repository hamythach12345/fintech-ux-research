import streamlit as st
from datetime import datetime
from fintech_ux_research.crew import FintechUxResearch
import os
import re

st.set_page_config(
    page_title="UX Research Agent - Fintech",
    page_icon="🔍",
    layout="wide"
)

# ============ SIDEBAR ============
with st.sidebar:
    st.title("🔍 UX Research Agent")
    st.markdown("*Fintech & Super App*")
    st.divider()
    st.markdown("""
    ### Pipeline
    1. 🧑‍🔬 Researcher
    2. 🧩 Synthesizer
    3. ✅ Reviewer
    4. 🎨 Visualizer
    """)
    st.divider()
    st.caption("Powered by CrewAI")

# ============ MAIN FORM ============
st.title("📋 Research Brief")
st.markdown("Điền thông tin bên dưới để agent nghiên cứu đúng nhu cầu của bạn.")

with st.form("research_brief"):
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.text_input(
            "Chủ đề research *",
            placeholder="VD: ví điện tử cho Gen Z"
        )
        
        research_type = st.selectbox(
            "Loại research",
            ["Feature research", "User segment", "Market/Competitor", "Trend research"]
        )
        
        market = st.selectbox("Thị trường", ["Việt Nam", "Đông Nam Á", "Toàn cầu"])
        
        user_segment = st.selectbox(
            "User segment",
            ["Gen Z", "Millennials", "Mass market", "Unbanked", "SME", "Khác"]
        )
        
        if user_segment == "Khác":
            user_segment = st.text_input("Mô tả user segment") or "Mass market"
    
    with col2:
        purpose = st.selectbox(
            "Mục đích",
            ["Validate ý tưởng mới", "Improve feature hiện có", 
             "Khám phá thị trường", "Competitive analysis"]
        )
        
        depth = st.selectbox(
            "Độ sâu",
            ["Quick scan (500-800 từ)", "Standard (1000-1500 từ)", "Deep dive (2000+ từ)"],
            index=1
        )
        
        extra_context = st.text_area(
            "Context đặc biệt (optional)",
            placeholder="VD: focus vào pricing strategy, compare với MoMo..."
        )
    
    submitted = st.form_submit_button("🚀 Chạy Research", type="primary", use_container_width=True)

# ============ RUN PIPELINE ============
if submitted:
    if not topic:
        st.error("❌ Vui lòng nhập chủ đề research!")
        st.stop()
    
    inputs = {
        'feature_name': topic,
        'research_type': research_type,
        'market': market,
        'user_segment': user_segment,
        'purpose': purpose,
        'depth': depth,
        'extra_context': extra_context or "Không có",
        'current_year': '2026'
    }
    
    # Progress
    progress_container = st.container()
    with progress_container:
        with st.spinner("⏳ Pipeline đang chạy... (mất khoảng 2-5 phút)"):
            try:
                result = FintechUxResearch().crew().kickoff(inputs=inputs)
                
                # Save
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                safe_name = re.sub(r'[^\w\-]', '_', topic)[:30].strip('_')
                session_folder = f"output/session_{safe_name}_{timestamp}"
                os.makedirs(session_folder, exist_ok=True)
                
                final_path = "output/04_final_report.md"
                
                st.success("🎉 Hoàn thành!")
                
                # Display output
                if os.path.exists(final_path):
                    with open(final_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    tab1, tab2, tab3 = st.tabs(["📄 Final Report", "🔍 Review", "📊 Raw Research"])
                    
                    with tab1:
                        st.markdown(content)
                        st.download_button(
                            "⬇️ Tải Final Report",
                            content,
                            file_name=f"report_{safe_name}_{timestamp}.md",
                            mime="text/markdown"
                        )
                    
                    with tab2:
                        review_path = "output/03_review_report.md"
                        if os.path.exists(review_path):
                            with open(review_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                    
                    with tab3:
                        raw_path = "output/01_raw_research.md"
                        if os.path.exists(raw_path):
                            with open(raw_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
            
            except Exception as e:
                st.error(f"❌ Lỗi: {e}")