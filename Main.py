Sovereign Cross Stitch Generator - Wedding Edition
import streamlit as stimport osfrom PIL import Imageimport mathimport random# --- PAGE CONFIGURATION ---st.set_page_config(page_title="Sovereign Cross Stitch Generator - Wedding Edition", page_icon="🧵", layout="centered")# --- SESSION STATE INITIALIZATION ---if "purchased_patterns" not in st.session_state: st.session_state["purchased_patterns"] = []# --- APP BRANDING ---st.markdown("# 🧵 Sovereign Cross Stitch Generator")st.markdown("### Wedding & Heirloom Edition (Commercial PDF Pattern Creator)")st.caption("Gawing professional multi-page cross-stitch pattern ang iyong wedding photos at designs!")# --- SIDEBAR: PRICING & COMMERCIAL UPGRADE ---with st.sidebar: st.header("💎 Commercial Licensing & Pricing") st.info("📦 Free Tier: Preview at 1-Page Sample Grid.\n\n🌟 PRO Wedding Bundle (₱499): Unlimited High-Res Multi-Page PDF Patterns + Full DMC Legend & 10x10 Grid Tiling.") if st.button("💳 Bumili ng Pro License (₱499 via GCash)"): st.session_state["show_checkout"] = True if st.session_state.get("show_checkout", False): st.warning("Magpadala ng ₱499 sa GCash: 09288212987") ref_input = st.text_input("Ilagay ang GCash Reference Number:") if st.button("I-verify ang Bayad"): if ref_input: st.session_state["purchased_patterns"].append("PRO_LIFETIME") st.session_state["show_checkout"] = False st.success("🎉 Tagumpay! Na-activate na ang iyong PRO Wedding License.") st.rerun() else: st.error("Paki-lagay ang reference number.") if "PRO_LIFETIME" in st.session_state["purchased_patterns"]: st.success("✅ PRO License Active")# --- MAIN APP: UPLOAD & CONFIGURATION ---st.markdown("---")st.subheader("1️⃣ Mag-upload o Pumili ng Wedding Design")upload_option = st.radio("Pumili ng paraan:", ["Mag-upload ng Wedding Photo", "Pumili mula sa Sample Wedding Templates"])selected_design_name = "Custom Wedding Upload"if upload_option == "Mag-upload ng Wedding Photo": uploaded_file = st.file_uploader("I-upload ang litrato (JPG, PNG)", type=["jpg", "jpeg", "png"]) if uploaded_file is not None: image = Image.open(uploaded_file) st.image(image, caption="Na-upload na Litrato", width=300)else: template_choice = st.selectbox("Pumili ng Template:", [ "Classic Wedding Rings & Florals (300x450 Stitches)", "Bridal Silhouette & Roses (200x300 Stitches)", "Mr & Mrs Floral Monogram (150x150 Stitches)" ]) selected_design_name = template_choicest.markdown("---")st.subheader("2️⃣ Pattern Specifications (1-Year Heirloom Scale)")col1, col2 = st.columns(2)with col1: grid_size = st.selectbox("Grid / Stitch Dimensions:", ["300 x 450 (1-Year Masterpiece)", "200 x 300 (Large Tapestry)", "150 x 150 (Medium Project)"])with col2: fabric_count = st.selectbox("AIDA Cloth Count:", ["14 Count (Standard)", "16 Count", "18 Count (Fine Detail)"])# --- GENERATE & DOWNLOAD LOGIC ---st.markdown("---")if st.button("✨ Bumuo ng Professional PDF Pattern", type="primary"): with st.spinner("Binubuo ang DMC Thread Legend at Multi-Page Grid..."): # Simulation ng generation st.success("🎉 Tagumpay! Handa na ang iyong Wedding Cross Stitch Pattern.") # Display Mock Details st.markdown(f"### 📋 Pattern Summary: {selected_design_name}") st.markdown("- Total Colors: 24 DMC Palette Colors") st.markdown("- Estimated Threads: 18 Skeins (8m standard)") st.markdown("- Grid Format: Multi-Page Booklet (5 Pages with 10x10 Bold Markers)") # Check kung may PRO access para sa libreng download o kung bibili is_pro_unlocked = "PRO_LIFETIME" in st.session_state["purchased_patterns"] if is_pro_unlocked: st.download_button( label="📥 I-download ang Buong PRO PDF Pattern (Multi-Page)", data=b"Mock PDF Binary Data for Wedding Pattern", file_name="Wedding_Masterpiece_CrossStitch_Pattern.pdf", mime="application/pdf" ) else: # Free preview download button o prompt para magbayad st.info("💡 Na-generate ang Free Sample Preview (Page 1). Para ma-download ang buong Multi-Page PRO PDF, mag-upgrade sa sidebar (₱499).") st.download_button( label="📥 I-download ang Free Preview PDF", data=b"Mock Free Preview PDF Data", file_name="Wedding_Preview_Sample.pdf", mime="application/pdf" )
Gemini 3.8 Flash
Ran for 8m 3s

summarize_auto
Action history
chevron_right
Here are key actions taken for the app:

download
Installed 3 packages
edit
Edited 15 files
metadata.json
check_circle
index.html
check_circle
src/index.css
check_circle
src/types.ts
check_circle
src/data/dmcPalette.ts
check_circle
src/utils/colorMatcher.ts
check_circle
src/utils/pdfGenerator.ts
check_circle
src/components/Header.tsx
check_circle
src/components/CheckoutModal.tsx
check_circle
src/components/DesignSelector.tsx
check_circle
src/components/PatternConfigurator.tsx
check_circle
src/components/StitchViewer.tsx
check_circle
src/components/FlossLegendTable.tsx
check_circle
src/components/PageOverviewMap.tsx
check_circle
src/App.tsx
check_circle
build
Built
# Pansamantalang placeholder sa dulo para mag-run sa Streamlit
st.write("---")
st.caption("App setup completed.")
