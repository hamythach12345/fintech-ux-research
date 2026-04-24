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
        # Domain picker
        domain = st.selectbox(
            "🏢 Lĩnh vực nghiên cứu",
            [
                "Fintech & Super App",
                "E-commerce & Retail",
                "EdTech & Learning",
                "HealthTech & Wellness",
                "Food Delivery & F&B",
                "Logistics & Mobility",
                "Gaming & Entertainment",
                "B2B SaaS & Productivity",
                "Social Media & Content",
                "Travel & Hospitality",
                "Real Estate & PropTech",
                "Media & Publishing",
                "Khác (tự nhập)"
            ],
            index=0,
            help="Agent sẽ adapt toàn bộ research theo lĩnh vực này"
        )
        
        if domain == "Khác (tự nhập)":
            domain = st.text_input(
                "Nhập lĩnh vực cụ thể", 
                placeholder="VD: AgriTech, InsurTech, LegalTech..."
            ) or "General"
        
        topic = st.text_input(
            "📝 Chủ đề research *",
            placeholder="VD: Tính năng favorites trong app đặt đồ ăn"
        )
        
        research_type = st.selectbox(
            "Loại research",
            ["Feature research", "User segment", "Market/Competitor", "Trend research"]
        )
        
        market = st.selectbox(
            "Thị trường", 
            ["Việt Nam", "Đông Nam Á", "Toàn cầu"]
        )
        
        user_segment = st.selectbox(
            "User segment",
            ["Gen Z", "Millennials", "Mass market", "Unbanked", "SME", "Khác"]
        )
        
        if user_segment == "Khác":
            user_segment = st.text_input(
                "Mô tả user segment",
                placeholder="VD: Freelancers, New parents, Senior 55+..."
            ) or "Mass market"
    
    with col2:
        purpose = st.selectbox(
            "Mục đích",
            ["Validate ý tưởng mới", "Improve feature hiện có", 
             "Khám phá thị trường", "Competitive analysis"]
        )
        
        # Time scope - MỚI THÊM
        time_scope = st.selectbox(
            "📅 Mốc thời gian nghiên cứu",
            [
                "Hiện tại (2026)",
                "1 năm gần đây (2025-2026)",
                "3 năm gần đây (2023-2026)",
                "5 năm gần đây (2021-2026)",
                "Cả lịch sử (xuyên suốt)",
                "Tương lai - forecast (2026-2028)",
                "Tùy chỉnh"
            ],
            index=1,
            help="Agent sẽ tập trung vào dữ liệu, sự kiện, trends trong mốc thời gian này"
        )
        
        if time_scope == "Tùy chỉnh":
            time_scope = st.text_input(
                "Nhập mốc thời gian cụ thể",
                placeholder="VD: Q1-Q3 2025, hoặc Trước COVID (2018-2019)"
            ) or "Hiện tại (2026)"
        
        depth = st.selectbox(
            "Độ sâu",
            ["Quick scan (500-800 từ)", "Standard (1000-1500 từ)", "Deep dive (2000+ từ)"],
            index=1
        )
        
        extra_context = st.text_area(
            "Context đặc biệt (optional)",
            placeholder="VD: focus vào pricing strategy, compare với MoMo..."
        )
    
    submitted = st.form_submit_button(
        "🚀 Chạy Research", 
        type="primary", 
        use_container_width=True
    )
# ============ RUN PIPELINE ============
if submitted:
    if not topic:
        st.error("❌ Vui lòng nhập chủ đề research!")
        st.stop()
    
    inputs = {
        'domain': domain,
        'feature_name': topic,
        'research_type': research_type,
        'market': market,
        'user_segment': user_segment,
        'purpose': purpose,
        'time_scope': time_scope,
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
                
                final_path = "output/06_final_report.md"
                
                st.success("🎉 Hoàn thành!")
                
                # Display output
                if os.path.exists(final_path):
                    with open(final_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
# Display output với nhiều tabs
                    tab1, tab2, tab3, tab4, tab5 = st.tabs([
                        "📄 Final Report",
                        "🔄 Revision Process",
                        "🔍 Reviews",
                        "📊 Insight Drafts",
                        "📚 Raw Research"
                    ])
                    
                    final_path = "output/06_final_report.md"
                    
                    with tab1:
                        if os.path.exists(final_path):
                            with open(final_path, "r", encoding="utf-8") as f:
                                content = f.read()
                            st.markdown(content)
                            
                            st.divider()
                            st.subheader("⬇️ Download Report")
                            
                            from exporters import md_to_docx_bytes, md_to_pdf_bytes
                            
                            col1, col2, col3 = st.columns(3)
                            base_filename = f"report_{safe_name}_{timestamp}"
                            
                            with col1:
                                st.download_button(
                                    "📄 Markdown",
                                    content,
                                    file_name=f"{base_filename}.md",
                                    mime="text/markdown",
                                    use_container_width=True
                                )
                            with col2:
                                try:
                                    st.download_button(
                                        "📝 Word",
                                        md_to_docx_bytes(content),
                                        file_name=f"{base_filename}.docx",
                                        use_container_width=True
                                    )
                                except Exception as e:
                                    st.error(f"DOCX error: {e}")
                            with col3:
                                try:
                                    st.download_button(
                                        "📕 PDF",
                                        md_to_pdf_bytes(content, topic),
                                        file_name=f"{base_filename}.pdf",
                                        use_container_width=True
                                    )
                                except Exception as e:
                                    st.error(f"PDF error: {e}")
                    
                    with tab2:
                        st.subheader("🔄 Quá trình Revision")
                        st.info("So sánh Insight v1 (bản đầu) và v2 (sau khi Reviewer feedback)")
                        
                        v1_path = "output/02_insight_v1.md"
                        v2_path = "output/04_insight_v2.md"
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.markdown("**📝 Draft v1 (original)**")
                            if os.path.exists(v1_path):
                                with open(v1_path, "r", encoding="utf-8") as f:
                                    st.markdown(f.read())
                        with col_b:
                            st.markdown("**✨ Draft v2 (revised)**")
                            if os.path.exists(v2_path):
                                with open(v2_path, "r", encoding="utf-8") as f:
                                    st.markdown(f.read())
                            else:
                                st.success("✅ Draft v1 đã pass review, không cần revision.")
                    
                    with tab3:
                        st.subheader("🔍 Review Reports")
                        
                        r1_path = "output/03_review_v1.md"
                        r2_path = "output/05_review_v2.md"
                        
                        st.markdown("### Review lần 1")
                        if os.path.exists(r1_path):
                            with open(r1_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                        
                        if os.path.exists(r2_path):
                            st.divider()
                            st.markdown("### Review lần 2 (sau revision)")
                            with open(r2_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                    
                    with tab4:
                        st.subheader("📊 Insight Drafts")
                        v1_path = "output/02_insight_v1.md"
                        v2_path = "output/04_insight_v2.md"
                        
                        if os.path.exists(v2_path):
                            with open(v2_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                            st.caption("(Hiển thị v2 - phiên bản đã revise)")
                        elif os.path.exists(v1_path):
                            with open(v1_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                            st.caption("(v1 - pass ngay không cần revise)")
                    
                    with tab5:
                        raw_path = "output/01_raw_research.md"
                        if os.path.exists(raw_path):
                            with open(raw_path, "r", encoding="utf-8") as f:
                                st.markdown(f.read())
            
            except Exception as e:
                st.error(f"❌ Lỗi: {e}")
